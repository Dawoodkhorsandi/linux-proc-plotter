from datasource.schema import PlotEnum
from renderer import Renderer

if __name__ == '__main__':
    Renderer(PlotEnum.free_memory).run()