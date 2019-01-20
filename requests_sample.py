"""
@author Ed Mamerto
"""
import requests
import json

GENDER_STATS = {
    'male': 0,
    'female': 0
}


def check_gender(name):
    """
Checks if name is a male or female name

Parameters:
name (list): first name (index 0),  last name (index 2)

Returns:
string: 'male' or 'female'

"""
    response_data = requests.get(
        'https://api.namsor.com/onomastics/api/json/gender/' +
        name[0] +
        '/' +
        name[1])
    obj = json.loads(response_data.text)

    return obj['gender']


def count_genders():
    """
counts how many users are male and female

Returns:
string: gender stats
"""
    response_data = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(response_data.text)

    for user in users:
        # split name on white space to save first and last name in an array
        name = user['name'].split()
        GENDER_STATS[check_gender(name)] += 1

    return 'there are ' + \
        str(GENDER_STATS['male']) + ' males and ' + str(GENDER_STATS['female']) + ' females'


if __name__ == "__main__":
    print count_genders()
