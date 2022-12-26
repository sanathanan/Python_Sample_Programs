""""
Best Time to Buy and Sell Stocks

Logic:
Input_list = [7,1,5,3,6,4]
It will check for minimum value and maximum value.
1st iteration: min_val =7, max_val=7, profit = 7-7 =0
2nd iteration: min_val =1, max_val=1, profit = 1-1 =0
3rd iteration: min_val =1, max_val=5, profit = 5-1 =4
4th iteration: min_val =1, max_val=3, profit = 3-1 =2
5th iteration: min_val =1, max_val=6, profit = 6-1 =5
6th iteration: min_val =1, max_val=4, profit = 4-1 =3

So, Maximum profit is '5' at the 5th iteration.
"""

prices =[7,1,5,3,6,4]

min_price = float('inf') # Declaring minimum value as infinity
max_profit = 0 # Maximum profit is set to 0

for i in prices:
    min_price = min(i, min_price) # Finding the minimum from the iterated value and min_price
    max_profit = max(i-min_price, max_profit) # finding the maximum from the max_profit and selling value i.e(iterated value - min_price)
print(max_profit)