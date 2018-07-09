#-*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ListProperty

import item

Builder.load_file("kvdialog/enter.kv")

class CItemLayout(StackLayout):
    def __init__(self, **kwargs):
        super(CItemLayout, self).__init__(**kwargs)
        self.m_ItemList = []

        self.init_items()

    def init_items(self):
        for idx in xrange(21):
            oItem = item.CItem(name="item%d" % idx)
            self.add_widget(oItem)
            self.m_ItemList.append(oItem)

class CEnterMenu(Screen):
    def __init__(self, **kwargs):
        super(CEnterMenu, self).__init__(**kwargs)

    def on_add_item(self):
        print "on_add_item"
    
    def on_del_item(self):
        print "on_del_item"
    
    def on_move_item(self):
        print "on_move_item"
    
    def on_confirm_item(self):
        print "on_confirm_item"