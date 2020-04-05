class Stack:

  def __init__(self):
    self.stack = []
  
  def push(self, data):
    self.stack.append(data)
  
  def pop(self):
    return stack.pop() if stack else None
  
  def peek(self):
    return self.stack[-1] if stack else None

  def isEmpty(self):
    return False if stack else True


st = Stack()
st.push(1)
st.push(2)
print(st.peek())
st.push(3)
print(st.peek())
