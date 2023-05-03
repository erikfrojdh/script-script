# script-script

Simple example on how to call a python script from another python script. 

**Usage**
```bash

python caller.py my arguments

```
caller.py first runs script.py passing 'some' and 'args' as arguments

```python
import subprocess
subprocess.run(['python', 'script.py', 'some', 'args'])
```

after you close the matplotlib figure it then imports do_stuff from script_with_main.py and calls the function with 'some', 'other', 'args'

```python
from script_with_main import do_stuff
do_stuff('some', 'other', 'args')
```

Both script.py and script_with_main.py can be called directly from the command line as well. 

```bash
$ python script_with_main.py some other                                    
Hello I'm: /home/l_frojdh/miniconda3/envs/py/bin/python
I was called with: ('some', 'other')

Hello I'm: /home/l_frojdh/miniconda3/envs/py/bin/python
I was called with: []
```

As is the functions accept a list/tuple of strings for the arguments as is when calling from the commandline but it's possible to implement argument parsing with argparse if needed.
