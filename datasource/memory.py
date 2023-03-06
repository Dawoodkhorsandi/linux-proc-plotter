import time

from datasource.base_resource import BaseResource
from datasource.schema import PlotEnum, DataPacketSchema


class Memory(BaseResource):
    def field_names(self):
        return ['MemTotal',
                'MemFree',
                'MemAvailable']


    def get_data(self, plot_type: PlotEnum = None) -> DataPacketSchema:
        if plot_type == PlotEnum.free_memory.value:
            return self._get_free_used_memory_data()

    def _get_free_used_memory_data(self) -> DataPacketSchema:
        raw_data = self.read_raw_data()
        for line in raw_data:
            if 'MemFree' in line:
                splitted_line = line.split(':')
                return DataPacketSchema(field_name='Free memory',
                                             x_label='Free Memory',
                                             y_label='Time (s)',
                                             x=time.time(),
                                             y=float(splitted_line[1].lower().replace('kb', '')))

    def file_path(self):
        return '/proc/meminfo'
