def test_case_3(s):
    if not s:
        return False
    if not s[0].islower():  
        return False
    return all(c.isdigit() or c.islower() for c in s)  

input_str = input("Enter string (lowercase alphabets and digits, starts with lowercase alphabet): ")

if test_case_3(input_str):
    print("String is valid")
else:
    print("String is invalid")
