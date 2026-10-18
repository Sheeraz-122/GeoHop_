# GeoHop

A lightweight Python tool that generates a GPX route where the location changes every 10 seconds (or any interval you choose). Built for app testing and privacy experiments on Android, and runs in Termux.

## Features

- New location every N seconds (default 10)
- Coordinates from the command line or a CSV file
- Repeat the route in a loop
- No third-party dependencies

## Requirements

- Python 3.8 or newer
- Android with Termux, or any Linux/macOS/Windows machine
- A mock location app that can import GPX files (for Android use)

## Installation (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
termux-setup-storage
git clone https://github.com/Sheeraz-122/GeoHop.git
cd GeoHop
pip install -r requirements.txt
```

## Installation (Linux / macOS / Windows)

```bash
git clone https://github.com/Sheeraz-122/GeoHop.git
cd GeoHop
pip install -r requirements.txt
```

## Usage

Using points on the command line:

```bash
python geohop.py -p 28.6139,77.2090 -p 28.6145,77.2100 -p 28.6152,77.2111 -o /sdcard/route.gpx
```

Using a CSV file (one `lat,lon` per line):

```bash
python geohop.py -c points.csv -i 10 -l 5 -o /sdcard/route.gpx
```

### Options

| Option | Description | Default |
|---|---|---|
| `-p`, `--point` | A `lat,lon` coordinate, repeat for more | none |
| `-c`, `--csv` | CSV file with coordinates | none |
| `-i`, `--interval` | Seconds between points | 10 |
| `-l`, `--loops` | Times to repeat the route | 1 |
| `-o`, `--output` | Output GPX file | route.gpx |

## Using the route on Android

1. Enable Developer Options on your phone.
2. Open Developer Options and select a mock location app.
3. Import the generated `route.gpx` in that app and press play.

Some apps ignore GPX timestamps and use their own speed setting, so adjust it in the app if needed.

## Responsible use

Use GeoHop only for testing your own apps and protecting your own privacy. Do not use it to bypass attendance systems, commit fraud, or break the terms of any service.

## License

Released under the MIT License. See [LICENSE](LICENSE).
