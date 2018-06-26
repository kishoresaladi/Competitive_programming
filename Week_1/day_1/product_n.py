import sys

def highest_product_of_3(list_of_ints):

    
    if(len(list_of_ints)<3):
        raise Exception
    l=list_of_ints
    max1=-sys.maxsize -1
    max2=-sys.maxsize -1
    max3=-sys.maxsize -1
    min1=sys.maxsize-1
    min2=sys.maxsize-1
    for i in range(0,len(l)):
    	if(max1<l[i]):
    		max3=max2
    		max2=max1
    		max1=l[i]
    		
    		
    	elif(max2<l[i]):
    		
    		max3=max2
    		max2=l[i]
    		
    
    	elif(max3<l[i]):
    		max3=l[i]
    		
    
    	if(l[i]<min1):
    		min2=min1
    		min1=l[i]
    		
    		
    	elif(l[i]<min2):
    		min2=l[i]

    return max((max3*max2*max1),(min1*min2*max1))