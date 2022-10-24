import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8')
    cursor = conn.cursor()

    cursor.execute('USE tooz')
    #cursor.execute('CREATE TABLE test (id int primary key, name varchar(255))')

    sql = 'INSERT INTO test (name) VALUES (%s)'
    cursor.execute(sql, ('test',))
    cursor.execute(sql, ('test',))
    cursor.execute(sql, ('test',))

    sql = 'SELECT * FROM test where name = %s'
    cursor.execute(sql, ('test',))
    result = cursor.fetchall()

    for data in result:
        print(data[0], end=" ")
        print(data[1], end=" ")
        print(data)

    conn.commit()
    conn.close()