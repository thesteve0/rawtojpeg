from pathlib import Path

from DuplicateCleaner import look_for_duplicates

#search_path = 'C:/Users/steve/tmp\photo-rename-tester/orig-images'
search_path = 'D:/pictures-for-AI/to-process'
#search_path = 'P:/'
top_path = Path(search_path)

look_for_duplicates(top_path)