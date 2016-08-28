source_list = [('1','a'),('2','b'),('3','c'),('4','d')]
list1, list2 = zip(*source_list)
print(list1)
print(list2)

list3 = ['A', 'B', 'C', 'D']
nGen = zip(list1, list2, list3)


source_list2 = []
for i in range(0, len(list1)):
    source_list2.append(next(nGen))
    print(source_list2[-1])

print(source_list2)
