import os
import sys
import yaml
from pathlib import Path
sys.path[0] = str(Path(__file__).parent.parent)

from notification_clustering.__init__ import *
from notification_clustering.constants.__init__ import *
from utils.read_config import ReadConfigs
from notification_clustering.notification_input import NotificationInput
from notification_clustering.notification_output import NotificationOutput

class NotificationClassifier:
    def __init__(self, config_file):
        config = ReadConfigs().read_yaml(config_file)
        self.vocabulary_size = config['vocabulary_size']
        self.num_clusters = config['num_clusters']
    
    def cluster_notification(self, request: NotificationInput) -> NotificationOutput:
        notifications = request.get_notifications()
    
        df = pd.DataFrame(notifications)
        column = df.columns.values

        vectorizer =TfidfVectorizer(analyzer="word", max_features=self.vocabulary_size, stop_words="english", ngram_range=(1,2))
        X = vectorizer.fit_transform(df[column[0]].values)

        # Retrieve the sentence of our example dataset most similar to some test sentences
        test_sentences = ["How to put an alpaca to sleep", "How to achieve a deep sleep"]
        test_data = vectorizer.transform(test_sentences)

        km = KMeans(n_clusters= self.num_clusters)
        km.fit(X)

        df["label"] = km.predict(X)
        
        clustered_notification = {}
        for index, row in df.iterrows():
            if row["label"] not in clustered_notification:
                clustered_notification[row["label"]] = [row[column[0]]]
            else:
                clustered_notification[row["label"]].append(row[column[0]])

        response = NotificationOutput()
        response.notification_output(clustered_notification)

        return response