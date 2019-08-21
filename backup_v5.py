import time
import os
import zipfile

#1. Files and catalogs which needed to be copy, add to list
source = ['"C:\\My documents']
# if name contains space use double quotes

#2. Backups must be in main catalog
target_dir = 'C:\\backups'

#3. Files add to archive
#4. Subcatalog name is current date
today = target_dir + os.sep + time.strftime('%Y_%m_%d')
# zip archive name is current time
now = time.strftime('%H_%M_%S')

# request user comment
comment = input('Input your comment--->')
if len(comment) == 0: # check for empty
    target = today + os.sep + now + '.zip' 
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

# Create folder, if it doesn't yet
if not os.path.exists(today):
    os.mkdir(today)
print('Folder successfully create!', today)

#5. Use zip command to move files into zip archive
zipf = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

# Run backup process
if zipfile.is_zipfile('zipf') == True:
    print('backup COMPLETE!!!-->', target)
else:
    print('backup FAILED')


