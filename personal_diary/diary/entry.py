import datetime

class DiaryEntry:
    """Represents a single entry in the diary."""
    def __init__(self, title, content, date=None):
        self.title = title
        self.content = content
        self.data = date or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        """User-friendly string representation of the entry."""
        return f"Date: {self.date}\nTitle: {self.title}\n\n{self.content}"

    def to_dict(self):
        """Converts the entry to a dictionary for JSON serialization."""
        return {'date': self.date, 'title': self.title, 'content': self.content}
    
    @staticmethod
    def from_dict(data_dict):
        """Creates a DiaryEntry object from a dictionary."""
        return DiaryEntry(data_dict['title'], data_dict['content'], data_dict['date'])