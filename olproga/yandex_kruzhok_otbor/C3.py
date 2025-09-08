n = int(input())
cnt = 0
k = 1
run = True
cnt = 0
while run:
    mn_num = 10**(k - 1)
    mx_pos_num = n // (10 ** k + 1)
    mx_num = 10 ** k - 1
    if mn_num > mx_pos_num:
        break
    cnt += min(mx_num, mx_pos_num) - mn_num + 1
    k += 1
print(cnt)