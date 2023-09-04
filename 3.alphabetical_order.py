alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'M': 11, 'N': 12, 'L': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,'Y': 24, 'Z': 25}
reached = 0
position = 0
not_order = 0

while reached != 1:
    string = input('Type a string in UPPERCASE to check if it is in alphabetical order')
    for i in string:
        if i in alphabet:
            reached = 1
    if reached == 0:
        print('The string is wrong')

first_char = string[0]
for i in alphabet:
    if i == first_char:
        break
    position += 1

for i in range (1, len(string)-1):
    if position > i:
        not_order = 1
        break

if not_order == 1:
    print('The string is not in alphabetical order')
else:
    print('The string is in alphabetical order')

