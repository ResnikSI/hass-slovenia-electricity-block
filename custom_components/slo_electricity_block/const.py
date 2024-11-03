"""Constants for the Slovenia Electricity Block integration."""

DOMAIN = "slo_electricity_block"

# Configuration keys
CONF_POWER_LIMIT_1 = "power_limit_1"
CONF_POWER_LIMIT_2 = "power_limit_2"
CONF_POWER_LIMIT_3 = "power_limit_3"
CONF_POWER_LIMIT_4 = "power_limit_4"
CONF_POWER_LIMIT_5 = "power_limit_5"

# Default power limits in kW
DEFAULT_POWER_LIMIT = 7  # 7kW default

# Slovenian holidays for 2024-2034
HOLIDAYS = [
    # 2024
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
    # 2025
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
    # 2026
    "2026-01-01",  # New Year's Day
    "2026-01-02",  # New Year's Day 2
    "2026-02-08",  # Prešeren Day
    "2026-04-06",  # Easter Monday
    "2026-04-27",  # Day of Uprising Against Occupation
    "2026-05-01",  # Labour Day
    "2026-05-02",  # Labour Day 2
    "2026-06-25",  # Statehood Day
    "2026-08-15",  # Assumption Day
    "2026-10-31",  # Reformation Day
    "2026-11-01",  # All Saints' Day
    "2026-12-25",  # Christmas Day
    "2026-12-26",  # Independence and Unity Day
    # 2027
    "2027-01-01",  # New Year's Day
    "2027-01-02",  # New Year's Day 2
    "2027-02-08",  # Prešeren Day
    "2027-03-29",  # Easter Monday
    "2027-04-27",  # Day of Uprising Against Occupation
    "2027-05-01",  # Labour Day
    "2027-05-02",  # Labour Day 2
    "2027-06-25",  # Statehood Day
    "2027-08-15",  # Assumption Day
    "2027-10-31",  # Reformation Day
    "2027-11-01",  # All Saints' Day
    "2027-12-25",  # Christmas Day
    "2027-12-26",  # Independence and Unity Day
    # 2028
    "2028-01-01",  # New Year's Day
    "2028-01-02",  # New Year's Day 2
    "2028-02-08",  # Prešeren Day
    "2028-04-17",  # Easter Monday
    "2028-04-27",  # Day of Uprising Against Occupation
    "2028-05-01",  # Labour Day
    "2028-05-02",  # Labour Day 2
    "2028-06-25",  # Statehood Day
    "2028-08-15",  # Assumption Day
    "2028-10-31",  # Reformation Day
    "2028-11-01",  # All Saints' Day
    "2028-12-25",  # Christmas Day
    "2028-12-26",  # Independence and Unity Day
    # 2029
    "2029-01-01",  # New Year's Day
    "2029-01-02",  # New Year's Day 2
    "2029-02-08",  # Prešeren Day
    "2029-04-02",  # Easter Monday
    "2029-04-27",  # Day of Uprising Against Occupation
    "2029-05-01",  # Labour Day
    "2029-05-02",  # Labour Day 2
    "2029-06-25",  # Statehood Day
    "2029-08-15",  # Assumption Day
    "2029-10-31",  # Reformation Day
    "2029-11-01",  # All Saints' Day
    "2029-12-25",  # Christmas Day
    "2029-12-26",  # Independence and Unity Day
    # 2030
    "2030-01-01",  # New Year's Day
    "2030-01-02",  # New Year's Day 2
    "2030-02-08",  # Prešeren Day
    "2030-04-22",  # Easter Monday
    "2030-04-27",  # Day of Uprising Against Occupation
    "2030-05-01",  # Labour Day
    "2030-05-02",  # Labour Day 2
    "2030-06-25",  # Statehood Day
    "2030-08-15",  # Assumption Day
    "2030-10-31",  # Reformation Day
    "2030-11-01",  # All Saints' Day
    "2030-12-25",  # Christmas Day
    "2030-12-26",  # Independence and Unity Day
    # 2031
    "2031-01-01",  # New Year's Day
    "2031-01-02",  # New Year's Day 2
    "2031-02-08",  # Prešeren Day
    "2031-04-14",  # Easter Monday
    "2031-04-27",  # Day of Uprising Against Occupation
    "2031-05-01",  # Labour Day
    "2031-05-02",  # Labour Day 2
    "2031-06-25",  # Statehood Day
    "2031-08-15",  # Assumption Day
    "2031-10-31",  # Reformation Day
    "2031-11-01",  # All Saints' Day
    "2031-12-25",  # Christmas Day
    "2031-12-26",  # Independence and Unity Day
    # 2032
    "2032-01-01",  # New Year's Day
    "2032-01-02",  # New Year's Day 2
    "2032-02-08",  # Prešeren Day
    "2032-03-29",  # Easter Monday
    "2032-04-27",  # Day of Uprising Against Occupation
    "2032-05-01",  # Labour Day
    "2032-05-02",  # Labour Day 2
    "2032-06-25",  # Statehood Day
    "2032-08-15",  # Assumption Day
    "2032-10-31",  # Reformation Day
    "2032-11-01",  # All Saints' Day
    "2032-12-25",  # Christmas Day
    "2032-12-26",  # Independence and Unity Day
    # 2033
    "2033-01-01",  # New Year's Day
    "2033-01-02",  # New Year's Day 2
    "2033-02-08",  # Prešeren Day
    "2033-04-18",  # Easter Monday
    "2033-04-27",  # Day of Uprising Against Occupation
    "2033-05-01",  # Labour Day
    "2033-05-02",  # Labour Day 2
    "2033-06-25",  # Statehood Day
    "2033-08-15",  # Assumption Day
    "2033-10-31",  # Reformation Day
    "2033-11-01",  # All Saints' Day
    "2033-12-25",  # Christmas Day
    "2033-12-26",  # Independence and Unity Day
    # 2034
    "2034-01-01",  # New Year's Day
    "2034-01-02",  # New Year's Day 2
    "2034-02-08",  # Prešeren Day
    "2034-04-10",  # Easter Monday
    "2034-04-27",  # Day of Uprising Against Occupation
    "2034-05-01",  # Labour Day
    "2034-05-02",  # Labour Day 2
    "2034-06-25",  # Statehood Day
    "2034-08-15",  # Assumption Day
    "2034-10-31",  # Reformation Day
    "2034-11-01",  # All Saints' Day
    "2034-12-25",  # Christmas Day
    "2034-12-26",  # Independence and Unity Day
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
