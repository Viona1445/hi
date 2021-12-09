# UAS ALPRO SEMESTER 1
# 10/12/2021

level = {
    "1" : "A",
    "2" : "B",
    "3" : "C"
}

# untuk mempermudah
def hiasan():
    print("-"*50)

def batas():
    print(">"*50)

def data_salah():
    print("input-an salah. Silakan masukkan ulang.")

def identitas():
    print(f"{nama_karyawan}, karyawan level {level[level_karyawan]}")
    hiasan()
    
# proses
def biodata_kariawan():
    global nama_karyawan, level_karyawan, gaji_pokok
    batas()
    hiasan()
    print("DATA KARYAWAN".center(50))
    hiasan()
    nama_karyawan = input("Nama Karyawan: ")
    while True:
        level_karyawan = input("Level Karyawan:\n1. A\n2. B\n3. C\n>>> ")
        if level_karyawan == "1" or level_karyawan == "2" or level_karyawan == "3":
            break
        else:
            data_salah()
    if level_karyawan == "1":
        gaji_pokok = 7000
    elif level_karyawan == "2":
        gaji_pokok = 5000
    else:
        gaji_pokok = 3000
    hiasan()
    print(f"Gaji pokok karyawan atas nama: {nama_karyawan}\n>>> Rp{gaji_pokok}")
    hiasan()

def data_coklat():
    global Coklat, bonus_coklat
    batas()
    hiasan()
    identitas()
    print("DATA PEMBUNGKUSAN".center(50))
    hiasan()
    print("silakan masukkan jumlah permen yang telah Anda".center(50))
    print("bungkus bulan ini berdasarkan variasi".center(50))
    hiasan()
    while True:
        try:
            Coklat = int(input("Coklat: "))
            if Coklat >= 3000 and Coklat <= 6000:
                bonus_coklat = Coklat
                break
            elif Coklat > 6000 or (Coklat < 3000 and Coklat >= 0):
                bonus_coklat = 0
                break
            else:
                data_salah()
        except:
            data_salah()
    hiasan()

def data_strawberry():
    global Strawberry, bonus_strawberry, bonus_coklat
    while True:
        try:
            Strawberry = int(input("Strawberry: "))
            if Strawberry >= 3000 and Strawberry <= 6000:
                if bonus_coklat == 0:
                    bonus_strawberry = Strawberry
                elif bonus_coklat == 3000:
                    bonus_strawberry = 3000
                elif bonus_coklat > 3000:
                    bonus_strawberry = 0
                break
            elif Strawberry > 6000 or (Strawberry < 3000 and Strawberry >= 0):
                bonus_strawberry = 0
                break
            else:
                data_salah()
        except:
            data_salah()
    hiasan()

def data_kacang():
    global Kacang, bonus_kacang, bonus_strawberry, bonus_coklat
    while True:
        try:
            Kacang = int(input("Kacang: "))
            if Kacang >= 3000 and Kacang <= 6000:
                if bonus_coklat + bonus_strawberry == 0:
                    bonus_kacang = Kacang
                elif bonus_coklat + bonus_strawberry == 3000:
                    bonus_kacang = 3000
                elif (bonus_coklat + bonus_strawberry) > 3000:
                    bonus_kacang = 0
                break
            elif Kacang > 6000 or (Kacang < 3000 and Kacang >= 0):
                bonus_kacang = 0
                break
            else:
                data_salah()
        except:
            data_salah()
    hiasan()

def kalkulasi_A():
    global bonus1, bonus2, bonus3
    # bonus Coklat
    if bonus_coklat in range(5001,6001):
        bonus1 = gaji_pokok * (35/100)
    elif bonus_coklat in range(4000, 5001):
        bonus1 = gaji_pokok * (30/100)
    elif bonus_coklat in range(3000, 4000):
        bonus1 = gaji_pokok * (25/100)
    # bonus strawberry
    if bonus_strawberry in range(5001,6001):
        bonus2 = gaji_pokok * (40/100)
    elif bonus_strawberry in range(4000, 5001):
        bonus2 = gaji_pokok * (30/100)
    elif bonus_strawberry in range(3000, 4000):
        bonus2 = gaji_pokok * (15/100)
    # bonus kacang
    if bonus_kacang in range(5001,6001):
        bonus3 = gaji_pokok * (40/100)
    elif bonus_kacang in range(4000, 5001):
        bonus3 = gaji_pokok * (30/100)
    elif bonus_kacang in range(3000, 4000):
        bonus3 = gaji_pokok * (15/100)

