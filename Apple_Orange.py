s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_fall = []
    orange_fall = []
    apple_count = 0
    orange_count = 0
    for apple in apples:
        apple_fall.append(a+apple)
    for orange in oranges:
        orange_fall.append(b+orange)
    for k in apple_fall:
        if s <= k <= t:
            apple_count += 1
    for o in orange_fall:
        if s <= o <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)
    return apple_count, orange_count


countApplesAndOranges(s, t, a, b, apples, oranges)
