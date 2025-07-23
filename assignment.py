print('========== ISI DATA TERLEBIH DAHULU ==========')
nama = input('Masukkan nama mahasiswa: ')
nim = input('Masukkan NIM: ')
nilai = int(input('Masukkan nilai ujian (0-100): '))

if nilai>=85:
    grade = 'A (Sangat Baik)'
elif nilai>=75:
    grade = 'B (Baik)'
elif nilai>=60:
    grade = 'C (Cukup)'
elif nilai>=40:
    grade = 'D (Kurang)'
elif nilai<40:
    grade = 'E (Sangat Kurang)'
else:
    print('Nilai tidak valid')

print('========== DATA ==========')
print(f"Nama: {nama} (type: {type(nama)})")
print(f"NIM: {nim} (type: {type(nim)})")
print(f"Nilai: {nilai} (type: {type(nilai)})")

print('Hasil evaluasi:')
print(f"Mahasiswa: {nama} (NIM: {nim})")
print(f"Nilai Ujian: {nilai}")
print(f"Kategori Nilai: {grade}")