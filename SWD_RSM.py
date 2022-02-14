from queue import Empty
import numpy as np
import pandas as pd
from RSM_Class import Point
from find_undominated import load_database
from find_classes import find_classes, create_class
from calculate_score import calculate_rectangulars, create_ranking, list_of_list_of_list


def rsm(criteria, prioritize_diesel, n_max):

    #prioritize_diesel = False
    # criteria = ["Rocznik", "Cena", "Spalanie"]
    #criteria = []
    cols_to_maximize = ["Rocznik", "Moc silnika", "Pojemność silnika", "Ilość drzwi", "Ilość miejsc", \
                    "Pojemność bagażnika", "Klimatyzacja", "Gwarancja", "Opinia"]

    # Wczytanie bazy danych
    [original_data, database, index] = load_database(criteria, cols_to_maximize, prioritize_diesel)

    # Utworzenie listy punktów
    set_of_points = list()
    for row in range(len(database)):
        set_of_points.append(Point(database[row][1:],database[row, 0]))

    # Wyznaczanie klas 
    [first_class, decision_class, last_class] = find_classes(set_of_points)

    # Jeżeli wyznaczonych klas jest zbyt mało (mniej niż 3) to dodajemy punkty odniesienia i ponawiamy próbę ich wyznaczenia
    added_points = False
    if len(decision_class) == 0 or len(last_class) == 0:
        
        added_points = True
        create_class(set_of_points, index)
        [first_class, decision_class, last_class] = find_classes(set_of_points)

    # Wyznaczenie prostokątów, obliczenie pól, odległości, wyznaczenie wartości funkcji scooringowej
    calculate_rectangulars(set_of_points)

    # Wyznaczenie rankingu
    ranking = create_ranking(set_of_points, original_data, added_points, n_max)

    # Stworzenie listy klas na potrzeby GUI
    class_list = list_of_list_of_list(original_data, database, first_class, last_class, ranking, index, n_max)

    return ranking, class_list

# result_df = rsm([], True, 99)[0]
# print(result_df)
# result_df.to_excel("RSM.xlsx")

#criteria = ["Rocznik", "Moc silnika", "Pojemność bagażnika"]
#result_df = ranking_to_dataframe_three(criteria, 6)
#print(result_df)