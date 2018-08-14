import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_width, self.body_height, self.body_length = body_whl

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def whl_string_to_floats(whl):
    floats = []
    if whl:
        splitted = whl.split(sep='x')
        for s in splitted:
            floats.append(float(s))
    else:
        floats = [0.0, 0.0, 0.0]
    return floats


def get_args_vals(reihe, *args):
    result = []
    for arg in args:
        try:
            arg_val = arg(reihe)
            result.append(arg_val)
        except:
            return 0
    return result


def get_car_list(csv_filename):
    car_list = []

    def brand(r):
        return r[1]

    def passenger_seats_count(r):
        return int(r[2])

    def photo_file_name(r):
        return r[3]

    def body_whl(r):
        return whl_string_to_floats(r[4])

    def carrying(r):
        return float(r[5])

    def extra(r):
        return r[6]

    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7 and row[0] in ['car', 'truck', 'spec_machine']:
                if row[0] == 'car' and not row[4] and not row[6]:
                    vals = get_args_vals(row, brand, photo_file_name, carrying, passenger_seats_count)
                    if vals:
                        car_list.append(Car(*vals))
                elif row[0] == 'truck' and not row[2] and not row[6]:
                    vals = get_args_vals(row, brand, photo_file_name, carrying, body_whl)
                    if vals:
                        car_list.append(Truck(*vals))
                elif row[0] == 'spec_machine' and not row[2] and not row[4]:
                    vals = get_args_vals(row, brand, photo_file_name, carrying, extra)
                    if vals:
                        car_list.append(SpecMachine(*vals))
    return car_list
