## Duolingo с блекджеком и глубокими знаниями

Привет, меня зовут Емельянов Михаил, я Python-программист и я хотел бы показать вам свой небольшой «проект выходного дня» — **Flywheel**, микро-платформу для изучения иностранных языков — смесь Duolingo и Anki, программу, которая может помочь вам правильно **писать** на английском. Flywheel доступна в исходниках, лежит на [GitHub](https://github.com/amaargiru/flywheel).

Как вы, возможно, знаете, обобщенное знание иностранного языка можно разложить на четыре относительно независимые составляющие: чтение, письмо, слушание и говорение. К сожалению, тренировка одной из этих способностей не будет напрямую отражаться на остальных компонентах, поэтому, например, развивая навык чтения, мы достаточно опосредованно влияем на навык письма. Flywheel — «точилка» именно для **письменного английского**.

Если вы когда-нибудь пользовались Duolingo, то имеете представление о формате, в котором будет идти обучение. Последовательность проста: вот тебе фраза, переведи её на другой язык; программа запомнит, когда ты в последний раз переводил ту или иную фразу и насколько успешно у тебя это получилось; в зависимости от правильности ответа будет определено время, когда тебе нужно задать эту же фразу еще раз. В целом, на мой взгляд, как сам Duolingo, так и используемый им подход — просто гениальны. Но... Есть нюансы, которые несколько портят впечатления от процесса учёбы, и именно для их устранения я и задумал Flywheel.

Во первых, и это самое главное, я хотел бы, чтобы все задания на перевод были *только* русско-английскими. Я хочу видеть только русские фразы, которые мне нужно перевести на английский. Переводить с английского на русский не хочу. Я не учусь на переводчика, я хочу изучить иностранный язык! А для этого гораздо правильнее, на мой взгляд, вообще не включать русскоязычную раскладку на клавиатуре во время учёбы. На Duolingo есть небольшой «лайфхак» — переключение с изучения английского для русскоговорящих на изучение *русского для англоговорящих* (этим, отчасти, и объясняется большое количество учащихся на этом курсе — это вовсе не жители США или туманного Альбиона, изучающие русский, а как раз наоборот, жители России, зубрящие английский язык), тогда учебный курс будет содержать больше русско-английских заданий, но количество англо-русских переводов всё равно останется очень большим. А я хочу 100 % времени урока писать на английском!

Во-вторых, я взрослый человек, и мне совершенно не нужна геймификация процесса обучения. Всё эти человечки, весело подмигивающие, приободряющие и дающие советы — один сплошной жирный, неуместный и раздражающий Круциатус. Доходит даже до выпуска расширений для браузера, которые пытаются вырезать весь этот ненужный функционал, сведя визуал сайта до необходимого уровня минимализма.

Третье — я взрослый человек (повторюсь) и у меня иногда нет времени на полноразмерный урок. Хотя на Duolingo он довольно короток, но, тем не менее, разбивка процесса обучения на фиксированный уроки по ...надцать вопросов удобна в первую очередь для обучающей платформы, а не для ученика. Я хочу, чтобы у меня была возможность повтора не двадцати фраз, а, скажем, пяти или трёх, даже одной, наконец. Хочу прерывать процесс обучения в любой момент без потери прогресса! В конце концов, я иногда могу заниматься только в редкие перерывы недетерминированной продолжительности, под чай с печенькой, или в передышке между общением с детьми. Если у меня есть буквально свободная минута, то я хочу сделать пару подходов и сохранить свой прогресс.

В-червертых, хочу иметь возможность всегда, на любом этапе обучения добавлять новые фразы! Услышав или вычитав что-то новое, полезное или просто интересное, хочу добавить фразу в список, пусть теперь программма позаботится о том, чтобы я эта фраза осталась в моей памяти навсегда.

Пятое, и тоже немаловажное соображение — хочу, чтобы программа показывала неправильно введенные фрагменты перевода. Иногда в введенном тексте есть мелкие ошибки, «поймать» которые глазами довольно затруднительно. Надо, чтобы программа наглядно показала разницу между моим переводом и правильным вариантом, а я бы сосредоточился на изучении английского, а не на игре «найди ошибочную букву в длинной фразе на иностранном языке».

Вот такой вот список пожеланий у меня накопился — хочу Duolingo, но только с русско-английскими заданиями, без геймификации, с сохранением прогресса после каждого задания, с возможностью добавлять новые фразы и с визуализацией сделанных ошибок, даже мелких.

Думаю, на этом предисловие можно закончить и перейти к сути. Если вы просто хотите начать учить английский язык — переходите к разделу «Использование» (ближе к концу статьи). Если вы хотите посмотреть, как программа устроена «под капотом», то переходите к следующему разделу, «Как это работает».
