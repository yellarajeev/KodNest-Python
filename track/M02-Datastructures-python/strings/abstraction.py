from abc import abstractmethod,ABC

class vehicle():
    @abstractmethod
    def Strat(slef):
        pass
    @abstractmethod
    def stop(self):
        pass
#Abstratct class
class car(vehicle):
    def start (self):
        print("car starts")

    @abstractmethod
    def stop(self):
        pass

#concrete  class
class sportscar(car):
    def stop(self):
        print("bike stop")

v =sportscar()
v.start()
v.stop()

         

