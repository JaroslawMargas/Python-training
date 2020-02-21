import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

print(deck)
# [(1,A),(1,B),...(n,n)]

# [(1, 'Spade'), (1, 'Heart'), (1, 'Diamond'), (1, 'Club'), (2, 'Spade'), (2, 'Heart'), (2, 'Diamond'), (2, 'Club'),
# (3, 'Spade'), (3, 'Heart'), (3, 'Diamond'), (3, 'Club'), (4, 'Spade'), (4, 'Heart'), (4, 'Diamond'), (4, 'Club'),
# (5, 'Spade'), (5, 'Heart'), (5, 'Diamond'), (5, 'Club'), (6, 'Spade'), (6, 'Heart'), (6, 'Diamond'), (6, 'Club'),
# (7, 'Spade'), (7, 'Heart'), (7, 'Diamond'), (7, 'Club'), (8, 'Spade'), (8, 'Heart'), (8, 'Diamond'), (8, 'Club'),
# (9, 'Spade'), (9, 'Heart'), (9, 'Diamond'), (9, 'Club'), (10, 'Spade'), (10, 'Heart'), (10, 'Diamond'), (10,
# 'Club'), (11, 'Spade'), (11, 'Heart'), (11, 'Diamond'), (11, 'Club'), (12, 'Spade'), (12, 'Heart'), (12,
# 'Diamond'), (12, 'Club'), (13, 'Spade'), (13, 'Heart'), (13, 'Diamond'), (13, 'Club')]
