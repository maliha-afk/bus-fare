class vehicle:
    def __init__(self,capacity_seating,maintenance_charge,total_fare=55000,):
      self.capacity_seating = capacity_seating
      self.total_fare = total_fare
      self.maintenance_charge=maintenance_charge  
    
class vehicle2(vehicle):
    def __init__(self, capacity_seating,maintenance_charge, total_fare=5500,):
       super().__init__(capacity_seating,maintenance_charge, total_fare,)

    
    

bus1 =vehicle(100,5500)
bus2=vehicle2 (50,550)
print(bus1.maintenance_charge)
print(bus2.capacity_seating)
