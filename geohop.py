#!/usr/bin/env python3
"""GeoHop - generate a GPX route with a new location every N seconds."""

import argparse
import csv
import sys
from datetime import datetime, timedelta, timezone


def parse_point(text):
    try:
        lat, lon = (float(x) for x in text.split(","))
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid point '{text}', use lat,lon")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise argparse.ArgumentTypeError(f"Point out of range: {text}")
    return lat, lon


def load_csv(path):
    points = []
    with open(path, newline="") as f:
        for row in csv.reader(f):
            if len(row) >= 2:
                points.append(parse_point(f"{row[0]},{row[1]}"))
    return points


def build_gpx(points, interval, loops):
    start = datetime.now(timezone.utc)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<gpx version="1.1" creator="GeoHop" xmlns="http://www.topografix.com/GPX/1/1">',
        "<trk><name>GeoHop route</name><trkseg>",
    ]
    step = 0
    for _ in range(loops):
        for lat, lon in points:
            ts = (start + timedelta(seconds=interval * step)).strftime("%Y-%m-%dT%H:%M:%SZ")
            lines.append(f'<trkpt lat="{lat}" lon="{lon}"><time>{ts}</time></trkpt>')
            step += 1
    lines.append("</trkseg></trk></gpx>")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Generate a GPX route that changes location every N seconds.")
    p.add_argument("-p", "--point", action="append", type=parse_point, metavar="LAT,LON",
                   help="a coordinate; repeat for multiple points")
    p.add_argument("-c", "--csv", help="CSV file with lat,lon per line")
    p.add_argument("-i", "--interval", type=int, default=10, help="seconds between points (default: 10)")
    p.add_argument("-l", "--loops", type=int, default=1, help="how many times to repeat the route (default: 1)")
    p.add_argument("-o", "--output", default="route.gpx", help="output file (default: route.gpx)")
    args = p.parse_args()

    points = list(args.point or [])
    if args.csv:
        points += load_csv(args.csv)
    if len(points) < 2:
        sys.exit("Provide at least 2 points with -p or -c.")
    if args.interval < 1 or args.loops < 1:
        sys.exit("Interval and loops must be 1 or more.")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(build_gpx(points, args.interval, args.loops))
    print(f"Saved {len(points) * args.loops} points to {args.output}")


if __name__ == "__main__":
    main()
