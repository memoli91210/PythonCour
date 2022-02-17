import cgi
import http.cookies
import datetime
import os
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# expiration=datetime.datetime.now()+ datetime.timedelta(days=365)
# expiration=expiration.strftime("%a,%d-%b-%y %H:%M:%S")

# my_cookies=http.cookies.SimpleCookie()
# my_cookies["pref_lang"]="fr"
# my_cookies["pref_lang"]["expires"]=expiration
# my_cookies["pref_lang"]["httponly"]=True

#print(my_cookies.output())

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
    <h1>Bienvenue</h1>
    <p>je fonctionne avec Python</p>
"""
print(html)

try:
  user_lang= http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
  print("la langue choisi est :", user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
  print("non trouve")
  
  
html="""
    <form method="post" action="result.py">
      <p><input type="text" name="username">
      <input type="submit" value"envoyer"></p>
    </form>
  </body>
</html>
"""
print(html)