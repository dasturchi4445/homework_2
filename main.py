"""
Lineer qidiruv algoritmi (Lineer search) ma'lum bir element ro'yxat yoki massiv ichida qidirish uchun ishlatiladi.
Bu algoritm har bir elementni birma-bir tekshiradi va qidirilayotgan elementni topganda to'xtidi
"""

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
#
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target = int(input("Target : "))
#
# index = linear_search(arr, target)
# if index != -1:
#     print(f"Element topildi, indeksi {index}")
# else:
#     print("Element topilmadi")
#
# print(target)

"""
Binary qidiruv algoritmi (Binary Search) saralangan (sorted) massiv ichida qidiruv uchun ishlatiladi. Algoritm dastlab 
massivni ikki qisimga bo'ladi va qidirilayotgan elementni massivning o'rtasidagi element bilan solishtiradi. Agar
element o'rtada bo'lsa qidiruv to'xtidi. Aks xolda, qidiruv chap yoki o'ng qisimda davom etadi.
"""

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
#
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target = int(input("Target : "))
#
# index = binary_search(arr, target)
# if index != -1:
#     print(f"Element topildi, indeksi {index}")
# else:
#     print("Element topilmadi")


"""
Lineer qidiruv algoritmi har bir elementni birma-bir tekshiradi va vaqt murakkabligi O(n).
Binary qidiruv saralangan massivda qidiruv qiladi va vaqt murakkabligi O(logn).

Binary qidiruv algoritmi faqat saralangan massivlar uchun ishlatiladi shuning uchun qidiruvdan oldin massivni saralash
talab qilinadi.
Lineer qidiruv algoritmi esa har qanday massivda ishlaydi.
"""


