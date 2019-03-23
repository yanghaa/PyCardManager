# coding=utf-8
import tools

while True:

    # 显示功能菜单
    tools.show_menu()

    action_str = input("请选择操作功能：")
    print("您选择的操作是：【%s】" % action_str)

    # 1,2,3 针对操作
    if action_str in ["1", "2", "3"]:

        # 新增
        if action_str == "1":
            tools.new_card()

        # 显示
        elif action_str == "2":
            tools.show_card()
        # 查询
        elif action_str == "3":
            tools.search_card()

        pass

    elif action_str == "0":
        print("欢迎再次使用")
        break

    else:
        print("您输入的操作有误请重新输入！")
