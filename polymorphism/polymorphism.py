class Bird:
    def fly(self):
        print("flying")
    
class Cockatiel(Bird):
    def fly(self):
        return super().fly()
    
class Penguin(Bird):
    def fly(self):
        print("penguin cant fly, unfortunately")

def start_flight(bird):
    bird.fly()
    
tiel = Cockatiel()
pen = Penguin()
start_flight(tiel)
start_flight(pen)