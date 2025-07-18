

def apply_operation(operation, numbers):
    result = []
    for num in numbers:
     result.append(operation(num))
    return result
    
def double(x):
    return x * 2
    

numbers_list = [1,2,3,4,5,6]


double_numbers = apply_operation(double, numbers_list)

print(f'Original Numbers: {numbers_list}')
print(f'Double Numbers: {double_numbers}')