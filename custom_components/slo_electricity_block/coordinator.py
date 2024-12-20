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
        """Get the current block number based on time and season."""
        hour = current_time.hour
        minute = current_time.minute
        time_decimal = hour + minute / 60
        is_winter = self._is_winter_season(current_time)
        is_working_day = self._is_working_day(current_time)

        _LOGGER.debug(
            f"Time check - Hour: {hour}, Minute: {minute}, "
            f"Season: {'winter' if is_winter else 'summer'}, "
            f"Day type: {'working' if is_working_day else 'non-working'}"
        )

        # Handle holidays and weekends
        if not is_working_day:
            if is_winter:
                _LOGGER.debug("Winter holiday/weekend - Block 3 (MT) all day")
                return 3
            else:
                _LOGGER.debug("Summer holiday/weekend - Block 4 (MT) all day")
                return 4

        # Working days
        if is_winter:
            # Winter season working day (November-February)
            if 0 <= time_decimal < 6:  # Period 1
                _LOGGER.debug("Winter working day - Block 3 (MT) - Night (00:00-06:00)")
                return 3
            elif 6 <= time_decimal < 7:  # Period 2
                _LOGGER.debug("Winter working day - Block 3 (MT) - Early Morning (06:00-07:00)")
                return 3
            elif 7 <= time_decimal < 14:  # Period 3
                _LOGGER.debug("Winter working day - Block 2 (VT2) - Morning (07:00-14:00)")
                return 2
            elif 14 <= time_decimal < 16:  # Period 4
                _LOGGER.debug("Winter working day - Block 2 (VT2) - Afternoon (14:00-16:00)")
                return 2
            elif 16 <= time_decimal < 18:  # Period 5
                _LOGGER.debug("Winter working day - Block 1 (VT1) - Peak (16:00-18:00)")
                return 1
            elif 18 <= time_decimal < 22:  # Period 6
                _LOGGER.debug("Winter working day - Block 2 (VT2) - Evening (18:00-22:00)")
                return 2
            else:  # Period 7: 22 <= time_decimal <= 24
                _LOGGER.debug("Winter working day - Block 3 (MT) - Late Night (22:00-24:00)")
                return 3
        else:
            # Summer season working day (March-October)
            if 0 <= time_decimal < 6:  # Period 1
                _LOGGER.debug("Summer working day - Block 4 (MT) - Night (00:00-06:00)")
                return 4
            elif 6 <= time_decimal < 7:  # Period 2
                _LOGGER.debug("Summer working day - Block 3 (VT) - Early Morning (06:00-07:00)")
                return 3
            elif 7 <= time_decimal < 14:  # Period 3
                _LOGGER.debug("Summer working day - Block 2 (VT) - Morning (07:00-14:00)")
                return 2
            elif 14 <= time_decimal < 17:  # Period 4
                _LOGGER.debug("Summer working day - Block 3 (VT) - Afternoon (14:00-17:00)")
                return 3
            elif 17 <= time_decimal < 20:  # Period 5
                _LOGGER.debug("Summer working day - Block 2 (VT) - Evening (17:00-20:00)")
                return 2
            elif 20 <= time_decimal < 22:  # Period 6
                _LOGGER.debug("Summer working day - Block 3 (VT) - Late Evening (20:00-22:00)")
                return 3
            else:  # Period 7: 22 <= time_decimal <= 24
                _LOGGER.debug("Summer working day - Block 4 (MT) - Late Night (22:00-24:00)")
                return 4

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
