data = [
    {
        '_id': 1,
        'name': 'Emmanuel',
        "age": 19
    },
    {
        "_id": 2,
        'name': 'Sampa',
        "age": 20
    },
    {
        "_id": 3,
        'name': 'Mutale',
        "age": 21
    }
]

data = list(filter(lambda d: d['_id'] != 1, data))
print(data)
