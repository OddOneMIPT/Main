class FileReader:
    def __init__(self, name):
        FileReader.name = name

    def read(self):
        try:
            with open(self.name, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.name, 'w') as f:
                f.write('')
        
        with open(self.name, 'r') as f:
            return f.read()            

