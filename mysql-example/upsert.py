import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8')
    cursor = conn.cursor()

    cursor.execute('USE tooz')

    sql = 'INSERT INTO test (date, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name = VALUES(`name`)'
    cursor.execute(sql, ('20221026', '고윤제'))
    cursor.execute(sql, ('20221026', 'test'))

    conn.commit()
    conn.close()