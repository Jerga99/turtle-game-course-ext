


# def increment_numbers(x: int, y: int, inc: int):
#     result = x + y
#     inc_result = result * inc
#     print(inc_result)

# increment_numbers(5, 2, 10)

def increment_numbers(x: int, y: int, inc: int, compute):
    result = compute(x, y)
    inc_result = result * inc

    def print_results(custom_text: str):
        print(f'{custom_text}, result is: {inc_result}')

    return print_results


def add(x: int, y: int):
    result = x + y
    return result

def multiply(x: int, y: int):
    result = x * y
    return result

show_results = increment_numbers(5, 2, 10, add)
show_results('Write here something')

increment_numbers(5, 2, 10, multiply)
increment_numbers(multiply(5, 2), add(2, 4), 10, multiply)
