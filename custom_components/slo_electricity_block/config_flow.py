"""Config flow for Slovenia Electricity Block integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN,
    CONF_POWER_LIMIT_1,
    CONF_POWER_LIMIT_2,
    CONF_POWER_LIMIT_3,
    CONF_POWER_LIMIT_4,
    CONF_POWER_LIMIT_5,
    DEFAULT_POWER_LIMIT,
)

_LOGGER = logging.getLogger(__name__)

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    return {"title": "Slovenian Electricity Block"}

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Slovenia Electricity Block."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        # Check if already configured
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            return self.async_create_entry(
                title="Slovenian Electricity Block",
                data=user_input,
            )

        # Show configuration form with power limit inputs
        data_schema = {
            vol.Required(CONF_POWER_LIMIT_1, default=DEFAULT_POWER_LIMIT): vol.Coerce(float),
            vol.Required(CONF_POWER_LIMIT_2, default=DEFAULT_POWER_LIMIT): vol.Coerce(float),
            vol.Required(CONF_POWER_LIMIT_3, default=DEFAULT_POWER_LIMIT): vol.Coerce(float),
            vol.Required(CONF_POWER_LIMIT_4, default=DEFAULT_POWER_LIMIT): vol.Coerce(float),
            vol.Required(CONF_POWER_LIMIT_5, default=DEFAULT_POWER_LIMIT): vol.Coerce(float),
        }

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(data_schema),
            description_placeholders={
                "name": "Slovenian Electricity Block",
                "description": "Set agreed power limits (kW) for each time block"
            },
            errors=errors,
        )

    async def async_step_import(self, import_info: dict[str, Any]) -> FlowResult:
        """Handle import from configuration.yaml."""
        return await self.async_step_user(import_info)
