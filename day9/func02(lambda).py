# def func01(*par):
#     print(type(par))
#     for i in par:
#         print(i)
# func01(10,20,30,40)

# def big(a,b):
#     if a>b:
#         return a 
#     else:
#         return b

# result = big(10,20)
# print(result)

# bi = lambda a,b : a if(a>b) else b
# result = bi(200,1000)
# print(result)

# bi = lambda a : a+1000
# print(bi(100))


# li=['100','200','300']
# #1
# for i in range(len(li)) :
#     li[i]=str(int(li[i])+10)
# print(li)

# #2
# li = list(map(int,li))
# for i in range(len(li)) :
#     li[i]=str(li[i]+10)
# print(li)

# #3
# def test1(a):
#     return str(int(a)+10)
# li = list(map(test1,li))
# print("함수" , li)

# #4
# lb = lambda x : str(int(x)+10)
# li = list(map(lb,li))
# print("lambda:",li)

# #4-1
# li = list(map(lambda x : str(int(x)+10),li))
# print("lambda:",li)


# day = {'날짜':['2018.01.01','2019.02.02','2020.03.03']}
# #1
# for i in day['날짜']:
#     li=i.split('.')
#     print(li[0]+'년'+li[1]+'월'+li[2]+'일')

# #2
# li= list(map(lambda x: x.split('.') , day['날짜']))
# for i in li:
#     print(f"{i[0]}년{i[1]}월{i[2]}일")


    
