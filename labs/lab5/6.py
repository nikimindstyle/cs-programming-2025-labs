import random
import string

def generate_random_string(length):  
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choice(characters) for _ in range(length))

dict_of_elements = {}
list_of_elements = []

for i in range(random.randint(1,1000)):
    list_of_elements.append(generate_random_string(random.randint(1,100)))

print(f'Данный список: {list_of_elements}')

for i in list_of_elements:
    dict_of_elements[i] = i

print(f'результат операций: {dict_of_elements}')