#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ф��
���ڣ�2022-5-8
"""




# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "ֽ":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
    else:
        return "error:no correct name"
    return number#����Ϸ�����Ӧ����ͬ������

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(num):
    if num == 0:
        return "ʯͷ"
    elif num == 1:
        return "ʷ����"
    elif num == 2:
        return "ֽ"
    elif num == 3:
        return "����"
    elif num == 4:
        return "����"
    return name
    
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    #��дִ�д���,������ɺ�passɾ��


import random
def rpsls(player_choice):
    print("����ѡ����",player_choice)
    player_number=name_to_number(player_choice)#���ú���������ת��Ϊ����
    comp_number=random.randrange(0,5)#���ѡ������
    com_choice=number_to_name(comp_number)#���ú���������ת��Ϊ����
    print("�������ѡ��Ϊ:%s"%com_choice)
    difference=(player_number-comp_number)%5#���庯���жϽ��
    if difference == 1 or difference ==2:
        print("��Ӯ��")
    elif difference == 3 or difference == 4:
        print("�����Ӯ��")
    else:
        print("���ͼ��������һ����")



    
    
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("�����ǣ������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ���ˣ�ʷ���˴��������������ն���棻����Ե�ֽ��ֽ����ʷ���ˣ�ʷ��������ʯͷ")
print("----------------")
print("����������ѡ��:")
choice=input()
rpsls(choice)#������Ϸ����



