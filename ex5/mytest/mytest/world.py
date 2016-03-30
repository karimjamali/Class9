
def func2():
  print' Sorry, didnt recognize you'

def main():
  print 'This is the world module'

class MyClass(object):
  def __init__(self,a,b,c):
     self.a = a
     self.b = b
     self.c = c

  def Hello(self):
     print self.a, self.b, self.c
 
  def Not_Hello(self):
     print 'not' , self.a, self.b, self.c
class Inherited_Class(MyClass):
   def Hello(self):
    print 'This is inheritance with overriding', self.a,self.b,self.c
 
if __name__ == '__main__':
   main()
