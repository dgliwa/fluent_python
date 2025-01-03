# builds a tuple from a generator expression
import array
symbols = '$¢£¥€¤'
tuple(ord(s) for s in symbols)

# build an array from a generator expression
symbols = '$¢£¥€¤'
array.array('I', (ord(s) for s in symbols))


# use generator expression to print strings instead of building entire cartesian product in memory
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
