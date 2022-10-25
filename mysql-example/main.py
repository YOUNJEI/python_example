import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8')
    cursor = conn.cursor()

    cursor.execute('USE tooz')
    #cursor.execute('CREATE TABLE test2 (id int primary key, name varchar(255), money int, weight double, time date)')

    sql = 'INSERT INTO test2 (name, money, weight, time) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, ('test', '15352', '69.2', '2022/10/25'))
    cursor.execute(sql, ('test', '-100000', '50.2', '1995/12/11'))

    sql = 'SELECT * FROM test2 where name = %s'
    cursor.execute(sql, ('test',))
    result = cursor.fetchall()

    for data in result:
        print(data[0], end=" ")
        print(data[1], end=" ")
        print(data[2], end=" ")
        print(data[3], end=" ")
        print(data)

    conn.commit()
    conn.close()