"""
if i < j:
    if i < k:
        i = j
    else:
        i = k
else:
    if i > k:
        j = i
    else:
        i = k
print("i =", i, "j=",j,"k=",k)
"""

"""
(a) i=3, j=5, k=7

i<j? 3<5 → True

j<k? 5<7 → True → i = j = 5
→ Kết quả: i=5, j=5, k=7

(b) i=3, j=7, k=5

i<j? 3<7 → True

j<k? 7<5 → False → j = k = 5
→ Kết quả: i=3, j=5, k=5

(c) i=5, j=3, k=7

i<j? 5<3 → False

j>k? 3>7 → False → i = k = 7
→ Kết quả: i=7, j=3, k=7

(d) i=5, j=7, k=3

i<j? 5<7 → True

j<k? 7<3 → False → j = k = 3
→ Kết quả: i=5, j=3, k=3

(e) i=7, j=3, k=5

i<j? 7<3 → False

j>k? 3>5 → False → i = k = 5
→ Kết quả: i=5, j=3, k=5

(f) i=7, j=5, k=3

i<j? 7<5 → False

j>k? 5>3 → True → j = i = 7
→ Kết quả: i=7, j=7, k=3
"""