def kalkulasi_B():
    global bonus1, bonus2, bonus3
    # bonus Coklat
    if bonus_coklat in range(5001,6001):
        bonus1 = gaji_pokok * (25/100)
    elif bonus_coklat in range(4000, 5001):
        bonus1 = gaji_pokok * (20/100)
    elif bonus_coklat in range(3000, 4000):
        bonus1 = gaji_pokok * (15/100)
    # bonus strawberry
    if bonus_strawberry in range(5001,6001):
        bonus2 = gaji_pokok * (30/100)
    elif bonus_strawberry in range(4000, 5001):
        bonus2 = gaji_pokok * (20/100)
    elif bonus_strawberry in range(3000, 4000):
        bonus2 = gaji_pokok * (7/100)
    # bonus kacang
    if bonus_kacang in range(5001,6001):
        bonus3 = gaji_pokok * (30/100)
    elif bonus_kacang in range(4000, 5001):
        bonus3 = gaji_pokok * (20/100)
    elif bonus_kacang in range(3000, 4000):
        bonus3 = gaji_pokok * (7/100)

def kalkulasi_C():
    global bonus1, bonus2, bonus3
    # bonus Coklat
    if bonus_coklat in range(5001,6001):
        bonus1 = gaji_pokok * (15/100)
    elif bonus_coklat in range(4000, 5001):
        bonus1 = gaji_pokok * (10/100)
    elif bonus_coklat in range(3000, 4000):
        bonus1 = gaji_pokok * (5/100)
    # bonus strawberry
    if bonus_strawberry in range(5001,6001):
        bonus2 = gaji_pokok * (20/100)
    elif bonus_strawberry in range(4000, 5001):
        bonus2 = gaji_pokok * (10/100)
    elif bonus_strawberry in range(3000, 4000):
        bonus2 = gaji_pokok * (5/100)
    # bonus kacang
    if bonus_kacang in range(5001,6001):
        bonus3 = gaji_pokok * (20/100)
    elif bonus_kacang in range(4000, 5001):
        bonus3 = gaji_pokok * (10/100)
    elif bonus_kacang in range(3000, 4000):
        bonus3 = gaji_pokok * (5/100)

def deklarasi():
    batas()
    hiasan()
    identitas()
    print("DATA ANDA".center(50))
    hiasan()
    print("Bulan ini Anda berhasil membungkus permen sebanyak:")
    print(f"coklat : {Coklat} bungkus")
    print(f"Strawberry : {Strawberry} bungkus")
    print(f"Kacang : {Kacang} bungkus")
    hiasan()
    print("Anda mendapatkan bonus, jika total bonus Anda".center(50))
    print("di antara 3000 dan 6000 point,".center(50))
    print("di masing-masing varian".center(50))
    hiasan()
    print(f"bonus coklat : {bonus_coklat} point")
    print(f"bonus Strawberry : {bonus_strawberry} point")
    print(f"bonus Kacang : {bonus_kacang} point")
    hiasan()

def gaji():
    batas()
    hiasan()
    identitas()
    print("PERHITUNGAN GAJI".center(50))
    hiasan()
    print(f"Gaji pokok Anda senilai Rp{gaji_pokok}")
    if bonus1 != 0:
        hiasan()
        print(f"Anda mendapatkan bonus dari pembungkusan permen\nCoklat sebesar Rp{bonus1}")
    if bonus2 != 0:
        hiasan()
        print(f"Anda mendapatkan bonus dari pembungkusan permen\nstrawberry sebesar Rp{bonus2}")
    if bonus3 != 0:
        hiasan()
        print(f"Anda mendapatkan bonus dari pembungkusan permen\nkacang sebesar Rp{bonus3}")
    if bonus1 == 0 and bonus2 == 0 and bonus3 == 0:
        hiasan()
        print("Anda tidak mendapatkan bonus.")
    hiasan()
    print(f"Gaji total yang Anda terima senilai Rp{gaji_pokok+bonus1+bonus2+bonus3}")
    hiasan()

def lanjutkan():
    global lanjut
    while True:
        batas()
        hiasan()
        lanjut = input("1. Hitung gaji karyawan lagi\n2. Matikan program\n>>> ")
        if lanjut == "1":
            break
        elif lanjut == "2":
            break
        else:
            data_salah()
    hiasan()

# program utama
lanjut = "1"
while lanjut == "1":
    bonus1 = 0
    bonus2 = 0
    bonus3 = 0
    hiasan()
    print("KALKULASI PERHITUNGAN DATA KARYAWAN PERMEN".center(50, "|"))
    hiasan()
    biodata_kariawan()
    # input-an data
    data_coklat()
    data_strawberry()
    data_kacang()
    # kalkulasi bonus
    if level_karyawan == "1":
        kalkulasi_A()
    elif level_karyawan == "2":
        kalkulasi_B()
    else:
        kalkulasi_C()
    # deklarasi input-an
    deklarasi()
    # total gaji
    gaji()
    # lanjut / matikan program
    lanjutkan()
    # jeda
    if lanjut == "1":
        print("\n")
