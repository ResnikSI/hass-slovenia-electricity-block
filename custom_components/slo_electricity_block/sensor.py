"""Platform for sensor integration."""
from datetime import datetime
import logging
from typing import Any, Dict, Optional

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from .const import (
    BLOCK_1,
    BLOCK_2,
    BLOCK_3,
    BLOCK_4,
    BLOCK_5,
    BLOCK_DESCRIPTIONS,
    DAY_TYPE_NON_WORKING,
    DAY_TYPE_WORKING,
    DOMAIN,
    HIGHER_SEASON_END_DAY,
    HIGHER_SEASON_END_MONTH,
    HIGHER_SEASON_START_DAY,
    HIGHER_SEASON_START_MONTH,
    HOLIDAYS,
    SEASON_HIGHER,
    SEASON_LOWER,
    TIME_RANGES,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([
        CurrentBlockSensor(),
        CurrentSeasonSensor(),
        DayTypeSensor(),
    ])

class CurrentBlockSensor(SensorEntity):
    """Sensor for current electricity block."""

    _attr_name = "Current Electricity Block"
    _attr_unique_id = "current_electricity_block"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None
        self._attr_extra_state_attributes: Dict[str, Any] = {}

    def _is_higher_season(self, current_date: datetime) -> bool:
        """Determine if current date is in higher season (winter)."""
        month = current_date.month
        day = current_date.day

        if month == HIGHER_SEASON_START_MONTH and day >= HIGHER_SEASON_START_DAY:
            return True
        if month > HIGHER_SEASON_START_MONTH or month < HIGHER_SEASON_END_MONTH:
            return True
        if month == HIGHER_SEASON_END_MONTH and day <= HIGHER_SEASON_END_DAY:
            return True
        return False

    def _is_working_day(self, current_date: datetime) -> bool:
        """Determine if current date is a working day."""
        if current_date.strftime("%Y-%m-%d") in HOLIDAYS:
            return False
        return current_date.weekday() < 5

    def _get_current_block(self, current_date: datetime) -> int:
        """Get current block based on time and season."""
        hour = current_date.hour
        is_higher_season = self._is_higher_season(current_date)
        is_working_day = self._is_working_day(current_date)
        tr = TIME_RANGES  # shorthand for readability

        if is_higher_season:
            if is_working_day:
                # Higher Season (Winter) - Working Days
                if tr["NIGHT_START"] <= hour < 24 or 0 <= hour < tr["NIGHT_END"]:
                    return BLOCK_3
                elif tr["MORNING_START"] <= hour < tr["MORNING_END"]:
                    return BLOCK_2
                elif tr["DAY1_START"] <= hour < tr["DAY1_END"]:
                    return BLOCK_1
                elif tr["DAY2_START"] <= hour < tr["DAY2_END"]:
                    return BLOCK_2
                elif tr["DAY3_START"] <= hour < tr["DAY3_END"]:
                    return BLOCK_1
                else:  # 20:00-22:00
                    return BLOCK_2
            else:
                # Higher Season (Winter) - Non-Working Days
                if tr["NIGHT_START"] <= hour < 24 or 0 <= hour < tr["NIGHT_END"]:
                    return BLOCK_4
                elif tr["MORNING_START"] <= hour < tr["MORNING_END"]:
                    return BLOCK_3
                elif tr["DAY1_START"] <= hour < tr["DAY1_END"]:
                    return BLOCK_2
                elif tr["DAY2_START"] <= hour < tr["DAY2_END"]:
                    return BLOCK_3
                elif tr["DAY3_START"] <= hour < tr["DAY3_END"]:
                    return BLOCK_2
                else:  # 20:00-22:00
                    return BLOCK_3
        else:
            if is_working_day:
                # Lower Season (Summer) - Working Days
                if tr["NIGHT_START"] <= hour < 24 or 0 <= hour < tr["NIGHT_END"]:
                    return BLOCK_4
                elif tr["MORNING_START"] <= hour < tr["MORNING_END"]:
                    return BLOCK_3
                elif tr["DAY1_START"] <= hour < tr["DAY1_END"]:
                    return BLOCK_2
                elif tr["DAY2_START"] <= hour < tr["DAY2_END"]:
                    return BLOCK_3
                elif tr["DAY3_START"] <= hour < tr["DAY3_END"]:
                    return BLOCK_2
                else:  # 20:00-22:00
                    return BLOCK_3
            else:
                # Lower Season (Summer) - Non-Working Days
                if tr["NIGHT_START"] <= hour < 24 or 0 <= hour < tr["NIGHT_END"]:
                    return BLOCK_5
                elif tr["MORNING_START"] <= hour < tr["MORNING_END"]:
                    return BLOCK_4
                elif tr["DAY1_START"] <= hour < tr["DAY1_END"]:
                    return BLOCK_3
                elif tr["DAY2_START"] <= hour < tr["DAY2_END"]:
                    return BLOCK_4
                elif tr["DAY3_START"] <= hour < tr["DAY3_END"]:
                    return BLOCK_3
                else:  # 20:00-22:00
                    return BLOCK_4

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        current_block = self._get_current_block(current_date)
        
        self._attr_native_value = current_block
        self._attr_extra_state_attributes = {
            "block_description": BLOCK_DESCRIPTIONS[current_block],
            "last_update": current_date.isoformat(),
        }

class CurrentSeasonSensor(SensorEntity):
    """Sensor for current season."""

    _attr_name = "Current Electricity Season"
    _attr_unique_id = "current_electricity_season"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None

    def _is_higher_season(self, current_date: datetime) -> bool:
        """Determine if current date is in higher season (winter)."""
        month = current_date.month
        day = current_date.day

        if month == HIGHER_SEASON_START_MONTH and day >= HIGHER_SEASON_START_DAY:
            return True
        if month > HIGHER_SEASON_START_MONTH or month < HIGHER_SEASON_END_MONTH:
            return True
        if month == HIGHER_SEASON_END_MONTH and day <= HIGHER_SEASON_END_DAY:
            return True
        return False

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        self._attr_native_value = SEASON_HIGHER if self._is_higher_season(current_date) else SEASON_LOWER

class DayTypeSensor(SensorEntity):
    """Sensor for day type (working/non-working)."""

    _attr_name = "Electricity Working Day"
    _attr_unique_id = "electricity_working_day"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        is_working_day = (
            current_date.weekday() < 5 and 
            current_date.strftime("%Y-%m-%d") not in HOLIDAYS
        )
        self._attr_native_value = DAY_TYPE_WORKING if is_working_day else DAY_TYPE_NON_WORKING
