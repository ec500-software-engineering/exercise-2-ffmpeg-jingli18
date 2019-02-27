import subprocess
import json
import os
from pathlib import Path

def ffprobe_sync(filein: Path) -> dict:
	""" get media metadata """
	meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(filein)],
                               	text=True)
return json.loads(meta)
dic = os.getcwd()
dic = dic +"\\test.mp4"
ffprobe_sync(dic)
