"""Sensor platform for Slovenia Electricity Block integration."""
from __future__ import annotations

import logging

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

from .const import DOMAIN
from .coordinator import SloveniaElectricityBlockCoordinator

_LOGGER = logging.getLogger(__name__)

BLOCK_ENTITY = SensorEntityDescription(
    key="current_block",
    name="Current Electricity Block",
    icon="mdi:flash",
)

SEASON_ENTITY = SensorEntityDescription(
    key="current_season",
    name="Current Electricity Season",
    icon="mdi:calendar",
)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    _LOGGER.debug("Setting up Slovenia Electricity Block sensor platform")
    coordinator: SloveniaElectricityBlockCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            SloveniaElectricityBlockSensor(coordinator, BLOCK_ENTITY),
            SloveniaElectricitySeasonSensor(coordinator, SEASON_ENTITY),
        ],
        True,
    )

class SloveniaElectricityBlockSensor(CoordinatorEntity[SloveniaElectricityBlockCoordinator], SensorEntity):
    """Representation of Slovenia Electricity Block Sensor."""

    entity_description: SensorEntityDescription

    def __init__(
        self,
        coordinator: SloveniaElectricityBlockCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        _LOGGER.debug("Initializing Slovenia Electricity Block sensor")

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("block")

    @property
    def extra_state_attributes(self) -> dict:
        """Return the state attributes."""
        if not self.coordinator.data:
            return {}
            
        return {
            "season": self.coordinator.data.get("season"),
            "last_update": self.coordinator.data.get("last_update")
        }

class SloveniaElectricitySeasonSensor(CoordinatorEntity[SloveniaElectricityBlockCoordinator], SensorEntity):
    """Representation of Slovenia Electricity Season Sensor."""

    entity_description: SensorEntityDescription

    def __init__(
        self,
        coordinator: SloveniaElectricityBlockCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        _LOGGER.debug("Initializing Slovenia Electricity Season sensor")

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        if not self.coordinator.data:
            return None
        season = self.coordinator.data.get("season")
        return "Higher" if season == "winter" else "Lower"

    @property
    def extra_state_attributes(self) -> dict:
        """Return the state attributes."""
        if not self.coordinator.data:
            return {}
            
        return {
            "last_update": self.coordinator.data.get("last_update")
        }
