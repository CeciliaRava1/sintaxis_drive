string = input('Type a text')
string_to_find = input('Type something to find in the text')
string_to_find_lenght = len(string_to_find)
times = 0
position = 0
first_position = 0
new_string = ''

if string_to_find not in string:
	print("The string is not in the text")
else:
	for i in string:
		position += 1
		if i == string_to_find[0]:
			first_position = position
			while position < string_to_find_lenght:
				position += 1
				for i in range (0, string_to_find_lenght-1):
					if string[first_position+i] == string_to_find[i]:
						correct = 1
					else:
						correct = 0

position = 0
for i in string:
	position += 1
	if first_position == position:
		new_string += '*'
		reached = 1
	else:
		new_string += i
print(f"This was the text entired: {string}")
print(f"This was the string entired to find: {string_to_find}")
print(f"This is the new string with '*' in the position where the string to find starts: {new_string}")