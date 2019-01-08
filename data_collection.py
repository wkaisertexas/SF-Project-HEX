import os


class DataCollection:
    def __init__(self, name, version, time):
        self.name = name
        self.version = version
        self.time = time

    def check_continued_experiment(self):
        files_list = os.listdir('Saves')

        for file in files_list:
            # this checks to make sure it is a folder
            if file.find('.') < 0:
                continue

            # this checks to see if the version is the same
            if self.version != int(file.split('V')[-1]):
                continue

            # this checks to see if the name of the experiment is the same
            if self.name == file.split(':')[1].split('V')[0]:
                return file, self.load_previous_save_script(file), self.load_previous_model(file)

        return None, None, None

    def save_game_set(self, game_array):


    def load_previous_model(self, dir):
        # this will be edited later once I know more about how to open/read these types of files
        return open('Saves' + dir, "rw")

    def load_previous_save_script(self, dir):
        return open('Saves' + '\\' + dir + '\\games.txt', 'rw')


# Testing
DataCollection().check_continued_experiment()
