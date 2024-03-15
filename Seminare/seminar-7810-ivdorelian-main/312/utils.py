def clear_file(filename):
    with open(filename, 'w'):
        pass


lst = [2, 4, 6, 4, 2, 1, 7, 8, 2]


def my_sorted(iterable, *, key=lambda x: x, reverse=False):
    return iterable


print(sorted(lst, key=lambda x: -x, reverse=True))
print(my_sorted(lst, key=lambda x: -x, reverse=True))
