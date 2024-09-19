
import flet as ft
from assets.variable import *
from assets.imports import *


class Visit_page(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        list_key = ['0','1','2','3','4','5','6','7','8','9',]
        count = 0
        self.visited_sl = {}
        if os.path.isfile(f'{str(os.getcwd())}/data_visited.txt'):
            with open(f'{str(os.getcwd())}/data_visited.txt') as file:
                for line in file:
                    if len(line)!=1:
                        self.visited_sl[str(count)] = line.split('|')
                        count+=1
                    
        else:
            # print('Файла нет')
            self.visited_sl = {
                '0':['0','0','0','0','0','0','0','0','0','0'],
                '1':['0','0','0','0','0','0','0','0','0','0'],
                '2':['0','0','0','0','0','0','0','0','0','0'],
                '3':['0','0','0','0','0','0','0','0','0','0'],
                '4':['0','0','0','0','0','0','0','0','0','0'],
                '5':['0','0','0','0','0','0','0','0','0','0'],
                '6':['0','0','0','0','0','0','0','0','0','0'],
                '7':['0','0','0','0','0','0','0','0','0','0'],
                '8':['0','0','0','0','0','0','0','0','0','0'],
                '9':['0','0','0','0','0','0','0','0','0','0'],
            }
            for key,value in self.visited_sl.items():
                file = open(f'{str(os.getcwd())}/data_visited.txt', 'a')
                file.write(f'\n{'|'.join(value)}')
                file.close()

    def click_visited(self,e):
        # print(e.control.content.value)
        des = (int(e.control.content.value)-1)//10
        celka = int(e.control.content.value) - des*10
        celka = celka-1
        if celka == -1: celka = 9
        # print(f'{des} - {celka}')
        if self.visited_sl[str(des)][celka] == '0':
            self.visited_sl[str(des)][celka] = '1'
        else:
            self.visited_sl[str(des)][celka] = '0'
        # print(self.visited_sl)
        f = open(f'{str(os.getcwd())}/data_visited.txt', 'w')
        f.close()
        for key,value in self.visited_sl.items():
            file = open(f'{str(os.getcwd())}/data_visited.txt', 'a')
            file.write(f'\n{'|'.join(value)}')
            file.close()
        self.callback('Посещение')
        

    def build(self):
        
        row_mas = []
        col_mas = []
        for key,value in self.visited_sl.items():
            count_data = 1
            for i in value:
                if i == '1':
                    row_mas.append(ft.Container(ft.Text((int(key)*10)+count_data,text_align='center',color='#808080',size=10),bgcolor=c_green,padding=ft.padding.only(top=3),data='1',width=24,height=24,border=ft.border.all(1,c_white),margin=-2,on_click=self.click_visited))
                else:
                    row_mas.append(ft.Container(ft.Text((int(key)*10)+count_data,text_align='center',color='#808080',size=10),padding=ft.padding.only(top=3),data='1',width=24,height=24,border=ft.border.all(1,c_white),margin=-2,on_click=self.click_visited))
                    
                count_data+=1
            col_mas.append(ft.Row(controls=row_mas))
            row_mas[:]=[]
        
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Посещение тренировок',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            ft.Text('Старт - 16.09.2024 г',text_align='center',color=c_white,width=390),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Прошло',text_align='center',color=c_white),
                                ft.Text(' 3 дня',text_align='center',color=c_yelow),
                            ]),width=390,padding=ft.padding.only(left=100)),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Посещено',text_align='center',color=c_white),
                                ft.Text(' 2 тренировки',text_align='center',color=c_yelow),
                            ]),width=390,padding=ft.padding.only(left=60),margin=ft.margin.only(bottom=20)),
                            ft.Container(ft.Column(controls=col_mas),margin=ft.margin.only(left=7))
                            # teble_now,
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page