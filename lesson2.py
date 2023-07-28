# print("S" in 'My name is Yaroslav') # перевірка чи входить, регістрочутливе
#
# test_string = 'My name is Yaroslav. my age is '

# print(test_string.upper())
# #MY NAME IS YAROSLAV
#
# print(test_string.lower())
# #my name is yaroslav
#
# print(test_string.startswith('My')) #перевіряє чи починається з
# print(test_string.startswith('name',3)) #старт з 3 символа (рахунок з 0)
# print(test_string.endswith('av')) #перевіряє чи закінчується з
# print(test_string.endswith('av'))
#print(test_string + str(26))
#print(test_string + '26')

# test_stringp = 'My name is Yaroslav. my age is %s'  # %s означає, що вставка тут
# procent_result = test_stringp % 26
# print(procent_result)

# test_stringf = 'My name is Yaroslav. my age is {}, i live in {}' вставляє значення по порядку
# format_result = test_stringf.format(26, 'Vin')
# print(format_result)

# test_stringf2 = 'My name is Yaroslav. my age is {age}, i live in {city}' вставляє значення по
# format_result2 = test_stringf2.format(city = 'Vin', age = 26)                     назві
# print(format_result2)

# my_age: int = 26
# city = 'Vin'
# test_stringfstr = f'My name is Yaroslav. my age is {my_age}, i live in {city}' # вставляє змінні
# print(test_stringfstr)
# print(test_stringfstr.capitalize()) #-робить  першу літеру велику, всі інші малі
# print(test_stringfstr.title())  # робить кожне слово з великої
# print(test_stringfstr.count('my')) # рахує кількість аргументів у в строці
# print(test_stringfstr.count('My'))
# print(len(test_stringfstr))
# print(test_stringfstr.find('Yar', 8)) # шукає по індексу де початок шукомої фрази, можна задати
                                    #старт пошуку
# strr = 'wef'
# inr = '12d3'
# print(strr.isalpha())    - перевіряє чи всі літери
# print(inr.isnumeric())  - перевіряє чи всі цифри
# print(inr.isalnum())   - перевіряє чи тільки літери і цифри


# rrr = '1234567890'
# # print(rrr[1])   # пише обраний елемент за індексом порядку
# # print(rrr[1:4]) # пище від : до
# # print(rrr[0:9:2]) # пише від : до : з заданим кроком
# # print(rrr[-1])   # якшо з мінусом то початок з кінця
# print(rrr[-1:-10:-2]) # якшо початок з кінця - кожний аргумент має -


# name = 'Yaroslav'
# count = len(name)
# print(f'Word {name} has {count} symbols!')



name1 =input()
count1 = len(name1)
print(f'Word {name1} has {count1} symbols!')
