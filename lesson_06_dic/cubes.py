# Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct
# color, but they want to know how many unique colors exist if they combine their block sets. To determine this,
# the kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried
# up, and you are invited to help them finish the task.
#
# Given two integers that indicate the number of blocks in Alice's and then Bob's sets N
# and M. The following N lines contain the numerical color value for each cube in Alice's set. Then the last M
#
# rows contain the numberical color value for each cube in Bob's set.
#
# Find three sets: the numerical colors of cubes in both sets, the numerical colors of cubes only in Alice's set,
# and the numerical colors of cubes only in Bob's set. For each set, print the number of elements in the set,
# followed by the numerical color elements, sorted in ascending order.

# to do:
# - ask about size of the set for Alice and Bob
# - create sets by asking  user with size
# - the numerical colors of cubes in both sets: common A and B
# - the numerical colors of cubes only in Alice's or Bob set: A -B or B-A


def create_set(size):
    cube_set = set(int(input("provide color for size[" + str(size) + "]")) for _ in range(size))
    return cube_set


def count_common(cube_one, cube_two):
    common = cube_one.intersection(cube_two)
    return common


def only_in(cube_one, cube_two):
    differ = cube_one - cube_two
    return differ


while True:
    try:
        N = int(input("Alice set size"))
        M = int(input("Bob set size"))
        break
    except ValueError:
        print("try again, it's not a proper vale")

alice_cube = create_set(N)
bob_cube = create_set(M)

print(count_common(alice_cube, bob_cube))
print(only_in(alice_cube, bob_cube))
print(only_in(bob_cube, alice_cube))
