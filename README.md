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
1. Run the updater (update_masterlist.py) from the command line.

```
$ python update_masterlist.py <input file> 
```

### Updater commandline options
1. Run the updater with 'help' option to get the available options.

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

