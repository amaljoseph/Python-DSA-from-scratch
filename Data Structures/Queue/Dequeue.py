class Dequeue:

  def __init__(self):
    self.dequeue = []

  def addAtFront(self, data):
    self.dequeue.insert(0, data)

  def addAtRear(self, data):
    self.dequeue.append(data)
  
  def deleteAtFront(self):
    return self.dequeue.pop(0) if self.dequeue else None
  
  def deleteAtRear(self):
    return self.dequeue.pop() if self.dequeue else None
  
  def peekFront(self):
    return self.dequeue[0]

  def peekRear(self):
    return self.dequeue[-1]
  

dq = Dequeue()
dq.addAtFront(2)
dq.addAtFront(1)
dq.addAtRear(3)
print(dq.peekFront())
print(dq.peekRear())
print(dq.deleteAtFront())
print(dq.deleteAtRear())
