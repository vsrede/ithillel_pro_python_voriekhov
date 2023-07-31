"""Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the
 interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be
less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4."""

# ________the first option for which there was not enough memory😁
# def sum_of_intervals(intervals):
#     result = []
#     for couple in intervals:
#         for digit in range(couple[0], couple[1]):
#             result.append(digit)
#
#     result = len(set(result))
#     return result


def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [list(intervals[0])]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        pre_interval = merged_intervals[-1]

        if current_interval[0] <= pre_interval[1]:
            merged_intervals[-1][1] = max(pre_interval[1], current_interval[1])
        else:
            merged_intervals.append(list(current_interval))

    total_sum = sum(end - start for start, end in merged_intervals)
    return total_sum


assert sum_of_intervals([(1, 5), (1, 5)]) == 4
assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
assert sum_of_intervals([(1, 5)]) == 4
assert sum_of_intervals([(1, 5), (6, 10)]) == 8
assert sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000
assert sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030
print("__________OK__________")







