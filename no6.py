def lamamenabung(uang, persen, uang_akhir):
    u = uang 
    p = persen / 100
    uang_akhir = uang_akhir - uang

    w = (uang_akhir * 12) / (uang * persen)
    return w 

print(lamamenabung(1400000, 15, 1522500))