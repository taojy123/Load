#Boa:Frame:Frame1
#coding=gbk

import wx
import wx.grid
import generictable
import winsound
import time

if time.time() > 1385782035:
    pass

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON10, wxID_FRAME1BUTTON11, 
 wxID_FRAME1BUTTON12, wxID_FRAME1BUTTON15, wxID_FRAME1BUTTON16, 
 wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, wxID_FRAME1BUTTON4, 
 wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, wxID_FRAME1BUTTON7, 
 wxID_FRAME1BUTTON8, wxID_FRAME1BUTTON9, wxID_FRAME1CHOICE2, 
 wxID_FRAME1CHOICE3, wxID_FRAME1GRID1, wxID_FRAME1GRID2, wxID_FRAME1GRID3, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, 
 wxID_FRAME1TEXTCTRL8, 
] = [wx.NewId() for _init_ctrls in range(30)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(813, 263), size=wx.Size(816, 638),
              style=wx.DEFAULT_FRAME_STYLE,
              title='\xc2\xb7\xb5\xa5\xb7\xd6\xce\xf6\xc6\xf7_v1.6')
        self.SetClientSize(wx.Size(800, 600))
        self.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.SetToolTipString('')

        self.grid1 = wx.grid.Grid(id=wxID_FRAME1GRID1, name='grid1',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(784, 152), style=0)
        self.grid1.SetDefaultCellFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Arial'))
        self.grid1.SetDefaultRowSize(18)
        self.grid1.SetDefaultColSize(18)
        self.grid1.SetRowLabelSize(18)
        self.grid1.SetColLabelSize(18)

        self.grid2 = wx.grid.Grid(id=wxID_FRAME1GRID2, name='grid2',
              parent=self, pos=wx.Point(8, 256), size=wx.Size(424, 139),
              style=0)
        self.grid2.SetDefaultCellFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Arial'))
        self.grid2.SetDefaultColSize(18)
        self.grid2.SetDefaultRowSize(18)
        self.grid2.SetRowLabelSize(18)
        self.grid2.SetColLabelSize(18)

        self.grid3 = wx.grid.Grid(id=wxID_FRAME1GRID3, name='grid3',
              parent=self, pos=wx.Point(8, 168), size=wx.Size(744, 80),
              style=0)
        self.grid3.SetDefaultCellFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Arial'))
        self.grid3.SetDefaultColSize(18)
        self.grid3.SetDefaultRowSize(18)
        self.grid3.SetRowLabelSize(18)
        self.grid3.SetColLabelSize(18)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='\xd7\xaf',
              name='button1', parent=self, pos=wx.Point(8, 544),
              size=wx.Size(72, 48), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='\xcf\xd0',
              name='button2', parent=self, pos=wx.Point(88, 544),
              size=wx.Size(75, 48), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(8, 408), size=wx.Size(152, 112),
              style=wx.TE_MULTILINE, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(168, 408), size=wx.Size(304, 128),
              style=wx.TE_MULTILINE, value='')

        self.choice2 = wx.Choice(choices=["1", "2", "3", "4", "5", "6", "7",
              "8", "9"], id=wxID_FRAME1CHOICE2, name='choice2', parent=self,
              pos=wx.Point(440, 288), size=wx.Size(32, 22), style=0)
        self.choice2.SetLabel('6')
        self.choice2.SetToolTipString('\xd1\xa1\xd4\xf1\xd7\xd4\xb6\xa8\xd2\xe5\xc2\xb7\xca\xfd')
        self.choice2.SetStringSelection('6')
        self.choice2.SetHelpText('')
        self.choice2.Bind(wx.EVT_CHOICE, self.OnChoice2Choice,
              id=wxID_FRAME1CHOICE2)

        self.choice3 = wx.Choice(choices=["1", "2", "3", "4", "5", "6", "7",
              "8", "9"], id=wxID_FRAME1CHOICE3, name='choice3', parent=self,
              pos=wx.Point(760, 200), size=wx.Size(32, 22), style=0)
        self.choice3.SetToolTipString('\xd1\xa1\xd4\xf1\xd7\xd4\xb6\xa8\xd2\xe5\xc2\xb7\xca\xfd')
        self.choice3.SetStringSelection('3')
        self.choice3.Bind(wx.EVT_CHOICE, self.OnChoice3Choice,
              id=wxID_FRAME1CHOICE3)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3,
              label='\xba\xf3\xcd\xcb', name='button3', parent=self,
              pos=wx.Point(168, 544), size=wx.Size(72, 48), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5,
              label='\xb5\xbc\xb3\xf6', name='button5', parent=self,
              pos=wx.Point(328, 544), size=wx.Size(72, 48), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6,
              label='\xb6\xc1\xc8\xeb', name='button6', parent=self,
              pos=wx.Point(408, 544), size=wx.Size(72, 48), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='0',
              name='staticText1', parent=self, pos=wx.Point(40, 528),
              size=wx.Size(7, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label='0',
              name='staticText2', parent=self, pos=wx.Point(120, 528),
              size=wx.Size(7, 14), style=0)

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8,
              label='\xd6\xd8\xd6\xc3', name='button8', parent=self,
              pos=wx.Point(248, 544), size=wx.Size(72, 48), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_FRAME1BUTTON8)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(720, 520), size=wx.Size(72, 23),
              style=0, value='0')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(624, 551), size=wx.Size(32, 24),
              style=0, value='100')

        self.button9 = wx.Button(id=wxID_FRAME1BUTTON9, label='-',
              name='button9', parent=self, pos=wx.Point(600, 551),
              size=wx.Size(24, 24), style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_FRAME1BUTTON9)

        self.button10 = wx.Button(id=wxID_FRAME1BUTTON10, label='+',
              name='button10', parent=self, pos=wx.Point(656, 551),
              size=wx.Size(24, 24), style=0)
        self.button10.Bind(wx.EVT_BUTTON, self.OnButton10Button,
              id=wxID_FRAME1BUTTON10)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4,
              label='\xcd\xea\xbd\xe1', name='button4', parent=self,
              pos=wx.Point(720, 544), size=wx.Size(72, 48), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7,
              label='\xbf\xaa\xca\xbc', name='button7', parent=self,
              pos=wx.Point(488, 544), size=wx.Size(72, 48), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_FRAME1BUTTON7)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(480, 256), size=wx.Size(312, 232),
              style=wx.TE_MULTILINE, value='')

        self.button11 = wx.Button(id=wxID_FRAME1BUTTON11, label='-',
              name='button11', parent=self, pos=wx.Point(600, 526),
              size=wx.Size(24, 24), style=0)
        self.button11.Bind(wx.EVT_BUTTON, self.OnButton11Button,
              id=wxID_FRAME1BUTTON11)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(624, 526), size=wx.Size(32, 24),
              style=0, value='100')

        self.button12 = wx.Button(id=wxID_FRAME1BUTTON12, label='+',
              name='button12', parent=self, pos=wx.Point(656, 526),
              size=wx.Size(24, 24), style=0)
        self.button12.Bind(wx.EVT_BUTTON, self.OnButton12Button,
              id=wxID_FRAME1BUTTON12)

        self.button15 = wx.Button(id=wxID_FRAME1BUTTON15, label='-',
              name='button15', parent=self, pos=wx.Point(600, 575),
              size=wx.Size(24, 24), style=0)
        self.button15.Bind(wx.EVT_BUTTON, self.OnButton15Button,
              id=wxID_FRAME1BUTTON15)

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(624, 575), size=wx.Size(32, 24),
              style=0, value='100')

        self.button16 = wx.Button(id=wxID_FRAME1BUTTON16, label='+',
              name='button16', parent=self, pos=wx.Point(656, 575),
              size=wx.Size(24, 24), style=0)
        self.button16.Bind(wx.EVT_BUTTON, self.OnButton16Button,
              id=wxID_FRAME1BUTTON16)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(480, 496), size=wx.Size(312, 22),
              style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.data = ""
        self.data1 = ""
        self.data2 = ""
        self.data3 = ""
        self.match_name = ""
        self.scores = []
        open("remind.txt","a")
        if not open("remind.txt","r").read().replace(" ","").replace("\n",""):
            open("remind.txt","w").write("BBBBBP,BBPBPB,BPBBPP,BPPPBB,PBBPBP,PBPPPB,PPBPPP,PPPBBB")
            
        open("match.txt", "a")
        if not open("match.txt","r").read().replace(" ","").replace("\n",""):
            open("match.txt","w").write("[]")
            
        self.show_match()


        g1 = self.add_blank([[""]], 7, 40)
        tableBase = generictable.GenericTable(g1,[""]*7,[""]*40) 
        self.grid1.SetTable(tableBase)
        g2 = self.add_blank([[""]], 6, 22)
        tableBase = generictable.GenericTable(g2,[""]*6,[""]*22) 
        self.grid2.SetTable(tableBase)
        g3 = self.add_blank([[""]], 3, 40)
        tableBase = generictable.GenericTable(g3,[""]*3,[""]*40) 
        self.grid3.SetTable(tableBase)
        
        
        """
        data = [[1,1,2,3,2,4,2,2,3,4,4,5,4,5,5,6,6,7,5,4,4,2,5,6,0,1,0,1],
        [1,1,2,3,2,4,2,2,3,4,4,5,4,5,5,6,6,7,5,4,4,2,5,6,0,1,0,1],
        [1,1,2,3,2,4,2,2,3,4,4,5,4,5,5,6,6,7,5,4,4,2,5,6,0,1,0,1],
        [1,1,2,3,2,4,2,2,3,4,4,5,4,5,5,6,6,7,5,4,4,2,5,6,0,1,0,1],
        [1,1,2,3,2,4,2,2,3,4,4,5,4,5,5,6,6,7,5,4,4,2,5,6,0,1,0,1]]
        rownums = range(len(data))
        colnums = range(len(data[0]))
        tableBase = generictable.GenericTable(data, rownums, colnums) 
        self.grid1.SetTable(tableBase)   
        self.grid1.SetCellTextColour(1, 1, "red")         
        self.grid1.SetCellBackgroundColour(0, 1, "red") 
        print self.grid1.GetCellValue(0, 0)
        """
        

    def OnButton1Button(self, event):
        self.data += "B"
        self.data1 += "B"
        self.data2 += "B"
        self.data3 += "B"
        self.update_bp()
        event.Skip()

    def OnButton2Button(self, event):
        self.data += "P"
        self.data1 += "P"
        self.data2 += "P"
        self.data3 += "P"
        self.update_bp()
        event.Skip()

    def OnButton3Button(self, event):
        # back
        self.data = self.data[:-1]
        self.data1 = self.data1[:-1]
        self.data2 = self.data2[:-1]
        self.data3 = self.data3[:-1]
        if self.data1[-1] == "-":
            self.data1  = self.data1 [:-3] + self.data[-3:]
        if self.data2[-1] == "=" and len(self.data2) % 6 != 0:
            self.data2  = self.data2 [:-5] + self.data[-5:]
        if self.data3[-1] == "+":
            self.data3  = self.data3 [:-4] + self.data[-4:]
        
        self.update_bp()
        event.Skip()
        
        
    def update_bp(self):
        if self.data:
            
            # bp text
            self.textCtrl2.SetValue(self.data)
            B_num = self.data.count("B")
            self.staticText1.SetLabel(str(B_num))
            P_num = self.data.count("P")
            self.staticText2.SetLabel(str(P_num))
            
            # grid1
            g1 = []
            t = ""
            for d in self.data:
                if t != d:
                    g1.append([])
                    t = d
                g1[-1].append(d)
                
            l = 0
            for line in g1:
                if len(line) > l:
                    l = len(line)
                
            for i in range(len(g1)):
                t = l - len(g1[i])
                g1[i] += [""] * t
                
            g1 = map(list, zip(*g1))
            g1 = self.add_blank(g1, 7, 40)
            rownums = range(1, len(g1)+1)
            colnums = range(1, len(g1[0])+1)
            tableBase = generictable.GenericTable(g1, rownums, colnums)
            self.grid1.SetTable(tableBase)
            self.grid1.SetColLabelSize(19)
            self.grid1.SetColLabelSize(18)
            self.add_color(g1, self.grid1)
            
            # grid2
            g2 = []
            load_num = int(self.choice2.GetLabel())
            for i in range(0, len(self.data), load_num):
                g2.append([])
                for j in range(load_num):
                    if len(self.data) > i+j:
                        g2[-1].append(self.data[i+j])
            t = load_num - len(g2[-1])
            g2[-1] += [""] * t
                
            g2 = map(list, zip(*g2))
            g2 = self.add_blank(g2, 6, 22)
            rownums = range(1, len(g2)+1)
            colnums = range(1, len(g2[0])+1)
            tableBase = generictable.GenericTable(g2, rownums, colnums) 
            self.grid2.SetTable(tableBase)
            self.grid2.SetColLabelSize(19)
            self.grid2.SetColLabelSize(18)
            self.add_color(g2, self.grid2)
            
            
            # grid3
            g3 = []
            load_num = int(self.choice3.GetLabel())
            for i in range(0, len(self.data), load_num):
                g3.append([])
                for j in range(load_num):
                    if len(self.data) > i+j:
                        g3[-1].append(self.data[i+j])
            t = load_num - len(g3[-1])
            g3[-1] += [""] * t
                
            g3 = map(list, zip(*g3))
            g3 = self.add_blank(g3, 3, 40)
            rownums = range(1, len(g3)+1)
            colnums = range(1, len(g3[0])+1)
            tableBase = generictable.GenericTable(g3, rownums, colnums) 
            self.grid3.SetTable(tableBase)
            self.grid3.SetColLabelSize(19)
            self.grid3.SetColLabelSize(18)
            self.add_color(g3, self.grid3)
            
            # check remind
            reminds = open("remind.txt","r").read().replace(" ","").replace("\n","")
            reminds = reminds.split(",")
            for r in reminds:
                if len(r) != 6:
                    continue
                
                if r == self.data[-6:] and len(self.data) % 6 == 0:
                    text = self.textCtrl1.GetValue()
                    text = r + ", Game Over!\n" + text
                    self.textCtrl1.SetValue(text)
                    #self.data1 = self.data1[:-6] + "======"
                    self.data2 = self.data2[:-6] + "======"
                    #self.data3 = self.data3[:-6] + "======"
                    self.add_background()
                    #wx.MessageBox("Game Over!")
                    #winsound.MessageBeep(30)
                    winsound.PlaySound("c.wav", 1)
                elif r == self.data[-6:] and len(self.data) % 6 == 3:
                    text = self.textCtrl1.GetValue()
                    text = r + ", Game Over!\n" + text
                    self.textCtrl1.SetValue(text)
                    #self.data1 = self.data1[:-6] + "======"
                    self.data2 = self.data2[:-6] + "======"
                    #self.data3 = self.data3[:-6] + "======"
                    self.add_background()
                    #wx.MessageBox("Game Over!")
                    #winsound.MessageBeep(30)
                    winsound.PlaySound("c.wav", 1)
                    
                elif r[:5] == self.data[-5:] and len(self.data) % 6 == 5:
                    text = self.textCtrl1.GetValue()
                    text = r + ", Danger.\n" + text
                    self.textCtrl1.SetValue(text)
                    #self.data1 = self.data1[:-5] + "+++++"
                    #self.data2 = self.data2[:-5] + "+++++"
                    self.data3 = self.data3[:-5] + "+++++"
                    self.add_background()
                    #wx.MessageBox("Danger")
                    #winsound.MessageBeep(15)
                    winsound.PlaySound("b.wav", 1)
                elif r[:5] == self.data[-5:] and len(self.data) % 6 == 2:
                    text = self.textCtrl1.GetValue()
                    text = r + ", Danger.\n" + text
                    self.textCtrl1.SetValue(text)
                    #self.data1 = self.data1[:-5] + "+++++"
                    #self.data2 = self.data2[:-5] + "+++++"
                    self.data3 = self.data3[:-5] + "+++++"
                    self.add_background()
                    #wx.MessageBox("Danger")
                    winsound.MessageBeep(15)
                    winsound.PlaySound("b.wav", 1)
                        
                elif r[:4] == self.data[-4:] and len(self.data) % 6 == 4:
                    winsound.MessageBeep(64)
                    text = self.textCtrl1.GetValue()
                    text = r + ", Careful.\n" + text
                    self.textCtrl1.SetValue(text)
                    self.data1 = self.data1[:-4] + "----"
                    #self.data2 = self.data2[:-4] + "----"
                    #self.data3 = self.data3[:-4] + "----"
                    self.add_background()
                    #winsound.MessageBeep(64)
                    winsound.PlaySound("a.wav", 1)
                elif r[:4] == self.data[-4:] and len(self.data) % 6 == 1:
                    text = self.textCtrl1.GetValue()
                    text = r + ", Careful.\n" + text
                    self.textCtrl1.SetValue(text)
                    self.data1 = self.data1[:-4] + "----"
                    #self.data2 = self.data2[:-4] + "----"
                    #self.data3 = self.data3[:-4] + "----"
                    self.add_background()
                    #winsound.MessageBeep(64)
                    winsound.PlaySound("a.wav", 1)
                    
                    
            self.add_background()
                    
        else:
            self.data = ""
            self.data1 = ""
            self.data2 = ""
            self.data3 = ""
            data = [[""]]
            self.textCtrl1.SetValue("")
            self.textCtrl2.SetValue("")
            tableBase = generictable.GenericTable(data) 
            self.grid1.SetTable(tableBase)   
            self.grid2.SetTable(tableBase)   
            self.grid3.SetTable(tableBase)   
                
               
    def add_background(self):
        
        # add grid1 add_background
        r_num = self.grid1.GetNumberRows()
        c_num = self.grid1.GetNumberCols()
        l = len(self.data2)
        n = 0
        for j in range(c_num):
            for i in range(r_num):
                if self.grid1.GetCellValue(i, j) in ["B", "P"]:
                    if len(self.data1) > n:
                        if self.data1[-1] not in ["+", "="] and self.data1[n] not in ["-"]:
                            self.data1 = self.data1[:n] + self.data[n] + self.data1[n+1:]
                        if self.data1[n] == "-":
                            self.grid1.SetCellBackgroundColour(i, j, "yellow")
                        elif self.data1[n] == "+":
                            self.grid1.SetCellBackgroundColour(i, j, "green")
                        elif self.data1[n] == "=":
                            self.grid1.SetCellBackgroundColour(i, j, "black")
                    n += 1
            
        # add grid2 add_background
        r_num = int(self.choice2.GetLabel())
        c_num = int((len(self.data2)-0.00001) / r_num) + 1
        n = 0
        for j in range(c_num):
            for i in range(r_num):
                if len(self.data2) > n:
                    if self.data2[-1] not in ["+", "-"] and self.data2[n] not in ["="]:
                        self.data2 = self.data2[:n] + self.data[n] + self.data2[n+1:]
                    if self.data2[n] == "-":
                        self.grid2.SetCellBackgroundColour(i, j, "yellow")
                    elif self.data2[n] == "+":
                        self.grid2.SetCellBackgroundColour(i, j, "green")
                    elif self.data2[n] == "=":
                        self.grid2.SetCellBackgroundColour(i, j, "black")
                n += 1
                
        # add grid3 add_background
        r_num = int(self.choice3.GetLabel())
        c_num = int((len(self.data3)-0.00001) / r_num) + 1
        n = 0
        
        for j in range(c_num):
            for i in range(r_num):
                if len(self.data3) > n:
                    # data3 handle
                    if self.data3[-1] not in ["-", "="] and self.data3[n] not in ["+"]:
                        self.data3 = self.data3[:n] + self.data[n] + self.data3[n+1:]
                        
                    if self.data3[n] == "-":
                        self.grid3.SetCellBackgroundColour(i, j, "yellow")
                    elif self.data3[n] == "+":
                        self.grid3.SetCellBackgroundColour(i, j, "green")
                    elif self.data3[n] == "=":
                        self.grid3.SetCellBackgroundColour(i, j, "black")
                n += 1
                
            
    def add_blank(self, g, max_r, max_c):
    
        r = max_r - len(g)
        c = max_c - len(g[0])
        for i in range(len(g)):
            g[i] += [""] * c
        g += [[""]*len(g[0]) ] * r

        return g
        
    
                    
    def add_color(self, data, grid):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "B":
                    grid.SetCellTextColour(i, j, "red")
                elif data[i][j] == "P":
                    grid.SetCellTextColour(i, j, "blue")

    def OnButton8Button(self, event):
        # reset
        
        self.data = ""
        self.data2 = ""
        self.data3 = ""
        self.update_bp()
        
        event.Skip()

    def OnButton5Button(self, event):
        # output
        
        dlg = wx.FileDialog(self, style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            dir = dlg.GetDirectory()
            filename = dlg.GetFilename()
            if "." not in filename:
                filename += ".txt"
            filename = dir + "\\" + filename
            open(filename, "w").write(self.data)
            wx.MessageBox("OK")
        
        dlg.Destroy()
        
        event.Skip()

    def OnButton6Button(self, event):
        # readin
        
        dlg = wx.FileDialog(self, style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dir = dlg.GetDirectory()
            filename = dlg.GetFilename()
            in_str = open(dir + "\\" + filename).read()
            self.OnButton8Button(event)
            for t in in_str:
                if t == "B" or t == "b":
                    self.OnButton1Button(event)
                elif t == "P" or t == "p":
                    self.OnButton2Button(event)
        dlg.Destroy()
               
        event.Skip()


    def OnButton4Button(self, event):
        # finish
        if self.scores:
                
            match = eval(open("match.txt").read())
            match.append([self.match_name, self.scores])
            open("match.txt", "w").write(str(match))
            self.textCtrl3.SetValue("0")
            self.textCtrl7.SetValue("")
            self.match_name = ""
            self.scores = []
            wx.MessageBox("Saved")
            
            self.show_match()
            
        event.Skip()
        
    def show_match(self):
        
        match = eval(open("match.txt","r").read())
        
        self.textCtrl5.SetValue("")
        
        for m in match:
            out_str = m[0] + ":\n"
            out_str += u"累计注码: %s \n" % str(m[1])[1:-1]
            out_str += u"累计结果: %d  总计: %d \n\n" % (sum(m[1]), len(m[1]))
            now_str = self.textCtrl5.GetValue()
            self.textCtrl5.SetValue(out_str + now_str)
            
            

    def OnChoice2Choice(self, event):
        self.update_bp()
        event.Skip()

    def OnChoice3Choice(self, event):
        self.update_bp()
        event.Skip()

    def OnButton7Button(self, event):
        # start
        if not self.match_name and not self.scores:
            self.OnButton4Button(event)
        self.match_name = wx.GetTextFromUser("Enter the name:")
        self.scores = []
        event.Skip()


    # + - score
    
    def OnButton9Button(self, event):
        # score - 
        num = int(self.textCtrl4.GetValue())
        self.scores.append(-num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()

    def OnButton10Button(self, event):
        # score + 
        num = int(self.textCtrl4.GetValue())
        self.scores.append(num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()
        
    def OnButton11Button(self, event):
        num = int(self.textCtrl6.GetValue())
        self.scores.append(-num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()

    def OnButton12Button(self, event):
        num = int(self.textCtrl6.GetValue())
        self.scores.append(num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()
        
    def OnButton15Button(self, event):
        num = int(self.textCtrl8.GetValue())
        self.scores.append(-num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()

    def OnButton16Button(self, event):
        num = int(self.textCtrl8.GetValue())
        self.scores.append(num)
        self.textCtrl3.SetValue(str(sum(self.scores)))
        self.textCtrl7.SetValue(u"%s   总计:%d" %(str(self.scores), len(self.scores)) )
        event.Skip()

                    
        
        
        
