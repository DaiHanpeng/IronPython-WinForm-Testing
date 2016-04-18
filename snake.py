#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import Application, Form, FormBorderStyle
from board import Board


class IForm(Form):

    def __init__(self):
        self.Text = 'Snake'
       
        self.FormBorderStyle = FormBorderStyle.FixedSingle
        
        borderWidth = (self.Width - self.ClientSize.Width) / 2
        titleBarHeight = self.Height - self.ClientSize.Height - borderWidth
        
        board = Board()
        board.BORDER_WIDTH = borderWidth
        board.TITLEBAR_HEIGHT = titleBarHeight

        self.Controls.Add(board)
        self.CenterToScreen()

Application.Run(IForm())