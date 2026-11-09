# a.
class Car:
    def move(self):
        print("The car drives on the road.")
class Boat:
    def move(self):
        print("The boat sails on water.")
class Drone:
    def move(self):
        print("The drone flies in the sky")
# b.
def start_trip(vehicle):
    vehicle.move()
# c.
car = Car()
boat = Boat()
drone = Drone()
#d.
start_trip(car)
start_trip(boat)
start_trip(drone)