import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QListWidget,
    QTextEdit,
    QPushButton,
    QLabel,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from settings import Settings, MODS_FOLDER
from mod_manager import ModManager
from mod_loader import ModLoader


class ModLoaderApp(QWidget):

    def __init__(self):

        super().__init__()

        self.settings = Settings.load()
        self.settings.generate()

        self.mod_manager = ModManager(MODS_FOLDER)
        self.mod_manager.discover()

        self.selected_mod = None

        self.setup_ui()

        if not self.settings.exe_target:
            self.select_game_exe()

        self.populate_mods()

    def setup_ui(self):

        self.setWindowTitle("Imperial Glory Mod Loader")
        self.resize(700, 450)

        # LEFT PANEL
        self.mod_list = QListWidget()
        self.mod_list.currentRowChanged.connect(self.mod_selected)

        # RIGHT PANEL
        self.title_label = QLabel("Select a mod")
        self.info_box = QTextEdit()
        self.info_box.setReadOnly(True)

        # BUTTONS
        self.select_exe_button = QPushButton("Select Game EXE")
        self.select_exe_button.clicked.connect(self.select_game_exe)

        self.launch_button = QPushButton("Launch Mod")
        self.launch_button.clicked.connect(self.launch_selected_mod)

        # RIGHT LAYOUT
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.title_label)
        right_layout.addWidget(self.info_box)
        right_layout.addWidget(self.select_exe_button)
        right_layout.addWidget(self.launch_button)

        # MAIN LAYOUT
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.mod_list, 1)
        main_layout.addLayout(right_layout, 2)

        self.setLayout(main_layout)

    def populate_mods(self):

        self.mod_list.clear()

        for mod in self.mod_manager.mods:
            self.mod_list.addItem(mod.name)

    def mod_selected(self, index):

        if index < 0:
            return

        mod = self.mod_manager.mods[index]
        self.selected_mod = mod

        self.title_label.setText(mod.name)

        info = (
            f"Author: {mod.author}\n"
            f"Version: {mod.version}\n\n"
            f"{mod.description}"
        )

        self.info_box.setText(info)

    def select_game_exe(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Imperial Glory EXE",
            "",
            "Executable (*.exe)"
        )

        if not file_path:
            return

        self.settings.exe_target = file_path
        self.settings.generate()
        self.settings.save()

    def launch_selected_mod(self):

        if not self.selected_mod:
            QMessageBox.warning(self, "Error", "No mod selected")
            return

        if not self.settings.exe_target:
            QMessageBox.warning(self, "Error", "No game executable selected")
            return

        try:

            loader = ModLoader(
                Path(self.settings.game_folder_path)
            )

            loader.install_mod(self.selected_mod.path)
            loader.launch_game(self.settings.exe_target)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


def main():

    app = QApplication(sys.argv)

    window = ModLoaderApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()