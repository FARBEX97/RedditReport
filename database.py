import os, json
import settings

class Database(object):

    def __init__(self):

        self.db_path ='databases.json'


    def load_databases(self):

        database_dict = {}

        with open(self.db_path) as database_dict:
            database_dict = json.load(database_dict)

        return database_dict


    def make_db_list(self, database_dict):

        database_list = []
        c = 0
        for db in database_dict.keys():
            database_list.append(db)
            print(str(c) + '.- ' + db)
            c = c + 1

        return database_list


    def select_database(self, database_dict, database_list):

        # exceptions: no files in database directory/no database directory

        print("Select database")


        database_selected = False

        while database_selected == False:
            try:
                selected_db = int(input('Write the number and press Int: '))
                database = database_dict[database_list[selected_db]]
                database_selected = True
            except ValueError:
                print('Please, put a number.')
            except IndexError:
                print('Please, select a valid option.')

        return database

