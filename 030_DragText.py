#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")


from System.Windows.Forms import Application, Form, Button
from System.Windows.Forms import TextBox, DragDropEffects, DataFormats
from System.Drawing import Size, Point

class IForm(Form):

    def __init__(self):
        self.Text = 'Drag & Drop'
        self.AllowDrop = True

        button = Button()
        button.Parent = self
        textBox = TextBox()
        textBox.Parent = self
 
        button.AllowDrop = True
        button.Location = Point(150, 50)
        button.DragDrop += self.OnDragDrop
        button.DragEnter += self.OnDragEnter

        textBox.Location = Point(15, 50)
        textBox.MouseDown += self.OnMousDown

        self.ClientSize = Size(250, 200)
        self.CenterToScreen()


    def OnMousDown(self, sender, event):
        sender.SelectAll()
        sender.DoDragDrop(sender.Text, DragDropEffects.Copy)
    

    def OnDragEnter(self, sender, event):
        if event.Data.GetDataPresent(DataFormats.Text):
            event.Effect = DragDropEffects.Copy
      

    def OnDragDrop(self, sender, event):
        sender.Text =  event.Data.GetData(DataFormats.Text)
    

Application.Run(IForm())