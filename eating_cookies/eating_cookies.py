'''
Input: an integer
Returns: an integer
'''
cache = []


def eating_cookies(n, cache):
    # Your code here
    # base case
    # if we've eaten to much
    if n < 0:
        return 0
    # if we've eaten the perfect amount
    if n == 0:
        return 1

    # before we try to solve our problem
    # lets see if the answer is already stored in cache

    # means answer provided
    # using cahce with list (can also use dict)

    if cache[n] > 0:
        # this must have been precomputer
        return cache[n]

    # what if I ate just 1 cookie, or 2 cookies, or 3 cookirs
    # recursive case
    number_of_ways = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    cache[n] = number_of_ways

    return number_of_ways


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")
