import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.visit_page.visit_page import Visit_page
from assets.src.pages.trenirovka_page.trenirovka_page import Trenirovka_page
from assets.src.pages.masa_page.masa_page import Masa_page
from assets.src.menu.menu import Menu
from assets.src.pages.trenirovka_page.pages.pervie_two_mounth_page.pervie_two_mounth_page import Pervie_two_mounth_page
from assets.src.pages.trenirovka_page.pages.pervie_two_mounth_page.print_tren import Print_tren

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page_one = 'Посещение'

    def build(self):
        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page,punkt_menu):
            platforma = ft.Container(
                ft.Column(
                    controls=[
                        ft.Container(width=360,height=30),
                        ft.Container(
                            expand=2, content=page
                        ),
                        ft.Container(
                            content=Menu(self.page,callback,punkt_menu),
                            
                        ),
                    ]),
            )
            return platforma
        
        # выбор пункта меню
        def callback(punkt_menu=self.page_one):
            self.page_select = punkts[punkt_menu]
            self.controls = []
            self.update()
            self.controls.append(print_window(self.page_select,punkt_menu))
            self.update()

        
        punkts = {
                'Посещение':Visit_page(callback),
                'Тренировка':Trenirovka_page(callback),
                'Вес':Masa_page(self.page,callback),
                'Первые 2 месяца':Pervie_two_mounth_page(callback),
                'Тренировка 1 | Плчечи':Print_tren('1'),
                'Тренировка 2 | Биц + триц':Print_tren('2'),
                'Тренировка 3 | Ноги':Print_tren('3'),
                'Тренировка 4 | Грудь':Print_tren('4'),
                'Тренировка 5 | Спина':Print_tren('5'),
            }

        self.page_select = punkts[self.page_one]

        # return ft.Text('12121')
        
        return print_window(self.page_select,self.page_one)