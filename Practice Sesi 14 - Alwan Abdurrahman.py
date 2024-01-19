#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math, sys


# In[2]:


import numpy
import scipy

print(math.pi)
print(math.e)
print(numpy.pi)
print(scipy.pi)


# ## Python Fundamental Practice

# In[3]:


# Operasi CRUD untuk List
my_list = [1, 2, 3, 4, 5]
print(my_list)

# CREATE: Menambahkan elemen baru
my_list.append(6)
print("Setelah ditambahkan:", my_list)

# READ: Membaca elemen berdasarkan indeks
print("Elemen pada indeks 2:", my_list[2])

# UPDATE: Mengubah nilai elemen berdasarkan indeks
my_list[1] = 10
print("Setelah diubah:", my_list)

# DELETE: Menghapus elemen berdasarkan nilai
my_list.remove(4)
print("Setelah dihapus:", my_list)


# In[5]:


# Operasi CRUD untuk Dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

# CREATE: Menambahkan pasangan kunci-nilai baru
my_dict['gender'] = 'Male'
print("Setelah ditambahkan:", my_dict)

# READ: Membaca nilai berdasarkan kunci
print("Usia:", my_dict['age'])

# UPDATE: Mengubah nilai berdasarkan kunci
my_dict['age'] = 26
print("Setelah diubah:", my_dict)

# DELETE: Menghapus pasangan kunci-nilai berdasarkan kunci
del my_dict['city']
print("Setelah dihapus:", my_dict)


# In[10]:


##1. buatlah program Python yang menerima 2 angka sebagai input, dan print angka yang lebih besar

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if num1 > num2:
    print(f'{num1} is greater.')

elif num1 < num2:
    print(f'{num2} is greater.')

else:
    print('Both numbers are equal.')


# In[11]:


##2. buatlah program Python yang bisa mengecek apakah tahun ini termasuk tahun kabisat atau bukan 

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):    
    print(f"{year} is a leap year.")

else:    
    print(f"{year} is not a leap year.")


# In[17]:


##3. Buatlah program yang menghitung total semua angka genap dari 1 sampai 100, gunakan ‘while’ loop

total = 0
number = 1

while number <= 100:
    if number % 2 == 0:
        total += number
    number += 1

print("Sum of even numbers from 1 to 100:", total)


# In[20]:


##4. Buatlah program yang terus meminta input user untuk memasukkan password hingga password “secret” terinput

secret_password = 'secret'

while True:
    user_input = input('Enter the password: ')
    if user_input == secret_password:
        print('Password is correct, Access granted!')
        break
    else:
        print('Password is wrong. Try again.')


# In[22]:


##5. buatlah program yang membuat tabel multiplikasi untuk sebuah angka dari 1*num hingga 10*num. gunakan ‘for’ loop.

num = int(input('Enter a number: '))

for i in range (1, 11):
    print(f'{i} x {num} = {i * num}')


# In[26]:


##6. buatlah program yang menghitung jumlah huruf hidup dalam sebuah string

text = input("Enter a string: ")
text = text.lower()  # Convert the input to lowercase for case 
vowel_count = 0

for char in text:    
    if char in "aeiou":        
        vowel_count += 1
        
print(f"Number of vowels in the string: {vowel_count}")


# In[34]:


##7. Buatlah sebuah fungsi bernama `sapa` yang menerima satu argumen berupa nama dan mencetak pesan sapaan. 
##Panggil fungsi tersebut dengan nama "John"

def sapa(nama):
    print(f'Halo, {nama}!')

sapa('John')


##8.Buatlah sebuah fungsi `kuadrat` yang menerima satu angka sebagai argumen dan mengembalikan kuadrat dari angka tersebut. 
##Cobalah fungsi ini dengan beberapa angka

def kuadrat(angka):
    print(f'{angka * angka} adalah kuadrat dari {angka}')
    
kuadrat(3)


# In[42]:


##9. Buatlah sebuah fungsi `hitung_luas_persegi` yang menerima dua argumen: panjang dan lebar. 
##Fungsi ini mengembalikan luas persegi tersebut. 
##Jika salah satu argumen tidak disediakan, gunakan nilai default 1.0

