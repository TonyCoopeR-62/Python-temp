import re
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = re.sub('[!@#$]', '', text)
    return text == reverse(text)

something = input('Input text')
if (is_palindrome(something)):
    print('Yes, palindrome')
else:
    print('No, not palindrome')