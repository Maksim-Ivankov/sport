


import flet as ft
from assets.variable import *
from assets.imports import *

class Menu(ft.UserControl):

    def __init__(self,collback):
        super().__init__()
        self.collback = collback

    def build(self):
        
        # Контейнер меню
        self.menu = ft.Container(
                
            ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Посещение"),
                    ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Тренировка"),
                    ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_BORDER,label="Вес"),
                ],
                on_change=self.collback
            )
            
        )
        
        return self.menu