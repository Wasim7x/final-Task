import os
import sys
import yaml
from pathlib import Path
sys.path[0] = str(Path(__file__).parent.parent)

from .__init__ import *
from notification_summarizer.constants.__init__ import *
from utils.read_config import ReadConfigs
from notification_summarizer.summarizer_input import SummarizerInput
from notification_summarizer.summarizer_output import SummarizerOutput

class NotificationSummarizer:
    def __init__(self, config_file):
        config = ReadConfigs().read_yaml(config_file)
        self.model = config['MODEL']
    
    def summarize_notification(self, request: SummarizerInput) -> SummarizerOutput:
        tokenizer = AutoTokenizer.from_pretrained(self.model)
        summarizer_model = AutoModelForSeq2SeqLM.from_pretrained(self.model)

        notifications = request.get_notifications()
        response = SummarizerOutput()
        
        for notification in notifications.values():
            input_ids = tokenizer(f"summarize: {notification}", return_tensors='pt').input_ids
            outputs = summarizer_model.generate(input_ids)
            summarized_notification = tokenizer.decode(outputs[0], skip_special_tokens=True)

            response.summarizer_output(summarized_notification)

        return response