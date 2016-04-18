#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import Shortcut, MainMenu, MenuItem
from System.Drawing import Size



class IForm(Form):

    def __init__(self):
        self.Text = 'Simple Menu'
        
        self.sb = StatusBar()
        self.sb.Parent = self
        self.sb.Text = "Ready"

        mainMenu = MainMenu()

        filem = mainMenu.MenuItems.Add("&File")    
        filem.MenuItems.Add(MenuItem("E&xit", 
                 self.OnExit, Shortcut.CtrlX))

        view = mainMenu.MenuItems.Add("&View")
        self.viewStatusBar = MenuItem("View StatusBar")
        self.viewStatusBar.Checked = True
        self.viewStatusBar.Click += self.ToggleStatusBar
        view.MenuItems.Add(self.viewStatusBar)

        self.Menu = mainMenu
        self.Size = Size(250, 200)

        self.CenterToScreen()
    
    def OnExit(self, sender, event):
        self.Close()


    def ToggleStatusBar(self, sender, event):
        check = self.viewStatusBar.Checked

        if (check):
            self.sb.Visible = False
            self.viewStatusBar.Checked = False
        else:
            self.sb.Visible = True
            self.viewStatusBar.Checked = True
        
    
Application.Run(IForm())