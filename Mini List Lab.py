# 1.Create a list with the numbers 10 - 20 in it.
mylist1 = range(10, 21)
print(mylist1)
#2.Create a list of 5 in length, filled with 0s.
mylist2 = [0,0,0,0,0]
print(mylist2)
#3. Create an empty list.
mylist3 = []
print(mylist3)
#4.Repeat question 2 using a loop (if you didn't already)
mylist4 = []
while len(mylist4)<6:
    mylist4.append(0)
print(mylist4)
#5. Get the length of this list: ["a", 5, "doodle", 3, 10]
mylist5 = ["a", 5, "doodle", 3, 10]
print(len(mylist5))
#6. Remove the 3rd element of this list: ["a", 5, "doodle", 3, 10]
mylist6 = ["a", 5, "doodle", 3, 10]
del mylist6[2]
print (mylist6)
#7. Add another element to the end of the list from question 5.
mylist5.append(5)
print (mylist5)
#8. Replace the first element of the list with question 5 with 8.4
mylist5[0] = 8.4
print (mylist5)
#9.  Add another element, of your choice, to the beginning the list from question 5.
mylist5.insert(0,1)
print (mylist5)
#10. Create a list and add only the odd numbers of 1-10 to the list in a loop.  
mylist10 = []
for i in range(1,11):
    if i%2 != 0:
       mylist10.append(i)
print (mylist10)