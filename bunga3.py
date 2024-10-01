def lamamenabung(u, p, b):
    p = p / 100
    w = (b * 1200) / (p * u) 
    return w 

print(lamamenabung(800000, 16, 192000))