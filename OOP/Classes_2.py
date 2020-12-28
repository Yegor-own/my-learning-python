class Camera:
    def camera_method(self):
        print('Parent method of class Camera')


class Radio:
    def radio_method(self):
        print('Parent method of class Radio')


class Phone(Camera, Radio):
    def phone_method(self):
        print('Doter method of classes Camera and Radio')


phone = Phone()
phone.camera_method()
phone.radio_method()
phone.phone_method()