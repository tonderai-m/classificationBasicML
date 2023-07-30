class do_classification: 
    def text_classification(X,y): 
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.svm import LinearSVC

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

        text_clf = Pipeline([('tfidf', TfidfVectorizer()),('clf', LinearSVC()),])
        text_clf.fit(X_train, y_train) 
        predictions = text_clf.predict(X_test) 
        return y_test, predictions