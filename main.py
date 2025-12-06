#  1 - misol
lst = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, lst))
print(result)


#  2 - misol
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))
print(result)


# 3 - misol
lst = ["salom", "dunyo", "python"]
result = list(map(lambda s: s.upper(), lst))
print(result)


# 4 - misol
lst = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, lst))
print(result)


# 5 - misol
lst = ["salom", "dunyo", "python", "kitob"]
result = list(filter(lambda s: len(s) > 5, lst))
print(result)


# 6 - misol
lst = [1, 2, 3, 4, 5, 7, 10]
result = list(filter(lambda x: x % 3 == 1, lst))
print(result)


# 7 - misol
lst = [3, 6, 7]
result = list(map(lambda x: x*2 if x*2 <= 10 else 10, lst))
print(result)


# 8 - misol
lst = ["salom", "dunyo", "python"]
result = list(map(lambda s: s.capitalize(), lst))
print(result)



























