#encoding utf=8
#定义一个函数，显示可以使用的功能列表给用户
#@_*_ coding: UTF-8: _*_
#@Time:2021/4/13
#@Software:Visual Studio 2019/Pycharm
#@team members:印龙飞，李浩林，李浪


import os
import time
import sys

global file_name 
global temp_file_name
global strX

file_name = ''
temp_file_name = ' '
#temp_file_name = file_name

temp_d = { }
students = []
students2 = []
students20 = []
stu_list_zero = []
Point_to_dict = []
stu_lsit2 = []

def printData(student_new):
    print('id\t姓名\t语文\t数学\t总成绩')
    for info in student_new:
      print(info.get('id') + '\t' +
          str(info.get('name') )+ '\t' +
          str(info.get('score_CN')) + '\t' +
          str(info.get('score_MATH') )+ '\t' +
          str(float(info.get('score_CN')) +float(info.get('score_MATH'))))

def sort():
    Expore()
    student_new = []
    if os.path.exists(file_name):
        # 打开文件，读取数据
        with open(file_name, 'r') as file:
            studentlist = file.readlines()  # 字符串
        # 将字符串转成dict存到列表中
        for list in studentlist:
            student_new.append(eval(list))
        #排序
        a = input("1：升序，2：降序")
        if a=='1':
            a = False
        else:
            a =True
        b = input("请选择排列方式（1语文，2数学,3总成绩）")
        if b == "1":
            student_new.sort(key=lambda x:float(x['score_CN']),reverse = a)
        elif b == "2":
            student_new.sort(key=lambda x: float(x['score_MATH']),reverse = a)
        elif b == "3":
            student_new.sort(key=lambda x: float(x['score_CN'])+float(x['score_MATH']),reverse = a)
        if  student_new:
            printData(student_new)

def Register():
     key2 = ''
     print("-"*30)
     print(" 1.Make the file")
     print(" 2.Use the file")
     print(" 0.Return")
     print("-"*30)
     key2 = int(input("请选择功能（序号）："))

     if key2 == 1:
        global file_name
        file_name = input("please make the filename!")
        print("the filename is ",file_name)
        print("Done")
     elif key2 == 2:
        #global file_name
        file_name = input("please Modify the User!")
        print("Done")
     elif key2 == 0:
        return 
     else:
         print("Warning!")
         

def menu_of_search():
    
    key = ''
    print( '-'*30)
    print(" 1.Piont to search")
    print(" 2.Exporl all")
    print(" 3.Sort")
    print(" 4.Statistics")
    print(" 5.Modify")
    print(" 0.Back to main menu")
    key9 = int(input("请选择功能（序号）："))
    print( '-'*30)

    if key9 == 1:
        choice_search()
    elif key9 == 2:
        Expore()
    elif key9 == 3:
        sort()
    elif key9 == 4:
        Statistics()
    elif key9 == 5:
        Modify()
    elif key9 == 0:
        main() 
    else:
        print("warning")

def menu_of_delete():
    key10 = ''
    print( '-'*30)
    print(" 1.Trash Can  ")
    print(" 2.Recycle Bin")
    print(" 0.Back to main menu")
    key10 = int(input("请选择功能（序号）："))
    print( '-'*30)

    if key10 == 1:
        Delete()
    elif key10 == 2:
        Delete_real()
    elif key10 == 0:
        main()  
    else:
        print("warning")
#定义一个列表，用来存储多个学生的信息


def Insert():
     while(True):
        #print("您选择了添加学生信息功能")
        name = input("请输入学生姓名：")
        print("\n")
        
        if not name:
            break

        age = input("请输入学生年龄:")
        print("\n")
        score_MATH = input("请输入学生MATH成绩：")
        print("\n")
        score_CN = input("请输入学生CN成绩：")
        print("\n")
        stuId = input("请输入学生学号(学号不可重复)：")
        print("\n")
 
        i = 0
        leap = 0

        for temp in students:
            if temp['id'] == stuId:
                leap = 1
                break
            else:
                i = i + 1

        if leap == 1:
            print("输入学生学号重复，添加失败！")
            continue;

        else:
            stuInfo = {}
            stuInfo['name'] = name
            stuInfo['id'] = stuId
            stuInfo['age'] = age
            stuInfo['score_CN'] = score_CN
            stuInfo['score_MATH'] = score_MATH

            students.append(stuInfo)
            print("添加成功！")
           

            condition_key = input("是否继续？(Y/N)")   
            if condition_key =='Y' or condition_key =='y':
                Save_resource(file_name)
                continue;
            elif condition_key == 'N'or condition_key == 'n' :
                Save_resource(file_name)
                main()
 

