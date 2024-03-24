#caulenhlap
#1
total = 0

for num in range(101):
    if num % 3 == 0:
        total += num

print("Tổng các số chia hết cho 3 trong khoảng từ 0 đến 100 là:", total)

#2
count_even = 0
for num1 in range(51):
    if num1 % 2 == 0:
        count_even += 1

print("Số lượng các số chẵn trong khoảng từ 0 đến 50 là:", count_even)

#3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập số cần kiểm tra: "))

if is_prime(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không là số nguyên tố.")