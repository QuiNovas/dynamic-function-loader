# dynamic-function-loader

### 

## Installation
```
pip install dynamic-function-loader
```


## Overview
dynamic-function-loader allows dynamically loading a Python function into the current execution
environment from a `string`.

### Usage

```python
import dynamic_function_loader

f = dynamic_function_loader.load("def foo():\n    return 'bar'")
f()
```

### Globals
All functions (and other Python objects) are provided a two symbol tables upon creation; globals and locals.

`dynamic_function_loader.load` takes an optional argument called `globals_dict`.
This is used during function creation to provide the loaded function with it's
globals.

There are several use cases regarding this:

1. **You wish to load the function *as-if* it was defined within your loading script**: In this case,
simply pass in `globals()`. The loadedfunction *will* have access to the loading script's symbol table.

2. **You wish to load the function *as-if* it was defined in a seperate module**:
In this case, either do not pass a value or pass in `None` or `{}`. The loaded 
function *will not* have access to the loading script's symbol table.

3. **You wish to load the function with *some* of the symbol table from the loading script**:
In this case, copy the result from `globals()` in the loading script and pare the items from
the script that you do **not** wish the loaded function to have access to and pass in the result. Be careful!
Python will let you pare down to an empty dict (`{}`), but your loaded function will have *no* access to even
the built-ins of Python. Generally, if you do this, it should at least contain those items that begin and end
with `__`. For example:

```python
func_globals = {}
# You must convert to a list because every
# variable you declare alters the symbol table
for k, v in list(globals().items()):
    if k.startswith("__") and k.endswith("__"):
        func_globals[k] = v
```

### Note
All Python packages used by the imported function must be loaded _within_ the function itself if the `globals_dict`
that you pass in does not contain that module already (options 2 and possibly 3 from above).

For example, if `re` was not already in the global symbol table you would have to import it as follows:

```python
def foo(regex):
  import re
  return re.compile(regex)
```
