

def generate_multiplier(factor: int):
    def multiplier(x: int):
        return x * factor
    return multiplier

def generate_incrementer(inc: int):
    def incrementer(x: int):
        return x + inc
    return incrementer

double = generate_multiplier(2)
triple = generate_multiplier(3)
increment_by_five = generate_incrementer(5)

result1 = double(10)
result2 = triple(7)
result3 = increment_by_five(12)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
