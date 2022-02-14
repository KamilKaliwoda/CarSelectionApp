import numpy as np
import pandas as pd
import openpyxl as op
from copy import deepcopy


def load_database(criteria, cols_to_maximize, prioritize_diesel):
        
        # Wczytanie z arkusza do dataframe'a
        wb_obj = op.load_workbook("Baza_samochodow.xlsx")
        ws = wb_obj['Arkusz1']
        data = ws.values
        index = next(data)[0:]
        original_data = pd.DataFrame(data, columns = index)
        df = deepcopy(original_data)

        # Zamiana stringów na wartości 
        df["Skrzynia biegów"].replace({"Automatyczna" : 0, "Manualna" : 1}, inplace=True)
        if prioritize_diesel:
            df["Paliwo"].replace({"Diesel" : 0, "Benzyna" : 1}, inplace=True)
        else:
            df["Paliwo"].replace({"Diesel" : 1, "Benzyna" : 0}, inplace=True)

        # Normalizacja i odwrócenie jeżeli maksymalizujemy
        columns = df.columns
        for col in columns:
            if col == "Marka i Model":
                continue
            norm = np.amax(df[col].values)
            if col in cols_to_maximize:
                normalized = 1 - (df[col].values / norm)
            else:
                normalized = df[col].values / norm
            df[col] = normalized

        # Wyłuskanie 3 kryteriów jeśli żądane
        if len(criteria) == 0:
            index = df.columns
            index = index[1:]
            df = df.values
            
        else:
            criteria_with_name = ["Marka i Model"] + criteria
            index = df[criteria].columns
            df = df[criteria_with_name].values
            original_data = original_data[criteria_with_name]

        return  original_data, df, index

# def find_undominated(list_of_points: np.ndarray):
#     P = []
#     dominated = []
#     size = len(list_of_points)
#     to_delete = []
#     i = 0
#     while True:
#         j = 1
#         Y = list_of_points[i]
#         while True:
#             X = list_of_points[j]
#             if all(np.less_equal(Y.criteria, X.criteria)) == True:
#                 list_of_points = np.delete(list_of_points, j)
#                 continue
#             elif all(np.less_equal(X.criteria, Y.criteria)) == True:
#                 list_of_points = np.delete(list_of_points, i)
#                 Y = X
#                 continue
#             if j == len(list_of_points) - 1:
#                 break
#             j += 1
#         P.append(Y)
#         for k in range(len(list_of_points)):
#             if all(np.less_equal(Y.criteria, list_of_points[k].criteria)):
#                 to_delete.append(k)
#         list_of_points = np.delete(list_of_points, to_delete)
#         if len(list_of_points) == 1:
#             P.append(list_of_points[0])
#             break
#         elif len(list_of_points) == 0:
#             break
    
#     return P


def undominated(data):

    appointed_class = list()
    dominated_class = list()

    for point1 in range(len(data)):

        if data[point1].class_number == 0:

            is_undominated = True
            reference = data[point1].criteria

            for point2 in range(len(data)):

                if data[point2].class_number == 0:

                    dominated_actual = 0
                    if point1 != point2:

                        actual = data[point2].criteria

                        for criterium in range(len(data[point1].criteria)):

                            if actual[criterium] <= reference[criterium]:

                                dominated_actual += 1

                    if dominated_actual == len(data[point1].criteria):

                        is_undominated = False

                        break

            if is_undominated:

                appointed_class.append(data[point1])
            else:
                dominated_class.append(data[point1])

    return np.array(appointed_class)

if __name__ =='__main__':
    pass