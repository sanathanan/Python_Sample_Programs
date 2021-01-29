# Sum of even numbers and odd numbers in list using for loop
lst=[1,2,3,4,5,6,7,8,9,10]
even_sum =0
odd_sum =0
    
for i in lst:
    if i%2 ==0:
        even_sum = even_sum+i
    else:
        odd_sum = odd_sum+i

print("The even number sum is:", even_sum)
print("The odd number sum is:", odd_sum)


# Sum of the even and odd numbers from the maximum given number
num = int(input("Enter the maximum number: "))
even_sum=0
odd_sum =0

for i in range(1,num+1):
    if i%2 == 0:
        even_sum+=i
    else:
        odd_sum+=i
        
print("The even number sum between the number from 0 to {0} is: {1}".format(i,even_sum))
print("The even number sum between the number from 0 to {0} is: {1}".format(i,odd_sum))
        

# sum of even numbers and odd numbers in list using list comprehension
lst=[1,2,3,4,5,6,7,8,9,10]

even_sum=sum(i for i in lst if i%2==0)
odd_sum=sum(i for i in lst if i%2!=0)

print("The even number sum is:", even_sum)
print("The odd number sum is:", odd_sum)