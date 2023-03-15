"""
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)

Example:
Input:
N = 5
Output: 15
Explanation: For n = 5, sum will be 1 + 2 + 3 + 4 + 5 = 15.
"""

#  Method 1
def seriesSum(n):
    count = 0
    for i in range(1, n+1):
        count = count + i

    return count

#  Method 2
def seriesSum2(n):
    count = []
    for i in range(1, n+1):
        count.append(i)

    return sum(count)

#  Method 3
def seriesSum3(n):

    # formula to calculate sum of 'n' natural numbers is n((n+1)/2)
    result_3 = int(n*((n+1)/2))

    return result_3

# Driver Code
n = 10

result = seriesSum(n)
print(result)

result_2 = seriesSum2(n)
print(result_2)

result_3 = seriesSum3(n)
print(result_3)