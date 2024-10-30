def can_place_cows(stalls, k, min_dist):
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1  # Place another cow
            last_position = stalls[i]

        if count == k:  # All cows are placed successfully
            return True

    return False

def aggressive_cows(stalls, k):
    stalls.sort()  # Sort the stall positions
    low, high = 1, stalls[-1] - stalls[0]  # Minimum and maximum possible distances
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place_cows(stalls, k, mid):
            result = mid  # Valid placement found, try for a larger distance
            low = mid + 1
        else:
            high = mid - 1  # Reduce the distance

    return result

# Example Usage
stalls = [1, 2, 8, 4, 9]
k = 3
print(aggressive_cows(stalls, k))  # Output: 3
