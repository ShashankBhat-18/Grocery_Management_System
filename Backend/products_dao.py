from sqlconnection import *

def get_all_products(connection):

    cursor=connection.cursor()

    query = ('select p.product_id,p.name,p.uom_id,p.price_per_unit,u.uom_name from product p inner join uom u where p.uom_id=u.uom_id;')
    cursor.execute(query)

    response=[]

    for (product_id,product_name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({'product_id':product_id,
                        'product_name':product_name,
                        'uom_id':uom_id,
                        'price_per_unit':price_per_unit,
                        'uom_name':uom_name
                        })

    cursor.close()
    connection.close()

    return response

def insert_new_product(connection,product):

    curosor=connection.cursor()
    query=('insert into product(name,uom_id,price_per_unit) values(%s,%s,%s)')

    data=(product['product_name'],product['uom_id'],product['price_per_unit'])
    curosor.execute(query,data)

    connection.commit()
    return curosor.lastrowid

def deleterow(connection,product_id):
    curosor=connection.cursor()
    query=('delete from product where product_id='+str(product_id))
    curosor.execute(query)
    connection.commit()


connection =get_sql_connection()
'''print(insert_new_product(connection,
    {'product_name':'Banana',
     'uom_id':1,
     'price_per_unit':20}))'''
#deleterow(connection,7)
print(get_all_products(connection))