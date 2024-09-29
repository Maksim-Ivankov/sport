import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.semia_page.semia_page import Semia_page
from assets.src.pages.timer_page.timer_page import Timer_page
from assets.src.pages.work_page.work_page import Work_page
from assets.src.menu.menu import Menu

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page_one = 'Работа'

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
                'Семья':Semia_page(self.page,callback),
                'Таймер':Timer_page(callback),
                'Работа':Work_page(callback),
            }

        self.page_select = punkts[self.page_one]

        # return ft.Text('12121')
        
        return print_window(self.page_select,self.page_one)