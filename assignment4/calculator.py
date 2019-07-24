class Calculator:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def multiply(self):
    result = self.x * self.y
    print(result)
  def plus(self):
    return self.x + self.y
  def minus(self):
    return self.x - self.y
  def divided(self):
    return self.x / self.y

num1 = int(input("Number1: ") )
num2 = int(input("Number2: ") )
ope = input("Operator:")

Cal = Calculator(num1,num2)
if ope == '*':
  Cal.multiply()
elif ope == '+':
  print(Cal.plus());
elif ope == '-':
  print(Cal.minus());
elif ope == '/':
  print(Cal.divided());
else:
  print("Please enter * / - +")
  




