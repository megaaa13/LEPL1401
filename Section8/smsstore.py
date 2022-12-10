class SMS_Store:
    def __init__(self):
        self.inbox = []
        pass

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.inbox.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        unread = []
        for i, sms in enumerate(self.inbox):
            if not sms[0]:
                unread.append(i)
        return unread

    def get_message(self, i):
        try:
            return self.inbox[i][1], self.inbox[i][2], self.inbox[i][3]
        except:
            return None

    def delete(self, i):
        try:
            self.inbox.remove(self.inbox[i])
        except:
            pass

    def clear(self):
        self.inbox.clear()
