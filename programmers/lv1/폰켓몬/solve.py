def solution(nums):

    poke = len(nums) // 2
    dictionary = {}
    for i in nums:
        if not i in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    if len(dictionary.keys()) > poke:
        return poke
    else:
        return len(dictionary)