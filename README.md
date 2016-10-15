# Master List

Developed initially for the DES SL group to handle list of candidates for follow up, but can handle any list of objects

## Getting started 
### Cloning the project

```
  $ git clone https://github.com/linea-it/masterlist.git
```

### Create a virtualenv and install software dependencies
```
  $ cd masterlist
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
```

## Run a sample of the code on your local host (only for example purposes)
### Run the app in development mode
```
  $ cd masterlist
  $ ./run.sh
```
1. The first time you will be asked to set a database password, use ```nobody```.
2. The app will run in your browser at http://localhost:8000

## Modifying the Web Page Back end
remove the old ```db.sqlite3``` databse and execute the ```run.sh``` script again to create a new db.
2. You can add/edit entries in the database using the Administration interface at http://localhost:8000/admin.
3. Use the username: ```nobody``` and password: ```nobody``` to access the admin interface.
4. The table allows an image column, if you place an image under ```static/img``` and register the name of
the image file in the ```thumb``` column the corresponding image will appear in the table.

### Changing the page layout
1. The layout of the page is defined at ```masterlist/candidates/templates```

### Customizing the table content
1. See ```masterlist/candidates/models.py``` to customize the columns of your table, once you changed the model

### Migrating changes
1. Perform the following if you have updated the page layout or the column definitions (from path ~/masterlist/masterlist/)):

``` 
$ python manage.py makemigrations
$ python manage.py migrate
```


## Updating the master catalog with a list of new objects

### Running the updater
1. Run the updater (update_masterlist.py) from the command line

```
$ python update_masterlist.py <input file> 
```

2. Run the updater with help to get the available options

```
$ python update_master.py -h

usage: update_masterlist.py [-h] [-t] [-b] [-i I]

description: update the masterlist by adding a list of objects from an input
file.

optional arguments:
  -h, --help       show this help message and exit
  -t, --test       test appending a list
  -b, --backup     create a backup of the masterlist only
  -i I, --input I  input file name
```


### File format for the list of new objects
1. The file format must be ".csv"
2. The required headings are:
``` ra, dec, data_season, rank ```

