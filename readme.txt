$sudo apt-get install libfreetype6-dev
$sudo apt-get install libjpeg-dev
$sudo apt-get install zlib1g-dev
$sudo apt-get install libpng12-dev

$virtualenv ~/ENV/sayfromage --no-site-packages

$source ~/ENV/sayfromage/bin/activate

$pip install --upgrade pip
$pip install -r requirements.txt
#pip install pillow --upgrade

$python duplicate_photos.py

$deactivate
