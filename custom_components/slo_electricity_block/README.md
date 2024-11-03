# Slovenia Electricity Block Sensor

A Home Assistant integration that shows the current electricity pricing block in Slovenia's new 5-block system.

## Features

- Automatically determines winter season (Nov 1 - Feb 28) or summer season (Mar 1 - Oct 31)
- Shows current block number based on time of day
- Updates every minute
- Includes additional attributes:
  - season: current season (winter/summer)
  - last_update: timestamp of last update

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

## Block Meanings

Winter Season (Nov 1 - Feb 28):
- Block 1: Highest peak (16:00-18:00)
- Block 2: Regular usage
- Block 3: Night/early morning (22:00-03:00, 06:00-07:00)

Summer Season (Mar 1 - Oct 31):
- Block 2: Regular usage
- Block 3: Mid-peak periods
- Block 4: Night block (22:00-06:00)

## Example Card Configuration

You can create a custom card in your dashboard to display the current block. Here's an example using an entities card:

```yaml
type: entities
entities:
  - entity: sensor.current_electricity_block
    name: Current Electricity Block
    secondary_info: attribute
    secondary_info_attribute: season
```

Or using a Markdown card for more detailed information:

```yaml
type: markdown
content: >
  ## Electricity Block Info
  Current Block: {{ states('sensor.current_electricity_block') }}
  
  Season: {{ state_attr('sensor.current_electricity_block', 'season') }}
  
  Last Updated: {{ state_attr('sensor.current_electricity_block', 'last_update') }}
