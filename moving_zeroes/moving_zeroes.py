'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # iterate  through the array
    for i, value in enumerate(arr):
        # Place 0 at front of array
        if value is not 0:
            arr.insert(0, arr.pop(i))
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
