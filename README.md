# dynamic-function-loader

### 

## Installation
```
pip install dynamic-function-loader
```


## Overview
dynamic-function-loader allows dynamically loading a Python function into the current execution environment from a `string`.

### Usage

```python
import dynamic_function_loader

f = dynamic_function_loader.load("def foo():\n    return 'bar'")
f()

```

### Note
All Python packages used by the imported function must be loaded _within_ the function itself. For example:

```python
def foo(regex):
  import re
  return re.compile(regex)
```
