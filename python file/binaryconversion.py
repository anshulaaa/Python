def binaryconversations(v):
    v=int(v)
    bits=[]
    actualbinary=[]
    actualbinarynum=""
    ls=0
    
    while v!=0:
        reminders=v%2
        bits.append(reminders)
        v=v//2
    for i in range(len(bits)-1,-1,-1):
        actualbinary.append(bits[i])
        actualbinarynum=actualbinarynum+str(bits[i])
        ls= len(actualbinarynum)
    if len(actualbinarynum)<8:
        for i in range(ls,8):
                actualbinarynum="0"+actualbinarynum
    return actualbinarynum

