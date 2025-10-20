# Câu 10: Vẽ hình dùng Sleep
# Yêu cầu:
# Vẽ 4 hình dưới đây, dùng sleep để xuất hiện từng hình sau 5 giây

# import turtle
# import time

import time
import os

# 4 hình dạng bằng chuỗi nhiều dòng
shape1 = r"""
      *
      * *
      * * *
* * * * * * *
* * *
* *
*
"""

shape2 = r"""
      *
      * *
      *   *
* * * * * * *
*   *
* *
*
"""

shape3 = r"""
      * * * *
      * * * 
      * *
      *
    * *
  * * * 
* * * * 
"""

shape4 = r"""
      * * * *
      *   * 
      * *
      *
    * *
  *   * 
* * * * 
"""

shapes = [shape1, shape2, shape3, shape4]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

for i, s in enumerate(shapes, start=1):
    clear_screen()
    print(f"HÌNH {i}:\n")
    print(s)
    # hiện 5 giây rồi chuyển sang hình tiếp
    time.sleep(5)

# kết thúc: giữ màn hình cuối cùng (tùy chọn)
print("\nHoàn thành.")


# def ve_hinh_1():
#     turtle.penup()  #Nhấc bút lên, nghĩa là con rùa di chuyển mà không vẽ nét trên màn hình.
#     turtle.goto(-100, 0)    #Di chuyển con rùa đến tọa độ (-100, 0)
#     turtle.pendown()    #Hạ bút xuống, nghĩa là con rùa di chuyển và vẽ nét
#     for i in range(3):  # 3 có nghĩa là vẽ 3 cạnh của tam giác
#         turtle.color("red")    #Đổi màu bút vẽ thành màu đỏ
#         turtle.forward(300)   # Vẽ 1 cạnh dài 300
#         turtle.left(120)      # Quay 120 độ để tạo góc tam giác đều
#         turtle.forward(150)
#         turtle.left(150) 
        
#         turtle.color("red")    #Đổi màu bút vẽ thành màu đỏ
#     turtle.done()   #Kết thúc chương trình vẽ

# def ve_hinh_2():
#     turtle.penup()  #Nhấc bút lên, nghĩa là con rùa di chuyển mà không vẽ nét trên màn hình.    
#     turtle.goto(-100, 0)    #Di chuyển con rùa đến tọa độ (-100, 0)
#     turtle.pendown()    #Hạ bút xuống, nghĩa là con rùa di chuyển và vẽ nét
#     turtle.square(100)  #Vẽ hình vuông có cạnh 100
#     turtle.done()   #Kết thúc chương trình vẽ

# def ve_hinh_3():
#     turtle.penup()  #Nhấc bút lên, nghĩa là con rùa di chuyển mà không vẽ nét trên màn hình.
#     turtle.goto(-100, 0)    #Di chuyển con rùa đến tọa độ (-100, 0)
#     turtle.pendown()    #Hạ bút xuống, nghĩa là con rùa di chuyển và vẽ nét
#     turtle.circle(100)  #Vẽ hình tròn có bán kính 100
#     turtle.done()   #Kết thúc chương trình vẽ

# def ve_hinh_4():
#     turtle.penup()
#     turtle.goto(-100, 0)
#     turtle.pendown()
#     turtle.rectangle(100, 50)
#     turtle.done()
# Vẽ hình 1
# ve_hinh_1() 
# time.sleep(5)
# Vẽ hình 2
# ve_hinh_2()
# time.sleep(5)
# # Vẽ hình 3
# ve_hinh_3()
# time.sleep(5)
# # Vẽ hình 4
# ve_hinh_4() 
# time.sleep(5)

