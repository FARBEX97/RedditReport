
# Coded by FARBEX97 (@fernando_arbex)

# This program extracts subreddit's best posts and make report in a new Excel workbook.



import os
import PySimpleGUI as sg
import report, database, gui


def main():
    
    db = database.Database()
    database_dict = db.load_databases()
    database_list= db.make_db_list(database_dict)


    GUI = gui.GUI(database_list,database_dict)

    layout = GUI.layout

    window = GUI.init_window()

    # Workflow control through gui
    GUI.gui_events(window)

    window.close()


if __name__ == "__main__":
    main()