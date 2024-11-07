# Science directory

This directory contains any science codes.

To be able to use them please add them to the sciece.__init__.py file as follows:

```python
from scarvs.science import test

# a dictionary of science functions
SCIENCE_FUNCS = dict()

# Test science function
SCIENCE_FUNCS['TEST'] = test.test
```

Make sure the function name (`TEST`) is unique.

You can add as many function as you like from a single file or from multiple files

Please add a comment to the function to describe what it does.

You must also add a `RUNSCI_{MYFUNC}` to the `scarvs.constants.constants.py` file.

e.g.

```python
# Add test function to science functions
CDict.add('RUNSCI_TEST', value=False, dtype=bool,
          source=__NAME__, user=True,
          active=True, group=cgroup,
          description='Run test science function')
```

You can import the plotting directory in science functions but never import 
any science functions into the plotting directory.