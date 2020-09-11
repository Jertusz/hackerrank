def hurdleRace(k, height):
    if k < max(height):
        return max(height) - k
    else:
        return 0 
