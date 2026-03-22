arr = [1,3,2,9]
x = int(input("Nhập số cần tim:"))

found = False

for i in range (len(arr)):
    if arr[i] == x:
        print("Tìm thấy tại vịt trí", i)
        found = True
        break

if not found:
    print("Không tìm thấy")