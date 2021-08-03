# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    h = int(seconds/3600)
    m = int((seconds/60)%60)
    s = (seconds%60)
    # return '%02d:%02d:%02d' % (h,m,s)
    return "{0:02d}:{1:02d}:{2:02d}".format(h,m,s)

print(make_readable(36676))