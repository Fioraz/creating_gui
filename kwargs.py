def calculator(n, **kwargs):
    print(kwargs)       # prints as a dictionary

    n += kwargs["add"]          # First, n (2) is added to the value of "add" key (3), then the sum of it multiply
    n *= kwargs["multiply"]     # By the value of "multiply" key (5) and results 25
    print(n)

    # Option 1
    for key, value in kwargs.items():
        print(key)      # All keys
        print(value)    # Value of each key

    # Option 2
    print(kwargs["add"])    # Value of "add" key


calculator(2, add=3, multiply=5)
