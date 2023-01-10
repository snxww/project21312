
def divider(a: object, b: object) -> object:
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

result = []
data = {10:2, 2: 5, 123: 4, 18: 0, 18: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except:
        print('sorry')
print(result)
