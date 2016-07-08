#!/bin/sh

# /etc/passwd will use sh
# we want to force the use of bash to have the startup env variables

bash -l -i -c '

function error_exit {
    echo "$1" >&2
    exit "${2:-1}"
}

echo
echo "= Updating the code ="
cd $DRI_HOME
git pull || error_exit "Error, exit" 1
mkdir -p masterlist/static/django || error_exit "Error, exit" 2

echo
echo "= Updating the images ="
test -d masterlist/static/img || git clone https://github.com/linea-it/masterlist_img.git masterlist/static/img || error_exit "Error, exit" 3
cd masterlist/static/img  || error_exit "Error, exit" 4
git pull  || error_exit "Error, exit" 5
cd ../../..

echo
echo "= Setting up env ="
source env/bin/activate || error_exit "Error, exit" 6

echo
echo "= Updating requirements ="
pip3 install -U -r requirements.txt || error_exit "Error, exit" 7

echo
echo "= Entering in the application folder ="
cd masterlist  || error_exit "Error, exit" 8

echo
echo "= Updating the database structure ="
python manage.py migrate || error_exit "Error, exit" 9

echo
echo "= Importing the database data ="
python manage.py loaddata initial_data.json || error_exit "Error, exit" 10

echo
echo "= Cleaning up the auto-generated static files ="
python manage.py collectstatic --clear --noinput --verbosity 0 || error_exit "Error, exit" 11
cd ..
### REMEMBER TO IMPLEMENT A WAY TO apache reload

echo
echo "= Exiting ="
deactivate' && exit 0 || exit 127



# End
