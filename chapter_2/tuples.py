# storing lat/longitude
lax_coordinates = (33.9425, -118.408056)

# multiple assignment from tuple
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)


traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# iterating over traveler_ids, passport assigned to each tuple
for passport in sorted(traveler_ids):
    # formatting operator understands tuples - treats each item as separate field
    print('%s/%s' % passport)

# for loop can unpack tuple
for country, _ in traveler_ids:
    print(country)

# Reference to mutable object in a tuple changing
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)
b[-1].append(99)
print(a == b)
print(b)

# determine if tuple has a fixed value using hash


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
print(fixed(tf))
print(fixed(tm))
