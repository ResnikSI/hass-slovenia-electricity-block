# Slovenia Electricity Block Sensor

A Home Assistant integration that shows the current electricity pricing block and season in Slovenia's new 5-block system, taking into account working days and weekends.

## Features

- Automatically determines winter (higher) season and summer (lower) season
- Shows current block number based on time of day and day type
- Handles weekends and working days differently
- Provides three sensors:
  1. Current Electricity Block (1-4)
  2. Current Electricity Season (Higher/Lower)
  3. Electricity Working Day (Working Day/Weekend)
- Updates every minute
- Includes additional attributes for detailed information

## Installation

### HACS Installation (Recommended)

1. Open HACS in your Home Assistant instance
2. Click the three dots in the top right corner
3. Select "Custom repositories"
4. Add this repository URL: https://github.com/ResnikSI/hass-slovenia-electricity-block
5. Select category: "Integration"
6. Click "Add"
7. Install through HACS interface
8. Restart Home Assistant
9. Go to Settings -> Devices & Services
10. Click "Add Integration"
11. Search for "Slovenia Electricity Block"
12. Click to configure

### Manual Installation

1. Copy the `custom_components/slo_electricity_block` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Go to Settings -> Devices & Services
4. Click "Add Integration"
5. Search for "Slovenia Electricity Block"
6. Click to configure

## Block and Season Information

### Working Days (Monday-Friday)
Winter Season (Nov 1 - Feb 28):
- Block 1: Highest peak (16:00-18:00)
- Block 2: Regular usage
- Block 3: Night/early morning (22:00-03:00, 06:00-07:00)

Summer Season (Mar 1 - Oct 31):
- Block 2: Regular usage
- Block 3: Mid-peak periods
- Block 4: Night block (22:00-06:00)

### Weekends (Saturday-Sunday)
- Winter Season: Always Block 3
- Summer Season: Always Block 4

### Seasons
- Higher Season (Winter): November 1 to February 28/29
- Lower Season (Summer): March 1 to October 31

## Example Card Configuration

You can create a custom card in your dashboard to display all sensors. Here's an example using an entities card:

```yaml
type: entities
entities:
  - entity: sensor.current_electricity_block
    name: Current Block
  - entity: sensor.current_electricity_season
    name: Current Season
  - entity: sensor.electricity_working_day
    name: Day Type
```

Or using a Markdown card for more detailed information:

```yaml
type: markdown
content: >
  ## Electricity Information
  Current Block: {{ states('sensor.current_electricity_block') }}
  
  Season: {{ states('sensor.current_electricity_season') }}
  
  Day Type: {{ states('sensor.electricity_working_day') }}
  
  Last Updated: {{ state_attr('sensor.current_electricity_block', 'last_update') }}
```

## Troubleshooting

If you encounter any issues:

1. Check the Home Assistant logs (Settings > System > Logs)
2. Look for entries containing "slo_electricity_block"
3. Make sure you've restarted Home Assistant after installation
4. Verify the integration appears in Settings > Devices & Services
