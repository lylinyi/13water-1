def judge(status):
    if (status == 1001):
        return ("用户名已被使用")
    elif (status == 1002):
        return("学号已绑定")
    elif (status == 1003):
        return("教务处认证失败")
    elif (status == 1005):
        return("用户名或密码错误，请重试！")
    elif (status == 2001):
        return("用户名已被使用")
    elif (status == 2002):
        return("出千")
    elif (status == 2003):
        return("不合法墩牌")
    elif (status == 2004):
        return("战局不存在或未结束")
    elif (status == 2005):
        return("格式错误")
    elif (status == 2006):
        return("超时")
    elif (status == 3001):
        return("战局不存在或未结束")
    elif (status == 3002):
        return("该账号不存在，请注册！")
    elif (status == 5000):
        return("出现未知错误，请重试！")
    else:
        return 0