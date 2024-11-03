"""Constants for the Slovenia Electricity Block integration."""

DOMAIN = "slo_electricity_block"

# Configuration keys
CONF_POWER_LIMIT_1 = "Block 1"
CONF_POWER_LIMIT_2 = "Block 2"
CONF_POWER_LIMIT_3 = "Block 3"
CONF_POWER_LIMIT_4 = "Block 4"
CONF_POWER_LIMIT_5 = "Block 5"
CONF_POWER_METER = "Power Meter"

# Default power limits in kW
DEFAULT_POWER_LIMIT = 7  # 7kW default

# Slovenian holidays for 2024-2034
HOLIDAYS = [
    # ... (previous holiday entries remain unchanged)
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
