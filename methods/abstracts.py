from abc import ABC, abstractmethod # importing abc module

class Remote(ABC): # inheriting/extending from abc
    # both on and off must be implemented in a child class
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @property
    @abstractmethod
    def brand(self):
        pass

class TVRemote(Remote):
    def on(self):
        print("turning tv on")

    def off(self):
        print("turning tv off")

    @property
    def brand(self):
        return "Samsung"

newremote = TVRemote()
newremote.on()
newremote.off()
print(newremote.brand)