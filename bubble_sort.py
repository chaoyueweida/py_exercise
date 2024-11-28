a = eval(input("请以'[,,,]'格式输入列表:\n"))

def bubble_sort(a):
    '''
    冒泡排序
    :param a: 列表
    :return: 排序后列表
    '''
    n = 0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            n += 1
    print('共比较了%d次' %n)
    return a
print(bubble_sort(a))

