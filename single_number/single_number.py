'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


def single_number(arr):

    # create empty set 1
    singles_set = []
    # create empty set 2
    doubles_set = []
    # add numbers to empty set 1 if number is not in there, if in there add to set 2
    for i in range(0, len(arr)):
        if arr[i] in singles_set:
            doubles_set.append(arr[i])
        else:
            singles_set.append(arr[i])

    # perform dif of two sets
    answer = Diff(singles_set, doubles_set)
    return answer[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

    ###
    # double_tracker = {}
    # for i in range(0, len(arr)-1):
    #     if arr[i] in double_tracker:
    #         double_tracker[i] = 2
    #     if arr[i] not in double_tracker:
    #         double_tracker[i] = 1

    # return sorted(double_tracker, key=double_tracker.get, reverse=True)
