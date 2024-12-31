def test_case_1(s):
    for i in range(len(s)-2):
        if s[i]=='0' and s[i+1]=='1' and s[i+2]=='1':
            return True
        return False

input_str = input("Enter string (over 0 and 1, where 0 is immediately followed by 11): ")

if test_case_1(input_str):
    print("Valid")
else:
    print("Invalid")
