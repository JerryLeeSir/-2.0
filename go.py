# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import requests
import datetime
from datetime import date
import smtplib
​
url = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
req_url = "https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus"
​
header = {
​
        'Host': 'zhxg.qau.edu.cn',##根据自己解析出的内容填写
        'Connection': 'keep-alive',##根据自己解析出的内容填写
        'Content-Length': '****',##根据自己解析出的内容填写
        'AppType': '*********',##根据自己解析出的内容填写
        'User-Agent': '*******',##根据自己解析出的内容填写
        'content-type': 'application/json',
        'Referer': '',##根据自己解析出的内容填写
        'Accept-Encoding': 'gzip, deflate, br',
​
}
Header = {
    'Host': 'zhxg.qau.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '*********',##根据自己解析出的内容填写
    'AppType': '*******',##根据自己解析出的内容填写
    'User-Agent': '*************',##根据自己解析出的内容填写
    'X-Token': '************',##根据自己解析出的内容填写
    'content-type': 'application/json;charset=UTF-8',##根据自己解析出的内容填写
    'Referer': 'https://zhxg.qau.edu.cn/xgwui/',
    'Accept-Encoding': 'gzip, deflate, br',
​
}
nowday = str(date.today().year)+"-"+str(date.today().month)+"-"+str(date.today().day)
Json = {
    'City': '***',##根据自己解析出的内容填写
    'Community': '***',##根据自己解析出的内容填写
    'CommunityDate': ****,##根据自己解析出的内容填写
    'ContactDate': *****,##根据自己解析出的内容填写
    'ContactPerson': '*****',##根据自己解析出的内容填写
    'Country': '****',##根据自己解析出的内容填写
    'County': '***',##根据自己解析出的内容填写
    'CurrentPosition': '******',##根据自己解析出的内容填写
    'DayTemperature': '****',##根据自己解析出的内容填写
    'FollowDate': ****,##根据自己解析出的内容填写
    'FollowingCon': '*****',##根据自己解析出的内容填写
    'GoToDate': ****,##根据自己解析出的内容填写
    'GoToEpidemic': '*****',##根据自己解析出的内容填写
    'Health': '*****',##根据自己解析出的内容填写
    'HealthRemark': '',##根据自己解析出的内容填写
    'IsColdChain': '0',##根据自己解析出的内容填写
    'IsHeat': '0',##根据自己解析出的内容填写
    'IsLowRiskPerson': '0',##根据自己解析出的内容填写
    'NowCity': '青岛市',##根据自己解析出的内容填写
    'NowCountry': '城阳区',##根据自己解析出的内容填写
    'NowDate': nowday,
    'NowProvince': '山东省',##根据自己解析出的内容填写
    'Practice': '0',##根据自己解析出的内容填写
    'PracticeAddress': '',##根据自己解析出的内容填写
    'PracticeRemark': '',##根据自己解析出的内容填写
    'PracticeTeacher': '',##根据自己解析出的内容填写
    'Province': '山东省',##根据自己解析出的内容填写
    'Remark': '',##根据自己解析出的内容填写
    'street_number': '正阳中路201号',##根据自己解析出的内容填写
    'UserType': '1',##根据自己解析出的内容填写
    'Vaccination': '2',##根据自己解析出的内容填写
}
# 输入账号密码
json = {
    "ApplyType": ******,##根据自己解析出的内容填写
    "LoginName": "***********",##你的学号
    "Pwd": "************"##你的学工系统密码
}
​
def emailgo(msg_to, subject):
    msg_from = '**********'  # 发送方邮箱
    passwd = '*****************'  # 填入发送方邮箱的授权码
    # msg_to = '2205237662@qq.com'  # 收件人邮箱
​
    # subject = "python邮件测试"  # 主题
    content = "此邮件为 佳俊的云端上报系统 发送, 感谢您的支持！"  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()
​
r = requests.post(url,json = json,headers = header,verify=False).json()
token = r["ResultValue"]["Token"]
Header["X-Token"] = token
r = requests.post(req_url,json = Json,headers = Header,verify=False)
time_now = datetime.datetime.now()
print(time_now)
today = str(date.today().month)+"月"+str(date.today().day)+"日"
​
print(r.text)
mase = "上报成功"
if r.text == "{\"ResultValue\":null,\"ResultCode\":1,\"ErrorCode\":2,\"RequestMsg\":\"疫情数据已上报，请勿重复上报\"," \
             "\"DevelopmentMessage\":null}": 
    mase = today + "已经上报过了！\n"
    emailgo("接收方邮箱", mase)
else:
    mase = today + "每日上报成功！\n"
    emailgo("接收方邮箱", mase)
​
with open("log.txt","a+") as f:
    f.write(mase)
​
