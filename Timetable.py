
timetable = [0]*16

P={'A':[0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],'B':[1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
'C':[0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0],'D':[0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0],'E':[0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],'F':[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],'G':[0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0], 'H':[ 0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0] }

for i in P :
    for j,k in enumerate(P[i]) :
        if k == 1 and timetable.count(i)<2 and timetable[j]==0 :
            timetable[j] = i
missing = [i for i in P if timetable.count(i)<2]
empty = [i for i,k in enumerate(timetable) if k ==0]



for z in empty :
    for k,i in enumerate(timetable) : 
        for j in [i for i in P if timetable.count(i)<2] :       
            if P[j][k] == 1 and P[i][z]== 1 :
                timetable[k], timetable[z] = j, i
                break

print(timetable)
count = [timetable.count(i) for i in P]
print(count)