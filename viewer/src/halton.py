def halton(b):
    """Generator function for Halton sequence."""
    n, d = 0, 1
    for _ in range(256):
        x = d - n
        if x == 1:
            n = 1
            d *= b
        else:
            y = d // b
            while x <= y:
                y //= b
            n = (b + 1) * y - x
        yield n / d

a = halton(3)
for x in a:
    print(x, end=", ")