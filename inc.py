
import re
from datetime import datetime
import sqlite3 as sql

# Regex for ios exports: [DD.MM.YY, HH:MM:SS]
regex_ios = r"^(?:\u200E|\u200F)*\[?(\d{1,4}[-/.] ?\d{1,4}[-/.] ?\d{1,4})[,.]? \D*?(\d{1,2}[.:]\d{1,2}(?:[.:]\d{1,2})?)(?: ([ap]\.? ?m\.?))?\]?(?: -|:)? (.+?): (?:\u200E|\u200F)*([\s\S]*)"

def chat_converter(data):
    messages = iter(data.splitlines())
    msg_list = []

    for msg in messages:
        if re.match(regex_ios, msg):
            message = re.match(regex_ios, msg).group(1, 2, 4, 5)
            timestamp = ' '.join(message[0:2])
            date_time = datetime.strptime(timestamp, '%d.%m.%y %H:%M:%S')
            msg_list.append([date_time, message[2], message[3]]) # Adds data to chats_list.
        else:
            msg_list[-1][2] += msg

    return msg_list