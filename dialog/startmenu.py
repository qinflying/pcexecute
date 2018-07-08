#-*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder

Builder.load_file("kvdialog/start.kv")

class CStartMenu(Screen):
    def on_enter_app(self):
        pass

    def on_quit_app(self):
        exit(1)