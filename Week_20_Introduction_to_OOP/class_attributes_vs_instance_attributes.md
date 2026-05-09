# Class Attributes vs Instance Attributes

There are two kinds of attributes, and understanding the difference is important.

## Instance Attributes

Defined inside `__init__` constructor using `self`. Each object gets its own copy. They're specific to that individual instance.

## Class Attributes

Define directly on the class, outside the `__init__` method/constructor. They are shared across all instances of the class. Use them for values that never change between instance - constants, configurations, etc.
