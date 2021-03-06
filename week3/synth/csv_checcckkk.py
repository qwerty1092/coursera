# to get .jpeg -> os.path.splitext
import csv
import os
class BaseCar():
    'parent class'
    def __init__(self,cartype, photo_file_name, brand, carrying):
        self._cartype=cartype
        self._brand=brand
        self._carrying=float(carrying)
        self._photo_file_name=photo_file_name
        
        
    def get_type(self):
        return self._cartype
        
        
    def get_photo_file_ext(self):
        res = os.path.splitext(self._photo_file_name)[1]
        if res=='':
            res='wrong extension'
        return res
        
        
    def get_brand(self):
        return (self._brand)


class Car(BaseCar):
    'Car class, unique: passenger_seats_count'
    def __init__(self,cartype, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(cartype, photo_file_name, brand, carrying)
        self._passenger_seats_count=int(passenger_seats_count)
        

class Truck(BaseCar):
    'Truck class, unique: body_width*height*length'
    def __init__(self,cartype,photo_file_name, brand, carrying, body_whl):
        super().__init__(cartype, photo_file_name, brand, carrying)
        if body_whl != "" :
            try:
                self._body_width=float(body_whl.split('x')[0])
                self._body_height=float(body_whl.split('x')[1])
                self._body_length=float(body_whl.split('x')[2])
            except IndexError:
                self._body_width=0
                self._body_height=0
                self._body_length=0
        else:
            self._body_width=0
            self._body_height=0
            self._body_length=0
    
    def get_body_volume(self):
        res = self._body_width*self._body_height*self._body_length
        return res
        
        
class SpecMachine(BaseCar):
    'SpecMachine class, unique: extra'
    def __init__(self,cartype,photo_file_name, brand, carrying,extra):
       super().__init__(cartype, photo_file_name, brand, carrying)
       self._extra=extra 
       


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, "r") as f_obj:
        reader = csv.DictReader(f_obj,delimiter=';')
        for row in reader:
            type=row['car_type']
            br = row['brand']
            psc = row['passenger_seats_count']
            ph=row['photo_file_name']
            body=row['body_whl']
            carr=row['carrying']
            ext=row['extra']
            if type=='car':
                if ph!='' and br!='' and carr!='' and psc!='':
                    try:
                        car_list.append(Car(type,ph,br,carr,psc))
                    except Exception:
                        pass
            elif type=='truck':
                if ph!='' and br!='' and carr!='':
                    try:
                        car_list.append(Truck(type,ph,br,carr,body))
                    except Exception:
                        pass
            elif type=='spec_machine':
                if ph!='' and br!='' and carr!='' and ext!='':
                    try:
                        car_list.append(SpecMachine(type,ph,br,carr,ext))
                    except Exception:
                        pass
        return car_list
            
            
            
            
#new=Truck('tr','new_photo.jpeg','AUDI','2.5','10x10x10')
#print(new.__dict__)

new_list=get_car_list('D:\coursera_week3_cars.csv')
for item in new_list:
    msg = f'Photo_ext for {item.get_brand()}: {item.get_photo_file_ext()}'
    if item.get_type()=='truck':
        msg +=f' body_vol: {item.get_body_volume()}'
    print(msg)