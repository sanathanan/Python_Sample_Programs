"""
Execute a given String of code
"""

# Method 1
def execute():
    LOC =  """ 
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
    """

    exec(LOC)

execute()

# Method 2
code = '6+5'
result = eval(code)
print(result)

