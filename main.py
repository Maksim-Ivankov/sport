import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.platforma import Platforma

class Main:
    def __init__(self):
        None

    def run(self, page):
        
        self.page: ft.Page = page
        self.page.title = "Треня"
        self.page.window_height, self.page.window_width = height_window_platforma, width_window_platforma
        # self.page.theme_mode = "dark" 
        # self.page.window_resizable = False
        # self.page.window_center()
        # self.page.bgcolor = c_blue
        self.main_print = ft.Container( # общий контейнер на страницу45rк
        #    content = ft.Text('123123123'),
           content = Platforma(self.page),
        #    expand = True,
           padding=ft.padding.only(bottom=-10)
        )
        self.page.add(self.main_print)



main = Main()
ft.app(target=Main().run, assets_dir="assets")


# if __name__ == '__main__':
#     main = Main()
#     ft.app(target=Main().run, assets_dir="assets")































































