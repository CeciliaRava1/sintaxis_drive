alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_to_m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

reached = 0

while reached != 1:
    char = input("Type a letter of the alphabet to find out if it comes before or after the letter 'm'.")
    if char not in alphabet:
        print('The letter is not in alphabet, try again')
    else:
        reached = 1

if char not in alphabet_to_m and char != 'm' and char != 'M':
    print(f'{char} is after the letter "m"')
elif char == 'm' or char == 'M':
    print('The letter entered was "m"')
elif char in alphabet_to_m:
    print(f'{char} is before the letter "m"')
