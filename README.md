# Mexico Volcano Map Project

## Overview

This project creates an interactive map visualization of volcanoes in Mexico along with global population data. It uses Python to process data and generate an HTML map that can be viewed in a web browser.

## Features

- Displays locations of major volcanoes in Mexico
- Color-codes volcanoes based on elevation
- Shows global population density
- Provides interactive layers that can be toggled on and off

## Requirements

- Python 3.x
- pandas
- folium

## Installation

1. Clone this repository or download the source code.
2. Install the required libraries:

```bash
pip install pandas folium
```

3. Ensure you have the following files in your project directory:
   - `volcanes-mexico-txt.txt`: CSV file containing volcano data
   - `world.json`: GeoJSON file containing world population data

## Usage

Run the main Python script:

```bash
python volcano_map.py
```

This will generate a `Map.html` file in the same directory. Open this file in a web browser to view the interactive map.

## How it works

1. The script reads volcano data from a CSV file using pandas.
2. It creates a base map centered on Mexico using folium.
3. Volcanoes are added to the map as circle markers:
   - Green: Elevation < 3000m
   - Orange: Elevation 3000-4000m
   - Red: Elevation > 4000m
4. Global population data is added as a choropleth layer:
   - Green: Population < 10 million
   - Orange: Population 10-20 million
   - Red: Population > 20 million
5. A layer control is added to toggle between volcano and population data.

## Customization

You can modify the `color_producer` function in the script to change the color scheme for volcano elevations. Similarly, you can adjust the population thresholds in the GeoJSON style function.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features.

## License

[Specify your chosen license here]

