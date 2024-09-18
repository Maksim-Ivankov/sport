


import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.menu.UI.modernNavBar import ModernNavBar

class Menu(ft.UserControl):

    def __init__(self,page,callback,punkt_menu_one):
        super().__init__()
        self.callback = callback
        self.page = page
        self.punkt_menu_one = punkt_menu_one

    def build(self):
                

        
        # Контейнер меню
        self.menu = ft.Container(
                content=ModernNavBar(self.callback,self.punkt_menu_one),
                width=width_window_platforma,
                # expand = 1,
                # expand=True,
                # height=height_window_platforma-39,
                bgcolor=c_blue,
                border_radius=0,
                # border = ft.border.all(1, c_white),
                alignment=ft.alignment.center,
                # animate=ft.animation.Animation(500,'decelerate'),
                # margin = ft.margin.only(left=-10,top=-10),
                # on_hover=open_menu
                

            
        )
        
        return self.menu