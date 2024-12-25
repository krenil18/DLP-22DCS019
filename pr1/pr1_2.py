
def pr1_2():
    print("For Finite automata: a+bb")
    str_input = input("Enter String: ")

    i = 0

    if str_input[i] == 'a':
        while i < len(str_input) and str_input[i] == 'a':
            i += 1
        if i < len(str_input) - 1 and str_input[i] == 'b' and str_input[i + 1] == 'b' and i + 2 == len(str_input):
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")


pr1_2()
