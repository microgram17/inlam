def primcalc(n):
    i = 1
    while i <= n:
        i = i + 1
        if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0) and (i != 2 and i != 3 and i != 5 and i != 7):
            continue
        elif i > 1:
            print(f"{i} is a prime number")

primcalc()