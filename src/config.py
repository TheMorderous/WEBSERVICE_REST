class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER ='root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'tienda_libros'
    
config = {
    'development' : DevelopmentConfig
}

