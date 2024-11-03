"""DataUpdateCoordinator for Slovenia Electricity Block integration."""
from datetime import datetime, timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class SloveniaElectricityBlockCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )

    def _is_winter_season(self, current_date: datetime) -> bool:
        """Determine if current date is in winter season."""
        month = current_date.month
        day = current_date.day
        
        # Winter season: November 1 to February 28/29
        if month == 11 or month == 12 or month == 1 or (month == 2 and day <= 28):
            return True
        return False

    def _get_current_block(self, current_time: datetime) -> int:
        """Get the current block number based on time."""
        hour = current_time.hour
        minute = current_time.minute
        current_time_decimal = hour + minute / 60

        is_winter = self._is_winter_season(current_time)
        _LOGGER.debug(f"Current time: {hour}:{minute}, Season: {'winter' if is_winter else 'summer'}")

        # Determine block based on time and season
        if is_winter:
            if 16 <= current_time_decimal < 18:  # Evening peak
                _LOGGER.debug("Winter Block 1 (Evening peak)")
                return 1
            elif (22 <= current_time_decimal < 24) or (0 <= current_time_decimal < 3) or (6 <= current_time_decimal < 7):
                _LOGGER.debug("Winter Block 3 (Night/early morning)")
                return 3
            else:
                _LOGGER.debug("Winter Block 2 (Regular)")
                return 2
        else:
            if (22 <= current_time_decimal < 24) or (0 <= current_time_decimal < 6):
                _LOGGER.debug("Summer Block 4 (Night)")
                return 4
            elif (6 <= current_time_decimal < 7) or (14 <= current_time_decimal < 17) or (20 <= current_time_decimal < 22):
                _LOGGER.debug("Summer Block 3 (Mid-peak)")
                return 3
            else:
                _LOGGER.debug("Summer Block 2 (Regular)")
                return 2

    async def _async_update_data(self):
        """Update data."""
        try:
            now = datetime.now()
            return {
                "block": self._get_current_block(now),
                "season": "winter" if self._is_winter_season(now) else "summer",
                "last_update": now.isoformat()
            }
        except Exception as error:
            _LOGGER.error("Error updating data: %s", error)
            raise UpdateFailed(error) from error
