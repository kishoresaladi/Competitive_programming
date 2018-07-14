x=int(input())
y=int(input())

s=bin(x)
s1=bin(y)



s2=s.split("b")
s3=s1.split("b")

s4=(s2[1])
s5=(s3[1])

s4=s4[::-1]
s5=s5[::-1]

while(len(s4)!=len(s5)):
	if(len(s4)>len(s5)):
		s5=s5+'0'
	else:
		s4=s4+'0'

count=0
for i in range(0,len(s4)):
	if(s4[i]!=s5[i]):
		count=count+1
print(count)




