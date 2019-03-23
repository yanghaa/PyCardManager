# coding=utf-8

# 记录所有名片字典
card_list = []
symbol_number = 60


def show_menu():

    print("*"*symbol_number)
    print("欢迎使用管理系统")
    print("")
    print("1、新增名片")
    print("2、显示名片")
    print("3、搜索名片")
    print("0、退出系统")
    print("")
    print("*"*symbol_number)


def new_card():
    """新增名片"""
    print("-"*50)
    print("新增名片")
    # 1.提示用户输入信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入email：")

    # 2.建立字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 3.添加到用户字典
    card_list.append(card_dict)
    # print(card_dict)
    # 4.提示用户添加成功
    print("添加%s的名片成功！" % name_str)
    print("")


def show_card():
    """显示名片"""
    print("-"*symbol_number)
    print("显示名片")

    # 判断是否存在名片
    if len(card_list) == 0:
        print("当前没有记录请添加新的记录！")
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "email"]:
        print(name, end="\t\t")

    print("")

    # 打印分割线
    print("="*symbol_number)
    # 遍历输出
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (
            card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
    print("="*symbol_number)
    print("")


def search_card():
    """查询名片"""
    print("-"*symbol_number)
    print("查询名片")
