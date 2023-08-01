 while True:
     user_input = input("Введіть слово, в якому є літера 'о': ")
     if 'о' in user_input.lower():
         print("Дякую! Ви ввели слово з літерою 'о'.")
         break
     else:
         print("Спробуйте ще раз. Введіть слово з літерою 'о'.")



lst1 = ['2', 'цуацау', 3, True, 'False', 5, '6', 'wefewf5', 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [i for i in lst1 if isinstance(i, str)]
print(lst2)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in numbers_list:
    if number % 2 == 0:
        sum += number
print("Сума парних чисел у списку:", sum)
