set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection)

union = set1.union(set2)
print("Union of set1 and set2:", union)

difference = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", difference)

symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference)

print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))

