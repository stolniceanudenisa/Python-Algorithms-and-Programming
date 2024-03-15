#
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])
#
#
#
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
#
#
#
#
#
#
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)
#
#
#
#
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)
#
#
#
#
#
#
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)
#
#
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# x = thisdict.get("model")
#
#
#
#
# org_list = [1, 2, 3, 4, 5]
# fin_list = list(map(lambda x:x**3, org_list))
# print(fin_list) # [1, 8, 27, 64, 125]
#
#
#
# org_list = ["Hello", "world", "freecodecamp"]
# fin_list = list(map(len, org_list))
# print(fin_list) # [5, 5, 12]
#
#
# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
#
#
#
# dict1 = {"key1":1, "key2":2}
# dict2 = {"key2":2, "key1":1}
# print(dict1 == dict2)
#
#
#
# aList = ["PYnative", [4, 8, 12, 16]]
# print(aList[0][1])
# print(aList[1][3])
#
#
#
#
# # The algorithm's time complexity in the worst case, best case and average case scenarios is O(n^4)
# #
# # In the worst case scenario, when n is very large, the number of iterations performed
# # by the nested loops will be n^2 * n^2 = n^4. This means that the time taken by the algorithm
# # will increase rapidly as the input size increases.
# #
# # In the best case scenario, when n is equal to 0, the number of iterations performed by the
# # nested loops will be 0 * 0 = 0. This means that the time taken by the algorithm will be constant
# # regardless of the input size.
# #
# # In the average case scenario, the number of iterations performed by the nested loops
# # will be (n^4 + n^4) / 2 = n^4/2. This means that the time taken by the algorithm will increase rapidly
# # as the input size increases.
# #
# # The space complexity of the algorithm is O(1) because it only uses a single variable "s" to keep
# # track of the sum and its size does not depend on the input size.
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# color_list1 = ["White", "Yellow"]
# color_list2 = ["Red", "Blue"]
# color_list3 = ["Green", "Black"]
# # color_list = color_list1 + color_list2 + color_list3
# color_list1.extend(color_list2)
# print(color_list1)
#
# color_list1.remove(color_list1[3]) # "Blue"
# print(color_list1)
#
# color_list1.pop(2)
# print(color_list1)
#
# number = [1,2,3]
# print(number[0]*4)
# print(number*4) # repetare de 4 ori a listei
#
#
# ######################################
#
# color_list=["Red", "Blue", "Green", "Black"] # The list have four elements
# print(color_list[0:2]) # cut fi
# # ramane "Red", "Blue"
#
#
# color_list=["Red", "Blue", "Green", "Black"] # The list have four elements
# # indices start at 0 and end at 3
# print(color_list[1:2])
# # ['Blue']
# print(color_list[1:-2])
# # ['Blue']
#
# color_list=["Red", "Blue", "Green", "Black"] # The list have four elements
# # indices start at 0 and end at 3
# print(color_list[1:-1])
# # ['Blue', 'Green']
#
# print(color_list[:3])
# print(color_list[:])
#
#
#
# olor_list=["Red", "Blue", "Green", "Black"]
# print(olor_list)
# # ['Red', 'Blue', 'Green', 'Black']
# olor_list.pop(2) # Remove second item and return it
# # 'Green'
# print(olor_list)
# # ['Red', 'Blue', 'Black']
#
#
# # color_list.sort(key=None, reverse=False)
# # print(color_list)
# # ['Black', 'Blue', 'Green', 'Red']
#
#
# # listx=[1, 5, 7, 3, 2, 4, 6]
# # >>> print(listx)
# # [1, 5, 7, 3, 2, 4, 6]
# # >>> sublist=listx[2:7:2] #list[start:stop:step], #step specify an increment
# # between the elements to cut of the list.
# # >>> print(sublist)
# # [7, 2, 6]
# # >>> sublist=listx[::3] #returns a list with a jump every 2 times.
# # >>> print(sublist)
# # [1, 3, 6]
# # >>> sublist=listx[6:2:-2] #when step is negative the jump is made back
# # >>> print(sublist)
# # [6, 2]
#
#
# #nested lists
# # listx = [["Hello", "World"], [0, 1, 2, 3, 4, 5]]
# # >>> print(listx)
# # [['Hello', 'World'], [0, 1, 2, 3, 4, 5]]
# # >>> listx = [["Hello", "World"], [0, 1, 2, 3, 3, 5]]
# # >>> print(listx)
# # [['Hello', 'World'], [0, 1, 2, 3, 3, 5]]
# # >>> print(listx[0][1])		#The first [] indicates the index of the outer list.
# # World
# # >>> print(listx[1][3])		#the second [] indicates the index nested lists.
# # 3
# # >>> listx.append([True, False])		#add new items
# # >>> print(listx)
# # [['Hello', 'World'], [0, 1, 2, 3, 3, 5], [True, False]]
# # >>> listx[1][2]=4
# # >>> print(listx)
# # [['Hello', 'World'], [0, 1, 4, 3, 3, 5], [True, False]]		#update value items
#
#
#
# # listy = list("HELLO WORLD")
# # >>> print(listy)
# # ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
# # >>> index = listy.index("L")	#get index of the first item whose value is passed as parameter
# # >>> print(index)
# # 2
# # >>> index = listy.index("L", 4)	#define the index from which you want to search
# # >>> print(index)
# # 9
# # >>> index = listy.index("O", 3, 5)	#define the segment of the list to be searched
# # >>> print(index)
# # 4
#
#
# # import itertools
# #
# # a = [[10, 20], [30, 40], [50]]
# # for j in (itertools.chain.from_iterable(a)):
# #     print(j)
# #
# # print(list(itertools.chain.from_iterable(a)))
# # 10
# # 20
# # 30
# # 40
# # 50
# # [10, 20, 30, 40, 50]
#
# # copy
# # deepcopy
#
# #
# # append()	The append() function adds an element at the end of the list.
# # clear()	Removes all the elements from the list.
# # copy()	Returns a copy of the list.
# # count()	Returns the number of elements with the specified value.
# # extend()	Add the elements of a list (or any iterable), to the end of the current list.
# # index()	Returns the index of the first element with the specified value.
# # insert()	Adds an element at the specified position.
# # pop()	Removes the element at the specified position.
# # remove()	Removes the item with the specified value.
# # reverse()	Reverses the order of the list.
# # sort()	Sorts the list.
#
#
#
# # adding list to a list
# # colors list
# # colors = ['Red', 'Green', 'Black']
# # nums = [1, 2, 3]
# # print("Original lists:")
# # print(colors)
# # print(nums)
# # print("Append nums to colors:")
# # colors.append(nums)
# # print("New list:",colors)
#
#
#
#
# # Add each element of a string to a list
# #
# # # colors list
# # colors = ['Red', 'Green', 'Black']
# # print("Original list:")
# # print(colors)
# # text = "Pink"
# # print("String to add:")
# # print(text)
# # print("Add each element of the said string to the colors list:")
# # colors.extend(text)
# # print(colors)
#
# # Original list:
# # ['Red', 'Green', 'Black']
# # String to add:
# # Pink
# # Add each element of the said string to the colors list:
# # ['Red', 'Green', 'Black', 'P', 'i', 'n', 'k']
#
# #
# # def test(data):
# #   return data['Math']
# # students = [
# #   {'V': 'Jenny Vang', 'Math': 99},
# #   {'V': 'Allan Barker', 'Math': 100},
# #   {'V': 'Bradley Whitney', 'Math': 97},
# #   {'V': 'Ellie Ross', 'Math': 98},
# #   {'V': 'Antoine Booker', 'Math': 99}
# # ]
# # print("Original students list:")
# # print(students)
# # students.sort(key=test)
# # print("\nStudents list after sorting on Math marks:")
# # print(students)
# def f(a, b, c):
#   a = a + 1
#   b.append(3)
#   c = c + [3]
#
# a = 7
# b = [1, 2]
# c = [1, 2]
# f(a, b, c)
# print(a, b, c)


