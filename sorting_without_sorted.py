# Sorting strings without using sorted function


def findSmallestString(the_list = []):
	if len(the_list) == 1:
		return the_list
	smallest = the_list[0]
	ordered_list = []

	for i in the_list[1:]:
		if i < smallest:
			temp = smallest
			smallest = i
	ordered_list.append(smallest)
	the_list.remove(smallest)
	ordered_list = ordered_list + findSmallestString(the_list)

	return ordered_list


dictionary = ["dsae","davc","grsp","brty","bart","bacz","jaeb"]
# ['bacz', 'bart', 'brty', 'davc', 'dsae', 'grsp', 'jaeb']


ordered = findSmallestString(dictionary)
print(ordered)


