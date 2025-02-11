names = ['Arya', 'Samson', 'Dora', 'Ollivander']
print(max(names, key=lambda n:len(n)))

import keyword
def contains_keyword(*args):
    if any(x for x in args if keyword.iskeyword(x)):
        return True
    return False

