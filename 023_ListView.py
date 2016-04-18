#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import ListView, View, ColumnHeader
from System.Windows.Forms import ListViewItem, DockStyle, SortOrder
from System.Drawing import Size


class IForm(Form):

    def __init__(self):
        self.Text = 'ListBox'
       

        actresses = { 'Jessica Alba' : '1981', 'Angelina Jolie' : '1975', 
            'Natalie Portman' : '1981', 'Rachel Weiss' : '1971', 
            'Scarlett Johansson' : 1984 }


        name = ColumnHeader()
        name.Text = 'Name'
        name.Width = -1
        year = ColumnHeader()
        year.Text = 'Year'

        self.SuspendLayout()

        lv = ListView()
        lv.Parent = self
        lv.FullRowSelect = True
        lv.GridLines = True
        lv.AllowColumnReorder = True
        lv.Sorting = SortOrder.Ascending
        lv.Columns.AddRange((name, year))
        lv.ColumnClick += self.OnColumnClick

        for act in actresses.keys():
            item = ListViewItem()
            item.Text = act
            item.SubItems.Add(str(actresses[act]))
            lv.Items.Add(item)
        

        lv.Dock = DockStyle.Fill
        lv.Click += self.OnChanged

        self.sb = StatusBar()
        self.sb.Parent = self
        lv.View = View.Details

        self.ResumeLayout()

        self.Size = Size(350, 300)
        self.CenterToScreen()
    

    def OnChanged(self, sender, event):

        name = sender.SelectedItems[0].SubItems[0].Text
        born = sender.SelectedItems[0].SubItems[1].Text
        self.sb.Text = name + ', ' + born
    

    def OnColumnClick(self, sender, event):

        if sender.Sorting == SortOrder.Ascending:
            sender.Sorting = SortOrder.Descending
        else: 
            sender.Sorting = SortOrder.Ascending


Application.Run(IForm())