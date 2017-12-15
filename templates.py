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
