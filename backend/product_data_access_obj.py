import mysql.connector
from sql_conn import get_sql_connection
def get_all_product(connection):


    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.uom_id, products.product_price_per_unit, uom.uom_name "
            "FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")

    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, product_price_per_unit, uom_name) in cursor:
        response.append(
            {
                "product_id": product_id,
                'name':name,
                'uom_id': uom_id,
                'product_price_per_unit': product_price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(product_id) FROM products")
    max_product_id = cursor.fetchone()[0]  # Pobierz maksymalny product_id
    new_product_id = max_product_id + 1

    query = ("insert into products "
             "(product_id, name, uom_id, product_price_per_unit) "
             "values (%s, %s, %s, %s)")
    data = (product['product_id'], product['product_name'], product['uom_id'], product['product_price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    curosor = connection.cursor()
    query = ("delete from products where product_id=" + str(product_id))
    curosor.execute(query)
    connection.commit()
def last_product_id(connection, all_products):

    max_product_id = max(all_products, key=lambda x: x['product_id'])

    return int(max_product_id['product_id'])


if __name__ == '__main__':
    connection = get_sql_connection()
    allProduct = get_all_product(connection)
    insert_new_product(connection, {'product_id': last_product_id(connection, allProduct) + 1,
                                    'product_name': 'cucumber',
                                    'uom_id': '1',
                                    'product_price_per_unit': '15'})


    print(type(last_product_id(connection, allProduct)))
    delete_product(connection, last_product_id(connection, allProduct))

