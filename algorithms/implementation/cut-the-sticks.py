def cutTheSticks(arr):
    res = []
    for _ in range(len(set(arr))):
        res.append(len(arr))
        cs = min(arr)
        arr = [x - cs for x in arr]
        while 0 in arr:
            arr.remove(0)
    return res
