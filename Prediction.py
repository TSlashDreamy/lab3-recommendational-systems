from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse
from pandas import DataFrame


class Model:
    def __init__(self, data_set: DataFrame):
        # Завантаження даних з DataFrame в Dataset
        self.reader = Reader(rating_scale=(1, 5))
        self.data_set = Dataset.load_from_df(data_set[['user_id', 'item_id', 'rating']], self.reader)
        # Розділення на навчальний та тестувальний набори
        self.train_set, self.test_set = train_test_split(self.data_set, test_size=0.2)
        # Побудова моделі з використанням KNN
        self.model = KNNBasic()
        # Навчання моделі на тренувальному наборі
        self.model.fit(self.train_set)

    def predict(self):
        # Прогнозування на тестовому наборі
        self.predictions = self.model.test(self.test_set)
        # Розрахунок метрик, наприклад, RMSE
        self.accuracy = rmse(self.predictions)
        print("RMSE:", self.accuracy)
