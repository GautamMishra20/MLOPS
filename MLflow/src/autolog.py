import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import dagshub
dagshub.init(repo_owner='GautamMishra20', repo_name='MLOPS', mlflow=True)


mlflow.autolog()

# set mlflow  tracking URI
mlflow.set_tracking_uri("https://dagshub.com/GautamMishra20/MLOPS.mlflow")

# Create or use an existing experiment
mlflow.set_experiment("RandomForest_wine_classification-2")


# Load wine datasets
wine = load_wine()
X = wine.data
y = wine.target

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.10,
    random_state=42
)

# Model Parameters
params = {
    'max_depth':10,
    'n_estimators':5
}


with mlflow.start_run(run_name="RandomForest-wine-autolog"):
    
    # That's the mlflow autolog() for logging the details.
    # mlflow.autolog() 
    
    # Train Model
    rf = RandomForestClassifier(
        **params,
        random_state=42
    )
    
    rf.fit(X_train,y_train)
    
    # Predictions
    y_pred = rf.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Log Matrics
    mlflow.log_metric('accuracy', accuracy)
    
    # Log Parameters
    mlflow.log_params(params)
    
    # Log Model
    mlflow.sklearn.log_model(
        sk_model=rf,
        artifact_path="random_forest_model"
    )

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Purples",
        xticklabels=wine.target_names,
        yticklabels=wine.target_names
    )

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # Save Plot
    plot_path = "confusion-matrix.png"
    plt.savefig(plot_path)
    plt.close()

    # Log Artifacts
    mlflow.log_artifact(plot_path)

    # Log Current Source Code File
    mlflow.log_artifact(__file__)

    print(f"Accuracy: {accuracy:.4f}")
    
    # Tags
    mlflow.set_tags(
        {
            'Author':'Ravi',
            'Project':'Random forest wine classifcation!!!'
        }
    )
     

print("MLflow Run Completed Successfully!")