---
title: "Using FOR XML EXPLICIT"
date: '2020-05-26T21:29:50-03:00'
category: webclip
summary: 'FOR XML EXPLICIT lets a query define XML nesting and column treatment through Tag and Parent metadata columns, plus directives such as hide, element, xml, and cdata.'
tags: ["sql-anywhere", "for-xml-explicit", "xml"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using FOR XML EXPLICIT"
    url: "http://dcx.sap.com/1200/en/dbusage/sqlxml-s-5569418.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/dcx-sap-com--using-for-xml-explicit.md"
    kind: repo
---

FOR XML EXPLICIT lets the query define the XML structure that is returned. The query must supply Tag and Parent metadata columns, then use specially named data columns to control element names, attributes, nesting, and optional directives. The row order becomes the document order.

## Reading notes

- Tag and Parent must be the first two columns in EXPLICIT mode, and they define parent-child relationships in the XML result.
- Tag values can range from 1 to 255, and a NULL Parent places a row at the top level of the XML hierarchy.
- Data column names are split by exclamation marks into ElementName, TagNumber, AttributeName, and an optional Directive.
- ElementName supplies the element name for the first column with a matching tag number, while later columns with the same tag number reuse that tag.
- AttributeName makes the column value appear as an attribute of the named element.
- hide excludes a column from the generated XML while still allowing it to be used for ordering.
- element turns a column value into a nested element instead of an attribute.
- xml inserts the value with no quoting, and cdata inserts the value as a CDATA section.
- Binary and varbinary data is returned as base64, and NULL values are omitted by default unless for_xml_null_treatment changes that behavior.
- The document order follows the query’s ORDER BY, and UNION queries must define the relevant column names in the first SELECT.
- The examples show how employee, order, department, customer, and product data can be shaped into nested XML by combining tag numbers, attributes, and directives.
