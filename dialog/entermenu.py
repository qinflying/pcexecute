#-*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

Builder.load_file("kvdialog/enter.kv")

class CItemLayout(StackLayout):
    pass

class CEnterMenu(Screen):
    pass

    def on_add_item(self):
        print "on_add_item"
    
    def on_del_item(self):
        print "on_del_item"
    
    def on_move_item(self):
        print "on_move_item"
    
    def on_confirm_item(self):
        print "on_confirm_item"