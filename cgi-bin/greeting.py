#!/usr/bin/env python3

#importing the needed modules for using the inputs through thr html form
import cgi
import cgitb

# enabling this module is needed to log errors to the browser
cgitb.enable()
# this stores the inputs in the FieldStorage Class
form = cgi.FieldStorage()
# this stores the value from the input in a variable
username = form.getvalue("username", "Your_Name")

# this is the part which the website is made of. the username variable is inserted and used here
website = """
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>Hello, {}</h1>
        <p>Hey {} you are looking good today!</p>
    </body>
</html>
""".format(username, username)
print(website)