def reverse_string(s):
    '''
    Reversed version of string s
    '''
    # Base Case
    if len(s) == 0:
        return s
    # Recursive Case
    return reverse_string(s[1::]) + s[0]

# Testing
assert reverse_string('') == '', 'reverse_string() does not work for empty string'
assert reverse_string('recursion') == 'noisrucer', 'reverse_string() does not work'
print('All tests pass! :)')
