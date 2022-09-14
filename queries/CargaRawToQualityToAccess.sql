################## ## customers ## ################# 
create or replace table `proyectolab01caqh.proyecto_quality.customers` as 
( 
    SELECT cast(customerNumber as int64) as customerNumber, 
    customerName, 
    contactLastName, 
    contactFirstName, 
    phone, 
    addressLine1, 
    addressLine2, 
    city, 
    state, 
    postalCode, 
    country, 
    ifnull(cast(cast(salesRepEmployeeNumber as float64) as int64),0) as salesRepEmployeeNumber,
     cast(creditLimit as float64) as creditLimit 
    FROM `proyectolab01caqh.proyecto_raw.customers` ); 
    
create or replace table `proyectolab01caqh.proyecto_access.customers` as 
( 
    SELECT 
        customerNumber, 
        customerName, 
        contactLastName, 
        contactFirstName, 
        phone, 
        addressLine1, 
        addressLine2, 
        city, 
        state, 
        postalCode, 
        country, 
        salesRepEmployeeNumber, 
        creditLimit 
    FROM `proyectolab01caqh.proyecto_quality.customers` ); 
    
    
################## ## employees ## ################# 
create or replace table `proyectolab01caqh.proyecto_quality.employees` as 
( 
    SELECT cast(employeeNumber as int64) as employeeNumber, lastName, firstName, extension, email, officeCode, ifnull(cast(cast(reportsTo as float64) as int64),0) as reportsTo, jobTitle FROM `proyectolab01caqh.proyecto_raw.employees` ); create or replace table `proyectolab01caqh.proyecto_access.employees` as ( SELECT employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle FROM `proyectolab01caqh.proyecto_quality.employees` ); ################## ## offices ## ################# create or replace table `proyectolab01caqh.proyecto_quality.offices` as ( SELECT officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory FROM `proyectolab01caqh.proyecto_raw.offices` ); create or replace table `proyectolab01caqh.proyecto_access.offices` as ( SELECT officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory FROM `proyectolab01caqh.proyecto_quality.offices` ); ################## ## orders ## ################# create or replace table `proyectolab01caqh.proyecto_quality.orders` as ( SELECT cast(orderNumber as int64) as orderNumber, cast(orderDate as date) as orderDate, cast(requiredDate as date) as requiredDate, cast(shippedDate as date) as shippedDate, status, comments, cast(customerNumber as int64) as customerNumber FROM `proyectolab01caqh.proyecto_raw.orders` ); create or replace table `proyectolab01caqh.proyecto_access.orders` as ( SELECT orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber FROM `proyectolab01caqh.proyecto_quality.orders` ); ################## ## payments ## ################# create or replace table `proyectolab01caqh.proyecto_quality.payments` as ( SELECT cast(customerNumber as int64) as customerNumber, checkNumber, cast(paymentDate as date) as paymentDate, ifnull(cast(amount as float64),0) as amount FROM `proyectolab01caqh.proyecto_raw.payments` ); create or replace table `proyectolab01caqh.proyecto_access.payments` as ( SELECT customerNumber, checkNumber, paymentDate, amount FROM `proyectolab01caqh.proyecto_quality.payments` ); ################## ## productlines ## ################# create or replace table `proyectolab01caqh.proyecto_quality.productlines` as ( SELECT productLine, textDescription, htmlDescription, image FROM `proyectolab01caqh.proyecto_raw.productlines` ); create or replace table `proyectolab01caqh.proyecto_access.productlines` as ( SELECT productLine, textDescription, htmlDescription, image FROM `proyectolab01caqh.proyecto_quality.productlines` ); ################## ## products ## ################# create or replace table `proyectolab01caqh.proyecto_quality.products` as ( SELECT productCode, productName, productLine, productScale, productVendor, productDescription, ifnull(cast(quantityInStock as int64),0) as quantityInStock, ifnull(cast(buyPrice as float64),0) as buyPrice, ifnull(cast(MSRP as float64),0) as MSRP FROM `proyectolab01caqh.proyecto_raw.products` ); create or replace table `proyectolab01caqh.proyecto_access.products` as ( SELECT productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP FROM `proyectolab01caqh.proyecto_quality.products` ); ################## ## orderdetails ## ################# create or replace table `proyectolab01caqh.proyecto_quality.orderdetails` as ( SELECT ifnull(cast(orderNumber as int64),0) as orderNumber, productCode, ifnull(cast(quantityOrdered as int64),0) as quantityOrdered, ifnull(cast(priceEach as float64),0) as priceEach, ifnull(cast(replace(orderLineNumber,');','') as int64),0) as orderLineNumber FROM `proyectolab01caqh.proyecto_raw.orderdetails` ); create or replace table `proyectolab01caqh.proyecto_access.orderdetails` as ( SELECT orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber FROM `proyectolab01caqh.proyecto_quality.orderdetails` );