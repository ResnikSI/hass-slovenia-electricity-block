# Slovenia Electricity Block Sensor

This custom component for Home Assistant creates a sensor that shows the current electricity pricing block in Slovenia's new 5-block system.

## Installation

1. Copy the `custom_components/slo_electricity_block` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: slo_electricity_block
    name: Current Electricity Block  # Optional, defaults to "Electricity Block"
```

## Features

- Automatically determines winter season (Nov 1 - Feb 28) or summer season (Mar 1 - Oct 31)
- Shows current block number (1-4) based on time of day
- Updates every minute
- Includes additional attributes:
  - season: current season (winter/summer)
  - last_update: timestamp of last update

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

You can create a custom card in your dashboard to display the current block. Here's an example using a Markdown card:

```yaml
type: markdown
content: >
  Current Block: {{ states('sensor.current_electricity_block') }}
  
  Season: {{ state_attr('sensor.current_electricity_block', 'season') }}
