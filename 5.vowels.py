vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string = input('Type something to know the quantify of vowels')
quantify_of_vowels = 0
for i in string:
	if i in vowels:
		quantify_of_vowels += 1

print(f'The quantify of vowels in the text is {quantify_of_vowels}')