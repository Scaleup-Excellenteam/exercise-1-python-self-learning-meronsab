class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found.")
        
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }
        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)
        
        return self.message_id
    
    def read_inbox(self, username, n=-1):
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found.")
        
        messages = self.boxes[username] if n == -1 else self.boxes[username][:n]
        for msg in messages:
            msg['unread'] = False
        return messages

    def search_inbox(self, username, search_str):
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found.")
        
        search_str = search_str.lower()
        return [msg for msg in self.boxes[username] 
                if search_str in msg['title'].lower() or search_str in msg['body'].lower()]
