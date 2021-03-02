import palindrome
import pytest 

def test_palindrome():
    assert palindrome.isPalindrome('Aibohphobia') == True

def test_word():
    assert palindrome.isPalindrome('nothing') == False

def test_number():
    assert palindrome.isPalindrome(12321) == True
 
def test_number_string():
    assert palindrome.isPalindrome('12321') == True

def test_list():
    assert palindrome.isPalindrome(['racecar', 'poop', 'kook']) == False

def test_palindrome_list():
    assert palindrome.isPalindrome(['r', 'a', 'c', 'e', 'c', 'a', 'r']) == True

def test_empty_string():
    assert palindrome.isPalindrome('') == False