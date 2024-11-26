# import dependencies for clustering module
from notification_clustering.__init__ import *
from notification_clustering.constants.__init__ import *
from notification_clustering.notification_input import NotificationInput
from notification_clustering.notification_classifier import NotificationClassifier

# import dependencies for summarizer module
from notification_summarizer.__init__ import *
from notification_summarizer.constants.__init__ import *
from notification_summarizer.summarizer_input import SummarizerInput
from notification_summarizer.notification_summarizer import NotificationSummarizer


from utils.read_config import ReadConfigs

class MainPipeline:
    def __init__(self):
        pass

    def classify_notification(self):
        clusteringObj = NotificationClassifier(CONFIG_FILE_PATH)
        notification_input_path = INPUT_PATH
        claasifier_input = NotificationInput(notification_input_path)
        clustered_notifications = clusteringObj.cluster_notification(claasifier_input)
        return clustered_notifications
    
    def summarize_notification(self):
        summarizerObj = NotificationSummarizer(CONFIG_FILE_PATH)
        notification_input_path = INPUT_PATH
        summarizer_input = NotificationInput(notification_input_path)
        summarized_notifications = summarizerObj.summarize_notification(summarizer_input)
        return summarized_notifications
    
def run_main_pipeline():
    main_pipeline_obj = MainPipeline()
    
    # Run clustering
    clustered_notifications = main_pipeline_obj.classify_notification()
    print(clustered_notifications.clustered_notification)
    
    # Run summarizer
    summarized_notifications = main_pipeline_obj.summarize_notification()
    print(summarized_notifications.summarized_notification[0])

if __name__ == "__main__":
    run_main_pipeline()