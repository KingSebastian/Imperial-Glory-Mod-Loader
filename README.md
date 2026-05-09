# Imperial Glory Mod Loader

Source code to a simple mod launcher for Imperial Glory.

## Features

- Automatic mod discovery
- EXE launcher
- Keeps original files intact

## Mod Structure

Mods go inside:

Mods/YourMod/

Add a mod.json (Optional):

mod.json

Possible fields:

````json
{
    "name": "",
    "author": "",
    "version": "",
    "description": ""
}
```

## Running From Source

Create a venv if you wish to, and/or

```bash
pip install -r requirements.txt
python main.py
````

## Building EXE

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --uac-admin main.py
```
