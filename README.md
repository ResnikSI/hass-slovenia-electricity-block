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

1. Power Meter (optional)
   - Select your power monitoring sensor
   - Enables automatic power limit monitoring
   - Must be a sensor with power or current readings

2. Power Limits
   - Set your agreed power limits ("dogovorjena obračunska moč") for each block:
   - Block 1 (kW) - Highest rate periods
   - Block 2 (kW) - High rate periods
   - Block 3 (kW) - Medium rate periods
   - Block 4 (kW) - Low rate periods
   - Block 5 (kW) - Lowest rate periods

## Sensors

The integration provides the following sensors:

1. Current Electricity Block (1-5)
   - Shows the current active block
   - Includes block description attribute
   - Includes current block's power limit in kW

2. Current Electricity Season
   - "high" (Winter season: Nov 1 - Feb 28/29)
   - "low" (Summer season: Mar 1 - Oct 31)

3. Electricity Working Day
   - "work-day"
   - "non-work-day"

4. Next Electricity Block (1-5)
   - Shows the upcoming block
   - Includes block description attribute
   - Includes next block's power limit in kW

5. Next Block Start Time
   - Shows when the next block will come into effect
   - ISO format timestamp

6. Power Limit Status (only if power meter configured)
   - Shows current power usage status
   - States: normal/warning/exceeded
   - Attributes:
     * current_usage: Current power consumption
     * current_limit: Current block's power limit
     * percentage_used: Percentage of limit used

## Lovelace Card Example

Here's an example of a Lovelace card that shows your power usage and limit:

```yaml
type: vertical-stack
cards:
  - type: entities
    title: Current Electricity Block
    entities:
      - entity: sensor.current_electricity_block
        name: Block
        secondary_info: attribute
        secondary_info_attribute: block_description
      - entity: sensor.next_electricity_block
        name: Next Block
        secondary_info: attribute
        secondary_info_attribute: block_description
      - entity: sensor.next_block_start_time
        name: Next Block Starts At

  - type: gauge
    title: Power Usage
    entity: sensor.power_limit_status
    attribute: percentage_used
    min: 0
    max: 100
    severity:
      green: 0
      yellow: 90
      red: 100
    needle: true

  - type: glance
    entities:
      - entity: sensor.power_limit_status
        name: Status
        icon: >
          {% set status = states('sensor.power_limit_status') %}
          {% if status == 'exceeded' %}
            mdi:alert-circle
          {% elif status == 'warning' %}
            mdi:alert
          {% else %}
            mdi:check-circle
          {% endif %}
      - entity: sensor.power_limit_status
        name: Current Usage
        attribute: current_usage
      - entity: sensor.power_limit_status
        name: Block Limit
        attribute: current_limit
```

You can also create an automation to notify you when approaching or exceeding the limit:

```yaml
automation:
  - alias: "Power Limit Warning"
    trigger:
      - platform: state
        entity_id: sensor.power_limit_status
    condition:
      - condition: template
        value_template: "{{ trigger.to_state.state in ['warning', 'exceeded'] }}"
    action:
      - service: notify.notify
        data:
          title: "Power Usage Alert"
          message: >
            {% if trigger.to_state.state == 'exceeded' %}
              Power usage ({{ trigger.to_state.attributes.current_usage }}kW) has exceeded the limit ({{ trigger.to_state.attributes.current_limit }}kW)!
            {% else %}
              Power usage ({{ trigger.to_state.attributes.current_usage }}kW) is approaching the limit ({{ trigger.to_state.attributes.current_limit }}kW)
            {% endif %}
```

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
