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

print("+"*30)
#print(list(range(10)))

x = [23, 49, 3293, 34,48, 392]
for m in x:
    print(m * 20, end="f_s ")

for k in range(len(x)):
    print(x[k] * 20)

print("+"*30)
# def count(nums):
#     total = 0
#     for d in nums:
#         if d <= 90:
#             print(d)
#     return total

# lis1 = [34,58,934,44,94,100,200,403]
# count(lis1)

#while
def count(nums):
    t = 0
    index = 0
    while index < len(nums):
        b = nums[index]
        if b <= 50:
            print(b)
            t += 1
        index += 1
    return t

lis1 = [34,58,934,44,94,100,200,403]
count(lis1)