#Question1
numbers=[10,20,30,40,50]
for i in numbers:
    print(i*2)
total_sum= sum(numbers)
print("Sum of all numbers is: ",total_sum)


# QUESTION2
numbers = [5, 12, 17, 24, 35]

# Filter numbers greater than 15
filtered_list = [num for num in numbers if num > 15]

# Square all numbers in the filtered list
squared_list = [num**2 for num in filtered_list]
print("Filtered List:", filtered_list)
print("Squared List:", squared_list)

#QUESTION3
list1= ["apple", "Banana", "cherry", "Date"]
list1.append("orange")
print("Your list1 is at initial satge is: ")
print(list1)

list1.insert(2,"orange")
print("The list afte removing 'Orange' is :")
print(list1)

list1.remove("Date")
print("Your list after removing 'Date' is: ")
print(list1)

#QUESTION4
list1= [42,12, 89, 33,7]
print("Your list before sorting is")
print(list1)
list1.sort(reverse=True)
print("Your list after sorting is")
print( list1)

# using reverse() method

list1.reverse()
print("The list in reverse order is:")
print(list1)

#QUESTION5
#create list
mylist= ["EMMA", "OLIVIA", "LIAM", "NOAH", "SOPHIA"]

# sort in alphanumeric order
mylist.sort()
print("Your list in alphanumeric order")
print(mylist)
# sort in reverse order
mylist.reverse()
print("Your list in Reverse order")
print(mylist)

#add james
mylist.append("JAMES")
print("Your list after adding JAMES")
print(mylist)

#sort after james 
mylist.sort()
print("Your list in alphanumeric order after adding JAMES")
print(mylist)

#reverse after james
mylist.reverse()
print("Your list after adding JAMES in reverse order")
print(mylist)

#QUESTION6
list1= [50, 10, 70, 30, 90]
print("Your list before sorting: ")
print(list1)
list1.sort(reverse=True)
print("Your list afetr sorting in Descending order: ")
print(list1)

list2= ["dog", "cat", "zebra", "elephant", "ant"]
print("Your list items in list2  are: ")
print(list2)
list2.sort()
list2.reverse()
print("Your list in reverse alphabetical order")
print(list2)
