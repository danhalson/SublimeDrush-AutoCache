import sublime
import sublime_plugin
import subprocess

# TODO: Use PATH to find drush (preferably cross platform method?)
# TODO: Menu Item
# TODO: Define default settings ala ST3 readonly ones

''' SublimeDrush: Parent Class '''

class SublimeDrush():

    # Init class vars
    name = "SublimeDrush AutoCache"
    cmd_name = ""
    drush_path = ""
    file_types = []
    working_dir = ""
    proceed = False

    ''' Retrieve and initialise settings '''
    def init_settings(self, view):

        # Load the settings file
        global_settings = sublime.load_settings("sublimedrush.sublime-settings")

        self.drush_path = global_settings.get("drush_path")
        self.allowed_types = global_settings.get("allowed_types")
        self.output_type = global_settings.get("output_type")

        # If option is set use project settings, else if set use global settings
        if sublime.active_window().active_view().settings().get("sublimedrush").get("drush_working_dir"):
            self.working_dir = sublime.active_window().active_view().settings().get("sublimedrush").get("drush_working_dir")
        elif global_settings.get("drush_working_dir"):
            self.working_dir = global_settings.get("drush_working_dir")

        # If current file type in allowed list, proceed - is determined by syntax type e.g. Python.tmLanguage
        for allowed_type in self.allowed_types:
            current_type = view.settings().get('syntax').split('/')[2]
            if (allowed_type + '.tmLanguage') == current_type:
                self.proceed = True
                break


    ''' Run commands '''
    def run_cmd(self, command):

        try:
            proc = subprocess.Popen(
                command, bufsize=0,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                universal_newlines=True, shell=True, cwd=self.working_dir)
            return proc
        except FileNotFoundError:
            sublime.error_message(self.name + ": Please check your working directory")

    ''' Print output '''
    def trace(self, proc):
        lines = []

        # Read the output into a variable
        while proc.poll() is None:
            # Read output
            line = proc.stdout.readline()
            if line:
                lines.append(line)

        return lines


''' Drush Cache; inherits SublimeDrush '''

class SublimeDrushCC(sublime_plugin.EventListener, SublimeDrush):

    # Event called after save
    def on_post_save_async(self, view):

        self.init_settings(view)

        if (self.proceed):
            # view.run_command('show_overlay', {"overlay": "command_palette", "text": "Your text here..." })
            sublime.status_message(self.name + ": Clearing...")
            proc = self.run_cmd([self.drush_path + " " + "cc all"])
            status = self.trace(proc)

            # Output confirmation dialog
            if (self.output_type == 1):
                sublime.status_message(self.name + ": Cleared")
            elif (self.output_type == 2):
                view.window().show_quick_panel(status, None, sublime.MONOSPACE_FONT)
