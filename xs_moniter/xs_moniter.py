from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static,Label

from .xs_nvidia import CUDA_device

class Info_area(Static):
    def inject(self,control_list):
        self.control_list=control_list
        return self
    
    def compose(self):
        for ctrl in self.control_list:
            yield ctrl
    
class GPU_Info_Box(Static):

    def on_mount(self):
        # """Event handler called when widget is added to the app."""
        self.update_timer = self.set_interval(2, self.update_info, pause=False)
    
    def update_info(self):
        self.info_labels['temperature'].update(f'temperature: {self._cuda_device.temperature}C')
        self.info_labels['fan_speed'].update(f'fan_speed: {self._cuda_device.fan_speed}%')
        self.info_labels['power'].update(f'power: {self._cuda_device.power}W')
        self.info_labels['core_clock'].update(f'core clk: {self._cuda_device.core_clock}MHz')
        self.info_labels['mem_clock'].update(f'mem clk:{self._cuda_device.mem_clock}MHz')

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
         
        self.info_labels={
            'temperature': Label('',classes='info_label'),
            'fan_speed': Label('',classes='info_label'),
            'power': Label('',classes='info_label'),
            'core_clock': Label('',classes='info_label'),
            'mem_clock': Label('',classes='info_label'),
        }
        yield Label(self._cuda_device.name)
        yield Label(f'PCIe link width: x{self._cuda_device.pcie_width} at {self._cuda_device.pci_id}')
        yield Info_area(classes='info_area').inject([v for k,v in self.info_labels.items()])

class MoniterApp(App):
    CSS_PATH = "xs_moniter.css"

    BINDINGS = [
        ("d", "action_toggle_dark", "Toggle dark mode"),
    ]
    
    def on_mount(self) -> None:
        self.gpus=CUDA_device.get_gpus()
        
        for gpu in self.gpus:
            _gpu_info_box=GPU_Info_Box()
            _gpu_info_box.__dict__['_cuda_device']=gpu
            _gpu_info_box.scroll_visible()
            self.query_one("#timers").mount(_gpu_info_box)

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(id="timers")
        
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

def main():
    app = MoniterApp()
    app.run()

if __name__ == "__main__":
    main()