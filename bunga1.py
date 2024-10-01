def bungatabungan(persen_bunga, tabungan, bulan):
    bunga = persen_bunga / 100
    waktu = bulan / 12
    besar_bunga = bunga * waktu * tabungan 
    return besar_bunga

print(bungatabungan(12, 1000000, 6))
#12 %, 1000000 tabungan , 6 bulan