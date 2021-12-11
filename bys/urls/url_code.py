import random
from bys.urls import store


def get_url_codes():
    num_code = random.randrange(1296, 60466176)
    if store.num_code_exists(num_code):
        raise ValueError()
    return num_code, _convert_to_alphanum(num_code)


alphanum_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def _convert_to_alphanum(num_code):
    alphanum = []
    if num_code == 0:
        return alphanum_list[0]

    count = len(alphanum_list)
    while num_code:
        alphanum.append(alphanum_list[int(num_code % count)])
        num_code //= count
    return ''.join(reversed(alphanum))
