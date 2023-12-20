import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Загрузка данных
data = pd.read_excel("Data1.xlsx", sheet_name="LOANS_1_code")

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(data[
                                                        ['Возраст', 'Иждивенцы', 'Доход', 'Срок проживания',
                                                         'Недвижимость',
                                                         'Благонадежный заемщик'
                                                         ]], data['Благонадежный заемщик'],
                                                    test_size=0.2)

# Масштабирование данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучение модели
model = LogisticRegression() # solver='lbfgs', max_iter=1000
model.fit(X_train, y_train)

# Оценка качества модели на тестовой выборке
y_pred = model.predict(X_test)

# Расчет чувствительности и специфичности
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
sensitivity = confusion_matrix[1, 1] / np.sum(confusion_matrix[1, :])
specificity = confusion_matrix[0, 0] / np.sum(confusion_matrix[0, :])
print('чувствительность:', sensitivity)
print('специфичность:', specificity)

# Оценка качества модели
score = model.score(X_test_scaled, y_test)

# Вывод AUC
print('AUC:', score)


