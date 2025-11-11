tuple_of_elements = (110,123,33,4,57,123, 'gfhfh')

print(f'Данный кортеж: {tuple_of_elements}')

tuple_only_of_int = all(isinstance(item, int) for item in tuple_of_elements)

if(tuple_only_of_int):
    result = tuple(sorted(tuple_of_elements))
else:
    result = tuple_of_elements

print(f'Результат операции: {result}')