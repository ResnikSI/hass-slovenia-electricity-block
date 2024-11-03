# SLO Electricity Block

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

A Home Assistant custom component that provides information about electricity block rates in Slovenia. This integration helps you monitor and manage your electricity consumption based on the current time block and its associated rates.

## Features

- 🕒 Real-time tracking of current electricity block
- 📊 Dynamic block rate calculation based on:
  - Season (Higher/Lower)
  - Day type (Working/Non-Working)
  - Time of day
- 🗓️ Automatic holiday detection
- 📱 Easy integration with Home Assistant automations
- 🔄 Regular data updates

## Time Blocks Overview

### Higher Season (Winter: Nov 1 - Feb 28/29) - Working Days
1. 00:00 - 06:00 (Block 3)
2. 06:00 - 07:00 (Block 2)
3. 07:00 - 14:00 (Block 1)
4. 14:00 - 16:00 (Block 2)
5. 16:00 - 20:00 (Block 1)
6. 20:00 - 22:00 (Block 2)
7. 22:00 - 00:00 (Block 3)

### Higher Season (Winter) - Non-Working Days
1. 00:00 - 06:00 (Block 4)
2. 06:00 - 07:00 (Block 3)
3. 07:00 - 14:00 (Block 2)
4. 14:00 - 16:00 (Block 3)
5. 16:00 - 20:00 (Block 2)
6. 20:00 - 22:00 (Block 3)
7. 22:00 - 00:00 (Block 4)

### Lower Season (Summer: Mar 1 - Oct 31) - Working Days
1. 00:00 - 06:00 (Block 4)
2. 06:00 - 07:00 (Block 3)
3. 07:00 - 14:00 (Block 2)
4. 14:00 - 16:00 (Block 3)
5. 16:00 - 20:00 (Block 2)
6. 20:00 - 22:00 (Block 3)
7. 22:00 - 00:00 (Block 4)

### Lower Season (Summer) - Non-Working Days
1. 00:00 - 06:00 (Block 5)
2. 06:00 - 07:00 (Block 4)
3. 07:00 - 14:00 (Block 3)
4. 14:00 - 16:00 (Block 4)
5. 16:00 - 20:00 (Block 3)
6. 20:00 - 22:00 (Block 4)
7. 22:00 - 00:00 (Block 5)

## Block Definitions
- Block 1: Highest Rate (Winter working days peak periods)
- Block 2: High Rate
- Block 3: Medium Rate
- Block 4: Low Rate
- Block 5: Lowest Rate (Summer non-working days lowest periods)

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
