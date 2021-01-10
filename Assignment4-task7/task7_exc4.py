# Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# from datetime import datetime

class Time:

    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(time1,time2):
        hr = time1.hours + time2.hours 
        min = time1.minutes + time2.minutes
        if min > 60:
            add_hr = min//60
        hr = hr+ add_hr
        new_min = min % 60
        add_time = Time(hr,new_min)
        return add_time
    
    def displayTime(self):
        print(self.hours,"hours and",self.minutes,"minutes")

    def displayMinutes(self):
        print("The time in minutes is: ", self.hours*60 + self.minutes)



obj_time1 = Time(1,20)
obj_time2 = Time(2,50)
# first_time = input("Enter first time in hours and minutes: ")
# second_time = input("Enter second time in hours and minutes")
obj_addtime = Time.addTime(obj_time1,obj_time2)
obj_addtime.displayTime()
obj_addtime.displayMinutes()
