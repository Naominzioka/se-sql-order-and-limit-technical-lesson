import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

#order by sorts numbers first then letters in alphabetical order
#if data to be sorted is starting with a number it will sort the numbers first then 
#sort letters next

# products_table = pd.read_sql("""
# SELECT *
#   FROM products;
# """, conn)
# print(products_table)

#1
# sort_orderby_productName = pd.read_sql("""
# SELECT *
#   FROM products
#  ORDER BY productName;
# """, conn)
# print(sort_orderby_productName)

#2
# sortby_asc_order = pd.read_sql("""
# SELECT *
#   FROM products
#  ORDER BY productName ASC;
# """, conn)
# print(sortby_asc_order)

#3
# sortby_desc_order = pd.read_sql("""
# SELECT *
#   FROM products
#  ORDER BY productName DESC;
# """, conn)
# print(sortby_desc_order)

#4
# sortby_length = pd.read_sql("""
# SELECT productName, length(productDescription) AS description_length
#   FROM products
#  ORDER BY description_length;
# """, conn)
# print(sortby_length)

#5 
# sort_one_column_at_a_time = pd.read_sql("""
# SELECT productVendor, productName, MSRP
#   FROM products
#  ORDER BY productVendor, productName;
# """, conn)
# print(sort_one_column_at_a_time)

#6 the fewer the unique values a column has,
# the earlier it should appear when sorting 2 tables
# calculate_uniquevalues_in_column = pd.read_sql("""
# SELECT COUNT(DISTINCT productVendor) AS num_product_vendors,
#        COUNT(DISTINCT productName) AS num_product_names
#   FROM products;
# """, conn)
# print(calculate_uniquevalues_in_column)
#with this value product vendor is ssorted first since it has few unique values

#7 specify sort by integer and treat the numbers as integers not strings
# sort_quantityinstock_byinteger = pd.read_sql("""
# SELECT productName, quantityInStock
#   FROM products
#  ORDER BY CAST(quantityInStock AS INTEGER);
# """, conn).head(10)
# print(sort_quantityinstock_byinteger)

#8 limit the number of results to be returned
# first_5_orders = pd.read_sql("""
# SELECT *
#   FROM orders
#  LIMIT 5;
# """, conn)
# print(first_5_orders)

#9 select the 10 orders with the longest comments to start a customer service audit
# result = pd.read_sql("""
# SELECT *
#   FROM orders
#  ORDER BY length(comments) DESC
#  LIMIT 10;
# """, conn)
# print(result)

#10 filter the cancelled orders then sort
# result = pd.read_sql("""
# SELECT *
#   FROM orders
#  WHERE status IN ("Cancelled", "Resolved")
#  ORDER BY length(comments) DESC
#  LIMIT 10;
# """, conn)
# print(result)

#11 finding the first 5 customers to place an order
# first_customers = pd.read_sql("""
# SELECT DISTINCT customerNumber, orderDate
#   FROM orders
#  ORDER BY orderDate
#  LIMIT 5;
# """, conn)
# print(first_customers)


#12 orders that have not been shipped and not cancelled
# new_orders = pd.read_sql("""
# SELECT *
#   FROM orders
#  WHERE shippedDate = ""
#    AND status != "Cancelled"
#  ORDER BY orderDate DESC
#  LIMIT 10;
# """, conn)
# print(new_orders)

#13 order that took the longest to fulfill
results = pd.read_sql("""
SELECT *,
       julianday(shippedDate) - julianday(orderDate) AS days_to_fulfill
  FROM orders
 WHERE shippedDate != ""
 ORDER BY days_to_fulfill DESC
 LIMIT 1;
""", conn)
print(results)

conn.close()