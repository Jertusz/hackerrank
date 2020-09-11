def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 2
    for _ in range(n-1):
        shared = liked * 3
        liked = math.floor(shared/2)
        cumulative += liked
    return cumulative
