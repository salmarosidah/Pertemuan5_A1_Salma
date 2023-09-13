









data = int(input("masukkan banyak data: "))
nilai = 0

for i in range (0, data) :
    data_input = int(input("masukkan nilai: "))
    nilai += data_input
    if data_input == data :
        break
    
rata_rata = nilai / data
print("rata-rata=", rata_rata)
    









