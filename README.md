# Nth Digit of Pi

A small Python desktop app that computes the nth digit of π (pi) and displays it in a simple GUI.

## Platform support

- Windows (build with PyInstaller)
- Linux (build manually or with AppImage)
- macOS (requires macOS build tools and notarization for a clean experience)

## What this project includes

- `Pi.py` — the main PyQt6 GUI application
- `requirements.txt` — project dependencies
- `.gitignore` — excludes `.venv`, build artifacts, and editor files

## Run locally

Use the project virtual environment:

```powershell
cd "c:\Users\a_had\Desktop\Coding\python\Projects\Nth Digit of Pi"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python Pi.py
```

## How to use

1. Open the app.
2. Enter a positive integer in the input box.
3. Click **Find digit**.
4. The result label shows the requested digit of π.

> Position 1 is the leading `3` before the decimal, position 2 is the first digit after the decimal, and so on.

## Build a standalone Windows executable

This project uses `PyInstaller` for packaging.

```powershell
.\.venv\Scripts\python.exe -m pip install pyinstaller
.\.venv\Scripts\python.exe -m pyinstaller --onefile Pi.py
```

The generated executable will appear in `dist\Pi.exe`.

## Release / shipping notes

- Do not commit generated binaries into the repository.
- Upload built binaries to GitHub Releases instead.
- Provide a release asset such as `Pi.exe` for Windows.
- Include instructions in the GitHub release notes explaining how to download and run the app.

## macOS Gatekeeper note

If you ship a macOS build, tell users how to open it if Gatekeeper blocks it:

```bash
xattr -cr /path/to/Pi.app
open /path/to/Pi.app
```

Or use Control-click → Open.

## Dependencies

- `mpmath`
- `PyQt6`

Install them with:

```powershell
python -m pip install -r requirements.txt
```

## Project status

This repository is intended for source code and release metadata. Pre-built binaries should be attached to GitHub Releases so users can download a working app without compiling from source.
