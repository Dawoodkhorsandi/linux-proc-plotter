from typing import List
from abc import abstractmethod

from datasource.schema import PlotEnum, DataPacketSchema


class BaseResource:
    @abstractmethod
    def field_names(self):
        raise NotImplementedError

    @abstractmethod
    def file_path(self):
        raise NotImplementedError

    @abstractmethod
    def get_data(self, plot_type: PlotEnum = None) -> List[DataPacketSchema]:
        raise

    def read_raw_data(self):
        with open(self.file_path(), 'r') as f:
            return f.readlines()