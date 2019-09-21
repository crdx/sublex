import sublime_plugin
import os

class PatternExcluder:
    @staticmethod
    def get_patterns(file):
        file_patterns = []
        folder_patterns = []

        for pattern in open(file):
            pattern = pattern.strip()

            if len(pattern) == 0 or pattern[0] == '#':
                continue

            # Trailing slash determines if this is is a folder
            if (pattern[-1] == os.sep):
                # Strip leading slash now too if it exists
                if pattern[0] == os.sep:
                    pattern = pattern[1:]
                folder_patterns.append(pattern[:-1])
            else:
                file_patterns.append(pattern)

        return [file_patterns, folder_patterns]

    @staticmethod
    def refresh_by_view(view):
        PatternExcluder(view.window()).refresh()

    def __init__(self, window):
        self.window = window
        self.load_project_data()

    def refresh(self):
        self.add_all_patterns()
        self.save_project_data()

    def load_project_data(self):
        self.project_data = self.window.project_data()

    def save_project_data(self):
        if self.project_data:
            self.window.set_project_data(self.project_data)

    def add_all_patterns(self):
        if self.project_data:
            self.add_patterns_from_file('.gitignore')

    def add_patterns_from_file(self, file_name):
        for folder in self.project_data['folders']:
            file = os.path.join(folder['path'], file_name)
            if (os.path.exists(file)):
                file_patterns, folder_patterns = self.get_patterns(file)
                folder['file_exclude_patterns'] = file_patterns
                folder['folder_exclude_patterns'] = folder_patterns

class Watcher(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        PatternExcluder.refresh_by_view(view)

    def on_post_save_async(self, view):
        file_name = os.path.basename(view.file_name())
        if file_name == '.gitignore':
            PatternExcluder.refresh_by_view(view)

class RefreshExcludedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        PatternExcluder.refresh_by_view(self.view)
