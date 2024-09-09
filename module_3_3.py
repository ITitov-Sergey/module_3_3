def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params("str", b = 25)
print_params(c = [1, 2, 3])
print_params()

values_list = [1, "str", False]
values_dict = {'a': 3, 'b': "STR", 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 2.5]
print_params(*values_list_2, 42)
