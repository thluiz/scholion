---
url: "http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html"
captured_at: "2020-05-26T21:29:50-03:00"
title: "Using FOR XML EXPLICIT"
domain: "dcx-sap-com"
---

# Using FOR XML EXPLICIT

FOR XML EXPLICIT allows you to control the structure of the XML document returned by the query. The query must be written
in a particular way so that information about the nesting you want is specified within the query result. The optional directives
supported by FOR XML EXPLICIT allow you to configure the treatment of individual columns. For example, you can control whether
a column appears as element or attribute content, or whether a column is used only to order the result, rather than appearing
in the generated XML.

For an example of how to write a query using FOR XML EXPLICIT, see [Writing an EXPLICIT mode query](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#writing-explicit-mode-query-example).

In EXPLICIT mode, the first two columns in the SELECT statement must be named **Tag** and **Parent**, respectively. Tag and Parent are metadata columns, and their values are used to determine the parent-child relationship,
or nesting, of the elements in the XML document that is returned by the query.

- **Tag column** 
  This is the first column specified in the select list. The Tag column stores the tag number of the current element.
  Permitted values for tag numbers are 1 to 255.
- **Parent column** 
  This column stores the tag number for the parent of the current element. If the value in this column is NULL, the row
  is placed at the top level of the XML hierarchy.

For example, consider a query that returns the following result set when FOR XML EXPLICIT is not specified. (The purpose of
the GivenName!1 and ID!2 data columns is discussed in the following section, [Adding data columns to the query](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#explicit-mode-adding-data-columns).)

| Tag | Parent | GivenName!1 | ID!2 |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| 1 | NULL | 'Beth' | NULL |
| 2 | NULL | NULL | '102' |

In this example, the values in the Tag column are the tag numbers for each element in the result set. The Parent column for
both rows contains the value NULL. This means that both elements are generated at the top level of the hierarchy, giving the
following result when the query includes the FOR XML EXPLICIT clause:

|  |  |
| --- | --- |
|  | ``` <GivenName>Beth</GivenName> <ID>102</ID> ``` |

However, if the second row had the value 1 in the Parent column, the result would look as follows:

|  |  |
| --- | --- |
|  | ``` <GivenName>Beth    <ID>102</ID> </GivenName> ``` |

For an example of how to write a query using FOR XML EXPLICIT, see [Writing an EXPLICIT mode query](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#writing-explicit-mode-query-example).

In addition to the Tag and Parent columns, the query must also contain one or more data columns. The names of these data columns
control how the columns are interpreted during tagging. Each column name is split into fields separated by an exclamation
mark (!). The following fields can be specified for data columns:

```
ElementName!TagNumber!AttributeName!Directive
```

**ElementName**  
the name of the element. For a given row, the name of the element generated for the row is taken from the *ElementName* field of the first column with a matching tag number. If there are multiple columns with the same *TagNumber*, the *ElementName* is ignored for subsequent columns with the same *TagNumber*. In the example above, the first row generates an element called <GivenName>.

**TagNumber**  
the tag number of the element. For a row with a given tag value, all columns with the same value in their *TagNumber* field will contribute content to the element that corresponds to that row.

**AttributeName**  
specifies that the column value is an attribute of the *ElementName* element. For example, if a data column had the name productID!1!Color, then Color would appear as an attribute of the <productID>
element.

**Directive**  
this optional field allows you to control the format of the XML document further. You can specify any one of the following
values for *Directive*:

- **hide** 
  indicates that this column is ignored when generating the result. This directive can be used to include columns that
  are only used to order the table. The attribute name is ignored and does not appear in the result.

  For an example using the hide directive, see [Using the hide directive](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#hide-directive-example).
- **element** 
  indicates that the column value is inserted as a nested element with the name *AttributeName*, rather than as an attribute.

  For an example using the element directive, see [Using the element directive](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#element-directive-example).
- **xml** 
  indicates that the column value is inserted with no quoting. If the *AttributeName* is specified, the value is inserted as an element with that name. Otherwise, it is inserted with no wrapping element. If
  this directive is not used, then markup characters are escaped unless the column is of type XML. For example, the value <a/>
  would be inserted as <a/>.

  For an example using the xml directive, see [Using the xml directive](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#xml-directive-using-example).
- **cdata** 
  indicates that the column value is to be inserted as a CDATA section. The *AttributeName* is ignored.

  For an example using the cdata directive, see [Using the cdata directive](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#cdata-directive-example).

Data in BINARY, LONG BINARY, IMAGE, and VARBINARY columns is automatically returned in base64-encoded format when you execute
a query that contains FOR XML EXPLICIT. By default, any NULL values in the result set are omitted. You can change this behavior
by changing the setting of the for\_xml\_null\_treatment option.

For more information about the for\_xml\_null\_treatment option, see [for\_xml\_null\_treatment option](http://dcx.sap.com/1200/en/dbadmin/dboptions-s-4270796.html) and [FOR XML and NULL values](http://dcx.sap.com/1200/en/dbusage/forxml-null.html).

Suppose you want to write a query using FOR XML EXPLICIT that generates the following XML document:

|  |  |
| --- | --- |
|  | ``` <employee EmployeeID='129'>    <customer CustomerID='107' Region='Eastern'/>    <customer CustomerID='119' Region='Western'/>    <customer CustomerID='131' Region='Eastern'/> </employee> <employee EmployeeID='195'>    <customer CustomerID='109' Region='Eastern'/>    <customer CustomerID='121' Region='Central'/> </employee> ``` |

You do this by writing a SELECT statement that returns the following result set in the exact order specified, and then appending
FOR XML EXPLICIT to the query.

| Tag | Parent | employee!1!EmployeeID | customer!2!CustomerID | customer!2!Region |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | NULL | 129 | NULL | NULL |
| 2 | 1 | 129 | 107 | Eastern |
| 2 | 1 | 129 | 119 | Western |
| 2 | 1 | 129 | 131 | Central |
| 1 | NULL | 195 | NULL | NULL |
| 2 | 1 | 195 | 109 | Eastern |
| 2 | 1 | 195 | 121 | Central |

When you write your query, only some of the columns for a given row become part of the generated XML document. A column is
included in the XML document only if the value in the *TagNumber* field (the second field in the column name) matches the value in the Tag column.

In the example, the third column is used for the two rows that have the value 1 in their Tag column. In the fourth and fifth
columns, the values are used for the rows that have the value 2 in their Tag column. The element names are taken from the
first field in the column name. In this case, <employee> and <customer> elements are created.

The attribute names come from the third field in the column name, so an EmployeeID attribute is created for <employee> elements,
while CustomerID and Region attributes are generated for <customer> elements.

The following steps explain how to construct the FOR XML EXPLICIT query that generates an XML document similar to the one
found at the beginning of this section using the SQL Anywhere sample database.

1. Write a SELECT statement to generate the top-level elements.

   In this example, the first SELECT statement in the query generates the <employee> elements. The first two values in the query
   must be the Tag and Parent column values. The <employee> element is at the top of the hierarchy, so it is assigned a Tag value
   of 1, and a Parent value of NULL.

   ###### Note

   If you are writing an EXPLICIT mode query that uses a UNION, then only the column names specified in the first SELECT statement
   are used. Column names that are to be used as element or attribute names must be specified in the first SELECT statement because
   column names specified in subsequent SELECT statements are ignored.

   To generate the <employee> elements for the table above, your first SELECT statement is as follows:

   |  |  |
   | --- | --- |
   |  | ``` SELECT       1          AS tag,       NULL       AS parent,       EmployeeID AS [employee!1!EmployeeID],       NULL       AS [customer!2!CustomerID],       NULL       AS [customer!2!Region] FROM Employees; ``` |
2. Write a SELECT statement to generate the child elements.

   The second query generates the <customer> elements. Because this is an EXPLICIT mode query, the first two values specified
   in all the SELECT statements must be the Tag and Parent values. The <customer> element is given the tag number 2, and because
   it is a child of the <employee> element, it has a Parent value of 1. The first SELECT statement has already specified that
   EmployeeID, CustomerID, and Region are attributes.

   |  |  |
   | --- | --- |
   |  | ``` SELECT       2,       1,       EmployeeID,       CustomerID,       Region FROM Employees KEY JOIN SalesOrders ``` |
3. Add a UNION ALL to the query to combine the two SELECT statements together:

   |  |  |
   | --- | --- |
   |  | ``` SELECT       1          AS tag,       NULL       AS parent,       EmployeeID AS [employee!1!EmployeeID],       NULL       AS [customer!2!CustomerID],       NULL       AS [customer!2!Region] FROM Employees UNION ALL  SELECT       2,       1,       EmployeeID,       CustomerID,       Region FROM Employees KEY JOIN SalesOrders ``` |
4. Add an ORDER BY clause to specify the order of the rows in the result. The order of the rows is the order that is used in
   the resulting document.

   |  |  |
   | --- | --- |
   |  | ``` SELECT       1          AS tag,       NULL       AS parent,       EmployeeID AS [employee!1!EmployeeID],       NULL       AS [customer!2!CustomerID],       NULL       AS [customer!2!Region] FROM Employees UNION ALL  SELECT       2,       1,       EmployeeID,       CustomerID,       Region FROM Employees KEY JOIN SalesOrders ORDER BY 3, 1 FOR XML EXPLICIT; ``` |

For information about the syntax of EXPLICIT mode, see [Parameters](http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html#for-xml-explicit-parameters-info).

The following example query retrieves information about the orders placed by employees. In this example, there are three types
of elements: <employee>, <order>, and <department>. The <employee> element has ID and name attributes, the <order> element
has a date attribute, and the <department> element has a name attribute.

|  |  |
| --- | --- |
|  | ``` SELECT         1           tag,         NULL        parent,         EmployeeID  [employee!1!ID],         GivenName   [employee!1!name],         NULL        [order!2!date],         NULL        [department!3!name] FROM Employees UNION ALL  SELECT         2,         1,         EmployeeID,         NULL,         OrderDate,         NULL FROM Employees KEY JOIN SalesOrders UNION ALL  SELECT         3,         1,         EmployeeID,         NULL,         NULL,         DepartmentName FROM Employees e JOIN Departments d    ON e.DepartmentID=d.DepartmentID ORDER BY 3, 1 FOR XML EXPLICIT; ``` |

You get the following result from this query:

|  |  |
| --- | --- |
|  | ``` <employee ID="102" name="Fran">    <department name="R & D"/> </employee> <employee ID="105" name="Matthew">    <department name="R & D"/> </employee>  <employee ID="129" name="Philip">    <order date="2000-07-24"/>    <order date="2000-07-13"/>    <order date="2000-06-24"/>    <order date="2000-06-08"/>    ...    <department name="Sales"/> </employee>  <employee ID="148" name="Julie">    <department name="Finance"/> </employee> ... ``` |

If you want to generate sub-elements rather than attributes, you can add the element directive to the query, as follows:

|  |  |
| --- | --- |
|  | ``` SELECT         1          tag,         NULL       parent,         EmployeeID [employee!1!id!element],         GivenName  [employee!1!name!element],         NULL       [order!2!date!element],         NULL       [department!3!name!element] FROM Employees  UNION ALL SELECT         2,         1,         EmployeeID,         NULL,         OrderDate,         NULL FROM Employees KEY JOIN SalesOrders UNION ALL  SELECT         3,         1,         EmployeeID,         NULL,         NULL,         DepartmentName FROM Employees e JOIN Departments d    ON e.DepartmentID=d.DepartmentID ORDER BY 3, 1 FOR XML EXPLICIT; ``` |

You get the following result from this query:

|  |  |
| --- | --- |
|  | ``` <employee>    <id>102</id>    <name>Fran</name>    <department>       <name>R & D</name>    </department> </employee>  <employee>    <id>105</id>    <name>Matthew</name>    <department>       <name>R & D</name>    </department> </employee>  <employee>    <id>129</id>    <name>Philip</name>    <order>       <date>2000-07-24</date>    </order>    <order>       <date>2000-07-13</date>    </order>    <order>       <date>2000-06-24</date>    </order>    ...    <department>       <name>Sales</name>    </department> </employee> ... ``` |

In the following query, the employee ID is used to order the result, but the employee ID does not appear in the result because
the hide directive is specified:

|  |  |
| --- | --- |
|  | ``` SELECT         1           tag,         NULL        parent,         EmployeeID  [employee!1!id!hide],         GivenName   [employee!1!name],         NULL        [order!2!date],         NULL        [department!3!name] FROM Employees UNION ALL  SELECT         2,         1,         EmployeeID,         NULL,         OrderDate,         NULL FROM Employees KEY JOIN SalesOrders UNION ALL  SELECT         3,         1,         EmployeeID,         NULL,         NULL,         DepartmentName FROM Employees e JOIN Departments d    ON e.DepartmentID=d.DepartmentID ORDER BY 3, 1 FOR XML EXPLICIT; ``` |

This query returns the following result:

|  |  |
| --- | --- |
|  | ``` <employee name="Fran">    <department name="R & D"/> </employee> <employee name="Matthew">    <department name="R & D"/> </employee>  <employee name="Philip">    <order date="2000-04-21"/>    <order date="2001-07-23"/>    <order date="2000-12-30"/>    <order date="2000-12-20"/>    ...    <department name="Sales"/> </employee>  <employee name="Julie">    <department name="Finance"/> </employee> ... ``` |

By default, when the result of a FOR XML EXPLICIT query contains characters that are not valid XML characters, the invalid
characters are escaped unless the column is of type XML. For information, see [Encoding illegal XML names](http://dcx.sap.com/1200/en/dbusage/xmldraftchapter-b-3488944b.html).

For example, the following query generates XML that contains an ampersand (&):

|  |  |
| --- | --- |
|  | ``` SELECT         1              AS tag,         NULL           AS parent,         ID             AS [customer!1!ID!element],         CompanyName    AS [customer!1!CompanyName] FROM Customers WHERE ID = '115' FOR XML EXPLICIT; ``` |

In the result generated by this query, the ampersand is escaped because the column is not of type XML:

|  |  |
| --- | --- |
|  | ``` <Customers CompanyName="Sterling & Co.">    <ID>115</ID> </Customers> ``` |

The xml directive indicates that the column value is inserted into the generated XML with no quoting. If you execute the same
query as above with the xml directive:

|  |  |
| --- | --- |
|  | ``` SELECT         1              AS tag,         NULL           AS parent,         ID             AS [customer!1!ID!element],         CompanyName    AS [customer!1!CompanyName!xml] FROM Customers WHERE ID = '115' FOR XML EXPLICIT; ``` |

The ampersand is not quoted in the result:

|  |  |
| --- | --- |
|  | ``` <customer>  <ID>115</ID>  <CompanyName>Sterling & Co.</CompanyName> </customer> ``` |

Note that this XML is not well-formed because it contains an ampersand, which is a special character in XML. When XML is generated
by a query, it is your responsibility to ensure that the XML is well-formed and valid: SQL Anywhere does not check whether
the XML being generated is well-formed or valid.

When you specify the xml directive, the *AttributeName* field is ignored, and elements are generated rather than attributes.

The following query uses the cdata directive to return the customer name in a CDATA section:

|  |  |
| --- | --- |
|  | ``` SELECT         1               AS tag,         NULL            AS parent,         ID              AS [product!1!ID],         Description     AS [product!1!!cdata] FROM Products FOR XML EXPLICIT; ``` |

The result produced by this query lists the description for each product in a CDATA section. Data contained in the CDATA section
is not quoted:

|  |  |
| --- | --- |
|  | ``` <product ID="300">    <![CDATA[Tank Top]]> </product> <product ID="301">    <![CDATA[V-neck]]> </product>  <product ID="302">    <![CDATA[Crew Neck]]> </product> <product ID="400">    <![CDATA[Cotton Cap]]> </product> ... ``` |
