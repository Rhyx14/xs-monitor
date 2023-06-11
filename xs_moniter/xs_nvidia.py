import pynvml

from pynvml import * 
nvmlInit()
print("Driver: ",nvmlSystemGetDriverVersion())

class CUDA_device():
    def __init__(self,handle):
        self.handle=handle
    
    @property
    def name(self)-> str:
        return nvmlDeviceGetName(self.handle)
    
    @property
    def pci_id(self)->str:
        info=nvmlDeviceGetPciInfo_v3(self.handle)
        return info.busId
    
    @property
    def temperature(self)->str:
        return nvmlDeviceGetTemperature(self.handle,0)
    
    @property
    def power(self)->str:
        return nvmlDeviceGetPowerUsage(self.handle)/1000
        
    @property
    def fan_speed(self)->str:
        return nvmlDeviceGetFanSpeed(self.handle)
    
    @property
    def core_clock(self)->str:
        return nvmlDeviceGetClockInfo(self.handle,NVML_CLOCK_GRAPHICS)
    
    @property
    def max_core_clock(self)->str:
        # TODO catch exception if not support
        raise NotImplementedError
        # return nvmlDeviceGetClock(self.handle,NVML_CLOCK_GRAPHICS,NVML_CLOCK_ID_APP_CLOCK_DEFAULT)

    @property
    def mem_clock(self)->str:
        return nvmlDeviceGetClockInfo(self.handle,NVML_CLOCK_MEM)
    
    @property
    def pcie_width(self)->str:
        return nvmlDeviceGetCurrPcieLinkWidth(self.handle)
    
    @property
    def pcie_io(self)->str:
        return nvmlDeviceGetPcieThroughput(self.handle)

    @staticmethod
    def get_gpus()-> list:
        rslt=[]
        deviceCount = nvmlDeviceGetCount() 
        for i in range(deviceCount): 
            rslt.append(nvmlDeviceGetHandleByIndex(i))
        return map(lambda h: CUDA_device(h),rslt)    

# nvmlShutdown()
if __name__=='__main__':
    pass