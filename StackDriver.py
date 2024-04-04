from Stack import Stack

stack = Stack()

print('Stack is empty? Should be True:', stack.is_empty())

# These lines push some numbers onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

print('Stack is empty? Should be False:', stack.is_empty())
print('Stack size. Should be 3:', stack.size())
print('Peeking at the top item, but not popping it! Should be 3:', stack.peek())

print('Popping the top item:', stack.pop())
print('Popping the top item:', stack.pop())
print('Popping the top item:', stack.pop())
print('Stack is empty? should be True', stack.is_empty())
print('Stack size. Should be 0:', stack.size())