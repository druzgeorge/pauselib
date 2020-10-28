#exceptions class

#imports
import sys

class exceptions:
    
    def __init__(self):
        pass
    @staticmethod
    def mutual_time_omission_error(msg):
        print("Error! Time must not be a NoneType!")
        print(f"Did you mean to type pause.pause_with_msg(time=10, Msg={msg})?")
        sys.exit(1)

def receive_input(time, msg="Paused", command=None):
     print("{:s}\r".format(" "), end="", flush=True)
     print("{:s}".format(msg), end=" ")
     sleep(time)
     t = 0
     inpt  = str()
     if command == None:
             while t < time:
                     sleep(1)
                     t += 1
                     inpt = str(input("Hi"))

