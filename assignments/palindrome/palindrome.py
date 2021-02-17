def isPalindrome(word):
    clean = ''
    for c in str(word):
        if c.isalnum():
            clean = clean + c.lower()
        reverse = clean[::-1]
    if clean == '':
        return False
    elif clean == reverse:
        return True
    else: return False
