# import mlflow
# print('printing tracking URI scheme below')
# print(mlflow.set_tracking_uri())
# print('\n')

# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# print("printing new tracking URI scheme below")
# print(mlflow.get_tracking_uri())
# print('\n')


import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.set_experiment("experiment-1")

# with mlflow.start_run():
#     mlflow.log_param("model", "RandomForest")
#     mlflow.log_param("n_estimators", 100)
#     mlflow.log_metric("accuracy", 0.95)

print("Logged Successfully")