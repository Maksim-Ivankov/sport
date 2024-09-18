
import flet as ft
from assets.variable import *
from assets.imports import *


class Visit_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        row_mas = []
        col_mas = []
        for i in range(10):
            row_mas.append(ft.Container(width=24,height=24,border=ft.border.all(1,c_white),margin=-2))
        for i in range(10):
            col_mas.append(ft.Row(controls=row_mas))
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Посещение тренировок',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            ft.Text('Старт - 16.09.2024 г',text_align='center',color=c_white,width=390),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Прошло',text_align='center',color=c_white),
                                ft.Text(' 3 дня',text_align='center',color=c_yelow),
                            ]),width=390,padding=ft.padding.only(left=100)),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Посещено',text_align='center',color=c_white),
                                ft.Text(' 2 тренировки',text_align='center',color=c_yelow),
                            ]),width=390,padding=ft.padding.only(left=60),margin=ft.margin.only(bottom=20)),
                            ft.Container(ft.Column(controls=col_mas),margin=ft.margin.only(left=7))
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page