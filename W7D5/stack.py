stack = list()
#stack = bottom[8,5,6,3,9]top

def peek():
    if isEmpty():
        return None
    return stack[-1] #stack[len(stack)-1]

def isEmpty():
    return len(stack) == 0

def push(x):
    stack.append(x)

def pop():
    if isEmpty():
        return None
    stack.pop()

push(10)
push(5)
push(77)
print(stack)
pop()
print(stack)
print(peek())
print(stack)
print(isEmpty())
