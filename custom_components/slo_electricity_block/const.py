"""Constants for the Slovenia Electricity Block integration."""

DOMAIN = "slo_electricity_block"

# Slovenian holidays
HOLIDAYS = [
    "2024-01-01",  # New Year's Day
    "2024-01-02",  # New Year's Day 2
    "2024-02-08",  # Prešeren Day
    "2024-04-01",  # Easter Monday
    "2024-04-27",  # Day of Uprising Against Occupation
    "2024-05-01",  # Labour Day
    "2024-05-02",  # Labour Day 2
    "2024-06-25",  # Statehood Day
    "2024-08-15",  # Assumption Day
    "2024-10-31",  # Reformation Day
    "2024-11-01",  # All Saints' Day
    "2024-12-25",  # Christmas Day
    "2024-12-26",  # Independence and Unity Day
    "2025-01-01",  # New Year's Day
    "2025-01-02",  # New Year's Day 2
    "2025-02-08",  # Prešeren Day
    "2025-04-21",  # Easter Monday
    "2025-04-27",  # Day of Uprising Against Occupation
    "2025-05-01",  # Labour Day
    "2025-05-02",  # Labour Day 2
    "2025-06-25",  # Statehood Day
    "2025-08-15",  # Assumption Day
    "2025-10-31",  # Reformation Day
    "2025-11-01",  # All Saints' Day
    "2025-12-25",  # Christmas Day
    "2025-12-26",  # Independence and Unity Day
]

# Time blocks
BLOCK_HIGHER_PEAK = 1      # VT1 - Higher peak
BLOCK_HIGHER_NORMAL = 2    # VT2 - Higher normal
BLOCK_HIGHER_LOW = 3       # MT - Higher low
BLOCK_LOWER_NORMAL = 2     # VT - Lower normal
BLOCK_LOWER_LOW = 4        # MT - Lower low

# Season dates
HIGHER_SEASON_START_MONTH = 11    # November
HIGHER_SEASON_START_DAY = 1
HIGHER_SEASON_END_MONTH = 2       # February
HIGHER_SEASON_END_DAY = 28        # or 29 in leap years

# Time ranges
NIGHT_START_HOUR = 22
NIGHT_END_HOUR = 6
MORNING_PEAK_START_HOUR = 6
MORNING_PEAK_END_HOUR = 7
AFTERNOON_PEAK_START_HOUR = 14
AFTERNOON_PEAK_END_HOUR = 17
EVENING_PEAK_START_HOUR = 20
EVENING_PEAK_END_HOUR = 22
WINTER_PEAK_START_HOUR = 16
WINTER_PEAK_END_HOUR = 18
