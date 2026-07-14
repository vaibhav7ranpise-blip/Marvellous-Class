from abc import ABC ,abstractmethod 
class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class derived(Base):  
    def Addition(self,No1,No2):
        return No1 + No2

dobj = derived()

ret = dobj.Addition(10,11)
print("Addition is :",ret)