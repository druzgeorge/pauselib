from datetime import datetime
import pause
from pause import pause
from exceptions import  exceptions

def write_to_tests_output(msg):
    with open('tests/testOutput.txt', 'a') as f:
        f.write(msg)

def success(function, **kwargs):
    now = datetime.utcnow()
    try:
        function(**kwargs)
        write_to_tests_output(f"Successfully run {str(function(**kwargs))} on {str(now)}!\n")
    except TypeError as e:
        print('Error')
        write_to_tests_output(f"Failed run {str(function(**kwargs))} on {str(now)}\nError=> {str(e)}\n")
    except Exception as e:
        print("Error!")
        write_to_tests_output(f"Failed run {str(function(**kwargs))} on {str(now)}.\nError=> {str(e)}\n")

# success(pause.pause, 1)
# success(pause.with_msg, None, "hello") -- returns nonetype error!
# success(pause.with_msg, Msg="hello", time=1)
# success(pause.with_msg,  time=1, Msg="hello")
# success(pause.for_input, time=5)
success(pause.for_input, time=10, command=True)
# contents = pause.for_input(5, SILENT=True)
# print(contents)