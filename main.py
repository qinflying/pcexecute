#-*- coding:utf-8 -*-
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager
import define 
import init 

class CScreenManager(ScreenManager):
    pass

class CPCExecuteApp(App):
    def build(self):
        mgr = CScreenManager()
        
        from dialog import startmenu
        oStartMenu = startmenu.CStartMenu(name=define.STAR_MENU)
        mgr.add_widget(oStartMenu)
        return mgr


if __name__ == "__main__":
    init.AllInit()
    
    CPCExecuteApp().run()