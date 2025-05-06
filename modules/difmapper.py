'''
DiffMapper

Image type: 

    - png
    - jpeg
    - Normal TIFF (tiff/tif)
    - GeoTIFF (tiff/tif) 
    - bmp
'''

from typing import Union
from pathlib import Path
import rasterio as rio
import numpy as np
import os

from pydantic import ValidationError

from modules.models import Inputs, ProcessModel
from modules.validators import Validators
from modules.io import IO

class DiffMapper:
    
    def __init__(self, image1:Union[str,Path], image2:Union[str,Path], output_dir:Union[str,Path]):
        if Validators.isFile(image1) and Validators.isFile(image2) and Validators.isDir(output_dir,mkdir=True):
            try:
                self.inputs = Inputs(image1=image1,image2=image2,outputDir=output_dir)
            except ValidationError as e:
                raise ValidationError(e)
        else:
            raise Exception("Invalid File Path or Directory Path")
        
        self.io = IO()
        self.data = self.io.read([self.inputs.image1,self.inputs.image2])
        
        