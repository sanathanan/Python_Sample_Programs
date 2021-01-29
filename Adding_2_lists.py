# Adding 2 List using List comprehension
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
result= (x+y for x,y in zip(lst1,lst2))
print(list(result))


# Adding 2 list using Map and Zip
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
result= map(sum,zip(lst1,lst2))
print(list(result))

