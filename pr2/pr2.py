def pr2():
    s = input("Enter string: ")
    current_state = int(input("Set starting state: "))
    A_state = int(input("Set acceptance test state: "))
    
    transition = [[0, 0], [2, 3], [1, 4], [4, 1], [3, 2]]
    
    for char in s:
        l = 0 if char == 'a' else 1
        print(f"{current_state} {char} {l} = ", end="")
        current_state = transition[current_state][l]
        print(current_state)
    
    if current_state == 2:
        print("Valid")
    else:
        print("invalid")


pr2()
