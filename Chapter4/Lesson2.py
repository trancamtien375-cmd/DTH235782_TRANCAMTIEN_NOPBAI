# Câu 2: Viết Hàm để chơi Game Đoán Số
# Yêu cầu:
# Máy ra 1 số trong đoạn [1...100]
# Trang 35/84
# Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số
# người chơi đoán nhỏ hơn hay lớn hơn số của mày và hiển thị số lần đoán
# Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
# Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?

from random import randint
while True:
    so_may = randint(1, 100)
    solandoan = 0
    win = False
    while solandoan < 7:
        so_doan = int(input("Nhap so ban doan (1-100): "))
        solandoan += 1
        if so_doan < so_may:
            print("So ban doan nho hon so may")
        elif so_doan > so_may:
            print("So ban doan lon hon so may")
        else:
            print("Chuc mung ban da doan dung")
            win = True
            break
        print("Ban da doan sai", solandoan, "lan")
    if win == False:
        print("Ban da doan sai qua 7 lan. So may la:", so_may)
    tiep_tuc = input("Ban co muon choi tiep khong (y/n)? ")
    if tiep_tuc.lower() != 'y':
        break
print("Cam on ban da choi game!")