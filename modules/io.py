from typing import Union
from pathlib import Path
import rasterio as rio

class IO:

    def __init__(self):
        pass

    def read(self,paths: Union[Union[str,Path], list[Union[str,Path]]]):
        print("IO:",paths)
        if isinstance(paths, list):
            return [rio.open(path).read() for path in paths]
        else:
            return rio.open(paths).read()

    def write(self,path:str):
        pass