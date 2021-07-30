import re


def solution(new_id):

    # step 1
    new_id = new_id.lower()

    # step 2
    new_id = "".join(re.findall('[a-zA-Z0-9._-]', new_id))

    # step 3
    while re.search('[.]{2}', new_id) is not None:
        new_id = new_id.replace('..', '.')

    # step 4
    if len(new_id) >= 1 and new_id[0] == ".":
        new_id = new_id[1:]

    if len(new_id) >= 1 and new_id[-1] == ".":
        new_id = new_id[:-1]

    # step 5
    if len(new_id.strip()) == 0:
        new_id = 'a'

    # step 6
    if len(new_id.strip()) >= 16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]

    # step 7
    if len(new_id) <= 2:
        ch = new_id[-1]
        while len(new_id) != 3:
            new_id += ch

    return new_id