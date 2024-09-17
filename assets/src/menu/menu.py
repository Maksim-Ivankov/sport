


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
                
        
        # def open_menu(e):
        #     self.time_event_hover = time.time()
        #     # print(self.time_event_hover - self.time_event_click)
        #     if (self.time_event_hover - self.time_event_click)>0.5:
        #         # print(self.time_event_hover)
        #         self.controls[0].width = 200
        #         self.controls[0].update()
        #         self.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].opacity = 1
        #         # self.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].content.opacity = 1
        #         # self.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].content.update()
        #         self.controls[0].content.controls[0].content.controls[0].content.src = 'src/img/logo_2.png'
        #         self.controls[0].content.controls[0].content.controls[0].update()
        #         for items in self.controls[0].content.controls[0].content.controls[2].controls:
        #             if isinstance(items,ft.Container):
        #                 items.content.controls[1].opacity = 1
        #                 items.content.update()
        
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