import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.message import EmailMessage

def send_email(sender,receiver,subject,body):
    """
    sender #EMAIL_ADDRESS 发件邮箱
    receiver #EMAIL_ADDRESS 收件邮箱
    """
    print(subject)  
    print(body)
    import smtplib
    smtp=smtplib.SMTP('smtp.qq.com',25)



    context=ssl.create_default_context()

    msg=EmailMessage()
    msg['subject']=subject       #邮件主题
    msg['From']=sender
    msg['To']=receiver
    msg.set_content(body)         #邮件内容


    key = 'uujvnuykcakbbgef'      #换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
    EMAIL_ADDRESS = '493564113@qq.com'      #换成你的邮箱地址
    EMAIL_PASSWORD = key
    with smtplib.SMTP_SSL("smtp.qq.com",465,context=context) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)


def main():
    key = 'uujvnuykcakbbgef'      #换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
    SENDER_ADDRESS = '493564113@qq.com'      #换成你的邮箱地址
    RECEIVER_ADDRESS = 'leanceaner@qq.com'
    EMAIL_PASSWORD = key
    EMAIL_SUBJECT = 'test text'
    EMAIL_BODY = "hello world!\n2022/7/2"
    send_email(SENDER_ADDRESS,RECEIVER_ADDRESS,EMAIL_SUBJECT,EMAIL_BODY)


if __name__ == "__main__":
    main()