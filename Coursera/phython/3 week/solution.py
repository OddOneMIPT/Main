import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        photo_ext = os.path.splitext(self.photo_file_name)
        return photo_ext[1]



class Car(CarBase):
    car_type = "car"
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if 'x' in body_whl:
            body = list(body_whl.split('x'))
            if len(body) == 3:
                try:
                    self.body_length = float(body[0])
                    self.body_width = float(body[1])
                    self.body_height = float(body[2])
                except (ValueError, IndexError):
                    self.body_length = 0.0
                    self.body_width = 0.0
                    self.body_height = 0.0
            else:
                self.body_length = 0.0
                self.body_width = 0.0
                self.body_height = 0.0


        else:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
    
    def get_body_volume(self):
        try:
            a = float(self.body_height)*float(self.body_length)*float(self.body_width)
            return a
        except ValueError:
            return 0.0




class SpecMachine(CarBase):
    car_type = "spec_machine"
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    dictionary = ['.jpeg', '.jpg', '.png', '.gif']
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if os.path.splitext(row[3])[1] in dictionary and os.path.splitext(row[3])[0] != '' and row[1] != '' and row[5].isdigit :
                    if row[0] == 'car':
                        data = Car(row[1],row[3],row[5],row[2])
                        car_list.append(data)

                    if row[0] == 'truck':
                        data = Truck(row[1],row[3],row[5],row[4])
                        car_list.append(data)

                    if row[0] == 'spec_machine' and row[6] != '':
                        data = SpecMachine(row[1],row[3],row[5],row[6])
                        car_list.append(data)
            except (IndexError, ValueError):
                continue
    return car_list


