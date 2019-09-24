# Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice
# tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the
# provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions Beatrice,
# totally confused, asks you to help her determine Augustus's secret number.
#
# Given the value of n in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated
# by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all
# the remaining possible secret numbers, in ascending order, separated by a space.


def print_error():
    print("this value is incorrect, try again")


while True:
    try:
        n = int(input("Augustus, provide range of set."))
        secret_set = set(range(1, n + 1))
        break
    except ValueError:
        print_error()

while True:
    guess_input = input("Beatrice, please provide your answer set")
    if guess_input == "HELP" :
        break
    else:
        answer_input = input("Augustus, is your value  included in this set ?")
        try:
            guess_set = set(int(x) for x in guess_input.split())
            if answer_input == "yes" :
                # take a intersection of  Augustus set and Beatrice answer set
                secret_set &= guess_set
            elif answer_input == "no" :
                # from the Augustus set deduct Beatrice answers
                secret_set -= guess_set
        except ValueError:
            print_error()


for elem in secret_set :
    print("".join(str(elem)))
