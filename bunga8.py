def lamamenabung(uang, persen, bunga):
    u = uang
    p = persen / 100
    b = bunga - uang

    w =(b * 12) / (uang * persen)
    return w

print(lamamenabung(2500000, 16,2600000)) 