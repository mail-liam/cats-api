import csv
import json
import os

data = []
os.chdir('tests')

with open('cats_test.csv', 'r', newline='') as file:
    csv_data = csv.reader(file, quotechar="'", escapechar="\\", skipinitialspace=True)

    for num, line in enumerate(csv_data):
        if len(line) != 8:
            #  Skip blank lines in file
            continue

        id, text, fact_type, user_id, user_firstname, user_lastname, upvotes, user_upvoted = line
        data.append({
            '_id': id,
            'text': text,
            'type': fact_type,
            'user': {
                '_id': user_id,
                'name': {
                    'first': user_firstname,
                    'last': user_lastname,
                },
            },
            'upvotes': upvotes,
            'userUpvoted': user_upvoted,
        })

data.pop(0)  # Hacky skip of headers

with open('cats_test.json', 'w') as file:
    json.dump(data, file, indent=2)
