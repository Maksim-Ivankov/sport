
import flet as ft
from assets.variable import *
from assets.imports import *


class ModernNavBar(ft.UserControl):

    def __init__(self,callback,punkt_menu_one):
        super().__init__()
        self.callback = callback
        self.punkt_menu_one = punkt_menu_one
        self.change_punkt_menu = self.punkt_menu_one

    # выбор пункта меню
    def change_menu(self,e):
        self.change_punkt_menu = e.control.data
        self.callback(e.control.data)

    # элемент меню
    def element_menu(self,punkt,color_text):
        if color_text == c_yelow:
            return ft.Container(
                data = punkt,
                border=ft.border.all(1,c_white),
                # on_hover=lambda e: self.HighLight(e),
                on_click=lambda e: self.change_menu(e),
                width=100,
                padding=ft.padding.only(top=20,bottom=20),
                height=60,
                border_radius=0,
                margin=ft.margin.only(bottom=-10),
                content=ft.Container(ft.Text(value=punkt,color=color_text,size=12,opacity=1,text_align='center'))
                )
        return ft.Container(
            data = punkt,
            # on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.change_menu(e),
            width=100,
            padding=ft.padding.only(top=20,bottom=20),
            height=60,
            border_radius=0,
            margin=ft.margin.only(bottom=-10),
            content=ft.Container(ft.Text(value=punkt,color=color_text,size=12,opacity=1,text_align='center'))
            )

 

    def build(self):

        punkts_menu = [
            'Работа',
            'Таймер',
            'Семья',
        ]
        self.items = []
        for punkt in punkts_menu:
            if punkt != self.change_punkt_menu:
                self.items.append(self.element_menu(punkt,c_white))
            else:
                self.items.append(self.element_menu(punkt,c_yelow))
              
        modern_nav_bar =  ft.Container(  
            width=width_window_platforma,
            height=60,
            expand=True,
            # padding=ft.padding.only(top=20),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    # ft.Text('111')
                    # ft.Container(ft.Image(src=f"src/img/logo_2.png",width=140,height=28,),margin = ft.margin.only(bottom=10)),
                    # ft.Container(ft.Image(src=f"src/img/icons/resize.png"),width=24,height=24,on_click=partial(self.func)),
                    ft.Row(self.items),
                    # self.date_time()
                ],
                horizontal_alignment='center',
                expand=True,
            )
        )

        return modern_nav_bar