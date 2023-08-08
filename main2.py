from main import process_arguments

arg1 = 5
arg2 = 3.5
result = process_arguments(arg1, arg2)
print(result)

arg1 = "Hello, "
arg2 = "world!"
result = process_arguments(arg1, arg2)
print(result)

arg1 = [1, 2, 3]
arg2 = {"a": 1, "b": 2}
result = process_arguments(arg1, arg2)
print(result)