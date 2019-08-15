detik= input("Masukan nilai detik =")
jam=detik/3600
menit=(detik%3600)/60
sisa_detik=((detik%3600)%60)
print detik, "detik Dirubah ke konversi waktu=",jam, " jam ",menit, " menit",sisa_detik, " detik "


