string_1 = input('Type a string')
string_2 = input("Type another string to know if it's an anagram")
list_string_1 = []
list_string_2 = []

for i in string_1:
    if i != ' ':
        list_string_1.append(i)
for i in string_2:
    if i != ' ':
        list_string_2.append(i)

list_string_1.sort()
list_string_2.sort()

if list_string_1 == list_string_2:
    print(f'{string_1} is an anagram of {string_2}')
else:
    print(f'{string_1} is not an anagram of {string_2}')