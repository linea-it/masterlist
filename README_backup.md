
## Run a sample of the code on your local host (only for example purposes)
### Run the app in development mode
```
  $ cd masterlist
  $ ./run.sh
```
1. The first time you will be asked to set a database password, use ```nobody```.
2. The app will run in your browser at http://localhost:8000

## Modifying the Web Page Back end
1.remove the old ```db.sqlite3``` databse and execute the ```run.sh``` script again to create a new db.
2. You can add/edit entries in the database using the Administration interface at http://localhost:8000/admin.
3. Use the username: ```nobody``` and password: ```nobody``` to access the admin interface.
4. The table allows an image column, if you place an image under ```static/img``` and register the name of the image file in the ```thumb``` column the corresponding image will appear in the table.

