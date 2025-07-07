import pytest
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

model = joblib.load("burnout_model.pkl")

sample_input = {
    "Age": 30,
    "Gender": 1,
    "YearsAtCompany": 5,
    "WorkHoursPerWeek": 45,
    "RemoteWork": 2,
    "BurnoutLevel": 6.5,
    "CommuteTime": 30,
    "HasMentalHealthSupport": 1,
    "ManagerSupportScore": 4.2,
    "HasTherapyAccess": 1,
    "MentalHealthDaysOff": 2,
    "WorkLifeBalanceScore": 6.0,
    "TeamSize": 10,
    "CareerGrowthScore": 7.5,
    "JobSatisfaction": 7.0,
    "PhysicalActivityHrs": 3.5,
    "ProductivityScore": 8.0,
    "SleepHours": 7.0,
    "StressLevel": 6.0
}


def test_model_load():
    assert model is not None


def test_prediction_format():
    df = pd.DataFrame([sample_input])[model.feature_names_in_]
    prediction = model.predict(df)[0]
    assert prediction in [0, 1]


def test_model_accuracy_threshold():

    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv")

    X_test = X_test[model.feature_names_in_]
    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    print(f"Acurácia real = {accuracy:.2f}")
    assert accuracy >= 0.80