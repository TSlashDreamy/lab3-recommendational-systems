import pandas as pd
import numpy as np

from config import *


class DataGenerator:
    def __init__(self):
        self.num_records = records_amount
        # Задаємо діапазон user_id та item_id
        self.user_ids = np.random.randint(1, max_users, self.num_records)
        self.item_ids = np.random.randint(1, max_items, self.num_records)
        # Генеруємо випадкові рейтинги
        self.ratings = np.random.randint(1, max_rating, self.num_records)
        # Створюємо DataFrame зі згенерованими даними
        self.df = pd.DataFrame({'user_id': self.user_ids, 'item_id': self.item_ids, 'rating': self.ratings})

    def get_generated_data(self):
        # Вивід дата фрейму
        print(self.df)
        return self.df
