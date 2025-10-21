import string

password = input("Введите пароль: ")
errors = []


if len(password) < 8:
    errors.append("длина менее 8 символов")


if not any(char.isupper() for char in password):
    errors.append("отсутствуют заглавные буквы")


if not any(char.islower() for char in password):
    errors.append("отсутствуют строчные буквы")


if not any(char.isdigit() for char in password):
    errors.append("отсутствуют числа")


special_chars = set(string.punctuation) #
if not any(char in special_chars for char in password):
    errors.append("отсутствуют специальные символы")

if errors:
    error_list = ", ".join(errors)
    print(f"Пароль ненадежный: {error_list}")
else:
    print("Пароль надежный")
