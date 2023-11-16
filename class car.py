class car () :
    def __init__(self, Brand, color, Horse_power, production_year, country_of_origin, price ) :
        self.Brand =  Brand
        self. color =  color
        self. Horse_power =  Horse_power
        self.production_year = production_year
        self. country_of_origin =  country_of_origin
        self.price = price

    def info(self):
        print("the car's Brand is : {},  the color: {},  Horse_power: {}, production_year : {},   country_of_origin: {}, price: {}"
              .format(self.Brand , self. color , self. Horse_power , self.production_year , self. country_of_origin , self.price))
        

emp1 = car("Audi", "green olive", "  from 252 PS to 367 PS", 2021,"Germany","600000DH" )
emp2 = car("Bently", "black", "  from 513 PS to 537 PS", 2016,"England","1350000DH" )
emp3 = car("BMW", "Blue", "  from 286 PS to 571 PS", 2023,"Germany","3500000DH" )

emp1.info()
emp2.info()
emp3.info()