import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import time

df = pd.read_csv("./Iris.csv")
df.drop(columns=['Id'], axis=1, inplace=True)

label_encoder = preprocessing.LabelEncoder().fit(df.Species)
df['Species'] = label_encoder.transform(df.Species)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['Species'], axis=1), df.loc[:, 'Species'].values, 
                                                    test_size=0.2, shuffle=True, random_state=182)

standard_scaler = preprocessing.StandardScaler().fit(X_train)
X_train, X_test = standard_scaler.transform(X_train), standard_scaler.transform(X_test)

if __name__ == '__main__':
    print(f"X/Y train shape: {X_train.shape} {y_train.shape}")
    print(f"X/y test shape: {X_test.shape} {y_test.shape}")
    print("KNeighborsClassifier: ")
    
    param_grid = {'n_neighbors': range(1, 21 + 1),
            'weights': ['uniform', 'distance']}
    var_knn = GridSearchCV(estimator=KNeighborsClassifier(n_jobs=-1), param_grid=param_grid, 
                            cv=StratifiedKFold(n_splits=10, shuffle=True, random_state=182))
    start_time = time.time()
    var_knn.fit(X_train, y_train)   
    knn_time_taken = time.time() - start_time
    preds = var_knn.predict(X_test)
    Knn_acc = accuracy_score(y_test, preds)

    print(f"Time taken to train (with cross validation AND grid search for parameters): {knn_time_taken}s")
    print(f"Accuracy: {Knn_acc * 100}%")
    print(f"Best parameters: {var_knn.best_estimator_}")

    
    pred_dataFra = pd.DataFrame(standard_scaler.inverse_transform(X_test), columns=df.columns[:-1])
    pred_dataFra['Species'] = label_encoder.inverse_transform(y_test)
    pred_dataFra['Pred. Species'] = label_encoder.inverse_transform(preds)
    pred_dataFra['Predicted'] = [x == y for x, y in pred_dataFra[['Species', 'Pred. Species']].values]
    print(pred_dataFra)
    print("\n")
    print("Gaussian Naive Bayes Classifier:")

    gnb = GaussianNB()
    gnb_accuracies = []
    stratified_kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=182)

    for fold, (train_batch, test_batch) in enumerate(stratified_kfold.split(X_train, y_train), 1):
        x_train_batch, y_train_batch = X_train[train_batch], y_train[train_batch]
        x_test_batch, y_test_batch = X_train[test_batch], y_train[test_batch]
        gnb.fit(x_train_batch, y_train_batch)
        accuracy = accuracy_score(y_test_batch, gnb.predict(x_test_batch)) * 100
        gnb_accuracies.append(accuracy)
        print(f"Fold: {fold}, Score: {accuracy}%")

    print(f"Best Accuracy: {max(gnb_accuracies)}%")
    print(f"Accuracy over test set -> {round(accuracy_score(y_test, gnb.predict(X_test)) * 100, 2)}%")