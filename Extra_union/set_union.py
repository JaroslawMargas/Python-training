# Intersection returns a new set with elements present in both a and b 
print({1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}))  # {3, 4, 5}
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})  # {3, 4, 5}

# Union  returns a new set with elements present in either a and b
print({1, 2, 3, 4, 5}.union({3, 4, 5, 6}))  # {1, 2, 3, 4, 5, 6}
print({1, 2, 3, 4, 5} | {3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6}

# Difference returns a new set with elements present in a but not in b
print({1, 2, 3, 4}.difference({2, 3, 5}))  # {1, 4}
print({1, 2, 3, 4} - {2, 3, 5})  # {1, 4}

# Symmetric difference with returns a new set with elements present in either a or b but not in both
print({1, 2, 3, 4}.symmetric_difference({2, 3, 5}))  # {1, 4, 5}
print({1, 2, 3, 4} ^ {2, 3, 5})  # {1, 4, 5}

# Superset check tests whether each element of c is in a.
print({1, 2}.issuperset({1, 2, 3}))  # False
print({1, 2}.issuperset({1}))  # True
print({1, 2} >= {1, 2, 3})  # False

# Subset check
print({1, 2}.issubset({1, 2, 3}))  # True
print({1, 2} <= {1, 2, 3})  # True

# Disjoint check
print({1, 2}.isdisjoint({3, 4}))  # True
print({1, 2}.isdisjoint({1, 4}))  # False
