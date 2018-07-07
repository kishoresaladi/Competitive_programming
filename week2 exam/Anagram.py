def myfun(s,t):
	s=s.lower()
	t=t.lower()
	ch=[]
	ch1=[]
	for i in s:
		if(i!=' '):
			ch.append(i)

	for i in t:
		if(i!=' '):
			ch1.append(i)
	ch.sort()
	ch1.sort()
	
	if(ch==ch1):
		print(True)
	else:
		print(False)

s=["anagram","keep","Mother In"]


def main():
	
	s1=["anagram","Keep","Mother In Law","School Master","ASTRONOMERS","Toss","joy","Debit Card","sileNt CAT","Dormitory"]
	t1=["nagaram","Peek","Hitler Woman","The Classroom","No MORE STARS","Shot","enjoy","Bad Credit","Listen AcT","Dirty Room"]
	for i in range(0,len(s1)):
		myfun(s1[i],t1[i])


if __name__ == '__main__':
    main()


