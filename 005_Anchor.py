#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Button, AnchorStyles
from System.Drawing import Size, Point


class IForm(Form):

    def __init__(self):
        self.Text = 'Anchor'        
        self.Size = Size(210, 210)
              
        btn1 = Button()
        btn1.Text = "Button"
        btn1.Parent = self
        btn1.Location = Point(30, 30)

        btn2 = Button()
        btn2.Text = "Button"
        btn2.Parent = self
        btn2.Location = Point(30, 80)
        btn2.Anchor = AnchorStyles.Right
        
        self.CenterToScreen()
    

Application.Run(IForm())