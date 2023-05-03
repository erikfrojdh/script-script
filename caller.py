import subprocess

#Call a script from another script
subprocess.run(['python', 'script.py', 'some', 'args'])

#import the function and run that instead
from script_with_main import do_stuff
do_stuff('some', 'other', 'args')