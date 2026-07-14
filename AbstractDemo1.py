from abc import ABC ,abstractmethod 
class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class derived(Base):   #ERROR
    pass

dobj = derived()
"""
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Python\OOP-12July_2026\Polymorphisum\AbstractDemo1.py", line 10, in <module>
    dobj = derived()
TypeError: Can't instantiate abstract class derived without an implementation for abstract method 'Addition'

"""