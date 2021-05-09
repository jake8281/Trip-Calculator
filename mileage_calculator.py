import pandas as pd
import ip
import dst


class Trip:
    def __init__(self, destination, mileage=1,
                 gas_price=1, tank_size=1):
        self.destination = destination
        self.mileage = mileage
        self.gas_price = gas_price
        self.tank_size = tank_size

        ip_info = ip.ip_info()
        self.my_city = ip_info.get('city').lower()
        self.my_region = ip_info.get('region')

    def get_distance(self):
        return dst.fetch_distance(self.my_city, self.destination)

    def summary(self):
        d = self.get_distance()
        c = round((self.gas_price * self.tank_size) * (d/(self.tank_size* self.mileage)), 2)

        data = {
                "My City": self.my_city.title(),
                "My State": self.my_region,
                "Destination": self.destination,
                "Distance": d,
                "Cost": c,
                "MPG": self.mileage,
                "Gas_price": self.gas_price,
                "Tank_size": self.tank_size
        }

        return pd.DataFrame(data, index=[0])