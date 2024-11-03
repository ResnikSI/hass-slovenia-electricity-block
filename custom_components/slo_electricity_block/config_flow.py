"""Config flow for Slovenia Electricity Block integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    _LOGGER.debug("Validating input for Slovenia Electricity Block")
    return {"title": "Slovenia Electricity Block"}

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Slovenia Electricity Block."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        _LOGGER.debug("Starting config flow for Slovenia Electricity Block")

        # Check if already configured
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_instance()

        if user_input is None:
            _LOGGER.debug("Showing configuration form")
            return self.async_show_form(step_id="user")

        _LOGGER.debug("Creating entry for Slovenia Electricity Block")
        return self.async_create_entry(
            title="Slovenia Electricity Block",
            data={}
        )
