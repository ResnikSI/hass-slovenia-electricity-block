# SLO Electricity Block

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

A Home Assistant integration for tracking Slovenian electricity pricing blocks. This integration provides real-time information about the current electricity block based on the season, time of day, and day type.

## Time Blocks Overview

### Higher Season (Winter: Nov 1 - Feb 28/29) - Working Days
1. 00:00 - 06:00 block 3
2. 06:00 - 07:00 block 2
3. 07:00 - 14:00 block 1
4. 14:00 - 16:00 block 2
6. 16:00 - 20:00 block 1
7. 20:00 - 22:00 block 2
8. 22:00 - 00:00 block 3

### Higher Season (Winter) - Non-Working Days
1. 00:00 - 06:00 block 4
2. 06:00 - 07:00 block 3
3. 07:00 - 14:00 block 2
4. 14:00 - 16:00 block 3
6. 16:00 - 20:00 block 2
7. 20:00 - 22:00 block 3
8. 22:00 - 00:00 block 4

### Lower Season (Summer: Mar 1 - Oct 31) - Working Days
1. 00:00 - 06:00 block 4
2. 06:00 - 07:00 block 3
3. 07:00 - 14:00 block 2
4. 14:00 - 16:00 block 3
6. 16:00 - 20:00 block 2
7. 20:00 - 22:00 block 3
8. 22:00 - 00:00 block 4

### Lower Season (Summer) - Non-Working Days
1. 00:00 - 06:00 block 5
2. 06:00 - 07:00 block 4
3. 07:00 - 14:00 block 3
4. 14:00 - 16:00 block 4
6. 16:00 - 20:00 block 3
7. 20:00 - 22:00 block 4
8. 22:00 - 00:00 block 5

## Configuration

During installation, you'll need to configure:

1. Power Limit for Block 1 (kW) - Agreed power limit for highest rate periods
2. Power Limit for Block 2 (kW) - Agreed power limit for high rate periods
3. Power Limit for Block 3 (kW) - Agreed power limit for medium rate periods
4. Power Limit for Block 4 (kW) - Agreed power limit for low rate periods
5. Power Limit for Block 5 (kW) - Agreed power limit for lowest rate periods

These values represent your "dogovorjena obračunska moč" for each block.

## Sensors

The integration provides five sensors:

1. Current Electricity Block (1-5)
   - Shows the current active block
   - Includes block description attribute
   - Includes current block's power limit

2. Current Electricity Season
   - "high" (Winter season: Nov 1 - Feb 28/29)
   - "low" (Summer season: Mar 1 - Oct 31)

3. Electricity Working Day
   - "work-day"
   - "non-work-day"

4. Next Electricity Block (1-5)
   - Shows the upcoming block
   - Includes block description attribute
   - Includes next block's power limit

5. Next Block Start Time
   - Shows when the next block will come into effect
   - ISO format timestamp

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

## Support
If you encounter any issues or have questions, please create an issue on the GitHub repository.
