"""
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.

""

def merge_intervals(intervals):
    sorted_intervals = sorted(intervals,key = lambda x:x[0])
    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_intervalend = current_interval
        next_interval_start,next_interval_end = next_interval
 