def hitung_luas_persegi(p=1.0, l=1.0):
    print(f'luas persegi dengan panjang {p} dan lebar {l} ialah {p*l}')

hitung_luas_persegi(p=2, l=4)

##10. Buatlah sebuah fungsi `bentuk_nama` yang menerima dua argumen: nama_depan dan nama_belakang. 
##Fungsi ini mengembalikan nama lengkap. Jika nama_belakang tidak disediakan, gunakan string kosong untuk nama_belakang

def bentuk_nama(nama_depan, nama_belakang=' '):
    print(f'{nama_depan} {nama_belakang}')

bentuk_nama('alwan','abdurrahman')


# In[45]:


def hitung_luas_persegi2(panjang=1.0, lebar=1.0):    
    return panjang * lebar

luas = hitung_luas_persegi2(4, 3)
print(luas)


# In[7]:


##11. Buatlah sebuah fungsi `konversi_fahrenheit_ke_celcius` yang menerima suhu dalam Fahrenheit dan mengembalikan suhu tersebut dalam Celcius.
## Rumus konversi adalah: Celsius = (Fahrenheit - 32) * 5/9

def konversi_fahrenheit_ke_celcius(suhu):
    suhu_celcius = (suhu - 32) * 5/9
    print(f'{suhu} derajat Fahrenheit ialah {suhu_celcius:.1f} derajat Celcius')

konversi_fahrenheit_ke_celcius(100)


# In[9]:


##12. Buatlah sebuah fungsi `hitung_pangkat` yang menerima dua argumen: angka dan pangkat.
## Fungsi ini mengembalikan hasil dari angka pangkat pangkat.

def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    print(f'Hasil dari {angka} pangkat {pangkat} ialah {hasil}')

hitung_pangkat(2, 2)


# In[11]:


def hitung_pangkat(angka, pangkat):    
    hasil = 1    
    for _ in range(pangkat):        
        hasil *= angka    
        return hasil
pangkat = hitung_pangkat(2, 3)
print(pangkat)


# In[20]:


##13. Membuat modul

# main.py
import my_module

# Menggunakan fungsi dari my_module
message = my_module.greet("Asep")
print(message)

# Menggunakan variabel dari my_module
radius = 5
area = my_module.pi * my_module.square(radius)
print(f"Luas lingkaran dengan radius {radius} adalah {area:.2f}")



# In[21]:


##14. Kalkulator sederhana
def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def bagi(x, y):
    if y == 0:
        return 'Tidak bisa dibagi oleh 0'
    return x / y
def kali(x, y):
    return x * y
def modulo(x, y):
    return x % y
def pangkat(x, y):
    return x ** y

while True:
    print('Pilihan operasi:')
    print('1. Penambahan')
    print('2. Pengurangan')
    print('3. Pembagian')
    print('4. Perkalian')
    print('5. Modulo')
    print('6. Pangkat')
    print('7. Keluar')

    pilihan = input('\nMasukkan nomor operasi (1/2/3/4/5/6/7): ')
    
    if pilihan == '5':
        print('\nAngka pertama ialah angka yang dibagi dan angka kedua ialah pembagi')
    elif pilihan == '6':
        print('\nAngka pertama ialah angka dan angka kedua ialah bilangan pangkat')
    elif pilihan == '7':
        print('\nKeluar dari kalkulator')
        break
    
    angka1 = float(input('\nMasukkan angka pertama: '))
    angka2 = float(input('\nMasukkan angka kedua: '))
    
    if pilihan == '1':
        print('\nHasil:', tambah(angka1, angka2))
    elif pilihan == '2':
        print('\nHasil:', kurang(angka1, angka2))
    elif pilihan == '3':
        print('\nHasil:', bagi(angka1, angka2))
    elif pilihan == '4':
        print('\nHasil:', kali(angka1, angka2))
    elif pilihan == '5':
        print('\nHasil:', modulo(angka1, angka2))
    elif pilihan == '6':
        print('\nHasil:', pangkat(angka1, angka2))
    else:
        print('\nPilihan tidak valid')


# In[27]:


##15. Daftar belanja sederhana

shopping_list = []

def tambah_item(item):
    shopping_list.append(item)
    print(f'{item} telah ditambahkan ke daftar belanja.')
