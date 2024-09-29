
import flet as ft
from assets.variable import *
from assets.imports import *


class Timer_page(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.print_sec = 0
        self.print_min = 0
        self.print_hour = 0
        self.state_timer = False
        self.current_time = datetime.datetime.now()
        
    def change_menu(self,e):
        self.change_punkt_menu = e.control.data
        self.callback(e.control.data)

    def start_timer(self,e):
        self.state_timer = True
        self.myThread = threading.Thread(target=self.timer_work(), args=(), daemon=True)
        self.myThread.start()

    def stop_timer(self,e):
        self.state_timer = False
        self.controls[0].content.controls[0].content.controls[2].content.color = c_red
        self.update()

    def complete_day(self,e):
        file = open(f'{str(os.getcwd())}/data_work.txt', 'a')
        file.write(f'{self.current_time.year}|{self.current_time.month}|{self.current_time.day}|{self.hour}|{self.min}|\n')
        file.close()
        file_timer = open(f'{str(os.getcwd())}/data_timer.txt', 'w')
        file_timer.write('00\n')
        file_timer.write('00\n')
        file_timer.write('00\n')
        file_timer.close()
        self.controls[0].content.controls[0].content.controls[2].content.value = f'00:00:00'
        self.controls[0].content.controls[0].content.controls[2].content.color = c_red
        self.update()


    def timer_work(self):
        while self.state_timer:
            time.sleep(1)
            self.sec += 1
            if self.sec == 60:
                self.sec = 0
                self.min +=1
            if self.min == 60:
                self.min = 0
                self.hour +=1
            if len(str(self.hour))!=2: self.print_hour = f'0{self.hour}'
            else: self.print_hour = f'{self.hour}'
            if len(str(self.min))!=2: self.print_min = f'0{self.min}'
            else: self.print_min = f'{self.min}'
            if len(str(self.sec))!=2: self.print_sec = f'0{self.sec}'
            else: self.print_sec = f'{self.sec}'
            
            file = open(f'{str(os.getcwd())}/data_timer.txt', 'w')
            file.write(self.print_hour+'\n')
            file.write(self.print_min+'\n')
            file.write(self.print_sec+'\n')
            file.close()

            self.controls[0].content.controls[0].content.controls[2].content.value = f'{self.print_hour}:{self.print_min}:{self.print_sec}'
            self.controls[0].content.controls[0].content.controls[2].content.color = c_green
            if self.state_timer == False:
                self.controls[0].content.controls[0].content.controls[2].content.color = c_red
            self.update()

    def build(self):
        array_data_time = []
        if os.path.isfile(f'{str(os.getcwd())}/data_timer.txt'):
            with open(f'{str(os.getcwd())}/data_timer.txt') as file:
                array_data_time = [row.strip() for row in file]
        list_print = '00:00:00'
        if len(array_data_time) != 0:
            list_print = f'{array_data_time[0]}:{array_data_time[1]}:{array_data_time[2]}'
            self.sec = int(array_data_time[2])
            self.min = int(array_data_time[1])
            self.hour = int(array_data_time[0])
        array_data_complite_time = []
        print_data_complite = []
        if os.path.isfile(f'{str(os.getcwd())}/data_work.txt'):
            with open(f'{str(os.getcwd())}/data_work.txt') as file:
                array_data_complite_time = [row.strip() for row in file]
                for i in array_data_complite_time:
                    row_data = i.split('|')
                    print_data_complite.append(ft.Container(ft.Text(f'{row_data[2]}.{row_data[1]}.{row_data[0]} - {row_data[3]} ч {row_data[4]} м',width=390,text_align='center')))
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(controls=[
                            ft.Text('Время работы сегодня',text_align='center',color=c_yelow,width=390),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=40),bgcolor=c_white),
                            ft.Container(ft.Text(list_print,size=60,color=c_red,text_align='center',width=390),margin=ft.margin.only(bottom=50)),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('Старт',color=c_blue,text_align='center',size=30),width=150,height=50,bgcolor=c_yelow,on_click=self.start_timer),
                                ft.Container(ft.Text('Пауза',color=c_blue,text_align='center',size=30),width=150,height=50,bgcolor=c_yelow,on_click=self.stop_timer),
                            ])),
                            ft.Container(ft.Text('Завершить день',color=c_blue,text_align='center',size=30),width=390,height=50,bgcolor=c_yelow,on_click=self.complete_day),
                            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=40),bgcolor=c_white),
                            ft.Container(
                                ft.Column(controls=reversed(print_data_complite),scroll=ft.ScrollMode.ALWAYS),
                                height=180,
                                width=390
                                
                            )
                        ]),padding=10,height=650,width=390
                    )
                ]
            ),expand=2
        )
        
        return self.main_page