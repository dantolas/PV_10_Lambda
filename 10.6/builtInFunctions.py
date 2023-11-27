pole = [100.10, 323.2, 355.9, 214.19, 87.0]


pole2 = map(lambda x:x*1.3,pole)
for x in pole2:
    print(x)
print("==============================================")
pole3 = filter(lambda x :x>120,pole)
for x in pole3:
    print(x)
print("==============================================")
pole4 = map()