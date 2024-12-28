firstlist=["hello,hi,a,b,c,z,x,y"]
firstlist.append("w")
firstlist.pop (1)
seclist=["i"]
seclist.extend(firstlist)
seclist.sort(reverse=True)
firstlist[::2]
print (firstlist)