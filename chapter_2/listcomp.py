# non-listcomp
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# list comp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# walrus operator := to set a var outside the local scope of the comprehension
x = 'ABC'
codes = [last := ord(c) for c in x]
print(last)

# using listcomp to replace map -> filter
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# build the cartesian product of two iterables
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
# note the order of the loops (sizes is the inner loop)
