# define a function
def ispalindrome(string):
    if string==string[::-1]:
        return "the string is a palindrome."
    else:
        return "tje string is not a palindrome."
    #enter input string
    string=input("enter string:")
    print(ispalindrome(string))
