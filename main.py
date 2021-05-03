import PySimpleGUI as sg
import workingDatabase
sqlDatabase = workingDatabase.DB()

sqlDatabase.performTextQuery("SELECT * FROM matches2020;")

#sg.theme('')   # Add a touch of color
# All the stuff inside your window.

sql_searh = [
    [
        sg.Text("Custom Query"),
        sg.In(size=(65, 6), enable_events=True, key="-esport-"),

    ],
    [
        sg.Listbox(

            values=['Games Won', 'Games Lost', 'Total games played', 'Player with most points'], enable_events=True, size=(75, 36), key="-FILE LIST-"
        )
    ],
]

sql_output = [

    [
        sg.Listbox(
            values=[], enable_events=True, size=(75, 36), key="-OUT LIST-"
        )
    ],
]
layout = [
    [
        sg.Column(sql_searh),
        sg.VSeperator(),
        sg.Column(sql_output),
    ]
]

window = sg.Window("Esports Data", layout)

event, values = window.read()

window.close()