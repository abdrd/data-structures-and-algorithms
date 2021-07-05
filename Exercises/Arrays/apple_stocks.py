"""
https://www.interviewcake.com/question/python/stock-price

https://prnt.sc/18qdn6b

Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called sp, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means sp[60] = 500.

Write an efficient function that takes sp and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

# ! Gotchas
You can't just take the difference between the highest price and the lowest price, because the highest price might come before the lowest price. And you have to buy before you can sell.
"""
# * O(n) Linear time complexity
def most_profitable(sp: list) -> int:
    if len(sp) == 0 or len(sp) == 1:
        raise Exception("list must contain at least 2 items")

    min_value = sp[0]
    profit = sp[1] - sp[0]

    for i in range(len(sp)):
        if sp[i] - min_value > profit:
            profit = sp[i] - min_value
        if sp[i] < min_value:
            min_value = sp[i]
    
    return profit

"""
Second version with a O(n^2) time complexity
"""
def mp(sp: list) -> int:
    profit = 0

    for i in range(len(sp)):
        for j in range(i + 1, len(sp)):
            cur_profit = sp[j] - sp[i]
            if cur_profit > profit:
                profit = cur_profit

    return profit

d1 = [1, 2, 51, 12, 66, 10, 0]
d2 = [5, 12, 5, 5, 17, -2]
d3 = [14, 62, 9, -5, -15]
d4 = [1]
d5 = [3, 5]
d6 = [1, 24, 0, 66]
d7 = [10, 9, 8, 4, 1, 0]

print(most_profitable(d1))  # 65
print(most_profitable(d2))  # 12
print(most_profitable(d3))  # 48
#print(most_profitable(d4)) # Exception
#print(most_profitable(d5)) # Exception
print(most_profitable(d6))  # 66
"""
this returns 0
which is not expected. (we expected to get -1)
"""
print(most_profitable(d7))  # -1

print(mp(d1))  # 65
print(mp(d2))  # 12
print(mp(d3))  # 48
#print(mp(d4)) # Exception
#print(mp(d5)) # Exception
print(mp(d6))  # 66
print(mp(d7))  # -1