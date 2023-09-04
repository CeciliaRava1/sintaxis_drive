reached = 0
quantify_of_a = 0
quantify_of_b = 0
while reached != 1:
	string = input('Type something to know the quantify of the letter "b". Max lenght: 100 char')
	if len(string) <= 100:
		reached = 1

for i in string:
	if i == 'b':
		quantify_of_b += 1

print(f'The quantify of letter "b" in the text is {quantify_of_b}')
