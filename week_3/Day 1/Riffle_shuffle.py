import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    l=half1
    l1=half2
    
    i=0
    j=0
    l2=shuffled_deck
    # print(len(l))
    while(i<len(l) and j<len(l1)):
    	if(l[i]<l1[j]):
    		# l2.append(l[i])
    		if(l2[i+j]!=l[i]):
    			return False
    # 			print("false")
    
    		i=i+1
    # 		print(l2)
    	else:
    		# l2.append(l1[j])
    		if(l2[i+j]!=l1[j]):
    			return False
    # 			print("false")
    # 		print(l2)
    		j=j+1
    while(i<len(l)):
    	if(l2[i+j]!=l[i]):
    # 		print("false")
    		return False
    
    	i=i+1
    
    while(j<len(l1)):
    	if(l2[i+j]!=l1[j]):
    # 		print("false")
    		return False
    	
    	j=j+1
    
    
    if(len(l)+len(l1)<len(l2)):
        return False
    return True


















# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)