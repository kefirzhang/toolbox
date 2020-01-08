import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置文件读取发送人员
config = configparser.ConfigParser()
config.read('config.ini')


class SendEmailWithAttach:
    def __init__(self, mail_host, mail_user, mail_pass):
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user  # 用户名
        self.mail_pass = mail_pass  # 口令
        self.smtpObj = smtplib.SMTP()
        self.smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
        self.smtpObj.login(self.mail_user, self.mail_pass)

    def send(self, sender, receivers, attach_file, file_name):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("菜鸟教程", 'utf-8')
        message['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(attach_file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="' + file_name + '"'
        message.attach(att1)

        try:

            self.smtpObj.sendmail(sender, receivers, message.as_string())
            return "邮件发送成功"
        except smtplib.SMTPException:
            return "Error: 无法发送邮件"


sender = SendEmailWithAttach(config['DEFAULT']['mail_host'], config['DEFAULT']['mail_user'],
                             config['DEFAULT']['mail_pass'])
recivers = config['DEFAULT']['receivers'].split(',')
back = sender.send(config['DEFAULT']['sender'], recivers, '/Users/zhangxiaobin/Downloads/蔡康永.epub', '蔡康永.epub')
print('蔡康永.epub' + back)
'''
文件名：蔡康永的说话之道（完整版）.epub
文件完整路径：/Users/zhangxiaobin/Downloads/doubanbooks250/蔡康永的说话之道（完整版）.epub
work_dir = '/Users/zhangxiaobin/Downloads/doubanbooks250/'
for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
    for filename in filenames:
        file_path = os.path.join(parent, filename)
        back = sender.send(config['DEFAULT']['sender'], recivers, file_path, filename)
        print(filename + back)
        time.sleep(10)


attach_file = '/Users/zhangxiaobin/Develop/github/toolbox/sendBooksToKindle/books/readMe.txt'
back = sender.send(config['DEFAULT']['sender'], recivers, attach_file, 'readMe.txt')
print("Start : %s" % time.ctime())
time.sleep(5)
print("End : %s" % time.ctime())
print(back)
'''
