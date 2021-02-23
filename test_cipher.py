from cipher import Cipher
import pytest

def test_encrypt_caesar_gives_empty_string_if_no_text_entered():
    cipher = Cipher()
    code = cipher.encrypt_caesar(" ", -3)
    assert code == " "

def test_encrypt_caesar_works_for_lower_case_word():
    cipher = Cipher()
    code = cipher.encrypt_caesar("abcde", 2)
    assert code == "cdefg"

def test_encrypt_caesar_works_for_upper_case_word():
    cipher = Cipher()
    code = cipher.encrypt_caesar("XYZ", 4)
    assert code == "BCD"

def test_encrypt_caesar_works_for_a_sentence():
    cipher = Cipher()
    code = cipher.encrypt_caesar("Hello how are you today", 5)
    assert code == "Mjqqt mtb fwj dtz ytifd"

def test_encrypt_caesar_works_if_numbers_in_string():
    cipher = Cipher()
    code = cipher.encrypt_caesar("abcABC123xyzXYZ", 2)
    assert code == "cdeCDE123zabZAB"

def test_encrypt_caesar_does_not_change_special_chars_in_string():
    cipher = Cipher()
    code = cipher.encrypt_caesar("?*£$%^", 5)
    assert code == "?*£$%^"

def test_encrypt_caesar_works_for_negative_shift():
    cipher = Cipher()
    code = cipher.encrypt_caesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", -3)
    assert code == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

def test_encrypt_caesar_raises_error_if_int_not_entered_for_shift():
    cipher = Cipher()
    with pytest.raises(TypeError) as e:
        code = cipher.encrypt_caesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "three")
    assert str(e.value) == "Invalid - must enter an integer for shift"