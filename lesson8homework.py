def number_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


start = 1
end = 10

for number in number_generator(start, end):
    print(number)
