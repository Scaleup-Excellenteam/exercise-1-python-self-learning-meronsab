class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, urgent=False):
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found.")
        
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)
        
        return self.message_id
    
    def read_inbox(self, username, n=-1):
        """ 
        Read the first `n` messages for `username`.
        If `n` is not given (or -1), read all messages.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found.")
        
        if n == -1:
            return self.boxes[username]  # Return all messages
        
        return self.boxes[username][:n]  # Return the first `n` messages

    def search_inbox(self, username, search_str):
        """ 
        Return a list of all messages containing `search_str`.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' not found.")
        
        return [msg for msg in self.boxes[username] if search_str in msg['body']]

