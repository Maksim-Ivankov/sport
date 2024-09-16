import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.main_page.main_page import Main_page

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page_one = 'Главная'

    def build(self):
        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page,punkt_menu):
            platforma = ft.Container(
                ft.Row(
                    controls=[
                        ft.Container(
                            expand=2, content=page
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
                'Главная':Main_page(),
                # 'Историческая торговля':Hisorical_trade_page(self.page),
                # 'Тестовая торговля':Test_trade_page(),
                # 'Торговый робот':Trade_robot_page(),
                # 'FAQ':Faq_page(),
                # 'Профиль':Prifile_page(),
                # 'Настройки программы':Settings_page(),
            }

        self.page_select = punkts[self.page_one]
        
        return print_window(self.page_select,self.page_one)