
import flet as ft
from assets.variable import *
from assets.imports import *


class Masa_page(ft.UserControl):
    def __init__(self,page,callback):
        super().__init__()
        self.page = page
        self.callback = callback
        self.input_data = 0
        self.cwd = 'none'
    

    def input_save(self,e):
        self.input_data = e.data
        print(self.page.client_storage.get("massa"))
        

    def save_massa(self,e):
        # data_old = self.page.client_storage.get("massa")
        # data_old[str(time.strftime("%m-%d-%Y | %H:%M"))] = str(self.input_data)
        # self.page.client_storage.set('massa', data_old)
        # self.cwd = os.getcwd()
        file = open(f'{str(os.getcwd())}/test_min.txt', 'r')
        self.cwd = file.read()
        file.close()
        self.callback('Вес')


    def build(self):
        file = open(f'{str(os.getcwd())}/test_min.txt', 'w')
        file.write('Hello!')
        file.close()
        # list_massa = []
        # if self.page.client_storage.get("massa") != None:
        #     for key,value in self.page.client_storage.get("massa").items():
        #         print(f'{key} - {value}')
        #         list_massa.append(ft.Container(
        #             ft.Row(controls=[
        #                 ft.Text(key),
        #                 ft.Text(f'{value} кг'),
        #             ])
        #         ))
        
        # list_massa = [ft.Container(ft.Row(controls=[ft.Text('09-17-2024 | 11:02'),ft.Text(f'132.56 кг'),])),
        #               ft.Container(ft.Row(controls=[ft.Text('09-16-2024 | 10:15'),ft.Text(f'132.50 кг'),])),
        #               ]
        # list_massa = list(reversed(list_massa))
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Изменения веса',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            ft.Text('Введи текущий вес в кг',text_align='center',color=c_white,width=390),
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
                            ft.Container(ft.Container(ft.Text('Сохранить вес',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=10,left=55),border = ft.border.all(0,c_white),width=200,on_click=self.save_massa ),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            # ft.Container(
                            #     ft.Column(controls=list_massa,scroll=ft.ScrollMode.ALWAYS),
                            #     height=350,
                                
                            # )
                            ft.Text(self.cwd,text_align='center',color=c_yelow,width=390),
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page