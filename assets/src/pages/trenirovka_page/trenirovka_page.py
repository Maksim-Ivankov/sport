
import flet as ft
from assets.variable import *
from assets.imports import *


class Trenirovka_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Тренировка',text_align='center',color=c_white),
                            
                        ]),padding=10,height=690
                    )
                ]
            ),expand=2
        )
        
        return self.main_page