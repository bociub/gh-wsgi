from extensions import db
greenHouse_list = []

"""Without database
def get_last_id():
    if greenHouse_list:
        last_greenHouse = greenHouse_list[-1]
    else:
        return 1
    return last_greenHouse.id + 1


class GreenHouse:

    def __init__(self, name, plant, postcode, plantingDate=0, forSale=False, bookedForSale=0,
                 energyPlan=0, harvestDate=0, counterForAVG=0, AVGofAirTemperature=0, 
                 GivenDaysWeather=0, currentParameters=0):
        self.id = get_last_id() #function above
        self.name = name
        self.plant = plant
        self.postcode = postcode
        self.plantingDate = 9
        self.forSale = True
        self.bookedForSale = 7
        self.energyPlan = 6
        self.harvestDate = 5
        self.counterForAVG = 4
        self.AVGofAirTemperature = 3
        self.GivenDaysWeather = 2
        self.currentParameters = 1 
    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'plant': self.plant,
            'forSale': self.forSale

        }"""
class GreenHouse(db.Model):
    __tablename__ = 'greenhouses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.user_id"))
    #bookedForSale = db.Column(db.Boolean())
    recordDateTime = db.Column(db.String(20))#db.Column(db.DateTime(), nullable=True)
    LightRelay = db.Column(db.Boolean())
    LightCurrent = db.Column(db.Boolean())
    FanRelay = db.Column(db.Boolean())
    FanCurrent = db.Column(db.Boolean())
    OutsideTemp = db.Column(db.Float)
    InsideTemp = db.Column(db.Float)
    Lightsensor = db.Column(db.Boolean())
    AirheaterRelay = db.Column(db.Boolean())
    AirHeaterCurrent = db.Column(db.Boolean())
    WaterPumpCurrent = db.Column(db.Boolean())
    WaterHeaterRelay = db.Column(db.Boolean())
    WaterHeaterCurrent = db.Column(db.Boolean())
    WaterTemp = db.Column(db.Float)
    AirPumpCurrent = db.Column(db.Boolean())

    
  

    def data(self):# do I need this?
        return {
          
            'id': self.id,
            'user_id': self.user_id,
            #'bookedForSale': self.bookedForSale,
            'recordDateTime': self.recordDateTime,
            'LightRelay':  self.LightRelay,
            'LightCurrent': self.LightCurrent,
            'FanRelay': self.FanRelay,
            'FanCurrent': self.FanCurrent,
            'OutsideTemp': self.OutsideTemp,
            'InsideTemp':  self.InsideTemp,
            'Lightsensor':  self.Lightsensor,
            'AirheaterRelay': self.AirheaterRelay,
            'AirHeaterCurrent' : self.AirHeaterCurrent,
            'WaterHeaterRelay' : self.WaterHeaterRelay,
            'WaterHeaterCurrent' : self.WaterHeaterCurrent,
            'WaterTemp' : self.WaterTemp,
            'AirPumpCurrent' : self.AirPumpCurrent

            
            
            
        }

    @classmethod
    def get_all_forSale(cls):
        return cls.query.filter_by(bookedForSale=True).all()

    @classmethod
    def get_by_id(cls, greenHouse_id):
        return cls.query.filter_by(id=greenHouse_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()







    
