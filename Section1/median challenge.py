import random as rd

### Var ###
a = rd.randrange(100) # Var alÃ©atoire entre 0 et 100
b = rd.randrange(100)
c = rd.randrange(100)
d = rd.randrange(100)
e = rd.randrange(100)

### if ... else ... ###
if a < b:
    p1, p2 = a, b
else:
    p1, p2 = b, a

if c < p1:
    p3, p2, p1 = p2, p1, c
    
else:
    if c < p2:
        p3, p2 = p2, c
    else:
        p3 = c

if d < p1:
    p4, p3, p2, p1 = p3, p2, p1, d
elif p1 < d < p2:
    p4, p3, p2 = p3, p2, d
elif p2 < d < p3:
    p4, p3 = p3, d
else:
    p4 = d

if e < p1:
    p5, p4, p3, p2, p1 = p4, p3, p2, p1, e
elif p1 < e < p2:
    p5, p4, p3, p2 = p4, p3, p2, e
elif p2 < e < p3:
    p5, p4, p3 = p4, p3, e
elif p3 < e < p4:
    p5, p4 = p4, e
else:
    p5 = e

median = p3

### TEST ###
list1 =[a,b,c,d,e]
list2 =sorted(list1)
test = list2[2]

if test == median:
    rep_test = True
else:
    rep_test = False


### PRINT ###
print(" a : ", a, "\n",
      "b : ", b, "\n",
      "c : ", c, "\n",
      "d : ", d, "\n",
      "e : ", e, "\n",
      "Median : ", median, "\n",
      "TEST : ", rep_test)