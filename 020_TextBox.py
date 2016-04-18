#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Label, TextBox
from System.Drawing import Size, Point



class IForm(Form):

    def __init__(self):

        self.Text = 'TextBox'

        self.text = Label()
        self.text.Parent = self
        self.text.Text = "..."
        self.text.AutoSize = True
        self.text.Location = Point(60, 40)

        tbox = TextBox()
        tbox.Parent = self
        tbox.Location = Point(60, 100)
        tbox.KeyUp += self.OnKeyUp

        self.Size = Size(250, 200)
        self.CenterToScreen()
    

    def OnKeyUp(self, sender, event): 
        self.text.Text = sender.Text
    

Application.Run(IForm())