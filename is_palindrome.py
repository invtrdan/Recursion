def is_palindrome(s):
    '''
    Returns True if the input string is a palindrome
    Returns False if the input string is not a palindrome
    '''
    # Base Cases
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    # Recursive Case
    return is_palindrome(s[1:-1])

assert is_palindrome('') == True, 'is_palindrome() does not work for an empty string'
assert is_palindrome('d') == True, 'is_palindrome() does not work for a string with a single character'
assert is_palindrome('danielle') == False, 'is_palindrome() does not work as expected'
assert is_palindrome('elle') == True, 'is_palindrome() does not work as expected'


