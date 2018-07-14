def base(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
sURLDict={}
fURLDict={}
count=0
base62=base("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def genShortURL(url):
    if (url in fURLDict):
        print("Duplicate url"+fURLDict[url])
        return
    global count
    s=""
    k=count
    count+=1
    if (k==0):
        s="0000000"
        if (s not in sURLDict):
            sURLDict[s]=url
            fURLDict[url]=s
            print("shortened url "+url+" is "+s)
            return
    while(k!=0):
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if (l<7):
        for i in range(7-l):
            s="0"+s
    if (s not in sURLDict):
        sURLDict[s]=url
        fURLDict[url]=s
    print("short url for "+url+" is https://ca.ke/"+s)

while (True):
    print("Enter \n\t1) generate ShortURL\n\t2)redirect ShortURL")
    userInput=int(input())
    if (userInput==1):
        url=input("url:")
        genShortURL(url)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if sURLDict.get(shortURL,None) is not None:
            print("Go to url:"+sURLDict[shortURL])
        else:
            print("not existing")
    else:
        print("Invalid Input")