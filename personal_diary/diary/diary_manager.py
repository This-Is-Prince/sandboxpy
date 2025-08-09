import json
from .entry import DiaryEntry
from .utils import logger

class DiaryManager:
    """Manages a collection of diary entries."""
    def __init__(self, filename="diary.json"):
        self.filename = filename
        self.entries = self._load_entries()

    def _load_entries(self):
        """Loads entries from the JSON file."""
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                return [DiaryEntry.from_dict(entry_data) for entry_data in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
    def _save_entries(self):
        """Saves all entries on the JSON file."""
        with open(self.filename, 'w', encoding="utf-8") as f:
            data = [entry.to_dict() for entry in self.entries]
            json.dump(data, f, indent=4)
    
    @logger
    def add_entry(self, title, content):
        """Adds a new entry and saves it."""
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        self._save_entries()
        print("Entry added successfully!")

    def list_titles(self):
        """Returns a list of all entry titles."""
        if not self.entries:
            return ["No entries yet."]
        return [f"{i+1}. {entry.title} ({entry.date})" for i, entry in enumerate(self.entries)]
    
    def get_entry(self, index):
        """Retrieves a single entry by its 1-based index."""
        if 0 <= index < len(self.entries):
            return self.entries[index]
        return None
    
    def search_entries(self, keyword):
        """A GENERATOR that yields entries containing a keyword in their title or content."""
        print(f"\n--- Searching for '{keyword}'... ---")
        found = False
        for entry in self.entries:
            if keyword.lower() in entry.title.lower() or keyword.lower() in entry.content.lower():
                yield entry
                found = True
        if not found:
            print("No matching entries found.")