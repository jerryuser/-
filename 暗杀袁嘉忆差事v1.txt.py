import datetime
import time
dt2 = datetime.datetime.now()
print(dt2)
xueliang = 100
print('欢迎来到暗杀袁嘉忆差事')
z = ('110104200712182563')
time.sleep(1)
problem = input('你的身份是?1.袁嘉忆 2.其他人')  #身份验证
if problem == 1:
    a = input('请输入你的生日,格式=年+月+日,如20010101')
    int(a)
    if a == 20071218:
        print('验证成功')
        name = 1
    else:
        print('验证失败')
if problem == 2:
    print('验证成功')
    name = 2
time.sleep(1)
b = input('请选择您要杀袁嘉忆的方式,1.自杀,2.眀杀')
if b == 1:
    c = input('你确定要自杀吗?,1.是,2.否')
    if c == 2:
        print('你已取消自杀')
    if c == 1:
        print('您已自杀')
if b == 2:
    d = input('进入眀杀?1.是,2.否')
    if d == 2:
        print('您已取消眀杀')
    if d == 1:
        print('正式进入眀杀袁嘉忆差事成功')
print('一天,你接到任务，需要暗杀袁嘉忆，因为她进行了反社会主义活动')
time.sleep(1)
print('这个是绝密，不能告诉任何人，他逃跑后对国家安全影响很大')
time.sleep(1)
print('于是你开始了漫长的搜索')
time.sleep(3)
print('突然,你发现了可疑人物，然后你开始跟踪他')
time.sleep(2)
print('你从反光镜中看到了她，并确认了是袁嘉忆，但是她没有发现你')
time.sleep(1)
print('你打开了车的自动驾驶功能，并设置为自动跟踪')
time.sleep(0)
e = input('你使用火箭筒瞄准了他的车，是否开炮?1.是，2.否')
if e == 2:
    xueliang = 100
if e == 1:
    xueliang = 70
print('袁嘉忆的血量剩余')
print(xueliang)
















