import unittest


def find_rotation_point(words):
    length=len(words)
    if(length==0):
        return
    elif(length==1):
        return 0
    return rotation_point(words,0,length-1)
def rotation_point(words,low,high):
    while(low<high):
        middle=(low+high)//2
        if (words[middle]<words[middle-1] and words[middle]<words[middle+1]):
            return middle
        low=middle+1
    if (middle+1==high):
        if(words[low-1]<words[high]):
            return 0
        else:
            return high
    return -1

    


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)