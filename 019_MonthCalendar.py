#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Label, MonthCalendar
from System.Drawing import Size, Point


class IForm(Form):

    def __init__(self):
        self.Text = 'MonthCalendar'
        self.Size = Size(240, 240)
        
        calendar = MonthCalendar()
        calendar.Parent = self
        calendar.Location = Point(0, 0)
        calendar.DateSelected += self.OnSelected

        self.date = Label()
        self.date.Location = Point(0, 180)
        self.date.Parent = self
        dt = calendar.SelectionStart
        self.date.Text = str(dt.Month) + "/" + str(dt.Day) + "/" + str(dt.Year)
        
        self.CenterToScreen()
    

    def OnSelected(self, sender, event): 
        dt = sender.SelectionStart
        self.date.Text = str(dt.Month) + "/" + str(dt.Day) + "/" + str(dt.Year)
    

Application.Run(IForm())