from datasource.memory import Memory
from datasource.schema import PlotEnum

PLOT_RESOURCE_CLASS_MAPPING = {
    PlotEnum.free_memory: Memory,
}
