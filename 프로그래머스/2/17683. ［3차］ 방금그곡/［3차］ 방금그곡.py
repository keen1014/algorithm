def solution(m, musicinfos):
    def rplace_sharps(s):
        return s.replace('C#', 'c').replace('D#','d').replace('F#', 'f').replace('G#', 'g').replace('A#','a').replace('E#','e').replace('B#','b')
    m=rplace_sharps(m)
    tmp = []
    for v,i in enumerate(musicinfos):
        li=[]
        i=i.split(',')
        i[0]=list(map(int,i[0].split(':')))[0]*60+list(map(int,i[0].split(':')))[1]
        i[1]=list(map(int,i[1].split(':')))[0]*60+list(map(int,i[1].split(':')))[1]
        i[3]=rplace_sharps(i[3])
        if not i[3]:
            continue
        for j in range(1,i[1]-i[0]+1):
            if len(i[3])<j:
                li.append(i[3][(j%len(i[3]))-1])
            else:
                li.append(i[3][j-1])
        if m in ''.join(li):
            tmp.append([i[1]-i[0],i[2], v])
    if tmp:
        tmp=sorted(tmp, key=lambda x: (-x[0], x[2]))
        return tmp[0][1]
    else:
        return "(None)"
  