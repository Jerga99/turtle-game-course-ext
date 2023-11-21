

# simple_add = lambda x,y:  x + y
# print(simple_add(3, 5))


def increment_numbers(x: int, y: int, inc: int, compute):
    result = compute(x, y)
    inc_result = result * inc

    return lambda custom_text: print(f'{custom_text}, result is: {inc_result}')

def add(x: int, y: int):
    result = x + y
    return result

def multiply(x: int, y: int):
    result = x * y
    return result

results_2 = increment_numbers(multiply(5, 2), add(2, 4), 10, lambda x, y: x ** y)
results_2('whatever')



# results_1 = increment_numbers(5, 2, 10, lambda x, y: x * y)
# results_1('something')
# show_results = increment_numbers(5, 2, 10, lambda x, y: x + y)
# show_results('Write here something')
