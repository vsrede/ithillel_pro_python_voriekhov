def calculate_deepth_lake(heights):
    if len(heights) < 2:
        return None
    # list_result = []
    # for i in range(len(heights)):
    #     next_num = i+1
    #     while next_num < len(heights) and heights[i] > heights[next_num]:
    #         if any(height > heights[i] for height in heights[next_num + 1:]):
    #             list_result.append(heights[i] - heights[next_num])
    #         next_num += 1
    #
    # for i in range(len(heights) - 1, -1, -1):
    #     next_num = i - 1
    #     while next_num >= 0 and heights[next_num] < heights[i]:
    #         if any(height > heights[i] for height in heights[:next_num]):
    #             list_result.append(heights[i] - heights[next_num])
    #         next_num -= 1
    # return max(list_result) if list_result else None
    max_depth = 0
    left_point, right_point = 0, len(heights) - 1

    while left_point < right_point:
        left_height, right_height = heights[left_point], heights[right_point]
        if left_height < right_height:
            next_point = left_point + 1
            while next_point < right_point and left_height > heights[next_point]:
                depth = left_height - heights[next_point]
                max_depth = max(max_depth, depth)
                next_point += 1
            left_point = next_point
        else:
            next_point = right_point - 1
            while next_point > left_point and right_height > heights[next_point]:
                depth = right_height - heights[next_point]
                max_depth = max(max_depth, depth)
                next_point -= 1
            right_point = next_point
    return max_depth if max_depth > 0 else None


assert calculate_deepth_lake([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6
assert calculate_deepth_lake([3, 1, 4, 6, 2, 5]) == 3
assert calculate_deepth_lake([3, 2, 4]) == 1
assert calculate_deepth_lake([1, 2, 4]) == None
assert calculate_deepth_lake([1, 2]) == None

"""https://www.codewars.com/kata/556deca17c58da83c00002db/train/python/643440030c91c40056278f7a"""


def tribonacci(signature, n):
    if n == 0:
        return []
    else:
        if n < 3:
            return signature[:n]
        if n > 2:
            while len(signature) != n:
                signature.append(sum(signature[-1:-4:-1]))
        return signature


"""https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python/64358092870c660a4af7f2c7"""
"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving 
the even numbers at their original positions."""


def sort_array(source_array):
    copy_source_array = [x for x in source_array if x % 2 != 0]
    copy_source_array = sorted(copy_source_array)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = copy_source_array[0]
            copy_source_array.pop(0)
    return source_array
