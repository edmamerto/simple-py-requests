# Count how many users are male or female 
[![Build Status](https://travis-ci.com/edmamerto/simple-py-requests.svg?branch=master)](https://travis-ci.com/edmamerto/simple-py-requests)
> This projects demonstrates how to call an api and do simple aggregation

In this project you will:

1. **GET** *users* data 
- API: https://jsonplaceholder.typicode.com/users
2. Extract *names* from the response
3. Use extracted name to **GET** *gender* 
- API: https://api.namsor.com/onomastics/api/json/gender/ed/mamerto 

check it out   >>> [requests_sample.py](https://github.com/edmamerto/simple-py-requests/blob/master/requests_sample.py)

## Install
Python `2` was used for this project
```sh
$ pip install virtualenv
$ cd path/to/proj
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
**note use name `venv` when you setup your virtualenv as this is `gitignored`*

## Run
Run the script
```sh
$ python sample_requests.py
```
to exit out of virtualenv
```sh
$ deactivate
```
Example Output
```sh
there are 3 males and 7 females
```

## License
Copyright © Ed Mamerto.
