# Câu 3: Viết Hàm tính BMI

def tinh_bmi(cannang, chieucao):
    return cannang / (chieucao ** 2)
def xep_loai(bmi):
    if bmi < 18.5:
        return "Gay"
    elif bmi <= 24.9:
        return "Binh thuong"
    elif bmi <= 29.9:
        return "Hoi beo"
    elif bmi <= 34.9:
        return "Beo cap do 1"
    elif bmi < 39.9:
        return "Beo cap do 2"
    else:
        return "Beo cap do 3"  
def NguyCoBenh (bmi):
    if bmi < 18.5:
        return "Thap"
    elif bmi <= 24.9:
        return "Binh thuong"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Rat cao"
    elif bmi <=  39.9:
        return "Nguy hiem"
    else:
        return "Rat nguy hiem"
print("Chuong trinh tinh BMI")
cannang = float(input("Nhap can nang (kg): "))
chieucao = float(input("Nhap chieu cao (m): "))
bmi = tinh_bmi(cannang, chieucao)
print("Chi so BMI cua ban la: ", bmi)
print("Xep loai: ", xep_loai(bmi))
print("Nguy co benh: ", NguyCoBenh(bmi))

