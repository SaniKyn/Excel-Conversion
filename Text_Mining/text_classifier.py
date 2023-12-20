# Импорт необходимых библиотек
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import nltk
from nltk.corpus import stopwords
import string

# Чтение данных из файла
df = pd.read_excel("SMSSpamCollection.xlsx")

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

df['Text'] = df['Text'].str.lower()  # Приведение к нижнему регистру
df["Text"] = df["Text"].apply(lambda x: ''.join([char for char in str(x) if not char.isdigit()]))  # Удаление цифр
df['Text'] = df['Text'].apply(lambda x: ''.join([char for char in x if char not in string.punctuation]))  # Удаление пунктуации
df['Text'] = df['Text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))  # Удаление стоп-слов

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Message'], test_size=0.3, random_state=42)

# Преобразование текста в матрицу признаков с использованием CountVectorizer
vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

# Обучение модели логистической регрессии
logreg_classifier = LogisticRegression()
logreg_classifier.fit(X_train_bow, y_train)

# Обучение модели метода опорных векторов
svm_classifier = SVC(kernel='linear')  # Используем линейное ядро для SVM
svm_classifier.fit(X_train_bow, y_train)

# Предсказание на тестовой выборке
y_pred = logreg_classifier.predict(X_test_bow)

# Оценка результатов
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)


# Вывод результатов
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{classification_rep}")

print("Метод опорных векторов (SVM):")
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)