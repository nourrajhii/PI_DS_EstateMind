import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Standard city mapping if needed
CITY_MAPPING = {
    "tunis": "Tunis",
    "lac 1": "Les Berges du Lac",
    "lac 2": "Les Berges du Lac 2",
    "marsa": "La Marsa",
    # Add more as discovered
}

def clean_city_name(city: str) -> str:
    if not city:
        return "Unknown"
    
    city_lower = city.lower().strip()
    return CITY_MAPPING.get(city_lower, city.strip().capitalize())

def normalize_price(price_str: str) -> float:
    if not price_str:
        return 0.0
    # Basic numeric cleaner
    cleaned = ''.join(c for c in price_str if c.isdigit() or c == '.')
    try:
        return float(cleaned)
    except:
        return 0.0
