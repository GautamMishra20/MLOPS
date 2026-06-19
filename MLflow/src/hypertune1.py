# import mlflow
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# Load the breast cancer datasets
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target,name='target')

X_train, X_test , y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)

rf = RandomForestClassifier(
    random_state = 42
)

param_grid = {
    'n_estimators': [10,50,100],
    'max_depth': [None,10,20,30]
}

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Run without MLflow 
grid_search.fit(X_train ,y_train)

# Displaying the best params and best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(best_params)
print(best_score)
