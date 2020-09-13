from libqtile.widget.volume import Volume
from libqtile.widget.memory import Memory
from libqtile.widget.cpu import CPU
from libqtile.widget.wlan import Wlan

from libqtile.log_utils import logger
import iwlib
import psutil


#--------------- Volume -----------------
class Volume(Volume):
    def __init__(self, **config):
        super().__init__(**config)
        self.low_thresshold  = config['low_thresshold']  if 'low_thresshold'  in config.keys() else 10
        self.high_thresshold = config['high_thresshold'] if 'high_thresshold' in config.keys() else 50

    def _update_drawer(self):
        if self.volume == -1:
            self.text = ''
        elif self.volume < self.low_thresshold:
            self.text = ' {}%'.format(self.volume)
        elif self.volume < self.high_thresshold:
            self.text = ' {}%'.format(self.volume)
        else:
            self.text = ' {}%'.format(self.volume)


#--------------- Memory -----------------
class Memory(Memory):
    def poll(self):
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        val = {}
        val["MemUsed"]   = round(mem.used     // 1024 // 1024 / 1024, 1)
        val["MemTotal"]  = round(mem.total    // 1024 // 1024 / 1024, 1)
        val["MemFree"]   = round(mem.free     // 1024 // 1024 / 1024, 1)
        val["Buffers"]   = round(mem.buffers  // 1024 // 1024 / 1024, 1)
        val["Active"]    = round(mem.active   // 1024 // 1024 / 1024, 1)
        val["Inactive"]  = round(mem.inactive // 1024 // 1024 / 1024, 1)
        val["Shmem"]     = round(mem.shared   // 1024 // 1024 / 1024, 1)
        val["SwapTotal"] = round(swap.total   // 1024 // 1024 / 1024, 1)
        val["SwapFree"]  = round(swap.free    // 1024 // 1024 / 1024, 1)
        val["SwapUsed"]  = round(swap.used    // 1024 // 1024 / 1024, 1)

        val["MemFree"] = round(val["MemTotal"] - val["MemUsed"], 1)

        if val["MemFree"] < 0.5:
            color = "#ff0000"
            val["SwapFree"] = " / Swap {}G".format(val["SwapFree"])
        elif val["MemFree"] < 1.0:
            color = "#fffC00"
            val["SwapFree"] = ""
        else:
            color = "#d0d0d0"
            val["SwapFree"] = ""

        return self.format.format(**val, color=color)

#--------------- CPU -----------------
class CPU(CPU):
    def poll(self):
        variables = dict()

        variables["load_percent"] = round(psutil.cpu_percent(), 1)
        freq = psutil.cpu_freq()
        variables["freq_current"] = round(freq.current / 1000, 1)
        variables["freq_max"] = round(freq.max / 1000, 1)
        variables["freq_min"] = round(freq.min / 1000, 1)

        color = "#d0d0d0"
        if variables["load_percent"] > 50:
           color = "#fffc00"
        if variables["load_percent"] > 80:
           color = "#ff0000"

        return self.format.format(**variables, color=color)


#--------------- Wifi -----------------
def get_status(interface_name):
    interface = iwlib.get_iwconfig(interface_name)
    if 'stats' not in interface:
        return None, None
    quality = interface['stats']['quality']
    essid = bytes(interface['ESSID']).decode()
    return essid, quality

class Wifi(Wlan):
    def poll(self):
        try:
            essid, quality = get_status(self.interface)
            disconnected = essid is None
            if disconnected:
                return self.disconnected_message

            if quality < 0.3*70:	#max quality = 70
                color = "#fffC00"
            else:
                color = "#00ff7f"
                #color = "#d0d0d0"

            return self.format.format(
                essid=essid,
                quality=quality,
                percent=(quality / 70),
                color=color
            )
        except EnvironmentError:
            logger.error(
                '%s: Probably your wlan device is switched off or '
                ' otherwise not present in your system.',
                self.__class__.__name__)
