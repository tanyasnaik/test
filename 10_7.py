R = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
T = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
"""
for i in R:
    if i in T:
        if T[i] > R[i]:
            R[i]=T[i]
"""
for x in T:
    if x not in R:
        R[x]=T[x]

for a in R:      
    print(a,':',R[a])