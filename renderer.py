from datasource.schema import PlotEnum
from datasource.mapping import PLOT_RESOURCE_CLASS_MAPPING
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Renderer:
    def __init__(self,
                 selected_plot: PlotEnum):
        self.selected_plot = selected_plot
        self.xs = []
        self.ys = []

    def resource_class(self):
        klass = PLOT_RESOURCE_CLASS_MAPPING.get(self.selected_plot)
        assert klass, 'Selected plot is not available.'
        return klass

    def run(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_autoscaley_on(True)

        ani = animation.FuncAnimation(self.fig, self.update_data, interval=100, cache_frame_data=False)
        plt.show()

    def update_data(self, frame):
        resource_class = self.resource_class()
        data = resource_class().get_data(self.selected_plot)
        plt.xlabel(data.x_label)
        plt.ylabel(data.y_label)
        plt.title(data.field_name)
        self.ax.set_xlim(data.x - 60, data.x)
        self.xs.append(data.x)
        self.ys.append(data.y)
        self.ax.plot(self.xs, self.ys, color='blue')
