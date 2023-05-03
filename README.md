# script-script

Simple example on how to call a python script from another python script. 

**Usage**
```python

python caller.py my arguments

```
caller.py first runs script.py passing 'some' and 'args' as arguments

```python
subprocess.run(['python', 'script.py', 'some', 'args'])
```

after you close the matplotlib figure it then imports do_stuff from script_with_main.py and calls the function with 'some', 'other', 'args'

```python
from script_with_main import do_stuff
do_stuff('some', 'other', 'args')
```

