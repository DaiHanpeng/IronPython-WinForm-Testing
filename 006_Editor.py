#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")


from System.Windows.Forms import Application, Form, MainMenu, StatusBar
from System.Windows.Forms import Shortcut, MenuItem, TextBox, DockStyle
from System.Drawing import Size, Point


class IForm(Form):

    def __init__(self):

        self.Text = 'Editor'
        self.Size = Size(210, 180)

        mainMenu = MainMenu()
        filem = mainMenu.MenuItems.Add('&File')
        filem.MenuItems.Add(MenuItem('E&xit',
                 self.OnExit, Shortcut.CtrlX))

        self.Menu = mainMenu

        tb = TextBox()
        tb.Parent = self
        tb.Dock = DockStyle.Fill
        tb.Multiline = True

        sb = StatusBar()
        sb.Parent = self
        sb.Text = 'Ready'

        self.CenterToScreen()
    

    def OnExit(self, sender, event): 
        self.Close()
    

Application.Run(IForm())