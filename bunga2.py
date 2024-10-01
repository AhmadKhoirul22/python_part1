def bungatabungan(p, w, b):
    p = p / 100
    w = w / 360 
    u =  b / (p * w) 
    return u 

print(bungatabungan(16, 90, 40000))