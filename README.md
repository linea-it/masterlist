# Master List

Developed initially for the DES SL group to handle list of candidates for follow up, but can handle any list of objects

## Cloning the project

```
  $ git clone https://github.com/linea-it/masterlist.git
```

## Create a virtualenv and install software dependencies
```
  $ cd masterlist
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
```

## Run the app in development mode
```
  $ cd masterlist
  $ ./run.sh
```

the first time you will be asked to set a database password, use ```nobody```.


The app will run in our browser at http://localhost:8000

## Changing the page layout
The layout of the page is defined at ```masterlist/candidates/templates```

## Customizing the table content
See ```masterlist/candidates/models.py``` to customize the columns of your table, once you changed the model, just
remove the old ```db.sqlite3``` databse and execute the ```run.sh``` script again to create a new db.

You can add/edit entries in the database using the Administration interface at http://localhost:8000/admin.

Use the username: ```nobody``` and password: ```nobody``` to access the admin interface.

The table allows an image column, if you place an image under ```static\img``` and register the name of
the image file in the ```thumb``` column the corresponding image will appear in the table.

