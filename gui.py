import PySimpleGUI as sg
import database
import report

class GUI(object):

    def __init__(self,database_list,database_dict):
        self.database_dict = database_dict
        self.database_list = database_list
        self.layout = [ [sg.Text('Select Database'), sg.Combo(self.database_list, default_value=database_list[0], size=(20, 1), key='selected')],
                        [sg.Button('Load Database'), sg.Button('Exit')],
                        [sg.Button('Create Report'), sg.Button('See Report')] ]


    def layout():
        return self.layout


    def layout_theme(self):
        sg.theme('DarkAmber')


    def gui_events(self,window):
        """Event Loop to process "events" and get the "values" of the inputs"""

        while True:
            event, values = window.read()
            if event in (None, 'Exit'):	# if user closes window or clicks cancel
                break

            if event == "Load Database":

                selected_db = self.database_list.index(values['selected'])
                print(selected_db)
                database = self.database_dict[self.database_list[selected_db]]

                window['Create Report'].Update(disabled=False)
                window.Refresh()

            if event == "Create Report":
                window['Load Database'].Update(disabled=True)
                window['Load Database'].Update(disabled=True)
                window['Create Report'].Update(disabled=True)

                rprt = report.Report()

                rprt.new_directory()

                report_file = rprt.name_report(self.database_list,selected_db)

                wb = rprt.new_report(report_file)

                ws = rprt.generate_data(wb,database)

                rprt.add_titles(ws)

                rprt.save_report(wb,report_file)

                window['Load Database'].Update(disabled=False)
                window['See Report'].Update(disabled=False)
                window['Create Report'].Update(disabled=False)
                window.Refresh()

            if event == 'See Report':
                window['See Report'].Update(disabled=True)
                rprt.open_report(report_file)

            window.Finalize()

    def init_window(self):
        """Initialize the window"""

        window = sg.Window('Report Maker(PySimpleGUI)', self.layout)

        window.Finalize()

        window['Create Report'].Update(disabled=True)
        window['See Report'].Update(disabled=True)
        window.Refresh()

        return window
