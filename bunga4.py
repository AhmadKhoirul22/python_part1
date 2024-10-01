def lamamenabung(u, p, b,):
    p = p / 100
    w = (b * 12) / (p * u)
    return w

print(lamamenabung(1200000, 15, 120000))