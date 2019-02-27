import subprocess
import json
from pathlib import Path
import os

def ffprobe(file_name) -> dict:
	""" get media metadata """
	meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	file_name],
                               	)

                    
	return json.loads(meta)

def convert(vidin, vidout, fbl):
	r = subprocess.call([
			'ffmpeg', 
			'-y',
			'-i', vidin,
			'-r', '30', 
			'-s', 'hd'+str(fbl), 
			'-b:v', '1024k', 
			vidout,
			
			'-loglevel', 'quiet'])
	print('Exit code:', r)
	return True
