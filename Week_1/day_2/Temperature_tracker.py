import sys
class TempTracker(object):

    def __init__(self):
        
        self.occurrences = [0] * 111  
        self.max_occurrences = 0
        self.mode = None

        
        self.number_of_readings = 0
        self.total_sum = 0.0  
        self.mean = None

        
        self.min_temp = sys.maxsize -1
        self.max_temp = -sys.maxsize -1

    def insert(self, temperature):
       
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        self.number_of_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.number_of_readings

        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode