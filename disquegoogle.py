def problema(s, subseq):
    counter = 0
    for sub in subseq:
        i=0
        d=0
    
        while i<len(s) and d<len(sub):
            
            if s[i] == sub[d]:
                d = d + 1
                i = i + 1

                if (d >= len(sub)):
                    counter = counter + 1
            else:
                i = i + 1

    return counter

res = problema("",["a", "bb", "acd","ace"])
res2 = problema("dsahjpjauf",["ahjpjau","ja", "ahbwdka", "tnmdnasd"])
print(res)
print(res2)