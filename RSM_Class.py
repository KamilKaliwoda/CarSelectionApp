import numpy as np


class Point:
    id = 1

    def __init__(self, criteria, name):
        self.name = name
        self.class_number = 0
        self.criteria = criteria
        self.areas = []
        self.d_left = []
        self.d_right = []
        self.score = 0
        self.id = Point.id
        Point.id = Point.id + 1


    # Oblicza wartość funkcji scoringowej 
    def calculate_score(self):

        self.normalize()
        score = 0

        for area in range(len(self.areas)):

            score += (self.d_right[area] / (self.d_left[area] + self.d_right[area])) * self.areas[area]

        self.score = score


    # Normalizuje wartości pól i odległości
    def normalize(self):
        
        sum_of_areas = sum(self.areas)
        sum_of_d_left = sum(self.d_left)
        sum_of_d_right = sum(self.d_right)

        for area in range(len(self.areas)):

            self.areas[area] /= sum_of_areas
            self.d_left[area] /= sum_of_d_left
            self.d_right[area] /= sum_of_d_right


    # Oblicza odległości od rogów "prostokąta"
    def calculate_d(self, coordinates1, coordinates2):

        d_left = 0
        d_right = 0

        for co in range(len(self.criteria)):

            d_left += (self.criteria[co] - coordinates1[co])**2
            d_right += (self.criteria[co] - coordinates2[co])**2

        self.d_left.append(np.square(d_left))
        self.d_right.append(np.square(d_right))


class Rectangular:
    id = 1

    def __init__(self, coordinates1, coordinates2):

        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2
        self.area = 0
        self.id = Rectangular.id
        Rectangular.id = Rectangular.id + 1

    # Oblicza pole stworzonego "prostokąta"
    def calculate_area(self):

        area = 1

        for co in range(len(self.coordinates1)):

            area *= abs(self.coordinates1[co] - self.coordinates2[co])

        self.area = area



if __name__ == '__main__':
    pass