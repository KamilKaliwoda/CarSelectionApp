import pandas as pd
from typing import Tuple, List
import openpyxl as op
import numpy as np

# Loading database from .xlsx file.

def load_database():
    wb_obj = op.load_workbook("Baza_samochodow.xlsx")
    ws = wb_obj['Arkusz1']
    data = ws.values
    index = next(data)[0:]
    df = pd.DataFrame(data, columns = index)
    return df

# Translators are very useful in ranking calculation. They can be modified at choice.

priority_translator = {'Rocznik': 'higher', 'Cena': 'lower', 'Przebieg': 'lower', 'Moc silnika': 'higher', 'Pojemność silnika': 'higher', \
    'Spalanie': 'lower', 'Masa': 'lower', 'Paliwo': 'dependable', 'Ilość drzwi': 'higher', 'Ilość miejsc': 'higher', 'Pojemność bagażnika': 'higher', \
    'Skrzynia biegów': 'automat', 'Klimatyzacja': 'higher', 'Gwarancja': 'higher', 'Opinia': 'higher'}

weights_translator = {'Rocznik': 0.089, 'Cena': 0.089, 'Przebieg': 0.089, 'Moc silnika': 0.067, 'Pojemność silnika': 0.067, \
    'Spalanie': 0.089, 'Masa': 0.067, 'Paliwo': 0.089, 'Ilość drzwi': 0.044, 'Ilość miejsc': 0.044, 'Pojemność bagażnika': 0.067, \
    'Skrzynia biegów': 0.044, 'Klimatyzacja': 0.067, 'Gwarancja': 0.044, 'Opinia': 0.044}

# The class Ranking stores informations about database and actual ranking. It contains methods to calculate and returns car ranking based on wages
# and other criteria.

class Ranking:
    def __init__(self, original_data: pd.DataFrame, fuel_preference: str):
        self.original_data = original_data
        self.criteria = original_data.drop(original_data.columns[[0]], axis=1)
        self.names = original_data['Marka i Model']
        self.fuel_preference = fuel_preference
        self.is_higher_better = []
        self.columns = original_data.columns[1:]
        self.weights = []
        self.ideal_values = []
        self.antyideal_values = []
        self.ranking = pd.DataFrame()
        self.result_ranking = pd.DataFrame()

    # Calculates the best and the worst value for each criteria.

    def initialize_max_and_min_vals(self):
        for index, name in enumerate(self.columns):
            if self.is_higher_better[index]:
                self.ideal_values.append(self.criteria[name].max())
                self.antyideal_values.append(self.criteria[name].min())
            else:
                self.ideal_values.append(self.criteria[name].min())
                self.antyideal_values.append(self.criteria[name].max())
    
    # Converts categorical value to numerical equivalents.

    def prepare_data(self):
        for name in self.columns:
            if name == 'Skrzynia biegów':
                self.criteria.loc[self.criteria["Skrzynia biegów"] == 'Automatyczna', "Skrzynia biegów"] = 1
                self.criteria.loc[self.criteria["Skrzynia biegów"] == 'Manualna', "Skrzynia biegów"] = 0
            elif name == 'Paliwo':
                if self.fuel_preference == 'Benzyna':
                    self.criteria.loc[self.criteria["Paliwo"] == 'Benzyna', "Paliwo"] = 1
                    self.criteria.loc[self.criteria["Paliwo"] == 'Diesel', "Paliwo"] = 0
                elif self.fuel_preference == 'Diesel':
                    self.criteria.loc[self.criteria["Paliwo"] == 'Diesel', "Paliwo"] = 1
                    self.criteria.loc[self.criteria["Paliwo"] == 'Benzyna', "Paliwo"] = 0
        self.criteria = self.criteria.astype(float)
    
    # Adds weigths. If sum of weights is not 1, weights are scaled.

    def add_weights(self):
        for name in self.columns:
            self.weights.append(weights_translator[name])
        if sum(self.weights) != 1:
            sum_weights = sum(self.weights)
            for index, weights in enumerate(self.weights):
                self.weights[index] = weights / sum_weights

    def initialize_arrays(self):
        for name in self.columns:
            if priority_translator[name] == 'higher':
                self.is_higher_better.append(True)
            elif priority_translator[name] == 'lower':
                self.is_higher_better.append(False)
            else:
                self.is_higher_better.append(True)
        self.prepare_data()
        self.initialize_max_and_min_vals()
        self.add_weights()
    
    # Scales values according to their own weights.

    def scale_values_by_weights(self):
        for index, name in enumerate(self.columns):
            self.criteria[name] = ((self.criteria[name] - self.antyideal_values[index]) / (self.ideal_values[index] - self.antyideal_values[index])) * self.wages[index]

    # Summarise values for each row in order to obtain ranking rate.

    def sum_values(self):
        self.summary = pd.DataFrame({'Wynik': self.criteria.sum(axis=1)})

    def create_result_dataframe(self):
        self.names = pd.DataFrame({'Marka i model': self.names})
        self.ranking = self.original_data
        self.ranking['Wynik'] = self.summary

    # Merges all previous methods in order to creates result ranking.

    def create_ranking(self):
        self.initialize_arrays()
        self.scale_values_by_weights()
        self.sum_values()
        self.create_result_dataframe()
        self.ranking = self.ranking.sort_values(by="Wynik", ascending=False)
    
    def return_result_ranking(self, n_rows: int) -> pd.DataFrame:
        self.result_ranking = self.ranking.drop(self.ranking.columns[[-1]], axis=1)
        return self.result_ranking.head(n_rows)
    
    def return_result_ranking_marks(self, n_rows: int) -> pd.DataFrame:
        return self.ranking.head(n_rows)

# Equivalent of previous class Ranking, but here takes only three criteria into account.

class RankingThreeCriteria(Ranking):
    def __init__(self, original_data: pd.DataFrame, three_criteria: list):
        super().__init__(original_data, 'Unavailable')
        self.criteria = original_data[three_criteria]
        self.columns = original_data[three_criteria].columns
    
    def return_result_ranking(self, n_rows: int) -> pd.DataFrame:
        criteria_names = self.columns.to_list()
        criteria_names.insert(0, 'Marka i Model')
        self.result_ranking = self.ranking[criteria_names]
        return self.result_ranking.head(n_rows)

# Uses class Ranking and returns result DataFrame in order to display on GUI.

def get_UTA_ranking_all_criteria(fuel_preference: str, n_rows: int) -> pd.DataFrame:
    ranking = Ranking(load_database(), fuel_preference)
    ranking.create_ranking()
    return ranking.return_result_ranking(n_rows)

# Equivalent of previous method but here for three criteria. Returns also points in order to display on chart.

def get_UTA_ranking_three_criteria(criteria: list, n_rows: int):
    ranking = RankingThreeCriteria(load_database(), criteria)
    ranking.create_ranking()
    result_ranking = ranking.return_result_ranking(n_rows)
    result_ranking.values 
    return result_ranking, [result_ranking.drop(result_ranking.columns[[0]], axis=1).values.tolist()]

# Returns also ranking rate in final DataFrame.

def get_UTA_ranking_all_criteria_marks(fuel_preference: str, n_rows: int) -> pd.DataFrame:
    ranking = Ranking(load_database(), fuel_preference)
    ranking.create_ranking()
    return ranking.return_result_ranking_marks(n_rows)


