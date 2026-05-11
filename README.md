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

## Dev Log

#### v0.0

Proof of concept

- Added automatic mod detection
- Simplified Injection

#### v0.1

GUI

- Added simple GUI
- Fixed broken path handling

## v1.0

Release

- Added view for Mod infos
- Improved loading speed
- Initial public release

## v1.1

Simplified modding overhead

- Fixed launcher mod invalidation on missing info file

#### v1.2

Simplified mod joining, and vanilla lauch

- Multimod and Vanilla launch
- Last public release
