import flet as ft
from assets.variable import *
from assets.imports import *

data_print = {
    '1': ft.Container(
        ft.Column(controls=[
            ft.Text('Тренировка 1 | Плчечи',text_align='center',color=c_white,width=390,size=18),
            ft.Text('Длительность - 1 час',text_align='center',color=c_white,width=390),
            ft.Container(width=390,height=1,margin=ft.margin.only(top=20,bottom=20),bgcolor=c_white),
            ft.Container(
                ft.Column(controls=[
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('1. Кардиотренажёр'),
                            ft.Text('   10 минут'),
                        ]),
                    width=390,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('2. Жим гантелей сидя'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('3. Махи гантелями в стороны'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('4. Жим Арнольда'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('5. Махи гантелями вперёд'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('6. Скручивания на наклонной лавке'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
                ft.Container(
                    ft.Column(controls=[
                            ft.Text('1. Кардиотренажёр'),
                            ft.Text('   10 минут'),
                        ]),
                    width=390,
                    height=100,
                    border=ft.border.all(1,c_white),
                    padding=ft.padding.all(10)
                ),
            ],scroll=ft.ScrollMode.ALWAYS),
                height=500
            )
        ],scroll=ft.ScrollMode.ALWAYS)
    ),
    '2': ft.Container(

    ),
    '3': ft.Container(

    ),
    '4': ft.Container(

    ),
    '5': ft.Container(

    ),
}