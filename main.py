import PySimpleGUI as sg
import workingDatabase

sqlDatabase = workingDatabase.DB()

# All the stuff inside your window.

sql_search = [
    [
        sg.Text("Optional Parameters"),
        sg.In(size=(25, 1), enable_events=True, key="-esport-"),

    ],
    [
        sg.Listbox(
            values=["Games Won",
                    "Games Lost",
                    "Player With Most Points",
                    "Game Stats"], enable_events=True, size=(75, 36), key="-FILE LIST-"
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
        sg.Column(sql_search),
        sg.VSeperator(),
        sg.Column(sql_output),
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    # Run the Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == 'submit':
        sqlDatabase.performInternalQuery(values[0], values[1])

window.close()
