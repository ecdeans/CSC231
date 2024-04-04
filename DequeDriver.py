from Deque import Deque

deque = Deque()

print('Deque is empty? Should be True:', deque.is_empty())

# These lines add some people to the rear of the deque
deque.add_rear('Horatio')
deque.add_rear('Inez')
deque.add_rear('Jessica')

print('Removing from the end of the deque. Should be Jessica:', deque.remove_rear())

# Add someone to the front of the deque
deque.add_front('ReallyImportantPerson')
print('Removing from the front of the deque. Should be ReallyImportantPerson:', deque.remove_front())


print('deque is empty? Should be False:', deque.is_empty())
print('deque size. Should be 2:', deque.size())

print('Removing from the front of deque. Should be Horatio:', deque.remove_front())
print('Removing from the front of deque. Should be Inez:', deque.remove_front())

print('deque size. Should be 0:', deque.size())
print('Deque is empty? Should be True:', deque.is_empty())