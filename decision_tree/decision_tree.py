import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Загрузка данных
data = pd.read_excel('Data 3 with codes.xls')


data['Profit_of_the_client'] = data['Profit_of_the_client'].astype(int)

# Разделение данных на признаки (X) и целевую переменную (y)
X = data.drop("Default", axis=1)
y = data["Default"]

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели дерева решений
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Вывод результатов
print(f'Точность: {accuracy}')
print(f'Отчет о классификации: {classification_rep}')

plt.figure(figsize=(20, 10))
plot_tree(model, filled=True, feature_names=X_train.columns, class_names=['Not Default', 'Default'], rounded=True)
plt.show()