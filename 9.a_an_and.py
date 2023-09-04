string = input('Type something to know the quantify of "a" and "an" and "and"')
string_in_list = []
quantify_of_a = 0
quantify_of_an = 0
quantify_of_and = 0
reached = 0

init = 0
end = 0
word = ''

for i in string:
	if i != ' ':
		end += 1
		word += i
	else:
		string_in_list.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
string_in_list.append(word)

for i in string_in_list:
	if i == 'a':
		quantify_of_a += 1
	elif i == 'an':
		quantify_of_an += 1
	elif i == 'and':
		quantify_of_and += 1

print(f'The quantify of letter "a" in the text is {quantify_of_a}')
print(f'The quantify of letter "an" in the text is {quantify_of_an}')
print(f'The quantify of letter "and" in the text is {quantify_of_and}')