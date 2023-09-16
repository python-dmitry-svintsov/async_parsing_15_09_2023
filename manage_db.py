import pymysql

updt_str = 'big_img not found'

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='test',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('seccessfully connected')
    print('#'*40)
    try:
        # with connection.cursor() as cursor:
        #     delete_data = "DELETE FROM `shop_it_book` WHERE id BETWEEN 289 AND 293"
        #     cursor.execute(delete_data)
        #     connection.commit()
        #     print('selected data deleted')
        #     print('#' * 20)
        # with connection.cursor() as cursor:
        #     update_querry = f"UPDATE `shop_it_book` SET book_foto='' WHERE book_foto='{updt_str}'"
        #     cursor.execute(update_querry)
        #     connection.commit()
        #     print('data updated')
        #     print('#' * 20)
        with connection.cursor() as cursor:
            select_data = f"SELECT id, title FROM `shop_it_book`;"
            cursor.execute(select_data)
            print('Print selected data')
            print('#'*20)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()
except Exception as ex:
    print('connect error')
    print(ex)