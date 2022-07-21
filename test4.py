def Test67(x, y):
    if x>20:
        for x in range(1, 50):
            print(x)
        x += 30
    else:
        while x<=50:
            print(x)
            x += 1
        x += 30
    return x
