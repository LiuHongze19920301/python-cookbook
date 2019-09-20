# example.py
#
# Example of calculating with dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'KAA': 10.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)

prices_sorted_map = {val: key for key, val in prices_sorted}
print(prices_sorted_map)

prices_sorted_map = {val: key for key, val in prices_sorted if key > 20}
print(prices_sorted_map)

prices_sorted_map = {val: key for key, val in prices_sorted if key > 20 if val.startswith('K')}
print(prices_sorted_map)

prices_sorted_map = {val: key for key, val in prices_sorted if 20 < key < 500}
print(prices_sorted_map)

prices_sorted_map = {val: str(val) + '-' + str(key) for key, val in prices_sorted if 20 < key < 500}
print(prices_sorted_map)
