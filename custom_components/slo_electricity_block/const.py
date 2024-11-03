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

# Block definitions
BLOCK_1 = 1  # Highest rate (winter working days peak)
BLOCK_2 = 2  # High rate
BLOCK_3 = 3  # Medium rate
BLOCK_4 = 4  # Low rate
BLOCK_5 = 5  # Lowest rate (summer non-working days)

# Season dates
HIGHER_SEASON_START_MONTH = 11    # November
HIGHER_SEASON_START_DAY = 1
HIGHER_SEASON_END_MONTH = 2       # February
HIGHER_SEASON_END_DAY = 28        # or 29 in leap years

# Time ranges for all periods
TIME_RANGES = {
    "NIGHT_START": 22,    # 22:00
    "NIGHT_END": 6,      # 06:00
    "MORNING_START": 6,   # 06:00
    "MORNING_END": 7,    # 07:00
    "DAY1_START": 7,     # 07:00
    "DAY1_END": 14,      # 14:00
    "DAY2_START": 14,    # 14:00
    "DAY2_END": 16,      # 16:00
    "DAY3_START": 16,    # 16:00
    "DAY3_END": 20,      # 20:00
    "EVENING_START": 20,  # 20:00
    "EVENING_END": 22,   # 22:00
}

# Block descriptions
BLOCK_DESCRIPTIONS = {
    BLOCK_1: "Highest Rate",
    BLOCK_2: "High Rate",
    BLOCK_3: "Medium Rate",
    BLOCK_4: "Low Rate",
    BLOCK_5: "Lowest Rate",
}

# Season descriptions
SEASON_HIGHER = "high"
SEASON_LOWER = "low"

# Day type descriptions
DAY_TYPE_WORKING = "work-day"
DAY_TYPE_NON_WORKING = "non-work-day"
