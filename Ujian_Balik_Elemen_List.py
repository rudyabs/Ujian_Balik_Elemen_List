def balik_posisi(list_saya):

   kiri = 0
   kanan = len(list_saya)-1

   #kondisi
   while kiri<kanan:

       #penukaran
       temp = list_saya[kiri]
       list_saya[kiri] = list_saya[kanan]
       list_saya[kanan] = temp

       #mengganti index
       kiri += 1
       kanan -= 1

   return list_saya

print(balik_posisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balik_posisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balik_posisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))



