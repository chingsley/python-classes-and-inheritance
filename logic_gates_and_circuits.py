class LogicGate:
  def __init__(self, n):
    self.label = n
    self.output = None

  def getLabel(self):
    return self.label

  def getOutput(self):
    self.output = self.performGateLogic()
    return self.output
  
  def validInput(self, user_input, func):
    if user_input != '0' and user_input != '1':
      print("input must be 0 or 1")
      return func() # if input is invalid, call the getPin* function again to request for another input from the user
    else:
      return int(user_input)


#We categorized the logic gates based on the number of input lines.
#The AND gate has two input lines. The OR gate also has two input lines.
#NOT gates have one input line. The BinaryGate class will be a subclass
#of LogicGate and will add two input lines. The UnaryGate class will
#also subclass LogicGate but will have only a single input line.
#In computer circuit desig+n, these lines are sometimes called “pins”
#so we will use that terminology in our implementation.

# the BinaryGate class inherits from the LogicGate class
class BinaryGate(LogicGate):
  def __init__(self, n):
    LogicGate.__init__(self, n)
    self.pinA = None
    self.pinB = None

  def getPinA(self):
    if self.pinA == None:
      user_input = input(f"Enter Pin A input for gate {self.getLabel()}-->")
      return self.validInput(user_input, self.getPinA)
    else:
      return self.pinA.getFrom().getOutput()

  def getPinB(self):
    if self.pinB == None:
      user_input = input(f"Enter Pin B input for gate {self.getLabel()}-->")
      return self.validInput(user_input, self.getPinB)
    else:
      return self.pinB.getFrom().getOutput()

  def setNextPin(self, source):
    if self.pinA == None:
        self.pinA = source
    else:
        if self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")



# the UnaryGate class also inherits from LogicGate
class UnaryGate(LogicGate):
  def __init__(self, n):
    LogicGate.__init__(self,n)
    self.pin = None

  def getPin(self):
    if self.pin == None:
      user_input = input(f"Enter Pin input for gate {self.getLabel()}-->")
      return self.validInput(user_input, self.getPin)
    else:
      return self.pin.getFrom().getOutput()

  def setNextPin(self, source):
    if self.pin == None:
        self.pin = source
    else:
        raise RuntimeError("Error: NO EMPTY PINS")




  
class AndGate(BinaryGate):
  def __init__(self, n):
    super(AndGate, self).__init__(n)

  def performGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()
    print('a = ', a, '::::::', 'b = ', b)
    if a == 1 and b == 1:
      return 1
    else:
      return 0



class OrGate(BinaryGate):
  def __init__(self, n):
    super(OrGate, self).__init__(n)

  def performGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()
    if a == 0 and b == 0:
      return 0
    else:
      return 1



class NotGate(UnaryGate):
  def __init__(self, n):
    super(NotGate, self).__init__(n)

  def performGateLogic(self):
    self.pin = self.getPin()
    return 1 if self.pin == 0 else 0


class NandGate(AndGate):
  def performGateLogic(self):
    if super().performGateLogic() == 1:
      return 0
    else:
      return 1


class NorGate(OrGate):
  def performGateLogic(self):
    if super().performGateLogic() == 1:
      return 0
    else:
      return 1

class Connector:
  def __init__(self, fgate, tgate):
    self.fromgate = fgate
    self.togate = tgate
    tgate.setNextPin(self)

  def getFrom(self):
    return self.fromgate

  def getTo(self):
    return self.togate

########################################
# TESTING THE AND GATE
#########################################
# g1 = AndGate("G1")
# result = g1.getOutput()
# print(result)


########################################
# TESTING THE AND GATE
#########################################
# g2 = OrGate("G2")
# result = g2.getOutput()
# print(result)
# print(g2.pinA, g2.pinB)


########################################
# TESTING THE AND GATE
#########################################
# g3 = NotGate("G2")
# result = g3.getOutput()
# print('input = ', g3.pin)
# print('result = ', result)


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

   g5 = NandGate("G5")
   print('g5.output() = ', g5.getOutput())

   g6 = NorGate("G6")
   print('g6.output() = ', g6.getOutput())

main()


