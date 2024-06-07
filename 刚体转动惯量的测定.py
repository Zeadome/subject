# function:该代码用于处理刚体转动惯量实验数据
# author:Zane
# date:2024.4.29
from math import pi

def J_cal(data):
    a2=0
    a1=0
    for i in range(1,5):
        a2+=2*pi*((i+4)*data[i]-i*data[i+4])/(data[i+4]**2*data[i]-data[i]**2*data[i+4])
    a2=a2/4
    k=int(input("请输入计算a1的起始k值,k从减速数据部分取:"))
    for i in range(k-1,k+3):
        a1+=2*pi*((i+4)*data[i]-i*data[i+4])/(data[i+4]**2*data[i]-data[i]**2*data[i+4])
    a1=a1/4
    j=(m/1000)*g*(r/100)/(a2-a1)-a2/(a2-a1)*(m/1000)*(r/100)**2
    return j

m=float(input("请输入砝码的质量m(g):"))
r=float(input("请输入塔轮半径r(cm):"))
m1=float(input("请输入铝环的质量m1(kg):"))
d1=float(input("请输入铝环的内径d1(cm):"))
d2=float(input("请输入铝环的外径d2(cm):"))
m2=float(input("请输入铝盘的质量m2(kg):"))
d=float(input("请输入铝盘的直径d(cm):"))
g=9.785
print("东莞本地重力加速度理论值为9.785,因此g=9.785m/s^2")

print("----------------")

print("以下求不放样J。")
data1=[0,0.892,1.264,1.549,1.789,2.001,2.193,2.369,2.533,2.688,2.835,2.982,3.130,3.278,3.426,3.576,3.725,3.875,4.025,4.176,4.327,4.480,4.632,4.785,4.938,5.092,5.246,5.401,5.556,5.713]    #改成自己的数据
re=J_cal(data=data1)
print(f"不放样J。为{re}")

print("--------------")

print("以下求铝环的J")
data2=[0,1.385,2.023,2.516,2.930,3.296,3.625,3.930,4.212,4.479,4.732,4.987,5.240,5.495,5.750,6.006,6.261,6.518,6.775,7.033,7.290,7.549,7.807,8.067,8.327,8.588,8.848,9.110,9.372,9.635]     #改成自己的数据
result1=m1*((d1/100)**2+(d2/100)**2)/8
result2=J_cal(data=data2)-re
delta1=result2-result1
e1=delta1/result1
print(f"铝环J的理论值为{result1}")
print(f"铝环J的测量值为{result2}")
print(f"测量值-理论值={delta1}")
print(f"相对误差E={e1}")

print("--------------")

print("以下求铝盘的J")
data3=[0,1.243,1.803,2.235,2.597,2.918,3.208,3.475,3.723,3.956,4.179,4.402,4.625,4.850,5.074,5.300,5.525,5.752,5.979,6.207,6.435,6.664,6.893,7.123,7.353,7.585,7.816,8.049,8.282,8.516]     #改成自己的数据
result3=m2*((d/100)**2)/8
result4=J_cal(data=data3)-re
delta2=result4-result3
e2=delta2/result3
print(f"铝盘J的理论值为{result3}")
print(f"铝盘J的测量值为{result4}")
print(f"测量值-理论值={delta2}")
print(f"相对误差E={e2}")
print("--------------")