def func(paramArray):
    global i
    if len(paramArray) > 4:
        sliceIndex = (len(paramArray)+1) // 2; i += 1
        arrayA = paramArray[:sliceIndex]; arrayB = paramArray[sliceIndex-1:]
        func(arrayA); func(arrayB)

while True:
    try:
        n = int(input("Enter number of urinals (0 to exit) - "))
    except:
        print('Invalid input, try again. Only non-negative integers allowed.')
    if n == 0:
        break
    if n == 1 or n == 2:
        print(1)
    else:
        occupancy = [0]*n; occupancy[0] = 2; occupancy[-1] = 1
        i=3
        func(occupancy)
        print(i-1)
