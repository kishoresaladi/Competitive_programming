
d={}
d["a"]=".-"
d["b"]="-..."
d["c"] ="-.-."
d["d"] ="-.."
d["e"] ="."
d["f"] ="..-."
d["g"]="--."
d["h"] ="...."
d["i"] =".."
d["j"]=".---"
d["k"] ="-.-"
d["l"]=".-.."
d["m"] ="--"	
d["n"]="-."
d["o"] ="---"
d["p"] =".--."
d["q"]="--.-"
d["r"]=".-."
d["s"]="..."
d["t"]="-"
d["u"]="..-"
d["v"]="...-"
d["w"]=".--"
d["x"]="-..-"
d["y"]="-.--"
d["z"]="--.."


n=eval(input())
l=[]

print(n[0])
for i in n:
	s=""
	for j in i:
		s=s+d[j]
	l.append(s)
print(l)

count=0
# for i in range(0,len(l)):
# 	for j in range(i+1,len(l)):
# 		if(i==j):
# 			count=count+1
d1={}
count=0
for i in l:
	if i not in d1:
		d1[i]=1
		count=count+1
print(count)



