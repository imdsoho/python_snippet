import collections


deQueue = collections.deque('1234567890')
print(deQueue)

deQueue.append('1')
print(deQueue)

deQueue.appendleft('6')
print(deQueue)