def hapus_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'{item} telah dihapus dari daftar belanja.')
    else:
        print(f'{item} tidak ditemukan di dalam daftar belanja.')
def tampilkan_daftar():
    print('\nDaftar Belanja:')
    for item in shopping_list:
        print('-', item)

while True:    
    print("\nApa yang ingin Anda lakukan?")    
    print("\n1. Tambah item ke daftar belanja")    
    print("2. Hapus item dari daftar belanja")    
    print("3. Tampilkan daftar belanja")    
    print("4. Keluar")    
    pilihan = input("\nPilih tindakan (1/2/3/4): ")    
    if pilihan == '1':        
        item = input("\nMasukkan item yang ingin ditambahkan: ")        
        tambah_item(item)    
    elif pilihan == '2':        
        tampilkan_daftar()
        item = input("\nMasukkan item yang ingin dihapus: ")        
        hapus_item(item)    
    elif pilihan == '3':        
        tampilkan_daftar()    
    elif pilihan == '4':        
        print("\nKeluar dari daftar belanja")        
        break    
    else:        
        print("\nPilihan tidak valid")


# In[29]:


#16. Kalkulator Body Mass Index

def hitung_bmi(berat, tinggi):
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)
    return bmi
def kategori_bmi(bmi):
    if bmi < 18.5:
        return 'Kurus'
    elif 18.5 <= bmi < 24.9:
        return 'Ideal'
    elif 25 <= bmi < 29.9:
        return 'Gemuk'
    else:
        return 'Obesitas'

berat = float(input('Masukkan berat badan (kg): '))
tinggi = float(input('Masukkan tinggi badan (cm):'))

bmi = hitung_bmi(berat, tinggi)
kategori = kategori_bmi(bmi)

print(f'BMI Anda adalah {bmi:.2f} ({kategori}).')


# In[32]:


#17. Pencarian kata dalam teks

teks = 'Halo, jika kamu sedang sendiri saat membaca ini mohon berhati-hati ya.'

kata_cari = input('Masukkan kata atau frasa yang ingin dicari: ')

if kata_cari in teks:
    print(f'"{kata_cari}" ditemukan dalam teks.')
else:
    print(f'"{kata_cari}" tidak ditemukan dalam teks.')


# In[16]:


##18. Kalkulator konversi mata uang dari Rupiah

def konversi_uang(jumlah, mata_uang_tujuan):
    nilai_tukar = {
        'USD': 14200,
        'YEN': 130,
        'WON': 12,
        'EURO': 15800,
        'POUND': 17500,
        'RUBEL': 190,
        'YUAN': 2200
    }

    return jumlah / nilai_tukar[mata_uang_tujuan]

while True:
    print('\nPilihan mata uang:')
    print('1. USD (Dolar Amerika)')
    print('2. YEN (Jepang)')
    print('3. WON (Korea)')
    print('4. EURO (Uni Eropa)')
    print('5. POUND (Inggris)')
    print('6. RUBEL (Rusia)')
    print('7. YUAN (Tiongkok)')
    print('8. Keluar')

    pilihan = input('\nMasukan pilihan 1/2/3/4/5/6/7/8: ')

    if pilihan == '8':
        print('\nKeluar dari kalkulator konversi mata uang')
        break

    if pilihan in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            jumlah_uang = float(input('\nMasukkan jumlah uang (dalam Rupiah): '))
        except ValueError:
            print('\nJumlah uang tidak valid. Masukkan angka.')
            continue

        # Mapping pilihan pengguna ke mata uang yang sesuai
        mata_uang_tujuan = {
            '1': 'USD',
            '2': 'YEN',
            '3': 'WON',
            '4': 'EURO',
            '5': 'POUND',
            '6': 'RUBEL',
            '7': 'YUAN'
        }.get(pilihan)

        if mata_uang_tujuan is None:
            print('\nMata uang tujuan tidak valid. Silakan pilih dari daftar yang tersedia.')
            continue

        hasil_konversi = konversi_uang(jumlah_uang, mata_uang_tujuan)
        print(f'\n{jumlah_uang:.2f} Rupiah setara dengan {hasil_konversi:.2f} {mata_uang_tujuan}')
    else:
        print('\nPilihan tidak valid. Silakan pilih nomor mata uang dari 1 hingga 7.')


