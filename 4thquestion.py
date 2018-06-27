import unittest
from operator import itemgetter

import unittest
from operator import itemgetter

def merge_ranges(meetings):
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings, key=itemgetter(0))

    print(meetings)
    p = [meetings[0]]
    print('p',p)
    for (first, last) in meetings[1:]:
        (start, end) = p[-1]
        print(p[-1])
        if first <= end:
            if end <= last:
                end = last
            p[-1] = (start, end)
        else:
            p.append((first, last))
    return p


# Tests

