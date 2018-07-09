#-*- coding:utf-8 -*-

from kivy.lang import Builder
from kivy.uix.image import Image

Builder.load_file("kvdialog/item.kv")

class CItem(Image):
    def init_executeinfo(self, info):
        pass
        
    def on_item_execute(self):
        pass