import logging

logging.basicConfig(filename='logs/test.log', level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s')

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logging.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logging.debug(f'Div: {num_1} / {num_2} = {div_result}')
