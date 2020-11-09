from balanced_brackets import check_balanced_brackets
from stacks import Stack

def decimalToBinaryConverter(decimal_number):
    if not isinstance(decimal_number, int): 
        raise Exception('Invalid object provided for conversion, valid datatype in INT')
    
    bin_stack = Stack()
    quotient = decimal_number
    remainder = None
    while quotient > 0:
        remainder = int(quotient % 2)
        quotient = int(quotient / 2)
        bin_stack.push(remainder)
    return str(bin_stack)

if __name__ == "__main__":
    dec_num = 15
    bin_conv = decimalToBinaryConverter(dec_num)
    print(f"Number: {dec_num}, binary_format: {bin_conv}, reverse_conv:{int(bin_conv, 2)}")