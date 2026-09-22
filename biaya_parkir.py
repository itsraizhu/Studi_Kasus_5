def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan == "Mobil" or jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "Motor" or jenis_kendaraan == "motor":
        tarif = 3000
    else:
        tarif = 0
    total_biaya = tarif * lama_parkir
    return total_biaya

print("SISTEM PERHITUNGAN BIAYA PARKIR")

while True:
    jenis = input("Masukkan jenis kendaraan (Mobil/Motor): ")
    if jenis == "Mobil" or jenis == "mobil" or jenis == "Motor" or jenis == "motor":
        break
    print("Input tidak valid! Silakan masukkan 'Mobil' atau 'Motor'.\n")

jam_masuk = int(input("Masukkan jam masuk (format 24 jam, misal 8): "))
jam_keluar = int(input("Masukkan jam keluar (format 24 jam, misal 12): "))

if jam_keluar >= jam_masuk:
    durasi = jam_keluar - jam_masuk
else:
    durasi = (24 - jam_masuk) + jam_keluar

total = hitung_biaya_parkir(jenis, durasi)

print(" HASIL PERHITUNGAN PARKIR")
print("Jenis Kendaraan:", jenis)
print("Jam Masuk      :", jam_masuk)
print("Jam Keluar     :", jam_keluar)
print("Lama Parkir    :", durasi, "jam")
print("Total Biaya    : Rp", total)
