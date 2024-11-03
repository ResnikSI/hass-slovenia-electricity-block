"""Sensor platform for Slovenia Electricity Block integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
)

from . import DOMAIN
from .coordinator import SloveniaElectricityBlockCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    _LOGGER.debug("Setting up Slovenia Electricity Block sensor platform")
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SloveniaElectricityBlockSensor(coordinator)], True)

class SloveniaElectricityBlockSensor(CoordinatorEntity, SensorEntity):
    """Representation of Slovenia Electricity Block Sensor."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_unique_id = "slovenia_electricity_block"

    def __init__(self, coordinator: SloveniaElectricityBlockCoordinator) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        _LOGGER.debug("Initializing Slovenia Electricity Block sensor")

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return self.coordinator.data.get("block") if self.coordinator.data else None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        if not self.coordinator.data:
            return {}
            
        return {
            "season": self.coordinator.data.get("season"),
            "last_update": self.coordinator.data.get("last_update")
        }
