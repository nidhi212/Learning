import pywhatkit as WA
import getpass as GP
print("welcome to learning")
num=GP.getpass(prompt='phoneno:',stream=None)
msg="I love you and i woke up at 4 am today"
WA.sendwhatmsg(num,msg,4,58)