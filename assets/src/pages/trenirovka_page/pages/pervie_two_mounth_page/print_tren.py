
import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.trenirovka_page.pages.pervie_two_mounth_page.data_page import data_print


class Print_tren(ft.UserControl):
    def __init__(self,change_menu):
        super().__init__()
        self.change_menu = change_menu

    def build(self):
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            data_print[self.change_menu],
                            
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page