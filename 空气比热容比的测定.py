# function:用于空气比热容比的测定实验
# author:Zane
# data:2024/5/12

import math

def r_calculate():      #计算r
    r_list=[]       #创建列表用于存储r
    for i in range(6):      #6组实验数据
        p1_1=float(input("请输入p1'的数据(mV):"))       #p1'的数据
        p2_1=float(input("请输入p2'的数据(mV):"))       #p2'的数据
        p1=(106.5+p1_1/20)/100      #根据公式算出p1
        p2=(106.5+p2_1/20)/100      #根据公式算出p2
        print(f"p1的数据:{p1}\np2的数据:{p2}")      #输出p1,p2用于表格填写
        r=math.log(p1/p0)/math.log(p1/p2)       #计算r
        r_list.append(r)        #将r存储到列表
        print(f"r={r}")         #输出r方便表格填写
    return r_list       #返回列表用于后期处理

def gap(list):      #计算偏差u和ur
    r_list=list     #继用列表
    n=6     #实验组数
    u=math.sqrt(sum([math.pow((r_ave-a),2) for a in r_list])/(n-1))     #计算标准偏差u
    print(f"标准偏差u:{u}")     #输出u,方便数据填写
    print(f"相对标准偏差ur:{u/r_ave}")      #输出ur，方便数据填写
    return u/r_ave      #返回r的平均值，用于后期处理

if __name__=='__main__':
    p0=1.065        #气压计测得，如果不同可自行修改
    r_list=r_calculate()        #获得包含6个实验组的r
    r_ave=sum(r_list)/len(r_list)       #求r的平均值
    print(f"r的平均:{r_ave}")       #输出r的平均值用于填写
    ur=gap(r_list)      #获取相对标准偏差ur
    print(f"r=({r_ave-ur},{r_ave+ur})")     #求上下浮动区间并输出
    