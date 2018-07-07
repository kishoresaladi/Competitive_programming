scores=[2,99,99,99,45,1,1]
max1=100
count=[0]*(max1+1)

for i in range(0,len(scores)):
	
	count[scores[i]]=count[scores[i]]+1

l=[]

for i in range(len(count)-1,0,-1):
	
	for j in range(count[i],0,-1):
		
		l.append(i)
print(l)


