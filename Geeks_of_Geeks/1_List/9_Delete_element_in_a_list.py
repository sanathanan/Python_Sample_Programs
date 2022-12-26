# Clear / Delete element in a list


lst_1 =[1,2,3,4,5,6,7,8]
lst_2 =[1,2,3,4,5,6,7,8]
lst_3 =[1,2,3,4,5,6,7,8,9]

print("------------Method 1 ---------------")
print("Given List: ", lst_1)
res = lst_1.clear()
print("Cleared List: ", res)

print("------------Method 2 ---------------")
print("Given List: ", lst_2)
del lst_2[:]
print("Cleared List: ", lst_2)

print("------------Method 3 ---------------")
print("Given List: ", lst_3)
res1 = lst_3.pop()
res1 = list(map(int, str(res1)))
res2 = res1.clear()
print("Cleared List: ", res2)
