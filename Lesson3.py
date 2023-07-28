# Homework from Yaroslav Baltak
unique = input("Введіть строку: ")
unique_chars = set(unique)
if len(unique_chars) > 10:
    print(True)
else:
    print(False)