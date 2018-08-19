class FFile:
    def __init__(self, location):
        self.location = location

    def read_file(self):
        file = open(self.location, "r")
        string = file.read()
        file.close()
        return string

    def write_file(self, string):
        file = open(self.location, "w")
        file.write(string)
        file.close()
        return 1