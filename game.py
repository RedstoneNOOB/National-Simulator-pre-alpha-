oil = 0
# 石油
money = 0
# 资金
woker = 0
# 工人
PT = 0
# 生产技术
while True:  # 更改循环条件为True，以便在需要时退出循环
    test = input("请输入命令: ")
    if test == "生产":
        money += woker * 2
        print("资金 =", money,"（+10）\n")
        # 生产模块
    elif test == "签到":
        oil += 2
        money += 10
        woker += 10
        PT += 1
        print ("石油 = ", oil, "（+2）\t 资金 = ", money, "（+10）\t 工人 = ", woker, "（+10）\t 生产技术 + 1")
        # 签到模块基本动作
    elif test == "生产石油":
        if money >= 10:  # 确保有足够的资金来生产石油
            money -= 10
            oil += 5
            print("资金 = ", money, "（-10）\t石油 = ", oil,"（+5）\n")
        else:
            print("资金不足，无法生产石油\n")
    # 添加退出循环的命令
    elif test == "退出调试":
        print("我草，你在调试我？！\n")
        # 你在看注释吗
        break
    elif test == "我的资料":
        print("石油 = ", oil,"\t资金 = ", money,"\t工人 = ", woker,"\t 生产技术 = ", PT, "\n")
    else:
        print("这不是命令\n")