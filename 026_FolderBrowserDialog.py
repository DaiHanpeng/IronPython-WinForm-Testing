#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import ToolBar, ToolBarButton, FolderBrowserDialog
from System.Windows.Forms import DialogResult


class IForm(Form):

    def __init__(self):
        self.Text = "FolderBrowserDialog"
 
        toolbar = ToolBar()
        toolbar.Parent = self
        openb = ToolBarButton()

        self.statusbar = StatusBar()
        self.statusbar.Parent = self

        toolbar.Buttons.Add(openb)
        toolbar.ButtonClick += self.OnClicked

        self.CenterToScreen()


    def OnClicked(self, sender, event):
        dialog = FolderBrowserDialog()

        if (dialog.ShowDialog(self) == DialogResult.OK):
            self.statusbar.Text = dialog.SelectedPath
       

Application.Run(IForm())