import json
import pathlib
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from comparator import Comparator
from complicator import Complicator
from db_schema import User
from examiner import Examiner
from fw_logger import FlyWheelLogger
from lower import Lower
from printer import Printer
from refiner import Refiner

log_max_file_size = 1024 ** 2  # Максимальный размер одного файла логов
log_max_file_count = 10  # Максимальное количество файлов логов
log_file_path = "logs//api.log"

# To get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "f6e936d318b4103412c142893d7331fb83c2228fc31155a8f96de27c3afdeea7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10 * 365 * 24 * 60


@dataclass
class Token:
    access_token: str
    token_type: str


@dataclass
class TokenData:
    username: Optional[str] = None


@dataclass
class LocalUser:
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    hashed_password: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

app = FastAPI()

origins = [
    "http://domainname.com",
    "https://domainname.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # = origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# http://127.0.0.1:8000/docs
# Example: http://127.0.0.1:8000/get_next_question?user_id=1
@app.post("/get_next_question_anonymous")
async def get_next_question_anonymous(user_id: int):
    question_id = Examiner.define_next_question_num(user_id)
    question = Examiner.get_question(question_id)

    return {"question_id": question_id,
            "native_phrase": f"{question.native_phrase}"}


# Example: http://127.0.0.1:8000/get_answer_check?user_id=1&question_id=1&user_input=qq
@app.post("/get_answer_check_anonymous")
async def get_answer_check_anonymous(user_id: int, question_id: int, user_input: str):
    question = Examiner.get_question(question_id)
    user_input_cleaned = Refiner.refine_user_input(user_input)
    user_input_complex = Complicator.complicate_user_input(user_input_cleaned)
    user_input_without_punctuation_lower = Lower.list_lower(user_input_complex.user_input_without_punctuation)
    references_lower = Lower.references_lower(question.references)
    index, ratio = Comparator.find_nearest_reference_index(user_input_without_punctuation_lower, references_lower)
    correction = Comparator.find_matching_blocks(user_input_without_punctuation_lower, references_lower, index)
    a = Printer.format_message_to_api(question.references, index, correction, ratio)

    return {"question_id": question_id, "answer": json.dumps(a)}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = None
    try:
        user = User.get(User.username == token_data.username)
    except Exception as e:
        logger.error(f"Ошибка \"{str(e)}\" при попытке найти пользователя в БД.")

    if user is None:
        raise credentials_exception
    return user


@app.post("/signin", response_model=Token)
async def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    user = None
    try:
        user = User.get(User.username == form_data.username)
    except Exception as e:
        logger.error(f"Ошибка \"{str(e)}\" при попытке найти пользователя в БД.")

    if user is None or not pwd_context.verify(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": access_token,
            "token_type": "bearer"}


@app.post("/signup")
async def signup(username: str, email: str, password: str):
    res: bool = False

    user = None
    try:
        user = User.get(User.username == username)
    except Exception as e:
        logger.error(f"Ошибка \"{str(e)}\" при попытке найти пользователя в БД.")

    if user is None:
        User.create(username=username, email=email, password_hash=pwd_context.hash(password))
        res = True

    if res:
        return {"result": "New user created successfully",
                "user": username}
    else:
        return {"result": "User exist",
                "user": username}


@app.post("/get_next_question")
async def get_next_question(current_user: LocalUser = Depends(get_current_user)):
    # return [{"item_id": "Foo", "owner": current_user.username}]
    question_id = Examiner.define_next_question_num(1)
    question = Examiner.get_question(question_id)

    return {"question_id": question_id,
            "native_phrase": f"{question.native_phrase}"}


@app.post("/get_answer_check")
async def get_answer_check(user_id: int, question_id: int, user_input: str, current_user: LocalUser = Depends(get_current_user)):
    # return [{"item_id": "Foo", "owner": current_user.username}]
    question = Examiner.get_question(question_id)
    user_input_cleaned = Refiner.refine_user_input(user_input)
    user_input_complex = Complicator.complicate_user_input(user_input_cleaned)
    user_input_without_punctuation_lower = Lower.list_lower(user_input_complex.user_input_without_punctuation)
    references_lower = Lower.references_lower(question.references)
    index, ratio = Comparator.find_nearest_reference_index(user_input_without_punctuation_lower, references_lower)
    correction = Comparator.find_matching_blocks(user_input_without_punctuation_lower, references_lower, index)
    a = Printer.format_message_to_api(question.references, index, correction, ratio)

    return {"question_id": question_id, "answer": json.dumps(a), "link_to_audio": question.links_to_audio[index]}


if __name__ == "__main__":
    try:
        path = pathlib.Path(log_file_path)  # Создаем путь к файлу логов, если он не существует
        path.parent.mkdir(parents=True, exist_ok=True)
        logger = FlyWheelLogger.get_logger(log_file_path, log_max_file_size, log_max_file_count)
    except Exception as err:
        print(f"Error when trying to create log directory {str(err)}")
        sys.exit()  # Аварийный выход

    uvicorn.run(app, host="0.0.0.0", port=8000)
