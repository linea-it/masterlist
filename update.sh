#!/bin/sh

# /etc/passwd will use sh
# we want to force the use of bash to have the startup env variables

bash -l -i -c '

function error_exit {
    echo "$1" >&2
    exit "${2:-1}"
}

echo "= Updating the code ="
cd $DRI_HOME
git pull || error_exit "Error, exit" 1
mkdir -p masterlist/static/django || error_exit "Error, exit" 2
echo "= Updating the images ="
test -d masterlist/static/img || git clone https://github.com/linea-it/masterlist_img.git masterlist/static/img || error_exit "Error, exit" 3
cd masterlist/static/img  || error_exit "Error, exit" 4
git pull  || error_exit "Error, exit" 5
cd ../../..
echo "= Setting up env ="
source env/bin/activate || error_exit "Error, exit" 2
echo "= Updating requirements ="
pip3 install -r requirements.txt || error_exit "Error, exit" 3
echo "= Entering in the application folder ="
cd masterlist  || error_exit "Error, exit" 4
echo "= Updating the database structure ="
python manage.py migrate || error_exit "Error, exit" 5
echo "= Importing the database data ="
python manage.py loaddata initial_data.json || error_exit "Error, exit" 6
echo "= Cleaning up the auto-generated static files ="
python manage.py collectstatic --clear --noinput || error_exit "Error, exit" 7
cd ..
### REMEMBER TO IMPLEMENT A WAY TO apache reload
echo "= Exiting ="
deactivate' && exit 0 || exit 127



# End
