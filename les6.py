def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

result = fibonacci_recursive(8)
print(result)


# я дуже сподіваюсь, шо це те шо треба...