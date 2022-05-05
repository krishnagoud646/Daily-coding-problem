#given data
l=[10,15,3,7]
k=17
def compute(list,k):
    for i in range(len(l)):
        list_len=len(list)
        base_num = list[0]
        sum_num=0
        #remove the first item 
        list.pop(0)
        list_len=len(list)
        for j in range(list_len):
            sum_num = base_num+list[j]
            if sum_num == k:
                return base_num, list[j]
    return False
i = compute(l,k)

print(f'k({k}),{i[0]}+{i[1]}')
