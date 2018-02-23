
def shiftedListSearch(shifted_list):
    assert (len(shifted_list) > 0)
    left = 0
    right = len(shifted_list) - 1
    current_max = shifted_list[0]
    # Binary Search
    while left <= right:
        mid = (left + right) / 2
        if shifted_list[mid] < current_max:
            right = mid - 1
        elif shifted_list[mid] >= current_max:
            left = mid + 1
            current_max = shifted_list[mid]
    return current_max


def mostOccurringTriplets(log_file):
    history = {}
    triplets = {}
    for request_path, user_id in log_file:
        # Check if user already exists
        if user_id in history:
            # Add to user history
            history[user_id].append(request_path)
        else:
            # Create history for user
            history[user_id] = [request_path]
        # Check if user has visited 3 unique pages consecutively
        if len(history[user_id]) >= 3 and len(set(history[user_id][-3:])) == 3:
            if ' '.join(history[user_id][-3:]) in triplets:
                triplets[' '.join(history[user_id][-3:])] += 1
            else:
                triplets[' '.join(history[user_id][-3:])] = 1
    # Sort all triplets in reverse order
    top10 = sorted(triplets, key=triplets.get, reverse=True)[:10]
    # Convert back to tuple
    for i in range(0, len(top10)):
        top10[i] = tuple(top10[i].split())
    return top10