from refiner import Refiner


class TestRefiner:
    def test_refine_user_input_normal_string(self):
        user_input = "It's a normal user input. Allowed characters: !?!.,;'"
        assert Refiner.refine_user_input(user_input) == user_input

    def test_refine_user_input_limit_string_size(self):
        assert len(Refiner.refine_user_input("a" * 400)) == 200

    def test_refine_user_input_strip(self):
        assert Refiner.refine_user_input("  a  ") == "a"

    def test_refine_user_input_delete_unwanted_symbols(self):
        assert Refiner.refine_user_input(r"/|\\=(%$#😀 abc 😀#$%)=/|\\") == "abc"

    def test_refine_user_input_replace_tabs_with_spaces(self):
        assert Refiner.refine_user_input("\t abc \t") == "abc"

    def test_refine_user_input_replace_multiple_spaces_with_one(self):
        assert Refiner.refine_user_input("a    b    c") == "a b c"

    def test_refine_user_input_replace_multiple_commas_with_one(self):
        assert Refiner.refine_user_input("a,,, b,, c,,,, d") == "a, b, c, d"
