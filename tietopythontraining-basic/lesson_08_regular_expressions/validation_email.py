import re

# accepted - in the middle:
# Uppercase and lowercase letters in English (A-Z, a-z)
# Digits from 0 to 9
# Special characters such as ! # $ % & ' * + - / = ? ^ _ ` { |

# DO NOT USE
# < > ( ) [ ] ; : , @ \ SPACE

# DO NOT USE AS FIRST char
# hyphens ( – ),
# underscores ( _ ),
# periods ( . ),
# and numeric characters (“0” through “9”) _ informal rule


def validation(email) :
    count_symbol = re.findall("@", email)
    # INFORMAL RULE - which start with numbers look awkward.
    regex_numeric = r"^[0-9]"
    regex_char = r"^[_.-]"
    regex_other = r"[\[\]<>();:,@\\]"
    regex_special = r"[!#$%&'*+/=?^_`{|]"
    # \] -> ]
    # \[ -> [
    # \\ -> \
    regex_space = ' '

    # if @ more then 1
    if 0 < len(count_symbol) < 2 :
        alias, domain = email.split("@")
        try :
            hosting, *top_level = domain.split(".")
            # top_level [co,uk]
            for tld in top_level :
                if len(tld) < 1 :
                    return False
        except ValueError :
            return False
        if len(alias) < 2 or \
                len(hosting) < 1 or \
                len(top_level) < 1 or \
                re.search(regex_numeric, alias) or \
                re.search(regex_space, alias) or \
                re.search(regex_char, alias) or \
                re.search(regex_other, alias) or \
                re.search(regex_other, domain) or \
                re.search(regex_space, domain) or \
                re.search(regex_special, domain):
            return False
        else :
            return True
    else :
        return False


if __name__ == '__main__' :
    if validation("1alias@domain.pl") :
        print("ok")
    else :
        print("incorrect")
