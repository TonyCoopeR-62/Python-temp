import os
import time

# 1. Files that need to be backuped
source = ['"C:\\My documents"']
# 2. Backups must be saved in main backup catalog
target_dir = 'C:\\backups'
# 3. Files put into archive
# 4. Current date serves as name of subcatalog in main catalog
today = target_dir + os.sep + time.strftime('%Y_%m_%d')
# 5. Current time serves as name of zip-archive
now = time.strftime('%H_%M_%S')

# create catalog, if doesn't yet
if not os.path.exists(today):
    os.mkdir(today) # create catalog
print('Catalog create success', today)
# name of zip-file
target = today + os.sep + now + '.zip'

# 5.Use zip command to add files to archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# run backup process
if os.system(zip_command) == 0:
    print('Backup complete in', target)
else:
    print('Backup failed')
