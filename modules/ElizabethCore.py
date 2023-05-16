import modules.Constants as const
from datetime import datetime
from modules.ElizabethVoice import ElizabethVoice

class ElizabethCore:
    EliSpeak = ElizabethVoice()

    def __init__(self):
        pass

    def execute_command(self, eli_tag, speech):
        datetime_now = datetime.today()
        if eli_tag == const.date_command:
            self.EliSpeak.eli_says(datetime_now.strftime("%Y-%m-%d %I:%M %p"))
            print(datetime_now.strftime("%Y-%m-%d %I:%M %p"))
        elif eli_tag == const.hour_command:
            self.EliSpeak.eli_says("Son las " + datetime_now.strftime('%I:%M %p'))
            print("Son las " + datetime_now.strftime('%I:%M %p'))
