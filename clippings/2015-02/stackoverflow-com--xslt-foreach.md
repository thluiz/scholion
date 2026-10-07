---
url: "http://stackoverflow.com/questions/9076323/xslt-looping-from-1-to-60"
captured_at: "2015-02-13T18:21:45-03:00"
title: "XSLT ForEach"
domain: "stackoverflow-com"
---

```
<xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:output method="text"/>

     <xsl:template match="/">
      <xsl:call-template name="displayNumbers">
        <xsl:with-param name="pStart" select="1"/>
        <xsl:with-param name="pEnd" select="1000000"/>
      </xsl:call-template>
     </xsl:template>

     <xsl:template name="displayNumbers">
      <xsl:param name="pStart"/>
      <xsl:param name="pEnd"/>

      <xsl:if test="not($pStart > $pEnd)">
       <xsl:choose>
        <xsl:when test="$pStart = $pEnd">
          <xsl:value-of select="$pStart"/>
          <xsl:text>&#xA;</xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:variable name="vMid" select=
           "floor(($pStart + $pEnd) div 2)"/>
          <xsl:call-template name="displayNumbers">
           <xsl:with-param name="pStart" select="$pStart"/>
           <xsl:with-param name="pEnd" select="$vMid"/>
          </xsl:call-template>
          <xsl:call-template name="displayNumbers">
           <xsl:with-param name="pStart" select="$vMid+1"/>
           <xsl:with-param name="pEnd" select="$pEnd"/>
          </xsl:call-template>
        </xsl:otherwise>
       </xsl:choose>
      </xsl:if>
     </xsl:template></xsl:stylesheet>
```
