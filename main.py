import PySimpleGUI as sg
import workingDatabase
sqlDatabase = workingDatabase.DB()

sqlDatabase.performTextQuery("SELECT * FROM matches2020;")

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

sql_searh = [
    [
        sg.Text("Search Esport"),
        sg.In(size=(25, 1), enable_events=True, key="-esport-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(75, 36), key="-FILE LIST-"
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

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    print('You entered ', values[0])

window.close()