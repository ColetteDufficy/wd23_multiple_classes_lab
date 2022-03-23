class Bus:
    def __init__(self, route_num, destination):
        self.route_num = route_num
        self.destination = destination
        
    def drive_noise(self):
        return "Brum brum"