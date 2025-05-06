from typing import Union
from pathlib import Path
from pydantic import BaseModel
import numpy as np

class Inputs(BaseModel):
    image1: Union[str,Path]
    image2: Union[str,Path]
    outputDir: Union[str,Path]

class ProcessModel(BaseModel):
    inputModel: Inputs
    imageArray1: np.ndarray
    imageArray2: np.ndarray
    metadata: dict