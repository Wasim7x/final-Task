import yaml
from utils.read_config import ReadConfigs
class NotificationInput:
    def __init__(self, notification_path):
        self.notification_path = notification_path
        self.notifications = {"notifications": []}
    
    def get_notifications(self ):
        notifications = ReadConfigs().read_yaml(self.notification_path)

        for key, value in notifications.items():
            self.notifications[key] = value
            
        return self.notifications