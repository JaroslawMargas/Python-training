def change_to_upper_case(text):
    new_upper = ""
    x = 0
    for i in text:
        # if it's a char [a-z or A-Z]
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            # for the fist sing
            if x == 0:
                # if first is upper then do not convert
                if 65 <= ord(i) <= 90:
                    i = ord(i)
                else:
                    # if first is not upper then convert
                    i = ord(i) - 32
            else:
                # not first then no convert
                i = ord(i)
        else:
            # it's some different char the do not convert
            i = ord(i)
        x += 1
        new_upper = new_upper + chr(i)
    return new_upper


string_to_split = str(input("Provide string to conversion: "))

list_split = string_to_split.split(" ")

new_text = ""
for word in list_split:
    changed = change_to_upper_case(word)
    new_text += changed + str(" ")

# remove last space
final_text = new_text.rstrip()
print(final_text)
