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
    BLOCK_HIGHER_PEAK,
    BLOCK_HIGHER_NORMAL,
    BLOCK_HIGHER_LOW,
    BLOCK_LOWER_NORMAL,
    BLOCK_LOWER_LOW,
    HIGHER_SEASON_START_MONTH,
    HIGHER_SEASON_START_DAY,
    HIGHER_SEASON_END_MONTH,
    HIGHER_SEASON_END_DAY,
    NIGHT_START_HOUR,
    NIGHT_END_HOUR,
    MORNING_PEAK_START_HOUR,
    MORNING_PEAK_END_HOUR,
    AFTERNOON_PEAK_START_HOUR,
    AFTERNOON_PEAK_END_HOUR,
    EVENING_PEAK_START_HOUR,
    EVENING_PEAK_END_HOUR,
    WINTER_PEAK_START_HOUR,
    WINTER_PEAK_END_HOUR,
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
        if month == HIGHER_SEASON_START_MONTH or month == 12 or month == 1 or (month == HIGHER_SEASON_END_MONTH and day <= HIGHER_SEASON_END_DAY):
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
        current_time_decimal = hour + minute / 60
        is_working_day = self._is_working_day(current_time)
        is_winter = self._is_winter_season(current_time)

        _LOGGER.debug(
            f"Time check - Hour: {hour}, Minute: {minute}, Decimal: {current_time_decimal}, "
            f"Season: {'winter' if is_winter else 'summer'}, "
            f"Day type: {'working' if is_working_day else 'non-working'}"
        )

        if not is_working_day:
            # Weekend/Holiday rules
            if is_winter:
                _LOGGER.debug("Winter weekend/holiday - Block 3 (Higher low)")
                return BLOCK_HIGHER_LOW
            else:
                _LOGGER.debug("Summer weekend/holiday - Block 4 (Lower low)")
                return BLOCK_LOWER_LOW

        # Working day rules
        if is_winter:
            # Winter season working day
            if WINTER_PEAK_START_HOUR <= current_time_decimal < WINTER_PEAK_END_HOUR:
                _LOGGER.debug("Winter working day - Block 1 (Higher peak)")
                return BLOCK_HIGHER_PEAK
            elif (NIGHT_START_HOUR <= current_time_decimal < 24) or (0 <= current_time_decimal < NIGHT_END_HOUR):
                _LOGGER.debug("Winter working day - Block 3 (Higher low)")
                return BLOCK_HIGHER_LOW
            elif MORNING_PEAK_START_HOUR <= current_time_decimal < MORNING_PEAK_END_HOUR:
                _LOGGER.debug("Winter working day - Block 3 (Higher low)")
                return BLOCK_HIGHER_LOW
            else:
                _LOGGER.debug("Winter working day - Block 2 (Higher normal)")
                return BLOCK_HIGHER_NORMAL
        else:
            # Summer season working day
            if (NIGHT_START_HOUR <= current_time_decimal < 24) or (0 <= current_time_decimal < NIGHT_END_HOUR):
                _LOGGER.debug("Summer working day - Block 4 (Lower low)")
                return BLOCK_LOWER_LOW
            elif MORNING_PEAK_START_HOUR <= current_time_decimal < MORNING_PEAK_END_HOUR:
                _LOGGER.debug("Summer working day - Block 3 (Lower peak)")
                return BLOCK_HIGHER_LOW
            elif AFTERNOON_PEAK_START_HOUR <= current_time_decimal < AFTERNOON_PEAK_END_HOUR:
                _LOGGER.debug("Summer working day - Block 3 (Lower peak)")
                return BLOCK_HIGHER_LOW
            elif EVENING_PEAK_START_HOUR <= current_time_decimal < EVENING_PEAK_END_HOUR:
                _LOGGER.debug("Summer working day - Block 3 (Lower peak)")
                return BLOCK_HIGHER_LOW
            else:
                _LOGGER.debug("Summer working day - Block 2 (Lower normal)")
                return BLOCK_LOWER_NORMAL

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
