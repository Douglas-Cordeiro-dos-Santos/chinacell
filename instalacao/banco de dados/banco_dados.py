import mysql.connector

#ALTERE DE ACORDO COM SEU BANCO DE DADOS
config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
}

def create_database_and_tables(cursor):
    cursor.execute("CREATE DATABASE chinacell")
    cursor.execute("USE chinacell")
    
    TABLES = {}
    TABLES['estoque'] = (
        "CREATE TABLE `estoque` ("
        "  `ID` INT NOT NULL AUTO_INCREMENT,"
        "  `PRODUTO` VARCHAR(255) NOT NULL,"
        "  `QUANTIDADE` VARCHAR(255) NOT NULL,"
        "  `COD_BARRAS` VARCHAR(13),"
        "  `PRECO_UNIT` VARCHAR(6) NOT NULL,"
        "  `CATEGORIA` VARCHAR(255),"
        "  `PRECO_TOTAL` VARCHAR(6),"
        "  PRIMARY KEY (`ID`)"
        ") ")

    TABLES['usuarios'] = (
        "CREATE TABLE `usuarios` ("
        "  `ID` INT NOT NULL AUTO_INCREMENT,"
        "  `NOME` VARCHAR(20) NOT NULL,"
        "  `SENHA` VARCHAR(20) NOT NULL,"
        "  PRIMARY KEY (`ID`)"
        ") ")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        
        cursor.execute(table_description)

    cursor.execute("INSERT INTO usuarios (NOME, SENHA) VALUES ('admin', 'admin')")

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

create_database_and_tables(cursor)
conn.commit()

cursor.close()
conn.close()
