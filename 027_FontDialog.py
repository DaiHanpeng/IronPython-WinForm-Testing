#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar, Label
from System.Windows.Forms import ToolBar, ToolBarButton, FontDialog
from System.Windows.Forms import DialogResult

class IForm(Form):

    def __init__(self):
        self.Text = "FolderBrowserDialog"
 
        self.text = Label()
        self.text.Parent = self
        self.text.Text = "Winforms tutorial"

        self.LocateText()
 
        toolbar = ToolBar()
        toolbar.Parent = self
        openb = ToolBarButton()

        toolbar.Buttons.Add(openb)
        toolbar.ButtonClick += self.OnClicked

        self.text.AutoSize = True
        self.Resize += self.OnResize
 
        self.CenterToScreen()   

    def OnResize(self, sender, event):
        self.LocateText()


    def LocateText(self): 
        self.text.Top = (self.ClientSize.Height - self.text.Height) / 2
        self.text.Left = (self.ClientSize.Width - self.text.Width) / 2
    

    def OnClicked(self, sender, event):

        dialog = FontDialog()

        if (dialog.ShowDialog(self) == DialogResult.OK):
           self.text.Font = dialog.Font
           self.LocateText()
       

Application.Run(IForm())