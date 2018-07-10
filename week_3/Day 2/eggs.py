def my_function(arg):
    x=arg
    count=0
    k=14
    y=0
    while(y<x):
    		z=y
    		y=y+k
    		k=k-1
    		count=count+1
    if(x==y):
        return count
    count=count+(x-z)
    return count

    
print(my_function(13))
