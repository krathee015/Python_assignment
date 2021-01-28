total_floors = 7
default_elevator_position = 0

class elevator(object):
    def __init__(self,num_of_floor, direction = "up"):
        self.total_floors = num_of_floor
        self.direct = direction

    def moveelevator(self):
        if self.total_floors == self.floor:
            self.direct = "down"
        if self.direct == "up":
            self.floor += 1
        else:
            self.floor -= 1

   
