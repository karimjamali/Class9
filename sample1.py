def func1():
  print 'Hello World'

def func2(arg1='SanFrancisco',arg2='Las Vegas', arg3='Mekkah'):
   print arg1,arg2,arg3

class MyClass(object):
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def sum(self):
      return self.x + self.y

class NewClass(MyClass):
    def product(self):
      return self.x * self.y

print 'How Python processes an import'

#print "This is the __name__ var: {}".format(__name__)
if __name__ == "__main__":
  print 'This code is not importable, only executable'
