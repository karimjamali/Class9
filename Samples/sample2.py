def func11():
  print 'Hello to the  World'

def func12(arg1='TRIPOLI',arg2='BEIRUT', arg3='JBEIL'):
   print arg1,arg2,arg3

class MyClass(object):
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def divide(self):
      return self.x / self.y


print 'How second file Python processes an import'

#print "This is the __name__ var: {}".format(__name__)
if __name__ == "__main__":
  print 'This code is not importable, only executable'
