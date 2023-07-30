class binary_classification_regression:
    def excecute_regression(X,y):
        import pandas as pd 
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)
        from sklearn.metrics import accuracy_score
        from sklearn.pipeline import Pipeline
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.svm import LinearSVC
        from sklearn.linear_model import LogisticRegression, SGDClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.svm import SVC
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
        from sklearn.naive_bayes import GaussianNB
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
        from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
        from xgboost import XGBClassifier
        classifiers = [
                        LogisticRegression(),
                        LinearSVC(),
                        KNeighborsClassifier(10),
                        SVC(kernel="linear"),
                        DecisionTreeClassifier(),
                        RandomForestClassifier(),
                        XGBClassifier(),
                        # AdaBoostClassifier(),
                        SGDClassifier(),
                        # GradientBoostingClassifier(),
                        # GaussianNB(),
                        # LinearDiscriminantAnalysis(),
                        # QuadraticDiscriminantAnalysis()
                        ]
        log_cols=["Classifier", "Accuracy", "Log Loss"]
        log = pd.DataFrame(columns=log_cols)

        for clf in classifiers:
            text_clf = Pipeline([('tfidf', TfidfVectorizer()),('clf', clf),])
            text_clf.fit(X_train, y_train) 
            name = clf.__class__.__name__
            
            print("="*30)
            print(name)
        
            print('****Results****')
            train_predictions = text_clf.predict(X_test)
            acc = accuracy_score(y_test, train_predictions)
            print("Accuracy: {:.4%}".format(acc))
            
            # ll = 0
            
            # log_entry = pd.DataFrame([[name, acc*100,ll]], columns=log_cols)
            # log = log.append(log_entry)
            
        print("="*30)
