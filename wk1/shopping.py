shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for i in food:
        total += prices[i]
        print 'The key represented by i is %s' % i
        print 'The number of %ss in stock is %s' % (i, stock[i])
        print 'The price of %ss in stock is $%s' % (i,prices[i])
    return total

print 'The total of your shopping is $%s' % compute_bill(shopping_list)
