
def convert_bytes(size):
   for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
       if size < 1024.0:
           return "%1.2f %s" % (size, x)
       size /= 1024.0

   return size
