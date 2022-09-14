#!/usr/local/bin/python3

"""
Will backup all the databases listed, will put files in same DIR as script'
To run: $ python dbbackup.py OR python3 dbbackup.py
"""

from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import mysql.connector as sql


HOST='34.125.166.191'
PORT='3306'
DB_USER='labfinalxs'
DB_PASS='clase@patch'

db = sql.connect(
    host=HOST,
    user=DB_USER,
    password=DB_PASS,
    database="classicmodels"
)

database="classicmodels"
tables=["productlines", "products", "orders", "customers", "payments", "employees", "offices"]

credentials_dict = {
    'type': 'service_account',
    "client_id": "client_id",
    "client_email": "client_email",
    "private_key_id": "private_key_id",
    "private_key": "private_key",
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict
)
client = storage.Client(credentials=credentials, project='proyectolab01caqh')
bucket = client.get_bucket("proyectogcpgrupo3-raw")

def map_offices(result):
    try:
        offices_codes = []
        cities = []
        phones = []
        address_lines_1 = []
        address_lines_2 = []
        states = []
        countries = []
        postal_codes = []
        territories = []

        for offices_code, city, phone, address_line_1, address_line_2, state, country, postal_code, territory in result:
            offices_codes.append(offices_code)
            cities.append(city)
            phones.append(phone)
            address_lines_1.append(address_line_1)
            address_lines_2.append(address_line_2)
            states.append(state)
            countries.append(country)
            postal_codes.append(postal_code)
            territories.append(territory)
        dic = {
            "officeCode": offices_codes,
            "city": cities,
            "phone": phones,
            "addressLine1": address_lines_1,
            "addressLine2": address_lines_2,
            "state": states,
            "country": countries,
            "postalCode": postal_codes,
            "territory": territories,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/offices.csv", index=False, sep="|")
    except Exception as e:
        print("map_offices")
        print(e)    

def map_payments(result):
    try:
        customer_numbers = []
        check_numbers = []
        payment_dates = []
        amounts = []

        for customer_number, check_number, payment_date, amount in result:
            customer_numbers.append(customer_number)
            check_numbers.append(check_number)
            payment_dates.append(payment_date)
            amounts.append(amount)
        dic = {
            "customerNumber": customer_numbers,
            "checkNumber": check_numbers,
            "paymentDate": payment_dates,
            "amount": amounts,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/payments.csv", index=False, sep="|")
    except Exception as e:
        print("map_payments")
        print(e)

def map_customers(result):
    try:
        customer_numbers = []
        customer_names = []
        contact_last_names = []
        contact_first_names = []
        phones = []
        address_lines1 = []
        address_lines2 = []
        cities = []
        states = []
        postal_codes = []
        countries = []
        sales_rep_employee_numbers = []
        credit_limits = []

        for customer_number, customer_name, contact_last_name, contact_first_name, phone, address_line1, address_line2, city, state, postal_code, country, sales_rep_employee_number, credit_limit in result:
            customer_numbers.append(customer_number)
            customer_names.append(customer_name)
            contact_last_names.append(contact_last_name)
            contact_first_names.append(contact_first_name)
            phones.append(phone)
            address_lines1.append(address_line1)
            address_lines2.append(address_line2)
            cities.append(city)
            states.append(state)
            postal_codes.append(postal_code)
            countries.append(country)
            sales_rep_employee_numbers.append(sales_rep_employee_number)
            credit_limits.append(credit_limit)
        dic = {
            "customerNumber": customer_numbers,
            "customerName": customer_names,
            "contactLastName": contact_last_names,
            "contactFirstName": contact_first_names,
            "phone": phones,
            "addressLine1": address_lines1,
            "addressLine2": address_lines2,
            "city": cities,
            "state": states,
            "postalCode": postal_codes,
            "country": countries,
            "salesRepEmployeeNumber": sales_rep_employee_numbers,
            "creditLimit": credit_limits,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/customers.csv", index=False, sep="|")
    except Exception as e:
        print("map_customers")
        print(e)

def map_orders(result):
    try:
        order_numbers = []
        order_dates = []
        required_dates = []
        shipped_dates = []
        statuses = []
        comments = []
        customer_numbers = []

        for order_number, order_date, required_date,shipped_date, status, comment, customer_number in result:
            order_numbers.append(order_number)
            order_dates.append(order_date)
            required_dates.append(required_date)
            shipped_dates.append(shipped_date)
            statuses.append(status)
            comments.append(comment)
            customer_numbers.append(customer_number)
        dic = {
            "orderNumber": order_numbers,
            "orderDate": order_dates,
            "requiredDate": required_dates,
            "shippedDate": shipped_dates,
            "status": statuses,
            "comments": comments,
            "customerNumber": customer_numbers,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/orders.csv", index=False, sep="|")
    except Exception as e:
        print("map_orders")
        print(e)

def map_product_lines(result):
    try:
        product_lines = []
        text_descriptions = []
        html_descriptions = []
        images = []

        for product_line, text_description, html_description, image in result:
            product_lines.append(product_line)
            text_descriptions.append(text_description)
            html_descriptions.append(html_description)
            images.append(image)
        dic = {
            "productLine": product_lines,
            "textDescription": text_descriptions,
            "htmlDescription": html_descriptions,
            "image": images,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/productlines.csv", index=False, sep="|")
    except Exception as e:
        print("map_product_lines")
        print(e)

def map_employees(result):
    try:
        employees_numbers = []
        last_names = []
        first_names = []
        extensions = []
        emails = []
        office_codes = []
        reports_tos = []
        job_titles = []

        for employee_number, last_name, first_name, extension, email, office_code, reports_to, job_title in result:
            employees_numbers.append(employee_number)
            last_names.append(last_name)
            first_names.append(first_name)
            extensions.append(extension)
            emails.append(email)
            office_codes.append(office_code)
            reports_tos.append(reports_to)
            job_titles.append(job_title)

        dic = {
            "employeeNumber": employees_numbers,
            "lastName": last_name,
            "firstName": first_name,
            "extension": extensions,
            "email": emails,
            "officeCode": office_codes,
            "reportsTo": reports_tos,
            "jobTitle": job_titles,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/employees.csv", index=False, sep="|")
    except Exception as e:
        print("map_employees")
        print(e)


def map_products(result):
    try:
        product_codes = []
        product_names = []
        product_lines = []
        product_scales = []
        product_vendors = []
        product_descriptions = []
        quantity_in_stocks = []
        buy_prices = []
        msrps = []

        for code, name, line, scale, vendor, description, quantity, price, msrp in result:
            product_codes.append(code)
            product_names.append(name)
            product_lines.append(line)
            product_scales.append(scale)
            product_vendors.append(vendor)
            product_descriptions.append(description)
            quantity_in_stocks.append(quantity)
            buy_prices.append(price)
            msrps.append(msrp)
        dic = {
            "productCode": product_codes,
            "productName": product_names,
            "productLine": product_lines,
            "productScale": product_scales,
            "productVendor": product_vendors,
            "productDescription": product_descriptions,
            "quantityInStock": quantity_in_stocks,
            "buyPrice": buy_prices,
            "MSRP": msrps,
        }
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("csv/products.csv", index=False, sep="|")
    except Exception as e:
        print("map_products")
        print(e)

def upload_data(table):
    try:
        cr = db.cursor(buffered=True)
        query = f"SELECT * FROM {table}"
        cr.execute(query)
        result_df = cr.fetchall()
        print(table)
        if table == "productlines":
            map_product_lines(result_df)
        elif table == "products":
            map_products(result_df)
        elif table == "orders":
            map_orders(result_df)
        elif table == "customers":
            map_customers(result_df)
        elif table == "payments":
            map_payments(result_df)
        elif table == "employees":
            map_employees(result_df)
        elif table == "offices":
            map_offices(result_df)
        print(bucket)
        blob = bucket.blob(f"raw-mysql/{table}.csv")
        blob.upload_from_filename(f"./csv/{table}.csv")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    for table in tables:
        upload_data(table)

# def create_keyfile_dict():
#     variables_keys = {
#         "type": os.environ.get("SHEET_TYPE"),
#         "project_id": os.environ.get("SHEET_PROJECT_ID"),
#         "private_key_id": os.environ.get("SHEET_PRIVATE_KEY_ID"),
#         "private_key": os.environ.get("SHEET_PRIVATE_KEY"),
#         "client_email": os.environ.get("SHEET_CLIENT_EMAIL"),
#         "client_id": os.environ.get("SHEET_CLIENT_ID"),
#         "auth_uri": os.environ.get("SHEET_AUTH_URI"),
#         "token_uri": os.environ.get("SHEET_TOKEN_URI"),
#         "auth_provider_x509_cert_url": os.environ.get("SHEET_AUTH_PROVIDER_X509_CERT_URL"),
#         "client_x509_cert_url": os.environ.get("SHEET_CLIENT_X509_CERT_URL")
#     }
#     return variables_keys

# then the following should work

# scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_dict(create_keyfile_dict(), scope)
# gs = gspread.authorize(creds)


# from googleapiclient import discovery
# from oauth2client.client import GoogleCredentials

# credentials = GoogleCredentials.get_application_default()
# service = discovery.build('storage', 'v1', credentials=credentials)

# filename = 'C:\\MyFiles\\sample.csv'
# bucket = 'my_bucket'

# body = {'name': 'dest_file_name.csv'}
# req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
# resp = req.execute()