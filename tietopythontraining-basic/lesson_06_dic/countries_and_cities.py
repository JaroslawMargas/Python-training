# Given a list of countries and cities of each country. Then given the names of the cities. For each city specify the
# country in which it is located.

while True :
    try :
        M = int(input("How many data to store?"))
        break
    except ValueError :
        print("no correct value")

data_dict = dict()

for i in range(M):
    country, *city = input("{}:". format(i+1)).split()
    data_dict[country] = city

while True :
    try :
        N = int(input("How many cities to find "))
        break
    except ValueError :
        print("no correct value")

res_list = []

for j in range(N):
    find_city = input("city?")
    for key, value in data_dict.items():
        if find_city in value:
            res_list.append(str(key))

for k in res_list:
    print("country: {}".format(k))

