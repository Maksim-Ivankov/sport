
import flet as ft
from assets.variable import *
from assets.imports import *


class Main_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('лоло11',text_align='center',color='black'),
                            ft.Text('лоло',color='black'),
                            ft.Text('лоло',color='black'),
                            ft.Text('лоло',color='black'),
                            ft.Text('лоло',color='black'),
                            ft.Text('лоло',color='black'),
                            ft.Row(controls=[
                                ft.Text('лоло',color='black'),
                                ft.Text('лоло',color='black'),
                                ft.Text('лоло',color='black'),
                                ft.Text('лоло',color='black'),
                            ])
                        ]),padding=ft.padding.only(left=30),bgcolor='red'
                    )
                ]
            ),expand=2
        )
        
        return self.main_page