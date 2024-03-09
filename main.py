from DataGenerator import DataGenerator
from Prediction import Model

# Генеруємо випадкові дані
New_data_generator = DataGenerator()
data = New_data_generator.get_generated_data()

# Використовуємо дані на моделі передбачення
New_prediction_model = Model(data)
New_prediction_model.predict()

