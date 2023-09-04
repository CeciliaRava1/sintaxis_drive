string = input('Type something to know the quantify of the letters "a" and "b"')
quantify_of_a = 0
quantify_of_b = 0
for i in string:
	if i == 'a':
		quantify_of_a += 1
	elif i == 'b':
		quantify_of_b += 1

print(f'The quantify of letter "a" in the text is {quantify_of_a}')
print(f'The quantify of letter "b" in the text is {quantify_of_b}')
