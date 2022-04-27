def score(x, y):

    radio = (x ** 2 + y ** 2)
    points = 10
    if radio > 100:
        points -= 10
    elif 25 < radio <= 100:
        points -= 9
    elif 1 < radio <= 25:
        points -= 5
    return points
