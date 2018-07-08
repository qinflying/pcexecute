#-*- coding:utf-8 -*-
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager

class CScreenManager(ScreenManager):
    pass

class CPCExecuteApp(App):
    def build(self):
        mgr = CScreenManager()
        
        from dialog import startmenu
        oStartMenu = startmenu.CStartMenu(name="startmenu")
        mgr.switch_to(oStartMenu)

        return mgr


if __name__ == "__main__":
    CPCExecuteApp().run()