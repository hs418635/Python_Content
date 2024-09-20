#1)Iterate both lists simultaneously
'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
#2)Remove empty strings from the list of strings
list1 = ["Livewire", "", "Aasif", "Ashja", "", "Asran"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

#3)Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#4)Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)


'''#5)Write a Python program to print a specified list after removing the 0th,
 #4th and 5th elements.
SampleList : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
ExpectedOutput : ['Green', 'White', 'Black']

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
