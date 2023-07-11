def add(*args):
    print(args[0])      # Prints the argument at 0

    arg_sum = 0
    for n in args:
        arg_sum += n
    print(arg_sum)


add(3, 5, 6, 2, 1)