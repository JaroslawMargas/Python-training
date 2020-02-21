import pickle


def store_data():
    # initializing data to be stored in db
    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
             'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
               'age': 50, 'pay': 50000}

    # database
    db = {'Omkar': Omkar, 'Jagdish': Jagdish}

    # Its important to use binary mode
    db_file = open('examplePickle', 'ab')

    # source, destination
    pickle.dump(db, db_file)
    db_file.close()


def load_data():
    # for reading also binary mode is important
    db_file = open('examplePickle', 'rb')
    db = pickle.load(db_file)
    # for keys in db:
    #     print(keys, '=>', db[keys])
    for keys, value in db.items():
        print(keys, '=>', value)
    db_file.close()


if __name__ == '__main__':
    store_data()
    load_data()
