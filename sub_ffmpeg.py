import subprocess
import threading
from queue import Queue

#main function
def call_F(q, m):
	file1 = '480' + str(m) + '.mp4'
	file2 = '720' + str(m) + '.mp4'		
	fname = [file1, file2]
	q.put(fname)

def ffedit(q):
	if not q.empty():
		name = q.get()
		print('$ nslookup www.python.org')
		r = subprocess.call([
			'ffmpeg', 
			'-y',
			'-i', 'test.mp4',
			'-r', '30', 
			'-s', 'hd480', 
			'-b:v', '1024k', 
			name[0],
			'-r', '30',
			'-s', 'hd720',
			'-b:v', '2048k',
			name[1],
			'-loglevel', 'quiet'])
		print('Exit code:', r)
		q.task_done()

def gen_Thread(n):
	i = 1
	q = Queue()
	while i < n :	
		print(i)
		t = threading.Thread(target=call_F, args=(q, str(i)))
		t1 = threading.Thread(target=ffedit, args=(q, ))
		t.start()
		t1.start()
		i += 1
	t.join()
	t1.join()
	q.join()
	print('m')
		


gen_Thread(10)