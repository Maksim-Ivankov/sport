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
        self.punkts = {
                'Посещение':Visit_page(),
                'Тренировка':Trenirovka_page(),
                'Вес':Masa_page(),
            }
        self.changes_menu = {
             '0':'Посещение',
             '1':'Тренировка',
             '2':'Вес',
        }

    def change_menu(self,e):
        self.menu_update(self.changes_menu[e.data])

    def print_window(self,page):
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
    def menu_update(self,punkt_menu='Посещение'):
        self.page_select = self.punkts[punkt_menu]
        self.controls = []
        self.update()
        self.controls.append(self.print_window(self.page_select))
        self.update()


    def build(self):
        return self.print_window(self.punkts['Посещение'])