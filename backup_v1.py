import os
import time

# 1. files and catalogs, which need to be saved compile to a list
source = ['"C:\\My documents']
#if path contains some space, then use double '
# in path

# 2. Backup files must be saved in main backup catalog
target_dir = 'C:\\backups' 
    
# 3. Files put into zip archive
# 4. name of this archive is current date
target = target_dir + os.sep + time.strftime('%Y-%m-%d_%H_%M_%S') + '.zip'

# 5. Use command 'zip' to put files into archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# run backup creation
if os.system(zip_command) == 0:
    print('Backup complete in', target)
else:
    print('Backup creation failed')
    
