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

    # 提示输入
    find_name = input("请输入要查找的姓名：")
    # 遍历查询如果没有则提示
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "QQ", "email"]:
                print(name, end="\t\t")
            print("")
            print("="*symbol_number)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (
                card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            print("="*symbol_number)

            # TODO 针对找到的名片进行修改
            deal_card(card_dict)
            break

    else:

        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """处理查询到的名片"""
    action_str = input("请输入要进行的操作：1 修改 2 删除 0 返回上级菜单！")

    if action_str in ["1", "2", "0"]:
        if action_str == "1":
            print("请输入要正确的信息：")
            find_dict["name"] = input_card_info(
                find_dict["name"], "请输入姓名[回车不修改]:")
            find_dict["phone"] = input_card_info(
                find_dict["phone"], "请输入电话[回车不修改]：")
            find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ[回车不修改]：")
            find_dict["email"] = input_card_info(
                find_dict["email"], "请输入email[回车不修改]：")
            print("修改成功！")
        elif action_str == "2":
            print("删除名片")
            card_list.remove(find_dict)
            print("成功删除了%s的名片。" % find_dict["name"])
        elif action_str == "3":
            return

    else:
        print("请输入正确的功能序号！1 修改 2 删除 0 返回上级菜单！")
        deal_card(find_dict)


def input_card_info(dict_value, tip_message):

    # 1提示用户输入
    result_str = input(tip_message)
    # 2针对输入判断修改
    if len(result_str) > 0:
        return result_str
    # 3如果没输入则保留原值
    else:
        return dict_value
