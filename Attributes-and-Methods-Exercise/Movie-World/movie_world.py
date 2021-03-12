class MovieWorld:
    _dvd_capacity = 15
    _customer_capacity = 10
    def __init__(self, name:str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld._dvd_capacity


    @staticmethod
    def customer_capacity():
        return MovieWorld._customer_capacity


    def add_customer(self, customer):
        if len(self.customers) < MovieWorld._customer_capacity:
            self.customers.append(customer)


    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld._dvd_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if c.id == customer_id]
        current_dvd = [d for d in self.dvds if d.id == dvd_id]
        if current_dvd:
            current_dvd = current_dvd[0]
        if current_customer:
            current_customer = current_customer[0]
            if current_dvd in current_customer.rented_dvds:
                return f"{current_customer.name} has already rented {current_dvd.name}"
            elif current_dvd.is_rented:
                return f"DVD is already rented"
            elif current_dvd.age_restriction > current_customer.age:
                return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
            current_dvd.is_rented = True
            current_customer.rented_dvds.append(current_dvd)
            return f"{current_customer.name} has successfully rented {current_dvd.name}"


    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id]
        dvd = [d for d in self.dvds if d.id == dvd_id]
        if customer:
            customer = customer[0]
        if dvd:
            dvd = dvd[0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"


    def __repr__(self):
        result = ""
        for i in range(1,len(self.customers)+1):
            result += f"{self.customers[i-1]}\n"
        for i in range(1,len(self.dvds)+1):
            result += f"{self.dvds[i-1]}\n"
        return result