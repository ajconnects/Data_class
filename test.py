def distance_from_zero(x):
    if isinstance(x, (int, float)):
        return abs(x)
    else:
        return "Not Possible"

    # #solutions 2
    # if type(x) == int or type(x) == float:
    #     return abs(x)
    # else:
    #     return "Not Possible"

a = distance_from_zero(-10.0)
b = distance_from_zero("new")
print(a)
print(b)

#how to calculate the the length and width of a rectangle

def rectangle_info(l, w):
    a = l * w
    p = 2 * (l + w)
    return a, p

print(rectangle_info(4, 10))