def Delete():
    global file_name
    global temp_file_name

    flag = 1
    while flag:
        id1 = input("请输入学生id：")
        if id1 != '':
            if os.path.exists(file_name):
                with open(file_name, 'r') as file1:#
                    student2 = file1.readlines()#
            else:
                print("Its Empty")
                student2 = []
            flag1 = False
            if student2:
                with open("temp_delete.txt", 'a') as file3:
                    with open(file_name, 'w') as file2:
                     d = {}
                     for s in student2:
                        d = dict(eval(s))  
                        if d['id'] != id1:
                           file2.write(str(d) + '\n')
                           #print("Test for str ,print str(d) ", str(d))
                            
                        else: 
                            file3.write(str(d) + '\n')
                            #print("Test2 for str ,print str(d) ", str(d))
                            flag1 = True
                            
                    if flag1:
                        print("id为" + id1 + "的学生已经被删除")
                        print("Test for file name one <file_name>:", file_name)
                        #file_name = temp_file_name
                        print("Test for file name one <file_name>:", file_name)
                        print("Test for file name two <temp_file_name>: " ,temp_file_name)
                    else:
                        print("没有找到id为" + id1 + "的同学")
            else:
                print("无该学生信息")
                # continue
            flag = int(input("是否继续删除(1：是/0；否)："))
            return

def Delete_real():
     #flag = 1
     global strX 
     
     key_for_delete = ''
     Expore_in_bin()
     print("\n")
     print("1.Reset your resourse")
     print("2.Delete your resourse")
     print("0.Back to up level menu")
     key_for_delete = int(input("Please choose you wanted: "))
     print( '-'*30)

     if key_for_delete == 1:
            if os.path.exists("temp_delete.txt"):
             sname = input("请输入要恢复的标识ID")
             with open("temp_delete.txt", 'r') as file4:
                student_read = file4.readlines()  
                for mm in student_read:  
                    student_dict = dict(eval(mm))  
                    if student_dict['name'] ==sname:  
                        stu_lsit2.append(student_dict)  
                        Reset_resource(file_name)
            else:
                print("Its Empty")
            file4.close()  

     elif key_for_delete == 2:
        if os.path.exists("temp_delete.txt"):
            os.remove("temp_delete.txt")
            print("Done")
        else:
            print("The file does not exist")

     elif key_for_delete == 0:
        menu_of_delete()

     else:
        print("Warning!")



def Modify():
    Expore()
    flag=1
    while flag:
      id1=input("请输入要修改学生的id")
      if os.path.exists(file_name):
        with open(file_name,'r') as file1:
            student2 = file1.readlines()
      else:
        return
      with open(file_name, 'w') as file2:
        d = { }
        for s in  student2:
            d = dict(eval(s))  # 得到一个学生字典
            if d["id"] == id1:#符合条件
                while 1:
                    try:  # 若输入为空
                        d["name"] = input("请输入修改后的姓名")
                        d["age"] = input("请输入修改后年龄")
                        d["score_CN"] = input("请输入修改后的CN成绩")
                        d["score_MATH"] = input("请输入修改后的MATH成绩")
                    except:
                        print("输入无效，请重新输入")
                    else:
                        break
                file2.write(str(d)+"\n")
                print("修改成功") 
                flag = int(input("是否继续修改(1：是/0；否)："))
            else:
                print("please input again")
                file2.write(str(d)+"\n")
        
      


def Search():
        
    stu_lsit1 = []
    while  True:
        if os.path.exists(file_name):
            num = input("请输入要查询的ID")
            with open(file_name, 'r') as file:
                student_read = file.readlines() 
                for mm in student_read:  
                    student_dict = dict(eval(mm))  
                    if student_dict['id'] ==num: 
                        stu_lsit1.append(student_dict) 
            # 关闭文件
            if file:
                file.close()
            # 显示查询的结果
            print("查询结果为：")
            print(stu_lsit1)
        else:
            print("文件不存在！请验证后重试")

        condition_key = input("是否继续？(Y/N)")   
        if condition_key =='Y':
            stu_lsit1.clear()
            continue;
        elif condition_key == 'N':
                break

