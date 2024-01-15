array = [('바나나', 2), ('사과', 5), ('당근', 3)]
array.sort(key=lambda x:x[1])
print(array)
def setting(data):
    return data[1]
array.sort(key=setting,reverse=True)
print(array)

