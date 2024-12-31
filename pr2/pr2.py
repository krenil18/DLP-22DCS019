n_symbols = int(input("Number of Symbols: "))
symbols = input("Enter Symbols: ").split()

n_states = int(input("Number of States: "))
initial_state = int(input("Initial State: "))
final_state = int(input("Final State: "))

table = {}
for i in range(1, n_states + 1):
    for sym in symbols:
        table[(i, sym)] = int(input(f"{i} to {sym} -> "))

s = input("Enter the string: ")

curr_state = initial_state
for char in s:
    if char not in symbols or (curr_state, char) not in table:
        print("String Invalid!")
        break
    curr_state = table[(curr_state, char)]
else:
    if curr_state == final_state:
        print("String Valid!")
    else:
        print("String Invalid!")
