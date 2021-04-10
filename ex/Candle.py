n = int(input())
l = int(input())
fr = list()
rez = list()

for i in range(n):
    m = list()
    for j in range(n):
        m.append(0)
    rez.append(m)

for y in range(n):
    st = input()
    fr.append(st)
    st = st.split()
    if 'C' in st:
        for x in range(len(st)):
            if st[x] == 'C':
                for yf in range(len(rez)):
                    for xf in range(len(rez)):
                        if rez[yf][xf] == l:
                            continue
                        elif (l - max(abs(xf - x), abs(yf - y))) <= rez[yf][xf]:
                            continue
                        rez[yf][xf] = l - max(abs(xf - x), abs(yf - y))

for i in rez:
    print(*i)