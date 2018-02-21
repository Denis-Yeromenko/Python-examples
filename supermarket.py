
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

# For manager
total = 0
for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  total_key = prices[key] * stock[key]
  print('total: %s' % total_key )
  total += total_key
print (total)


# for shopper
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    print(total)
    return total



compute_bill(shopping_list)
