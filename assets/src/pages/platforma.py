import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.visit_page.visit_page import Visit_page
from assets.src.pages.trenirovka_page.trenirovka_page import Trenirovka_page
from assets.src.pages.masa_page.masa_page import Masa_page
from assets.src.menu.menu import Menu

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page_one = 'Посещение'
        

    def change_menu(self,e):
        print(e.data)

    def print_page(self):
        

    def build(self):
        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page,punkt_menu):
            platforma = ft.Container(
                ft.Column(
                    controls=[
                        ft.Container(
                            expand=2, content=page
                        ),
                        ft.Container(
                            content=Menu(self.change_menu),
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
                'Посещение':Visit_page(),
                'Тренировка':Trenirovka_page(),
                'Вес':Masa_page(),
                # 'Историческая торговля':Hisorical_trade_page(self.page),
                # 'Тестовая торговля':Test_trade_page(),
                # 'Торговый робот':Trade_robot_page(),
                # 'FAQ':Faq_page(),
                # 'Профиль':Prifile_page(),
                # 'Настройки программы':Settings_page(),
            }

        self.page_select = punkts[self.page_one]
        
        return print_window(self.page_select,self.page_one)