# x = [1, 2, 3]
#
# x1 = [1] + x[1:]
# x2 = x[:2] + [x[-1]]
#
# print (x1, id(x1) == id(x))
# print (x2, id(x2) == id(x))
# print ( id(x1) == id(x2) )

#
# class A():
#   def f(self, a):
#     a = a + 1
#
#   def h(self, l1, l2):
#     a = l1[0]

# f(a)
# l1[0] = a
# l2 = l2 + l1
# a = A()
# l1 = [1]
# l2 = []
# a.h(l1, l2)
# print(l1, l)
# def f(a):

#   a['a'] = 1
#   a['e'] = 3
#
#
# a = {}
# f(a)
# a['b'] = 2

#
# def f5(l, n):
#     for i in range(len(l)):
#         l[i] += [n]
#
# def g5(l):
#     l=l[::-1]
#
# def h5(n):
#     n=n*n
#
# def m5():
#     lf=[1,2,3]
#     lg=[1,2,3]
#     n=3
#     f5(lf,n)
#     g5(lg)
#     h5(n)
#     print(lf,lg,n)
#
# m5()


# def f(a):
#     if a>1:
#         return a*g(a)
#     return 1
#
# def g(a):
#     if a == 0:
#         return 1
#     return f(a-1)
#
# print(f(2)==g(2))
# print(id(f(2))==id(g(2)))
# print(g(f(1))==f(g(2)))
# print(id(g(f(1)))==id(f(g(2))))
# print(g(2))
# print(f(1))
