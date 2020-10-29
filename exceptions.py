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

    @staticmethod
    def TimedoutError(SILENT=False):
        if SILENT == False:
            print("\nThe input process timedout!")
            print("\nTo suppress this error in the future, set SILENT=True")
        else:
            pass
