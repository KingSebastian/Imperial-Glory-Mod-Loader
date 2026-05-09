from pathlib import Path
from mod import Mod


class ModManager:

    def __init__(self, mods_folder: Path):
        self.mods_folder = mods_folder
        self.mods = []

    def discover(self):

        self.mods.clear()

        if not self.mods_folder.exists():
            self.mods_folder.mkdir(parents=True)

        for folder in self.mods_folder.iterdir():

            if not folder.is_dir():
                continue

            try:
                mod = Mod.load(folder)
                self.mods.append(mod)

            except Exception as e:
                print(f"Failed to load mod '{folder.name}': {e}")