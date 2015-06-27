for n in range(1, 101):
    s = ''
    if n % 3 == 0:
        s += 'Fizz'
    if n % 5 == 0:
        s += 'Buzz'
    print(s if s != '' else str(n))
