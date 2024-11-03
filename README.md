# SLO Electricity Block

A Home Assistant integration for tracking Slovenian electricity pricing blocks. This integration provides real-time information about the current electricity block based on the season, time of day, and day type.

## Time Blocks Overview

### Higher Season (Winter) - Working Days
1. 00:00 - 06:00 (Higher Low - Block 3)
2. 06:00 - 07:00 (Higher Low - Block 3)
3. 07:00 - 16:00 (Higher Normal - Block 2)
4. 16:00 - 18:00 (Higher Peak - Block 1)
5. 18:00 - 22:00 (Higher Normal - Block 2)
6. 22:00 - 24:00 (Higher Low - Block 3)
7. Regular Period (Higher Normal - Block 2)

### Higher Season (Winter) - Free Days (Weekends/Holidays)
1. 00:00 - 06:00 (Higher Low - Block 3)
2. 06:00 - 07:00 (Higher Low - Block 3)
3. 07:00 - 22:00 (Higher Low - Block 3)
4. 22:00 - 24:00 (Higher Low - Block 3)
5. Weekend Period (Higher Low - Block 3)
6. Holiday Period (Higher Low - Block 3)
7. Special Period (Higher Low - Block 3)

### Lower Season (Summer) - Working Days
1. 00:00 - 06:00 (Lower Low - Block 4)
2. 06:00 - 07:00 (Lower Low - Block 4)
3. 07:00 - 14:00 (Lower Normal - Block 2)
4. 14:00 - 17:00 (Lower Low - Block 4)
5. 17:00 - 20:00 (Lower Normal - Block 2)
6. 20:00 - 22:00 (Lower Low - Block 4)
7. 22:00 - 24:00 (Lower Low - Block 4)

### Lower Season (Summer) - Free Days (Weekends/Holidays)
1. 00:00 - 06:00 (Lower Low - Block 4)
2. 06:00 - 07:00 (Lower Low - Block 4)
3. 07:00 - 22:00 (Lower Low - Block 4)
4. 22:00 - 24:00 (Lower Low - Block 4)
5. Weekend Period (Lower Low - Block 4)
6. Holiday Period (Lower Low - Block 4)
7. Special Period (Lower Low - Block 4)

## Block Definitions
- Block 1 (VT1): Higher Peak Rate
- Block 2 (VT2/VT): Higher/Lower Normal Rate
- Block 3 (MT): Higher Low Rate
- Block 4 (MT): Lower Low Rate

## Seasons
- Higher Season (Winter): November 1 - February 28/29
- Lower Season (Summer): March 1 - October 31

## Installation

### HACS Installation (Recommended)
1. Make sure you have HACS installed
2. Add this repository as a custom repository in HACS
3. Install through HACS interface
4. Restart Home Assistant

### Manual Installation
1. Copy the `custom_components/slo_electricity_block` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Configure through the UI

## Configuration
1. Go to Settings > Devices & Services
2. Click "Add Integration"
3. Search for "Slovenia Electricity Block"
4. Follow the configuration steps

## Support
If you encounter any issues or have questions, please create an issue on the GitHub repository.
