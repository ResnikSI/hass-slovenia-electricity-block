# SLO Electricity Block

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

A Home Assistant custom component that provides information about electricity block rates in Slovenia. This integration helps you monitor and manage your electricity consumption based on the current time block and its associated rates.

## Features

- 🕒 Real-time tracking of current electricity block
- 📊 28 different time blocks throughout the day
- 💡 Automatic block rate updates
- 📱 Easy integration with Home Assistant automations
- 🔄 Regular data updates
- 📈 Historical data tracking capability

## Installation

### HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance
2. Add this repository as a custom repository in HACS:
   - Click on HACS in the sidebar
   - Click on "Integrations"
   - Click the three dots in the top right corner
   - Select "Custom repositories"
   - Add the repository URL: `https://github.com/YourUsername/slo_electricity_block`
   - Category: Integration
3. Click "Install"
4. Restart Home Assistant

### Manual Installation

1. Download the latest release from the GitHub repository
2. Copy the `custom_components/slo_electricity_block` folder to your Home Assistant's `custom_components` directory
3. Restart Home Assistant

## Configuration

1. Go to Settings > Devices & Services
2. Click the "+ ADD INTEGRATION" button
3. Search for "SLO Electricity Block"
4. Follow the configuration steps

## Time Blocks

The integration provides information about 28 different time blocks throughout the day. Each block represents a specific time period with its associated electricity rate.

### Block Schedule

| Block | Time Period | Description |
|-------|-------------|-------------|
| VT1 | 06:00 - 07:00 | Higher Rate |
| VT2 | 07:00 - 08:00 | Higher Rate |
| VT3 | 08:00 - 09:00 | Higher Rate |
| VT4 | 09:00 - 10:00 | Higher Rate |
| VT5 | 10:00 - 11:00 | Higher Rate |
| VT6 | 11:00 - 12:00 | Higher Rate |
| VT7 | 12:00 - 13:00 | Higher Rate |
| VT8 | 13:00 - 14:00 | Higher Rate |
| VT9 | 14:00 - 15:00 | Higher Rate |
| VT10 | 15:00 - 16:00 | Higher Rate |
| VT11 | 16:00 - 17:00 | Higher Rate |
| VT12 | 17:00 - 18:00 | Higher Rate |
| VT13 | 18:00 - 19:00 | Higher Rate |
| VT14 | 19:00 - 20:00 | Higher Rate |
| VT15 | 20:00 - 21:00 | Higher Rate |
| MT1 | 21:00 - 22:00 | Lower Rate |
| MT2 | 22:00 - 23:00 | Lower Rate |
| MT3 | 23:00 - 00:00 | Lower Rate |
| MT4 | 00:00 - 01:00 | Lower Rate |
| MT5 | 01:00 - 02:00 | Lower Rate |
| MT6 | 02:00 - 03:00 | Lower Rate |
| MT7 | 03:00 - 04:00 | Lower Rate |
| MT8 | 04:00 - 05:00 | Lower Rate |
| MT9 | 05:00 - 06:00 | Lower Rate |
| KT1 | Saturday | Weekend Rate |
| KT2 | Sunday | Weekend Rate |
| KT3 | Holiday | Holiday Rate |
| KT4 | Special | Special Rate |

## Usage Examples

You can use this integration to:
- Create automations based on electricity rates
- Monitor current block status
- Plan energy-intensive activities during lower-rate periods
- Track historical rate patterns

## Sensors

The integration provides the following sensors:
- Current Block Status
- Current Rate Type
- Next Block Time
- Time Until Next Block

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the [FAQ](../../wiki/FAQ) section
2. Search through [existing issues](../../issues)
3. Create a [new issue](../../issues/new) if needed

---

Made with ❤️ for the Home Assistant Community
