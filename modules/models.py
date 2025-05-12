from typing import Union,Optional
from pathlib import Path
from pydantic import BaseModel

class Inputs(BaseModel):
    image1: Union[str,Path]
    image2: Union[str,Path]
    outputDir: Union[str,Path]

class ProcessModel(BaseModel):
    inputModel: Inputs
    imageObjects: list
    metadata: Optional[dict]