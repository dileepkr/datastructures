from myqueue import Queue

def hotPotato(namelist, numrounds):
    namequeue = Queue()
    for name in namelist:
        namequeue.enqueue(name)
    
    while namequeue.size() > 1:
        for i in range(numrounds):
            namequeue.enqueue(namequeue.dequeue())
        namequeue.dequeue()
    
    return namequeue.dequeue()

if __name__ == "__main__":
    print(hotPotato(['a','b','c','d','e','f'], 3))