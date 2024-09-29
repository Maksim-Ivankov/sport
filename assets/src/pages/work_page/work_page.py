
import flet as ft
from assets.variable import *
from assets.imports import *

#111
class Work_page(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        count = 0
        self.visited_sl = {}
        if os.path.isfile(f'{str(os.getcwd())}/data_visited.txt'):
            with open(f'{str(os.getcwd())}/data_visited.txt') as file:
                for line in file:
                    if len(line)!=1:
                        self.visited_sl[str(count)] = line.split('|')
                        if self.visited_sl[str(count)][6][-1] == '\n':
                            self.visited_sl[str(count)][6] = self.visited_sl[str(count)][6][:-1]
                        count+=1
            # print(self.visited_sl)
        else:
            # print('Файла нет')
            self.visited_sl = {
                '0':['0','0','0','0','0','0','0'],
                '1':['0','0','0','0','0','0','0'],
                '2':['0','0','0','0','0','0','0'],
                '3':['0','0','0','0','0','0','0'],
                '4':['0','0','0','0','0','0','0'],
                '5':['0','0','0','0','0','0','0'],
                '6':['0','0','0','0','0','0','0'],
                '7':['0','0','0','0','0','0','0'],
                '8':['0','0','0','0','0','0','0'],
                '9':['0','0','0','0','0','0','0'],
                '10':['0','0','0','0','0','0','0'],
                '11':['0','0','0','0','0','0','0'],
                '12':['0','0','0','0','0','0','0'],
            }
            file = open(f'{str(os.getcwd())}/data_visited.txt', 'a')
            for key,value in self.visited_sl.items():
                # file.write(f'\n{'|'.join(value)}')
                file.write(f'\n{"|".join(str(bit) for bit in value)}')
            file.close()

    def daterange(self,start_date: date, end_date: date):
        days = int((end_date - start_date).days)
        for n in range(days):
            yield start_date + timedelta(n)   
        

    def build(self):
        start_date = date(2024, 9, 30)
        end_date = date(2024, 12, 31)
        date_data = []
        for single_date in self.daterange(start_date, end_date):
            date_data.append(single_date.strftime("%d.%m"))

        row_mas = []
        col_mas = []
        count_day_vizit = 0
        for key,value in self.visited_sl.items():
            count_data = 1
            for i in value:
                # print(i)
                if i == '0':
                    row_mas.append(ft.Container(ft.Text(str(date_data[count_day_vizit]),text_align='center',color=c_yelow,size=10),bgcolor=c_blue,padding=ft.padding.only(top=3),data='1',width=38,height=24,border=ft.border.all(1,c_white),margin=-2))  
                    count_day_vizit+=1
                count_data+=1
            col_mas.append(ft.Row(controls=row_mas))
            row_mas[:]=[]
        
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Индикатор работы',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
                            # ft.Text('Старт - 16.09.2024 г',text_align='center',color=c_white,width=390),
                            # ft.Container(ft.Row(controls=[
                            #     ft.Text('Прошло',text_align='center',color=c_white),
                            #     ft.Text(f' {self.day_old} дня',text_align='center',color=c_yelow),
                            # ]),width=390,padding=ft.padding.only(left=100)),
                            # ft.Container(ft.Row(controls=[
                            #     ft.Text('Посещено',text_align='center',color=c_white),
                            #     ft.Text(f' {count_day_vizit} тренировки',text_align='center',color=c_yelow),
                            # ]),width=390,padding=ft.padding.only(left=60),margin=ft.margin.only(bottom=20)),
                            ft.Container(ft.Column(controls=col_mas),margin=ft.margin.only(left=7))
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page