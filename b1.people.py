people = input('Type the surnames separates with ",", then the names, separates with ","')
people_in_list = []
people_in_new_list = []
people_in_vector = [0]*3
end = 0
word = ''
init = 0
reached = 0

for i in people:
	if i != ',':
		end += 1
		word += i
	else:
		people_in_list.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
people_in_list.append(word)

people_in_vector[0] = people_in_list[0] + ' ' + people_in_list[3]
people_in_vector[1] = people_in_list[1] + ' ' + people_in_list[4]
people_in_vector[2] = people_in_list[2] + ' ' + people_in_list[5]

for i in people_in_vector:
	people_in_new_list.append(i)

people_in_new_list.sort()
print(people_in_new_list)