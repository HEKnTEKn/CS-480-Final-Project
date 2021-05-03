import PySimpleGUI as sg
import workingDatabase
import random
import string

sqlDatabase = workingDatabase.DB()

sqlDatabase.performTextQuery("SELECT * FROM matches2020;")

sg.theme('DarkBlue2')   # Add a touch of color
# All the stuff inside your window.

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]

sql_search = [
    [
        sg.Text("Optional Arguments"),
        sg.Multiline(size=(25, 1), enable_events=True, key="-inputArgs-"),
        sg.Button('Submit', font=('Times New Roman', 12))

    ],
    [
        sg.Listbox(
            values=["1. Custom Query - Input: a mySQL query within the bounds of Select permissions - Output: The result of that query.",
                    "2. Most Popular Champion - Input: role - Output: Champion and number of times played",
                    "3. Number of Wins - Input: 'TeamName' (surrounded by quotation marks) - Output: the number of wins that the given team had that year.",
                    "4. Match Winner - Input: 'matchID' (ex.'5655-7249') - Output: the Winning team, and players of that team.",
                    "5. Tag-Move Speed - Input: A tag of a champion (ex. Mage, Bruiser) - Output: The movespeeds of the champions, asc.",
                    "6. Difficulty - Input: Champion Name (multiple can be selected in format 'champ1, champ2, champ3') - Output: Difficulty levels."
                    ], enable_events=True, size=(125, 36), auto_size_text=True,  key="-FILE LIST-"
        )
    ],
]

sql_output = [
    [
        sg.Text("Look Into The Esports Data To Stay Updated!", font=('Times New Roman', 20)),
    ],

    [

        sg.Table(

                    values=data[1:][:], headings=headings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
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

    if event == 'Submit':
        print("submit button pressed!")

        if values['-FILE LIST-'][0][0] == "1":
            result = sqlDatabase.performTextQuery(values['-inputArgs-'])
            window['-OUT LIST-'].update(result)
        elif values['-FILE LIST-'][0][0] == "2":
            result = sqlDatabase.performInternalQuery("mostPlayed.sql", values['-inputArgs-'])
            window['-OUT LIST-'].update(result)
        elif values['-FILE LIST-'][0][0] == "3":
            result = sqlDatabase.performInternalQuery("numWins.sql", values['-inputArgs-'])
            window['-OUT LIST-'].update(result)
        elif values['-FILE LIST-'][0][0] == "4":
            result = sqlDatabase.performInternalQuery("winner.sql", values['-inputArgs-'])
            window['-OUT LIST-'].update(result)
        else:
            window['-OUT LIST-'].update("Sorry, but the selection you entered is not acceptable. Please try again!")


window.close()
