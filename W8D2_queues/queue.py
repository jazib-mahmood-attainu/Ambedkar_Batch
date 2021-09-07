queue = list()

def enqueue(x):
    queue.append(x)

def dequeue():
    if IsEmpty():
        return
    x = queue[0]
    queue.pop(0)
    return x

def IsEmpty():
    return len(queue)==0

enqueue(5)
enqueue(6)
enqueue(8)


print(queue)

print(dequeue())

print(queue)