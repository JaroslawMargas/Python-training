find_word = []

# build list of the word for replacing
rep_word = open("replace.txt" , "r")
for line in rep_word:
    for word in line.split(","):
        find_word.append(word)
rep_word.close()

# open input file and create string text
in_file = open("input.txt", "r")
in_text = in_file.read()
in_file.close()

# iterate through word in list and replace it with input
for word in find_word:
    new_word = str(input("replace {}:".format(word)))
    in_text = in_text.replace(word, new_word)

# save new replaced string to new output file
out_file = open("output.txt","w")
out_file.write(in_text)
out_file.close()


