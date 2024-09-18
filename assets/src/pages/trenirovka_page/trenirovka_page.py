
import flet as ft
from assets.variable import *
from assets.imports import *


class Trenirovka_page(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        
    def change_menu(self,e):
        self.change_punkt_menu = e.control.data
        self.callback(e.control.data)

    def build(self):
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Тринировки | Техники | Инструкции',text_align='center',color=c_white,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=40),bgcolor=c_white),
                            ft.Container(
                                ft.Text('Первые 2 месяца',color=c_blue,text_align='center',size=16),
                                data='Первые 2 месяца',
                                width=200,
                                height=60,
                                bgcolor=c_yelow,
                                padding=ft.padding.only(top=20),
                                margin = ft.margin.only(left=50),
                                on_click=self.change_menu
                            )
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page