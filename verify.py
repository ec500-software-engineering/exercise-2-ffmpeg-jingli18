from myffmpeg import ffprobe as probe
from myffmpeg import convert as convert
from pytest import approx

def test_duration():
    fnin = 'test.mp4'
    fnout = '4801.mp4'

    orig_meta = probe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    if(convert(fnin, fnout, 480)):
        meta_480 = probe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    print(orig_duration)
    print(duration_480)
    if ((orig_duration-duration_480)<0.3):
    	return True
    else:
    	return False

print(test_duration())
 
