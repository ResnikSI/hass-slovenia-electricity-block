"""Slovenia Electricity Block Sensor."""
from __future__ import annotations

from datetime import datetime
import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

_LOGGER = logging.getLogger(__name__)

WINTER_BLOCKS = [
    # Block 3
    [(0, 0), (3, 0)],
    # Block 2
    [(3, 0), (6, 0)],
    # Block 3
    [(6, 0), (7, 0)],
    # Block 2
    [(7, 0), (14, 0)],
    # Block 2
    [(14, 0), (16, 0)],
    # Block 1
    [(16, 0), (18, 0)],
    # Block 2
    [(18, 0), (20, 0)],
    # Block 2
    [(20, 0), (22, 0)],
    # Block 3
    [(22, 0), (24, 0)]
]

SUMMER_BLOCKS = [
    # Block 4
    [(0, 0), (6, 0)],
    # Block 3
    [(6, 0), (7, 0)],
    # Block 2
    [(7, 0), (14, 0)],
    # Block 3
    [(14, 0), (17, 0)],
    # Block 2
    [(17, 0), (20, 0)],
    # Block 3
    [(20, 0), (22, 0)],
    # Block 4
    [(22, 0), (24, 0)]
]

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([SloveniaElectricityBlockSensor()], True)

class SloveniaElectricityBlockSensor(SensorEntity):
    """Representation of Slovenia Electricity Block Sensor."""

    _attr_name = "Current Electricity Block"
    _attr_unique_id = "slovenia_electricity_block"
    _attr_native_unit_of_measurement = None
    _attr_has_entity_name = True

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_extra_state_attributes = {}

    def _is_winter_season(self, current_date: datetime) -> bool:
        """Determine if current date is in winter season."""
        month = current_date.month
        day = current_date.day
        
        # Winter season: November 1 to February 28/29
        if month == 11 or month == 12 or month == 1 or (month == 2 and day <= 28):
            return True
        return False

    def _get_current_block(self, current_time: datetime) -> StateType:
        """Get the current block number based on time."""
        hour = current_time.hour
        minute = current_time.minute
        current_time_decimal = hour + minute / 60

        blocks = WINTER_BLOCKS if self._is_winter_season(current_time) else SUMMER_BLOCKS

        for block_info in blocks:
            start_time = block_info[0][0] + block_info[0][1] / 60
            end_time = block_info[1][0] + block_info[1][1] / 60
            
            if start_time <= current_time_decimal < end_time:
                # Determine block number based on time range
                if self._is_winter_season(current_time):
                    if start_time >= 16 and start_time < 18:  # Evening peak
                        return 1
                    elif (6 <= start_time < 7) or (22 <= start_time < 24) or (0 <= start_time < 3):  # Night/early morning
                        return 3
                    else:
                        return 2
                else:  # Summer season
                    if (0 <= start_time < 6) or (22 <= start_time < 24):  # Night block
                        return 4
                    elif (6 <= start_time < 7) or (14 <= start_time < 17) or (20 <= start_time < 22):  # Mid-peak
                        return 3
                    else:
                        return 2

        return None

    def update(self) -> None:
        """Fetch new state data for the sensor."""
        now = datetime.now()
        self._attr_native_value = self._get_current_block(now)
        
        self._attr_extra_state_attributes = {
            "season": "winter" if self._is_winter_season(now) else "summer",
            "last_update": now.isoformat()
        }
