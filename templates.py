def task3(distances):
    result = {}
    for (a, b, c) in distances:
        if (a) not in result:
            result[a] = {}
        if (b) not in result:
            result[b] = {}
        result[b][a] = c
        result[a][b] = c
    print (result)
    return result








result = task3((
        ('Oslo', 'Chita', 234),
        ('London', 'Astana', 743),))
"""
def task(seq):
    result = []
    for each in seq:
        if isinstance(each, (list, set, tuple)):
            result.extend(each)
        else:
            result.append(each)
    result.sort()

    print(result)
    return result
def task2(seq):
    result = {}
    for val in seq:
        if val not in result:
            result[val] = 1
        else:
            result[val] +=1
    print (result)
    return result

task2([10, 20, 20, 21, 30, 21, 10])
"""
