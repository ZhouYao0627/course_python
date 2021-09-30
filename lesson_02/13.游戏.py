# 唐僧大战白骨精

print('欢迎光临唐僧大战白骨精游戏！')
print('请选择你的身份:')
print('1.唐僧')
print('2.白骨精')
print('请选择(按-1退出程序)：')
player_choose = input()
while player_choose != -1:
    if player_choose == '1':
        print('您选择的是唐僧')

        attack_tan = 1
        life_tan = 10
        attack_Boss = 5
        life_Boss = 100
        print('唐僧 攻击力:%d 生命值:%d'%(attack_tan,life_tan))
        print('Boss 攻击力:%d 生命值:%d'%(attack_Boss,life_Boss))

        print('您可以选择：')
        print('1、练级')
        print('2、打Boss')
        print('3、逃跑')
        print('请选择：')
        choose = input()
        while choose != 0:
            if choose == '1':
                print('练级')
                attack_tan += 1
                life_tan += 10
                print('唐僧 攻击力:%d 生命值:%d' % (attack_tan, life_tan))
            elif choose == '2':
                print('打Boss')
                life_Boss -= attack_tan
                if life_Boss < '0':
                    print('唐僧攻击Boss%d点伤害，剩余生命值%d' % (attack_tan, life_tan))
                    break
                life_tan -= attack_Boss
                if life_tan < '0':
                    print("Boss攻击唐僧%d点伤害，剩余生命值%d" % (attack_Boss, life_Boss))
                    break
                # if life_tan <= 0:
                #     print('唐僧牺牲')
                # elif life_Boss <= 0:
                #     print('Boss牺牲')
            elif choose == '3':
                print('退出游戏！')
                exit()
            else:print('您的输入有误，请重新输入')
            print('您可以选择：')
            print('1、练级')
            print('2、打Boss')
            print('3、逃跑')
            print('请选择：')
            choose = input()
    elif player_choose == '2':
        print('您选择的是白骨精')
    elif player_choose == '-1':
        print('退出成功')
        exit()
    else:
        print('您选择的不合规范，请重新输入：')
    player_choose = input()

















