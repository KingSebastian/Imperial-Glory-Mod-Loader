from dataclasses import dataclass
from pathlib import Path
import json


@dataclass
class Mod:
    name: str
    author: str
    version: str
    description: str
    path: Path

    @classmethod
    def load(cls, mod_folder: Path):

        info_file = mod_folder / "mod.json"

        # Default values
        data = {
            "name": mod_folder.name,
            "author": "Unknown",
            "version": "Unknown",
            "description": "No description provided."
        }

        # Override if mod.json exists
        if info_file.exists():

            with open(info_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)

            data.update(loaded)

        return cls(
            name=data["name"],
            author=data["author"],
            version=data["version"],
            description=data["description"],
            path=mod_folder
        )