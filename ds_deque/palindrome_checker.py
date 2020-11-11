from mydeque import Deque

def check_palindrome(check_str) -> bool:
    ch_deque = Deque() 
    for letter in check_str:
        ch_deque.addFront(letter)
    
    while ch_deque.size() > 1:
        if not ch_deque.removeFront() == ch_deque.removeRear():
            return False
    return True

if __name__ == "__main__":
    print(check_palindrome('radars'))