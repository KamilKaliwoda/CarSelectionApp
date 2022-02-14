import numpy as np
import pandas as pd
from RSM_Class import Rectangular


def calculate_rectangulars(set_of_points):
    
    # Stworzenie prostokątów
    set_of_rectangulars = list()

    for point1 in set_of_points:

        if point1.class_number == 1:   

            for point2 in set_of_points:

                if point2.class_number == 3:

                    rectangular = Rectangular(point1.criteria, point2.criteria)
                    rectangular.calculate_area()
                    set_of_rectangulars.append(rectangular)


    for point in set_of_points:

        for rectangular in set_of_rectangulars:

            if (point.criteria >= rectangular.coordinates1).all and (point.criteria <= rectangular.coordinates2).all:
            
                point.areas.append(rectangular.area)
                point.calculate_d(rectangular.coordinates1, rectangular.coordinates2)

    for point in set_of_points:

        if point.class_number == 2:

            point.calculate_score()


# Wyznaczenie rankingu
def create_ranking(set_of_points, original_data, added_points, n_max):

    score_list = list()

    for point in set_of_points:

        if not added_points:

            score_list.append(point.score)

        else:

            if point.class_number == 2:

                score_list.append(point.score)

    original_data['Score'] = score_list
    ranking = original_data.sort_values(by=['Score'], ascending=False)
    # Wycięcie scoore'a
    ranking = ranking.iloc[:n_max, :-1]
    # ranking = ranking.iloc[:n_max, :]

    return ranking


def list_of_list_of_list(original_data, database, first_class, last_class, ranking, index, n_max):

        class_list = list()
        first_class_list = list()
        last_class_list = list()

        # Dodanie do listy decyzji
        decision_sorted_class_list = ranking[index].values
        decision_sorted_class_list = np.ndarray.tolist(decision_sorted_class_list[:n_max])
        
        class_list.append(list(decision_sorted_class_list))

        # Dodanie do listy punktów pierwszej klasy
        for point in first_class:

            for iter in range(len(database)):

                if point.name == original_data.values[iter, 0] and (point.criteria == database[iter, 1:]).all:

                    first_class_list.append((original_data.values[iter, 1:-1]).tolist())

                    break
        
        class_list.append(first_class_list)

        # Dodanie do listy punktów ostatniej klasy

        for point in last_class:

            for iter in range(len(database)):

                if point.name == original_data.values[iter, 0] and (point.criteria == database[iter, 1:]).all:

                    last_class_list.append((original_data.values[iter, 1:-1]).tolist())
                    
                    break

        class_list.append(last_class_list)

        return class_list