# In[19]:


##19. Read and Write from Excel

import pandas as pd
#Read data from a Excel file
df_excel = pd.read_excel('C:/Users/USER/Downloads/start_station.xlsx')
df_excel

#Save the processed data to a new CSV file
# df.to_csv('processed_csv_data.csv', index=False)

#Save the processed data to an Excel file
# df.to_excel('processed_csv_data.xlsx', index=False)


# In[32]:


##19. Read and Write from Excel
import pandas as pd

def baca_data(file_path):
    try:
        df_excel2 = pd.read_excel(file_path)
        return df_excel2
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None

def tampilkan_data(df_excel2):
    if df_excel2 is not None:
        print(df_excel2)

def tambah_data(df_excel2, data_baru):
    if df_excel2 is not None:
        new_row = pd.DataFrame(data_baru, index=[0])
        return pd.concat([df_excel2, new_row], ignore_index=True)

def simpan_data(df_excel2, file_path):
    try:
        df_excel2.to_excel(file_path, index=False)
        print("Data berhasil disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Nama file Excel
file_path = 'C:/Users/USER/Downloads/start_station.xlsx'

# Baca data dari file Excel
dataframe = baca_data(file_path)

# Tampilkan data
tampilkan_data(dataframe)

# Tambahkan data baru
data_baru = {'start_station': 'Cisauk', 'name': 'BSD', 'num': '9999999'}
dataframe = tambah_data(dataframe, data_baru)

# Simpan data kembali ke file Excel
simpan_data(dataframe, file_path)


# In[ ]:


##21. Read and Write from SQL
import pyodbc

# Fungsi untuk membaca data dari tabel
def baca_data_sql(database_file):
    engine_sql = pyodbc.connect(database_file)
    df = pd.read_sql('SELECT * FROM books_inventories', engine_sql)
    return df

# Fungsi untuk menambahkan data ke dalam tabel
def tambah_data_sql(database_file, start_station, name, num):
    engine_sql = pyodbc.connect(database_file)
    cursor = engine_sql.cursor()
    cursor.execute("INSERT INTO BitMedia (start_station, name, num) VALUES (?, ?, ?)", (start_station, name, num))
    connection.commit()
    connection.close()

def main():
    database_file = 'Driver={SQL Server};'
                          'Server=LAPTOP-8K05SUQ5;'
                          'Database=BitMedia;'
                          'Trusted_Connection=yes;'
    station = baca_data_sql(database_file)
    
    print("Data Station:")
    for name in station:
        print(f"{name[1]}: {name[2]} Start_station, Number: {item[3]}")
    
    tambah_station = input("Tambah station baru? (y/n): ")
    
    if tambah_station.lower() == 'y':
        start_station = input("Nama start station: ")
        name = input("Nama wilayah: ")
        number = input("Nomor station: ")
        
        tambah_data_sql(database_file, start_station, name, num)
        print("Station berhasil ditambahkan dan disimpan.")

if __name__ == "__main__":
    main()


# In[35]:


##21. Read and Write from CSV
import pandas as pd

def baca_data(file_path):
    try:
        df_csv = pd.read_csv(file_path)
        return df_csv
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None

def tampilkan_data(df_csv):
    if df_csv is not None:
        print(df_csv)

def tambah_data(df_csv, data_baru):
    if df_csv is not None:
        new_row = pd.DataFrame(data_baru, index=[0])
        return pd.concat([df_csv, new_row], ignore_index=True)

def simpan_data(df_csv, file_path):
    try:
        df_csv.to_csv(file_path, index=False)
        print("Data berhasil disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Nama file Excel
file_path = 'C:/Users/USER/Downloads/start_station.csv'

# Baca data dari file Excel
dataframe = baca_data(file_path)

# Tampilkan data
tampilkan_data(dataframe)

# Tambahkan data baru
data_baru = {'start_station': 'Cisauk', 'name': 'BSD', 'num': '9999999'}
dataframe = tambah_data(dataframe, data_baru)

# Simpan data kembali ke file Excel
simpan_data(dataframe, file_path)

