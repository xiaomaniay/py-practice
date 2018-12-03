from .variables import datawarehouse_name


# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'datawarehouse_sql_server',
    'database': '{}'.format(datawarehouse_name),
    'user': '',
    'password': '',
    'autocommit': True,
}

# sql-server (source db)
sqlserver_db_config = [
    {
        'Trusted_Connection': 'yes',
        'driver': '{SQL Server}',
        'server': 'your_sql_server',
        'database': 'db1',
        'user': 'your_db_username',
        'password': '',
        'autocommit': True,
    }
]

#mysql
mysql_db_config = {
    {
        'user': '',
        'password': '',
        'host': 'db_connection_string_1',
        'database': 'db_1',
    },
    {
        'user': '',
        'password': '',
        'host': 'db_connection_string_2',
        'database': 'db_2'
    },
}

#firebird
fbd_db_config = [
    {
        'dsn': '',
        'user': '',
        'password': '',
    }
]