sampleDictionary = {
    'fdag' : 'asda',
    'sdfh' : 'fgdf',
    'sadg' : {
        'want' : '7391',
        'fdag' : {
            'gfhj' : 'sadf',
            'want' : '4567',
            'gser' : {
                'lkjf' : 'vfrt',
                'want' : '8523',
                'lsae' : 'sdgh' },
            'want' : '3568' },
        'hgfd' : 'dfhj' },
    'jkfd' : 'jfdk',
    'want' : '6524' }

def dictSearch(myDict):
    for key, value in myDict.items():
        if isinstance(value, dict):
            dictSearch(value)
        else:
            if key == 'want':
                print(value)

dictSearch(sampleDictionary)

myjson = {
    'transportation': 'car',
    'address': {
        'driveway': 'yes',
        'home_address': {
            'state': 'TX',
            'city': 'Houston'}
    },
    'work_address': {
        'state': 'TX',
        'city': 'Sugarland',
        'location': 'office-tower',
        'salary': 30000}
}
def get_keys(some_dictionary, parent=None):
    for key, value in some_dictionary.items():
        if '{}.{}'.format(parent, key) not in my_list:
            my_list.append('{}.{}'.format(parent, key))
        if isinstance(value, dict):
            get_keys(value, parent='{}.{}'.format(parent, key))
        else:
            pass
my_list = []
get_keys(myjson, parent='myjson')
print(my_list)

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
dicc = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(dicc)

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
