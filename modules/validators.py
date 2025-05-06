from typing import Union
from pathlib import Path
import os

class Validators:

    def pathValidator(path:Union[str,Path]) -> bool:
        if isinstance(path,Path):
            path = str(path)
        if os.path.exists(path):
            return True
        else:
            return False
        
    def isFile(path:Union[str,Path]) -> bool:
        if isinstance(path,Path):
            path = str(path)
        if os.path.isfile(path):
            return True
        else:
            return False
    
    def isDir(path:Union[str,Path],mkdir:bool) -> bool:
        if isinstance(path,Path):
            path = str(path)
        if os.path.isdir(path):
            return True
        else:
            if mkdir:
                os.makedirs(path,exist_ok=False)
                return True
            return False
        
    def isImage(path:Union[str,Path]) -> bool:
        if isinstance(path,Path):
            path = str(path)
        if path.endswith(".png") or path.endswith(".jpeg") or path.endswith(".jpg") or path.endswith(".tiff") or path.endswith(".tif") or path.endswith(".bmp"):
            return True
        else:
            return False
        
    def isFileOrDir(path:Union[str,Path]) -> bool:
        if isinstance(path,Path):
            path = str(path)
        if os.path.isfile(path) or os.path.isdir(path):
            return True
        else:
            return False