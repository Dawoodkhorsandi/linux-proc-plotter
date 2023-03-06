from dataclasses import dataclass
from enum import Enum


class PlotEnum(str, Enum):
    used_memory = 'used_memory'
    free_memory = 'free_memory'


@dataclass
class DataPacketSchema:
    field_name: str
    x: float
    x_label: str
    y: float
    y_label: str
