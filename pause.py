#pause class

#imports
from time import sleep
import exceptions
import threading

class pause:
    def __init__(self):
        pass
    
    #basic pause function
    @staticmethod
    def pause(time):
        if not type(time) is int:
            raise TypeError("Time must be integer!")
        sleep(time)
    
    #pause with message:
    @staticmethod
    def with_msg(time=None, Msg="Program paused!"):
        if not time:
            raise Exception(exceptions.exceptions.mutual_time_omission_error(Msg))
        if not Msg:
            raise Exception("Msg must not be a NoneType!")
        print("{:s}\r".format(" "), end="", flush=True)
        print("{:s}".format(Msg), end=" ")
        # print(Msg)
        sleep(time)

    #pause for input
    #this method can be used when you want to execute some code when an error occurs
    #what you do with it is completely up to you!
    #this can be used to request user input for a specified number of seconds(converted to other units)
    @staticmethod
    def for_input(time, msg="Paused for input: ", command=None):
        if not time:
            raise Exception(exceptions.exceptions.mutual_time_omission_error(msg))
        if not msg:
            raise Exception("Msg must not be a NoneType")
        if not type(time) is int:
            raise TypeError("Time must be integer!")
        if not type(msg) is str:
            raise TypeError("msg Must be str()")
        timedout = False
        class inputThreading(threading.Thread):
            def initiate(self):
                self.timedout = False
                self.usr_input = " "
            #todo: implement timer
            #todo:implrtment timer thread
            #todo: implemet detect_user_input
            @staticmethod
            detect_user_input()