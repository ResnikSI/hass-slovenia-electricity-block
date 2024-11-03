"""Platform for sensor integration."""
from datetime import datetime, timedelta
import logging
from typing import Any, Dict, Optional

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.event import async_track_state_change_event

from .const import (
    BLOCK_1,
    BLOCK_2,
    BLOCK_3,
    BLOCK_4,
    BLOCK_5,
    BLOCK_DESCRIPTIONS,
    CONF_POWER_METER,
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
    config_data = config_entry.data
    entities = [
        CurrentBlockSensor(config_data),
        CurrentSeasonSensor(),
        DayTypeSensor(),
        NextBlockSensor(config_data),
        NextBlockTimeSensor(),
    ]

    # Add power limit status sensor if power meter is configured
    if CONF_POWER_METER in config_data and config_data[CONF_POWER_METER]:
        entities.append(PowerLimitStatusSensor(config_data))

    async_add_entities(entities)

class BlockCalculationMixin:
    """Mixin for block calculation methods."""

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

    def _get_next_block_info(self, current_date: datetime) -> tuple[int, datetime]:
        """Get next block and its start time."""
        hour = current_date.hour
        tr = TIME_RANGES
        next_time = None
        
        # Find the next time block
        if hour < tr["NIGHT_END"]:  # Before 06:00
            next_time = current_date.replace(hour=tr["NIGHT_END"], minute=0, second=0, microsecond=0)
        elif hour < tr["MORNING_END"]:  # Before 07:00
            next_time = current_date.replace(hour=tr["MORNING_END"], minute=0, second=0, microsecond=0)
        elif hour < tr["DAY1_END"]:  # Before 14:00
            next_time = current_date.replace(hour=tr["DAY1_END"], minute=0, second=0, microsecond=0)
        elif hour < tr["DAY2_END"]:  # Before 16:00
            next_time = current_date.replace(hour=tr["DAY2_END"], minute=0, second=0, microsecond=0)
        elif hour < tr["DAY3_END"]:  # Before 20:00
            next_time = current_date.replace(hour=tr["DAY3_END"], minute=0, second=0, microsecond=0)
        elif hour < tr["NIGHT_START"]:  # Before 22:00
            next_time = current_date.replace(hour=tr["NIGHT_START"], minute=0, second=0, microsecond=0)
        else:  # After 22:00, next block starts at 06:00 tomorrow
            next_time = (current_date + timedelta(days=1)).replace(hour=tr["NIGHT_END"], minute=0, second=0, microsecond=0)
        
        # Get the block that will be active at next_time
        next_block = self._get_current_block(next_time)
        
        return next_block, next_time

class CurrentBlockSensor(BlockCalculationMixin, SensorEntity):
    """Sensor for current electricity block."""

    _attr_name = "Current Electricity Block"
    _attr_unique_id = "current_electricity_block"

    def __init__(self, config_data: dict) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None
        self._attr_extra_state_attributes: Dict[str, Any] = {}
        self._config_data = config_data

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        current_block = self._get_current_block(current_date)
        
        # Get power limit for current block
        power_limit_key = f"Block {current_block}"
        power_limit = self._config_data.get(power_limit_key, 0)
        
        self._attr_native_value = current_block
        self._attr_extra_state_attributes = {
            "block_description": BLOCK_DESCRIPTIONS[current_block],
            "power_limit": power_limit,
            "last_update": current_date.isoformat(),
        }

class CurrentSeasonSensor(BlockCalculationMixin, SensorEntity):
    """Sensor for current season."""

    _attr_name = "Current Electricity Season"
    _attr_unique_id = "current_electricity_season"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        self._attr_native_value = SEASON_HIGHER if self._is_higher_season(current_date) else SEASON_LOWER

class DayTypeSensor(BlockCalculationMixin, SensorEntity):
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

class NextBlockSensor(BlockCalculationMixin, SensorEntity):
    """Sensor for next electricity block."""

    _attr_name = "Next Electricity Block"
    _attr_unique_id = "next_electricity_block"

    def __init__(self, config_data: dict) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None
        self._attr_extra_state_attributes: Dict[str, Any] = {}
        self._config_data = config_data

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        next_block, _ = self._get_next_block_info(current_date)
        
        # Get power limit for next block
        power_limit_key = f"Block {next_block}"
        power_limit = self._config_data.get(power_limit_key, 0)
        
        self._attr_native_value = next_block
        self._attr_extra_state_attributes = {
            "block_description": BLOCK_DESCRIPTIONS[next_block],
            "power_limit": power_limit,
            "last_update": current_date.isoformat(),
        }

class NextBlockTimeSensor(BlockCalculationMixin, SensorEntity):
    """Sensor for next block start time."""

    _attr_name = "Next Block Start Time"
    _attr_unique_id = "next_block_start_time"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None
        self._attr_extra_state_attributes: Dict[str, Any] = {}

    def update(self) -> None:
        """Update the sensor."""
        current_date = datetime.now()
        _, next_time = self._get_next_block_info(current_date)
        
        self._attr_native_value = next_time.isoformat()
        self._attr_extra_state_attributes = {
            "last_update": current_date.isoformat(),
        }

class PowerLimitStatusSensor(BlockCalculationMixin, SensorEntity):
    """Sensor for power limit status."""

    _attr_name = "Power Limit Status"
    _attr_unique_id = "power_limit_status"

    def __init__(self, config_data: dict) -> None:
        """Initialize the sensor."""
        self._attr_native_value = None
        self._attr_extra_state_attributes: Dict[str, Any] = {}
        self._config_data = config_data
        self._power_meter = config_data.get(CONF_POWER_METER)

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""
        if self._power_meter:
            self.async_on_remove(
                async_track_state_change_event(
                    self.hass, [self._power_meter], self._handle_power_meter_change
                )
            )

    async def _handle_power_meter_change(self, event) -> None:
        """Handle power meter state changes."""
        self.async_schedule_update_ha_state(True)

    def update(self) -> None:
        """Update the sensor."""
        if not self._power_meter:
            self._attr_native_value = "unavailable"
            return

        current_date = datetime.now()
        current_block = self._get_current_block(current_date)
        power_limit_key = f"Block {current_block}"
        block_limit = float(self._config_data.get(power_limit_key, 0))

        try:
            current_power = float(self.hass.states.get(self._power_meter).state)
            percentage_used = (current_power / block_limit * 100) if block_limit > 0 else 0

            if current_power > block_limit:
                status = "exceeded"
            elif current_power > (block_limit * 0.9):
                status = "warning"
            else:
                status = "normal"

            self._attr_native_value = status
            self._attr_extra_state_attributes = {
                "current_usage": current_power,
                "current_limit": block_limit,
                "percentage_used": round(percentage_used, 1),
                "last_update": current_date.isoformat(),
            }
        except (ValueError, AttributeError):
            self._attr_native_value = "error"
            self._attr_extra_state_attributes = {
                "error": "Failed to read power meter",
                "last_update": current_date.isoformat(),
            }
