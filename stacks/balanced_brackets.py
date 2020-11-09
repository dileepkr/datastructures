from stacks import Stack

def pair_match(symbol1, symbol2):
    pair_dict = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    return pair_dict[symbol1] == symbol2 
    # return ord(symbol1) == ord(symbol2) 

def check_balanced_brackets(bracket_str):
    bracket_list = list(bracket_str)
    bracket_stack = Stack()
    for symbol in bracket_list:
        if symbol in ['(','{','[']:
            bracket_stack.push(symbol)
            continue
        elif symbol in [')','}',']']:
            if not bracket_stack.is_empty() and pair_match(symbol, bracket_stack.peak()):
                bracket_stack.pop()
            else:
                return False
        else:
            raise Exception('Invalid symbol found')
    return bracket_stack.is_empty()

if __name__ == "__main__":
    print(check_balanced_brackets('((()))'))
    print(check_balanced_brackets('([{}])'))
    print(check_balanced_brackets('([{]})'))
    print(check_balanced_brackets('([{])'))
    print(check_balanced_brackets('((((()()()()))'))