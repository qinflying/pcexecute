#-*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder
import define 

Builder.load_file("kvdialog/start.kv")

class CStartMenu(Screen):
    def on_enter_app(self):
        if self.manager.has_screen(define.ENTER_MENU):
            self.manager.current = define.ENTER_MENU 
        else:
            import entermenu
            oScreen = entermenu.CEnterMenu(name=define.ENTER_MENU)
            self.manager.switch_to(oScreen)

    def on_quit_app(self):
        exit(1)