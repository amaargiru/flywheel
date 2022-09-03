import pytest

from refiner import Refiner

class TestRefiner:
    def test_refine_user_input_normal_string(self):
        user_input = "It's OK input"
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == user_input

    def test_refine_user_input_limit_string_size(self):
        user_input = "a" * 400
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert len(user_input_cleaned) == 200

    def test_refine_user_input_strip(self):
        user_input = "  a  "
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == "a"

    def test_refine_user_input_delete_unwanted_symbols(self):
        user_input = r"/|\\=(%$#😀 abc 😀#$%)=/|\\"
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == "abc"

    def test_refine_user_input_replace_tabs_with_spaces(self):
        user_input = "\t abc \t"
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == "abc"

    def test_refine_user_input_replace_multiple_spaces_with_one(self):
        user_input = "a    b    c"
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == "a b c"

    def test_refine_user_input_replace_multiple_commas_with_one(self):
        user_input = "a,,, b,, c,,,, d"
        user_input_cleaned = Refiner.refine_user_input(user_input)
        assert user_input_cleaned == "a, b, c, d"
