import numpy as np
from copy import deepcopy
from find_undominated import undominated
from RSM_Class import Point


# Przenumerowanie klas
def renumerate_class(my_class, class_number):

    for point in my_class:

        point.class_number = class_number


# Wyznaczenie klsy punktów niezdominowanych
def find_class(set_of_points, class_number):

    my_class = undominated(set_of_points)

    for point in my_class:

        point.class_number = class_number

    return my_class


# Wyznaczenie zbiorów odniesienia
def find_classes(set_of_points):

    renumerate_class(set_of_points, 0)

    class_number = 1
    my_classes = list()
    
    while True:

        my_class = find_class(set_of_points, class_number)
        
        if len(my_class) == 0:
        
            break
        
        my_classes.append(my_class)
        class_number += 1

    first_class = my_classes[0] 
    last_class = list()
    decision_class = list()

    if len(my_classes) >= 3:
    
        last_class = my_classes[-1]
                
        for point in set_of_points:

            if point.class_number != 1 and point.class_number != last_class[0].class_number:
                
                decision_class.append(point)

        decision_class = np.array(decision_class)
        renumerate_class(decision_class, 2)
        renumerate_class(last_class, 3)

    return first_class, decision_class, last_class


# Wyznaczenie punktów idealnego i antyidealnego
def imaginary(set_of_points):

    ideal = list()
    antyideal = list()

    for criterium in range(len(set_of_points[0].criteria)):

        minimum = np.inf
        maximum = 0

        for point in set_of_points:

            if point.criteria[criterium] < minimum:

                minimum = point.criteria[criterium]

            elif point.criteria[criterium] > maximum:

                maximum = point.criteria[criterium]

        ideal.append(minimum)
        antyideal.append(maximum)

    ideal = np.array(ideal)
    antyideal = np.array(antyideal)

    return ideal, antyideal


# Wynzaczenie zbiorów odniesienia gdy nie da się wyznaczyć trzech klas
def create_class(set_of_points, index):

    criteries_translator = {'Rocznik': 0, 'Cena': 1, 'Przebieg': 2, 'Moc silnika': 3, 'Pojemność silnika': 4, \
        'Spalanie': 5, 'Masa': 6, 'Paliwo': 7, 'Ilość drzwi': 8, 'Ilość miejsc': 9, 'Pojemność bagażnika': 10, \
        'Skrzynia biegów': 11, 'Klimatyzacja': 12, 'Gwarancja': 13, 'Opinia': 14}

    decision_criteries = ["Rocznik", "Cena", "Przebieg", "Moc silnika", "Pojemność silnika", "Spalanie", "Masa", \
        "Pojemność bagażnika", "Opinia"]

    scale = 0.25
    [ideal, antyideal] = imaginary(set_of_points)
    distance = antyideal - ideal
    
    set_of_points.append(Point(ideal, 'Ideal'))
    set_of_points.append(Point(antyideal, 'Antyideal'))

    for criterium1 in index[:-1]:

        for criterium2 in index[:-1]:
            
            if criterium1 != criterium2:
        
                ideal_copy = deepcopy(ideal)
                antyideal_copy = deepcopy(antyideal)

                if (criterium1 in decision_criteries) and (criterium2 in decision_criteries):
                    
                    ideal_copy[criteries_translator[criterium1]] -= scale*distance[criteries_translator[criterium1]]
                    ideal_copy[criteries_translator[criterium2]] += scale*distance[criteries_translator[criterium2]]
                    set_of_points.append(Point(ideal_copy, 'Ideal'))

                    antyideal_copy[criteries_translator[criterium1]] += scale*distance[criteries_translator[criterium1]]
                    antyideal_copy[criteries_translator[criterium2]] -= scale*distance[criteries_translator[criterium2]]
                    set_of_points.append(Point(antyideal_copy, 'Antyideal'))