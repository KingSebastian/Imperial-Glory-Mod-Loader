from pathlib import Path
import shutil
import subprocess
import os
import stat

MOD_OVERRIDE_FOLDERS = [
    "Effects",
    "Engine",
    "Fonts",
    "Game",
    "Models",
    "Teclas",
    "Textures"
]

class ModLoader:

    def __init__(self, game_folder: Path):
        self.game_folder = game_folder

    def launch_game(self, exe_path: str):
        subprocess.Popen(
            exe_path,
            cwd=str(Path(exe_path).parent)
        )

    def force_writable(self, path: Path):

        if not path.exists():
            return

        try:
            os.chmod(path, stat.S_IWRITE)
        except Exception as e:
            print(f"Failed making writable: {path} -> {e}")

    def install_mod(self, mod_path: Path):

        self.clear_override_folders()

        files_folder = mod_path / "Files"

        source_folder = files_folder if files_folder.exists() else mod_path

        for item in source_folder.rglob("*"):

            if item.name == "mod.json":
                continue

            relative = item.relative_to(source_folder)
            destination = self.game_folder / relative

            if item.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue

            destination.parent.mkdir(parents=True, exist_ok=True)

            # REMOVE READONLY ATTRIBUTE
            self.force_writable(destination)

            # DELETE OLD FILE FIRST
            if destination.exists():
                try:
                    destination.unlink()
                except Exception as e:
                    raise Exception(
                        f"Could not delete:\n{destination}\n\n{e}"
                    )

            try:
                shutil.copy(item, destination)

            except Exception as e:
                raise Exception(
                    f"Failed copying:\n{item}\n->\n{destination}\n\n{e}"
                )
            

    def clear_override_folders(self):

        for folder_name in MOD_OVERRIDE_FOLDERS:

            target = self.game_folder / folder_name

            if target.exists():
                shutil.rmtree(target)