string = input('Type something to know the quantify of the letter "i"')
quantify_of_i = 0
for i in string:
	if i == 'i':
		quantify_of_i += 1

print(f'The quantify of letter "i" in the text is {quantify_of_i}')