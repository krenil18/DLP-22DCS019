def test_case_2(s):
    if not s:
        return False
    if s[0] != s[-1]:
        return False
    return all(c in 'abc' for c in s)

input_str = input("Enter string (over a, b, c, starts and ends with same letter): ")

if test_case_2(input_str):
    print("Valid")
else:
    print("Invalid")
