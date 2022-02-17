import cgi
import cgitb

cgitb.enable()  #mode debug active
form=cgi.FieldStorage()


print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Une page web avec Python</title>
  </head>
  <body>
"""

print(html)

try:
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"<p>Bonjour {username}</p>")
    else:
        raise Exception("speudo non valide")
except:
    print("<p>pseudo non transmis</p>")
 
html="""  
  </body>
</html>
"""
print(html)