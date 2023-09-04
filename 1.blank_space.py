string_without_blank_space = ''
reached = 0

while reached != 1:
    string = input('Type a sentence ending with "." ')
    if string[-1] == '.':
        reached = 1

for i in string:
    if i != ' ':
        string_without_blank_space += i

print(f'The sentence without blank spaces is {string_without_blank_space}')
