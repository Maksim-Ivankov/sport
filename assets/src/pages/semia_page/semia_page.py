
import flet as ft
from assets.variable import *
from assets.imports import *


class Semia_page(ft.UserControl):
    def __init__(self,page,callback):
        super().__init__()
        self.page = page
        self.callback = callback
        self.input_data = 0
        self.cwd = 'None'
    

    def input_save(self,e):
        self.input_data = e.data
        

    def save_massa(self,e):
        # записали время и вес
        file = open(f'{str(os.getcwd())}/data_massa.txt', 'a')
        file.write(f'\n{str(time.strftime("%m-%d-%Y | %H:%M"))} | {str(self.input_data)}')
        file.close()
        self.callback('Семья')


    def build(self):
        array_mass_text = []
        if os.path.isfile(f'{str(os.getcwd())}/data_massa.txt'):
            with open(f'{str(os.getcwd())}/data_massa.txt') as file:
                array_mass_text = [row.strip() for row in file]
        
        list_massa = []
        if len(array_mass_text) != 0:
            for item in array_mass_text:
                if len(item)>0:
                    list_massa.append(ft.Container(
                        ft.Text(f'{item}')
                    ))
        list_massa = reversed(list_massa)
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Развлечения с семьёй',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            ft.Text('Введи комментарии',text_align='center',color=c_white,width=390),
                            ft.Container(
                                ft.TextField(
                                on_change=self.input_save,
                                width=200,
                                border_radius=0,
                                border_color=c_yelow,
                                height=30,
                                content_padding=ft.padding.only(left=5,right=5),
                                text_align='center',
                                text_size=12,
                                
                            ),margin=ft.margin.only(left=55)),
                            ft.Container(ft.Container(ft.Text('Сохранить',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=10,left=55),border = ft.border.all(0,c_white),width=200,on_click=self.save_massa ),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            ft.Container(
                                ft.Column(controls=list_massa,scroll=ft.ScrollMode.ALWAYS),
                                height=350,
                                width=390
                                
                            )
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page