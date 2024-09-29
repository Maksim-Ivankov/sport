
import flet as ft
from assets.variable import *
from assets.imports import *


class Pervie_two_mounth_page(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        self.tren = [
            'Тренировка 1 | Плчечи',
            'Тренировка 2 | Биц + триц',
            'Тренировка 3 | Ноги',
            'Тренировка 4 | Грудь',
            'Тренировка 5 | Спина',
        ]
    
    def change_menu(self,e):
        self.change_punkt_menu = e.control.data
        self.callback(e.control.data)
        

    def btn_number_tren(self,number_name):
        return ft.Container(
            ft.Text(number_name,color=c_blue,text_align='center'),
            data=number_name,
            width=200,
            height=60,
            bgcolor=c_yelow,
            padding=ft.padding.only(top=20),
            margin = ft.margin.only(left=50),
            on_click=self.change_menu
            
        )

    def build(self):
        
        self.items = []
        for punkt in self.tren:
            self.items.append(self.btn_number_tren(punkt))
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Первые два месяца тренировок',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=40),bgcolor=c_white),
                            ft.Column(self.items)
                            
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page