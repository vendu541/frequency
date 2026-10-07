n=[1,2,3,1,2,3,3,4]
freq={}
for x in n:
    freq[x]=freq.get(x,0)+1
print(freq)