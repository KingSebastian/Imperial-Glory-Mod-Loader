from dataclasses import dataclass, asdict, field
from pathlib import Path
import json
import sys

if getattr(sys, 'frozen', False):
    MODLOADER_PATH = Path(sys.executable).resolve().parent
else:
    MODLOADER_PATH = Path(__file__).resolve().parent

MODS_FOLDER = MODLOADER_PATH / "Mods"
SETTINGS_FILE = MODLOADER_PATH / "settings.json"


@dataclass
class Settings:
    exe_target: str = ""
    game_folder_path: str = ""
    last_enabled_mods: list[str] = field(default_factory=list)

    def generate(self):
        if self.exe_target:
            self.game_folder_path = str(Path(self.exe_target).parent)

    def save(self):
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=4)

    @classmethod
    def load(cls):
        if not SETTINGS_FILE.exists():
            settings = cls()
            settings.save()
            return settings

        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(**data)