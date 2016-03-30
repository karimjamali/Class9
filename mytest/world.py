
def func2():
  print' Sorry, didnt recognize you'

def main():
  print 'This is the world module'

class MyClass(object):
  def __init__(self,a,b,c):
   self.a=a
   self.b=b
   self.c=c
  def Say_Hello(self):
   print 'The three values pertaining to the Class are ', self.a,self.b,self.c


if __name__ == '__main__':
   main()
