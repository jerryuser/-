import datetime
import time
dt2 = datetime.datetime.now()
print(dt2)
xueliang = 100
print('��ӭ������ɱԬ�������')
z = ('110104200712182563')
time.sleep(1)
problem = input('��������?1.Ԭ���� 2.������')  #�����֤
if problem == 1:
    a = input('�������������,��ʽ=��+��+��,��20010101')
    int(a)
    if a == 20071218:
        print('��֤�ɹ�')
        name = 1
    else:
        print('��֤ʧ��')
if problem == 2:
    print('��֤�ɹ�')
    name = 2
time.sleep(1)
b = input('��ѡ����ҪɱԬ����ķ�ʽ,1.��ɱ,2.�bɱ')
if b == 1:
    c = input('��ȷ��Ҫ��ɱ��?,1.��,2.��')
    if c == 2:
        print('����ȡ����ɱ')
    if c == 1:
        print('������ɱ')
if b == 2:
    d = input('����bɱ?1.��,2.��')
    if d == 2:
        print('����ȡ���bɱ')
    if d == 1:
        print('��ʽ����bɱԬ������³ɹ�')
print('һ��,��ӵ�������Ҫ��ɱԬ���䣬��Ϊ�������˷��������')
time.sleep(1)
print('����Ǿ��ܣ����ܸ����κ��ˣ������ܺ�Թ��Ұ�ȫӰ��ܴ�')
time.sleep(1)
print('�����㿪ʼ������������')
time.sleep(3)
print('ͻȻ,�㷢���˿������Ȼ���㿪ʼ������')
time.sleep(2)
print('��ӷ��⾵�п�����������ȷ������Ԭ���䣬������û�з�����')
time.sleep(1)
print('����˳����Զ���ʻ���ܣ�������Ϊ�Զ�����')
time.sleep(0)
e = input('��ʹ�û��Ͳ��׼�����ĳ����Ƿ���?1.�ǣ�2.��')
if e == 2:
    xueliang = 100
if e == 1:
    xueliang = 70
print('Ԭ�����Ѫ��ʣ��')
print(xueliang)
















