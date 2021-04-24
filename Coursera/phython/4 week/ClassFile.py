import os
import tempfile
import pprint

class File:
    def __init__(self, name):
        self._name = name
        self._path =  os.path.join(tempfile.gettempdir(), name)
        self.current = -1
        try: 
            with open(self._path, 'r') as f:
                f.read()
        except (FileNotFoundError, FileExistsError):
            with open(self._path, 'w') as f:
                f.write('')

    def read(self):
        with open(self._path, 'r') as f:
            return(f.read())

    def write(self, data_to_write):
        with open(self._path, 'w') as f:
            f.write(data_to_write)

    def __str__(self):
        return self._path

    def __add__(self, file_1):
        
        file_0 = File(self._name + '_0')
        with open(file_0._path, 'w') as f0:
            with open(file_1._path, 'r') as f2:
                with open(self._path, 'r') as f1:
                    wroten = f1.read() + f2.read()
                    f0.write(wroten)
        return file_0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == -1:
            with open(self._path, 'r') as f:
                count = 0
                for _ in f:
                    count += 1
            self.end = count
            self.current = 0
        if self.current >= self.end:
            self.current = -1
            raise StopIteration

        with open(self._path, 'r') as f:
            a = 0
            for line in f:
                if a == self.current:
                    result = line
                a += 1
        self.current += 1
        return result    


file1 = File('text1')
file1.write('Привет, как дела')
file2 = File('text2')
file2.write( 'Может быть познакомимся? \n Ye xnj ns vjkxbim')
file0 = file1 + file2

for line in file0:
    print(line)
