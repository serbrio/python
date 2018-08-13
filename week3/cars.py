import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    #def car_type(self):
    #    return self.__class__.__name__

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count
        super().__init__(brand)
        super().__init__(photo_file_name)
        super().__init__(carrying)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = 'truck'
        self.body_width, self.body_height, self.body_length = body_whl
        super().__init__(brand)
        super().__init__(photo_file_name)
        super().__init__(carrying)

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = 'spec_machine'
        self.extra = extra
        super().__init__(brand)
        super().__init__(photo_file_name)
        super().__init__(carrying)


def whl_string_to_floats(whl):
    floats = []
    splitted = whl.split(sep='x')
    for s in splitted:
        floats.append(float(s))
    return floats

def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7 and row[0] in ['car', 'truck', 'spec_machine']:
                brand = row[1]
                passenger_seats_count = int(row[2])
                photo_file_name = row[3]
                body_whl = whl_string_to_floats(row[4])
                carrying = float(row[5])
                extra = row[6]
                if row[0] == 'car':
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif row[0] == 'truck':
                    car_list.append(Car(brand, photo_file_name, carrying, body_whl))
                elif row[0] == 'spec_machine':
                    car_list.append(Car(brand, photo_file_name, carrying, extra))
    return car_list
