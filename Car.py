class Car(object):
    make = ""
    model = ""
    driven_kms = 0
    last_service = "1.1.1900"

    def __init__(self, make, model, driven_kms, last_service):
        self.make = make
        self.model = model
        self.driven_kms = driven_kms
        self.last_service = last_service

    def set_last_service_date(self, day, month, year):
        self.last_service = day + ". " + month + ". " + year

