def pillars(num_pill, dist, width):
    if num_pill == 1:
        distance = (num_pill - 1) * dist * 100
    elif num_pill == 2:
        distance = dist * 100
    elif num_pill > 2:
        distance = (num_pill - 1) * dist * 100 + width * (num_pill - 2)
    else:
        print("Invalid input")
    return distance