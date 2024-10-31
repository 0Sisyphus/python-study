# use the next() function and write your code to catch the StopIteration exception
# normally, StopIteration is used to signal the end of iteration
with open('../static/秋夜.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# if you`re using next() manually ,
# you can also instruct it to return a terminating value,
# such as None
with open('../static/秋夜.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