def search_by_name():
    stu_lsit1 = []
    while  True:
        if os.path.exists(file_name):
            # 输入查询的关键字
            name = input("请输入要查询的姓名")
            # 打开文件
            with open(file_name, 'r') as file:
                student_read = file.readlines()  
                # 匹配与查询关键字
                for mm in student_read:  
                    student_dict = dict(eval(mm))  
                    if student_dict['name'] ==name:  
                        stu_lsit1.append(student_dict)  
            # 关闭文件
            if file:
                file.close()
            # 显示查询的结果
            print("查询结果为：")
            print(stu_lsit1)
        else:
            print("文件不存在！请验证后重试")   
        condition_key = input("是否继续？(Y/N)")   
        if condition_key =='Y':
            stu_lsit1.clear()
            continue;
        elif condition_key == 'N':
                break


def choice_search():
    print('*'*20)
    print("1.按姓名查询")
    print("2.按学号查询")
    print("0.返回上一级菜单")
    print('*'*20)
    choice =int( input("请选择:"))
    
    if choice == 1:
        print('*'*20)
        search_by_name()
        print('*'*20)
    elif choice == 2:
        print('*'*20)
        Search()
        print('*'*20)
    elif choice == 0:
        menu_of_search() 
    else:print("Warning!")

        

def Expore():
       if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            stu_str = file.readlines()
            print('{:>8}{:>15}{:>20}{:>20}{:>16}'.format('id', '姓名', 'CN成绩', 'MATH成绩', '总成绩'))
            for stu in stu_str:
                temp_students = dict(eval(stu))
                print('{:>8}{:>15}{:>17}{:>24}{:>20}'.format(temp_students['id'], temp_students['name'], temp_students['score_CN'], temp_students['score_MATH'], int(temp_students['score_CN'])+int(temp_students['score_MATH'])))
       else:
        print("文件不存在，无法显示！")
           
def Expore_in_bin():
        if os.path.exists("temp_delete.txt"):
         with open("temp_delete.txt", 'r', encoding='utf-8') as file:
            stu_str = file.readlines()
            print('{:>8}{:>15}{:>20}{:>20}{:>16}'.format('id', '姓名', 'CN成绩', 'MATH成绩', '总成绩'))
            for stu in stu_str:
                temp2_students = dict(eval(stu))
                print('{:>8}{:>15}{:>17}{:>24}{:>20}'.format(temp2_students['id'], temp2_students['name'], temp2_students['score_CN'], temp2_students['score_MATH'], int(temp2_students['score_CN'])+int(temp2_students['score_MATH'])))
        else:
         print("文件不存在，无法显示！")
        file.close()

def  Save_resource(file_name):
        try:
            file = open(file_name, 'a', encoding='utf-8')  # 追加数据文件
        except:
            file = open(file_name, 'w', encoding='utf-8')  # 覆盖
             # 字典数据写入文件
        else:
            for file_test in students:
                file.write(str(file_test) + "\n")
                students.clear()
                
        print("保存成功")

def  Reset_resource(file_name):
        try:
            file = open(file_name, 'a', encoding='utf-8')  # 追加数据文件
        except:
            file = open(file_name, 'a', encoding='utf-8')  # 覆盖
             # 字典数据写入文件
        else:
            
            file.write("\n")
            for file_test in stu_lsit2:
                file.write(str(file_test))
                students.clear()
                
        print("恢复成功")


def  Statistics():
    student_new = []
    if os.path.exists(file_name):
        # 打开文件，读取数据
        with open(file_name, 'r') as file:
            studentlist = file.readlines()  # 字符串
            if studentlist:
                print("一共有%d名学生"% len(studentlist))
            else:
                print("没有录入学生")
    else:
        print("未找到文件")


def showMenu():
    print("\n")
    print( '-'*30)
    key = 0 
    print(" 1.注册 ")
    print(" 2.录入数据")
    print(" 3.查询数据")
    print(" 4.回收站  ")
    print(" 0.退出 ")
    print( '-'*30)

def Process_bar():
    glag = 0
    if glag == 0:
        for i in range(1, 101):
            print("\r", end="")
            print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
            sys.stdout.flush()
            time.sleep(0.05)
        glag = 1
    else:
        main()

def main():
    while True:
        showMenu()
        key = ''
        key = int(input("请选择功能（序号）："))
 
        if key == 1:
          Register()

        elif key == 2:
          Insert() 
 
        elif key == 3:
           menu_of_search()

        elif key == 4:
            menu_of_delete()

        elif key == 0:
        
            quitconfirm = input("亲，真的要退出么 （yes或者no）??~~(>_<)~~??")
            if quitconfirm == 'yes':
               print("欢迎使用本系统，谢谢")
               exit(0) 
        else:
            print("您输入有误，请重新输入")


Process_bar()
main()
        

