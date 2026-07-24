#Write a Python program that takes a name as an input from the user and then creates a function that accepts the same name as a parameter and greets the user.

# n=input("Enter your name")
# def greet():
#     e="hello"+n
#     return e
# print(greet())
def Palindrome(string):
    left_pos = 0
    right_pos = len(string)-1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print("Is this a Palindrom?")
print(Palindrome('malayalam'))