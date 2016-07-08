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
echo "= Setting up env ="
source env/bin/activate || error_exit "Error, exit" 2
echo "= Entering in the application folder ="
cd masterlist  || error_exit "Error, exit" 3
echo "= Updating the database structure ="
python manage.py migrate || error_exit "Error, exit" 4
echo "= Importing the database data ="
python manage.py loaddata initial_data.json || error_exit "Error, exit" 5
echo "= Cleaning up the auto-generated static files ="
python manage.py collectstatic --clear --noinput || error_exit "Error, exit" 6
cd ..
echo "= Exiting ="
deactivate' && exit 0 || exit 127



# End
