#BasicFunctions -- contains functions which are needed by the program

#imports
import threading
import time
import sys
import exceptions
import signal
import keyboard

def alarm(signNum, Frame):
    raise Exception(exceptions.exceptions.TimedoutError(SILENT=silent))


def detetct_user_input(Dur, Msg, SILENT=False):
    global silent
    usr_input = str()
    silent = SILENT
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(Dur)
    try:
        usr_input = str(input(Msg))
        # keyboard.on_press_key("enter", lambda _: sys.exit(1))
        if keyboard.is_pressed("enter"):
            # if usr_input != None:
            #     # print(usr_input)
            return usr_input
    except Exception:
        signal.alarm(0)
        return usr_input

def detetct_user_input_with_commnad(Dur, Msg, SILENT=False):
    global silent
    command_input = str()
    silent = SILENT
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(Dur)
    try:
        command_input = str(input(Msg))
        # keyboard.on_press_key("enter", lambda _: sys.exit(1))
        if keyboard.is_pressed("enter"):
            # if command_input != None:
            #     print(command_input)
            return command_input
    except Exception:
        signal.alarm(0)
        return command_input