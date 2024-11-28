n = 0
def hanoi(j,p1,p2,p3):
    '''
    函数定义：将n个盘子从p1挪到p3
    :param j:盘子数量
    :param p1:柱子1
    :param p2:柱子2
    :param p3:柱子3
    :return:一共移动的次数
    '''
    global n
    if j == 1:
        print('将1片圆环从%s挪到%s' %(p1,p3))
    else:
        hanoi(j-1, p1, p3, p2)
        print('将1片圆环从%s挪到%s' % (p1, p3))
        hanoi(j-1, p2, p1, p3)
    n += 1
    return n

j = int(input('输入盘子的总数：'))

print('一共移动了%d次盘子' %(hanoi(j,'z1','z2','z3')))
