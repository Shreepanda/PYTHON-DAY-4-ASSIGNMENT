n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    elem = input("Enter the element" + str(i+1) + ": ")
    lst.append(elem)

new_lst = list(set(lst))
print("Non-duplicate items:", new_lst)
Enter the number of elements in the list: 7
Enter element1: 10
Enter element2: 20
Enter element3: 20
Enter element4: 30
Enter element5: 40
Enter element6: 40
Enter element7: 50
Non-duplicate items: ['10', '20', '40', '30', '50']
