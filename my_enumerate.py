
"""
Project: Custom Enumerate
Create your own version of Python's built-in enumerate() called my_enumerate()
that works with any iterable and allows setting a custom starting index.
"""

def my_enumerate(iterable, start=0):
    # Custom implementation of Python's enumerate()
    index = start
    for item in iterable:
        yield index, item
        index += 1


# Test the function with a different list
fruits = ['Apple', 'Banana', 'Cherry', 'Date']

for index, fruit in my_enumerate(fruits):
    print(f"{index}: {fruit} is tasty!")
