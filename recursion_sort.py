import math

a = eval(input("请以'[,,,]'格式输入列表:\n"))
list1 = []

def recursion_sort(a):
    '''
    递归排序
    :param a: 待排序列表
    :return: 已排序列表
    '''
    if len(a) == 1:
        list1.append(a[0])
        return list1
    else:
        max1 = math.inf
        cur = 0
        for j in range(len(a)) :
            if int(a[j]) < max1 :
                max1 = a[j]
                cur = j
        list1.append(max1)
        a.pop(cur)
        return recursion_sort(a)

print(recursion_sort(a))




