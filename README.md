# Amazon Check

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=plastic)](LICENSE.md) [![approved](https://img.shields.io/badge/approved-by%20Marco%20Hecker-green.svg?style=plastic)](https://encrypted.google.com/search?q=Marco+Hecker) [![powered_by](https://img.shields.io/badge/part%20of-Likando%20Publishing-red.svg?style=plastic)](https://www.likando.de)

An Amazon price tracker written in python.
This Skript was written by [Webklex][link-contributors], but I added a ***MySQL-Database*** and ***Config-file*** to it.

### Requirements
- bs4
- configparser
- mysql-connector
- mysql-connector-python
- requests

### Installation / Setup
```bash
pip install -r requirements.txt
```
Then install a ***MySQL-Database*** with a Table. (See [create_MySQL-DB.sql](create_MySQL-DB.sql))


### Config
Edit the [settings.ini](settings.ini.sample)
```bash
[DB]
host = mysql_server
user = mysql_user
passwd = mysql_passwd
database = mysql_database

[Email]
host = smtp.gmail.com
port = 587
username = your_email@gmail.com
password = gmail_passwd

[EmailTo]
email = email_to@gmail.com
```

### Run
```bash
python main.py
```

## Credits
- [Webklex][link-contributors]

## License
The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

[link-contributors]: https://github.com/Webklex/python_amazon_price_tracker
