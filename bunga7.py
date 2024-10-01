def uangcicilan(uang, persen, waktu):
    u = uang
    p = persen / 100
    w = waktu 

    b = w * p * u 
    u = (u + b) / 24
    return u 

print(uangcicilan(5000000, 10,2))