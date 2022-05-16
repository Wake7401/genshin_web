##Bai 1
##ls = [i for i in range(0,101)]
##print(ls)

##Bai 2
##ls = [i for i in range(0, 101)]
##n = int(input('Nhap n: '))
##print('Cac so nguyen chia het cho {0}: '.format(n))
##for i in ls:
##    print(i, end = '  ') if i % n == 0 else None

##Bai 3
##def Func3(ls):
##    print('Số nhỏ nhất: {0}'.format(min(ls)))
##    print('Số lớn nhất: {0}'.format(max(ls)))
##    print('Tổng các số trong danh sách: {0}'.format(sum(ls)))
##    ls.sort()
##    print('Danh sách đã sắp xếp: {0}'.format(ls))
##
##ls = [10, 12, 9, 8, 13, 23, 14]
##Func3(ls)


##Bai 4
##ls = [1, 'abc', 2, 'bdc', 3.5]
##for i in ls:
##    print(i) if (isinstance(i, int) == True or isinstance(i, float)) else None


##Bai 5
##ls2 = []
##str_num = input('Nhap day so, cac so cach nhau boi phay: ')
##ls1 = str_num.split(',')
##for i in ls1:
##    ls2.append(int(i))
##print(ls2)


##Bài 6
##n, m = int(input('Nhap n: ')), int(input('Nhap m: '))
##ls1 = []
##for i in range(0, n):
##    ls2 = []
##    for j in range(0, m):
##        ls2.append(i * j)
##    ls1.append(ls2)
##print(ls1)

##Bài 7
##ls = []
##while(True):
##    x = input('Nhập số nguyên (exit để thoát): ')
##    if x != 'exit':
##        ls.append(int(x))
##    else:
##        break
##print('Cac so o vi tri chan: ')
##for i in range(0, len(ls)):
##    print(ls[i], end = ' ') if i % 2 != 0 else None

##Bai 8
##ls = []
##while(True):
##    x = input('Nhập phần tử của tuple (exit để thoát): ')
##    if x != 'exit':
##        ls.append(int(x))
##    else:
##        break
##tup = tuple(ls)
##print('Tuple vừa nhập: {0}'.format(tup))
##print(type(ls))

##Bai 9
##ls = [5, '10', 6, '20', 5, '10']
##tup = tuple(ls)
##print(tup)

##Bai 10
##ls_num = []
##ls_string = []
##ls = [4,'b',2,'a',7,'c',1,'d']
##for i in ls:
##    if(type(i) is int):
##        ls_num.append(i)
##    else:
##        ls_string.append(i)
##tup_num = tuple(ls_num)
##tup_string = tuple(ls_string)
##
##print(tup_num)
##print(tup_string)

##Bai 11
##ls = [(2,1),(1,2),(2,2),(3,4)]
##print(sorted(ls))
##Output: [(1, 2), (2, 1), (2, 2), (3, 4)]

##Bai 12
##x = [(2,1,5),(1,2,6),(2,2,2),(3,1,5)]
##def items(i):
##    a = i[1]
##    b = i[2]
##    return a,b
##print(sorted(x, key=items))
##print(sorted(x, key= lambda item: (item[1], item[2])))

##Bai 13
##s = {'a','b','c','a','d','c'}
##print(s)

##Bai 14
##s = set()
##while(True):
##    sp = input('Nhap ten san pham: ')
##    if(sp != 'exit'):
##        s.add(sp)
##    else:
##         break
##print(s)

##Bai 15
##s = set({})
##string = input('Nhập câu tiếng Anh: ')
##string_split = string.split(' ')
##for i in string_split:
##    s.add(i.lower())
##print('Có {0} từ {1}'.format(len(s), s))

##Bai 16
##S = {'a','b','c','d'}
##T = {'b','e','d','f','h'}
##print('Hoi: ', S.union(T))
##print('Giao: ', S.intersection(T))

##Bai 17
##dic = {}
##while(True):
##    sv = input('Nhap thong tin sinh vien (mssv-tenSV): ')
##    if(sv != 'exit'):
##        ls = sv.split('-')
##        dic[ls[0]] = ls[1]
##    else:
##        break
##print(dic)

##Bai 18
##eng = input('Nhập câu tiếng Anh: ')
##ls = eng.split(' ')
##print('So tu: ', len(ls))
##print('So ky tu(khong tinh khoang trang): ', len(''.join(ls)))

##Bai 19
##nhaphang = {}
##while(True):
##  n = input('Nhap ten san pham: ')
##  if(n != 'exit'):
##      s = int(input('Nhap so luong: '))
##      if(n in nhaphang):
##          nhaphang[n] = nhaphang[n] + s
##      else:
##          nhaphang[n] = s
##  else:
##      break
##print(nhaphang)
