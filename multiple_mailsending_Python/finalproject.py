import wx
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

sendermail="xuetianhc@gmail.com"
senderpass="2226223326sparkbrain"

def testfun():
    print("this is from testfun")

all_receiver=[]


def finishallwork(content):
    messageobj = MIMEMultipart()

    messagecontent = content;
    messageobj['Subject'] = "One important notic for all"

    messageobj.attach(MIMEText(messagecontent, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(sendermail, senderpass)
    for i in range(len(all_receiver)):
        receiver=all_receiver[i]
        server.sendmail(sendermail, receiver, messageobj.as_string())
    server.quit()
    return "ok"





def countt():
    return str(len(all_receiver))

class multipl_mail_sender(wx.Frame):


    def __init__(self,parentvar,id, title):
        wx.Frame.__init__(self,parentvar,id,title,size=(1200,600))
        self.panell=wx.Panel(self)
        self.btn=wx.Button(self.panell, 5, "Add New Gamil",pos=(30,30))
        self.Bind(wx.EVT_BUTTON, self.Take_input, self.btn)

        self.btn2=wx.Button(self.panell, 4, 'Check All List', pos=(30,100))
        self.Bind(wx.EVT_BUTTON, self.cheklisttt, self.btn2)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(self.panell, -1, "Multiline Text",pos=(70,200))
        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.TextCtrl(self.panell, size=(500, 100), style=wx.TE_MULTILINE, pos=(70,220))

        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)
        self.btn3 = wx.Button(self.panell, 2, 'Now Send this to all user', pos=(190, 360))
        self.btn3.BackgroundColour="blue"
        self.Bind(wx.EVT_BUTTON, self.OnEnterPressed, self.btn3)



    def OnEnterPressed(self, e):
        con=self.t3.GetValue()
        msg=finishallwork(con)
        if(msg=="ok"):
            static = wx.StaticText(self, label="sending is complete, thank you", pos=(450, 500))
            static.ForegroundColour="green"

    def Take_input(self, e):
        dilog=wx.TextEntryDialog(self.panell, "Adde a Gamil", "Gamil adder","", style=wx.OK)
        dilog.ShowModal()
        rcvmail=dilog.GetValue()

        all_receiver.append(rcvmail)
        static = wx.StaticText(self, label="Already = " + countt(), pos=(150, 35))
        static.ForegroundColour = "white"
        dilog.Destroy()

    def cheklisttt(self, e):
        allmail = wx.ListBox(self,-1, (300, 50), (250, 120), all_receiver, wx.LB_SINGLE)






if __name__=="__main__":
    app=wx.App()
    frame=multipl_mail_sender(parentvar=None, id=-1, title="Multiple mail sending")
    frame.Center()
    frame.BackgroundColour="#393C3E"
    frame.Show()
    app.MainLoop()