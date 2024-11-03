"""DataUpdateCoordinator for Slovenia Electricity Block integration."""
from datetime import datetime, timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import (
    DOMAIN,
    HOLIDAYS,
)

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

    def _is_working_day(self, current_date: datetime) -> bool:
        """Determine if current date is a working day."""
        # Check if it's weekend
        if current_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            return False
        
        # Check if it's a holiday
        date_str = current_date.strftime("%Y-%m-%d")
        if date_str in HOLIDAYS:
            return False
        
        return True

    def _get_current_block(self, current_time: datetime) -> int:
        """Get the current block number based on time and day type."""
        hour = current_time.hour
        minute = current_time.minute
        time_decimal = hour + minute / 60
        is_working_day = self._is_working_day(current_time)
        is_winter = self._is_winter_season(current_time)

        _LOGGER.debug(
            f"Time check - Hour: {hour}, Minute: {minute}, "
            f"Season: {'winter' if is_winter else 'summer'}, "
            f"Day type: {'working' if is_working_day else 'non-working'}"
        )

        # Non-working days (weekends and holidays)
        if not is_working_day:
            if is_winter:
                _LOGGER.debug("Winter weekend/holiday - Block 3 (MT)")
                return 3
            else:
                _LOGGER.debug("Summer weekend/holiday - Block 4 (MT)")
                return 4

        # Working days
        if is_winter:
            # Winter season working day
            if 16 <= time_decimal < 18:  # VT1 (Block 1)
                _LOGGER.debug("Winter working day - Block 1 (VT1)")
                return 1
            elif (22 <= time_decimal < 24) or (0 <= time_decimal < 6):  # MT (Block 3)
                _LOGGER.debug("Winter working day - Block 3 (MT)")
                return 3
            elif 6 <= time_decimal < 7:  # MT (Block 3)
                _LOGGER.debug("Winter working day - Block 3 (MT)")
                return 3
            else:  # VT2 (Block 2)
                _LOGGER.debug("Winter working day - Block 2 (VT2)")
                return 2
        else:
            # Summer season working day
            if (22 <= time_decimal < 24) or (0 <= time_decimal < 6):  # MT (Block 4)
                _LOGGER.debug("Summer working day - Block 4 (MT)")
                return 4
            elif 6 <= time_decimal < 7:  # VT (Block 3)
                _LOGGER.debug("Summer working day - Block 3 (VT)")
                return 3
            elif 14 <= time_decimal < 17:  # VT (Block 3)
                _LOGGER.debug("Summer working day - Block 3 (VT)")
                return 3
            elif 20 <= time_decimal < 22:  # VT (Block 3)
                _LOGGER.debug("Summer working day - Block 3 (VT)")
                return 3
            else:  # VT (Block 2)
                _LOGGER.debug(f"Summer working day - Block 2 (VT) at {hour}:{minute}")
                return 2

    async def _async_update_data(self):
        """Update data."""
        try:
            now = datetime.now()
            block = self._get_current_block(now)
            season = "winter" if self._is_winter_season(now) else "summer"
            working_day = self._is_working_day(now)
            
            _LOGGER.debug(
                f"Update result - Block: {block}, Season: {season}, "
                f"Working day: {working_day}, Time: {now.strftime('%H:%M:%S')}"
            )
            
            return {
                "block": block,
                "season": season,
                "working_day": working_day,
                "last_update": now.isoformat()
            }
        except Exception as error:
            _LOGGER.error("Error updating data: %s", error)
            raise UpdateFailed(error) from error
