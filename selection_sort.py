a = eval(input("请以'[,,,]'格式输入列表:\n"))

def selection_sort(a):
    '''
    选择排序：通过调换位置逐次确定出最小的元素
    :param a: 列表
    :return: 排序后列表
    '''
    n = 0
    for i in range(len(a)-1):
        minL = i
        for j in range(i+1,len(a)):
            if a[j] < a[minL]:
                a[j],a[minL] = a[minL],a[j]

    return a
print(selection_sort(a))


