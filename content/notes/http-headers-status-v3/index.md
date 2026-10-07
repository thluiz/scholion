---
title: "http headers status v3"
date: '2015-01-28T01:37:19-03:00'
category: note
summary: "Diagrama de atividade que mostra como os cabeçalhos de uma requisição HTTP/1.1 determinam o código de status da resposta."
tags: ["alan-dean"]
has_commentary: false
sources:
  - title: "http headers status v3"
    author: "Alan Dean"
    kind: web
---

Tirinha de Alan Dean.

![Diagrama de atividade em fundo branco sobre uma grade com colunas A a P e linhas 1 a 26. Losangos azuis de decisão, identificados pela coordenada (B3, C4, G7 etc.), ligados por setas verdes ("true") e laranja ("false") até caixas azuis com códigos de status HTTP. O fluxo começa num ponto preto em B14 e sobe pela coluna B. Cabeçalho: "HTTP/1.1 (DELETE, GET, HEAD, PUT, POST)", "An activity diagram to describe the resolution of the response status code, given various headers", selo de licença Creative Commons "BY", "Creator: http://thoughtpad.net/alan-dean", "Source: http://thoughtpad.net/alan-dean/http-headers-status" e o rótulo "v3". Decisões: "B13 Available?", "B12 Known method?", "B11 URI too long?", "B10 Is method allowed on this resource?", "B9 Malformed?", "B8 Authorized?", "B7 Forbidden?", "B6 Unknown or unsupported Content-* header?", "B5 Unknown Content-Type?", "B4 Request entity too large?", "B3 OPTIONS?", "C3 Accept exists?", "C4 Acceptable media type available?", "D4 Accept-Language exists?", "D5 Acceptable language available?", "E5 Accept-Charset exists?", "E6 Acceptable charset available?", "F6 Accept-Encoding exists?", "F7 Acceptable encoding available?", "G7 Resource exists?", "G8 If-Match exists?", "G9 If-Match: * exists?", "G11 Etag in If-Match?", "H7 If-Match: * exists?", "H10 If-Unmodified-Since exists?", "H11 If-Unmodified-Since is valid date?", "H12 Last-Modified > If-Unmodified-Since?", "I4 Server desires that the request be applied to a different URI?", "I7 PUT?", "I12 If-None-Match exists?", "I13 If-None-Match: * exists?", "J18 GET/HEAD?", "K5 Resource moved permanently?", "K7 Resource previously existed?", "K13 Etag in If-None-Match?", "L5 Resource moved temporarily?", "L7 POST?", "L13 If-Modified-Since exists?", "L14 If-Modified-Since is valid date?", "L15 If-Modified-Since > Now?", "L17 Last-Modified > If-Modified-Since?", "M5 POST?", "M7 Server permits POST to missing resource?", "M16 DELETE?", "M20 Delete enacted?", "N5 Server permits POST to missing resource?", "N11 Redirect?", "N16 POST?", "O14 Conflict?", "O16 PUT?", "O18 Multiple representations?", "O20 Response includes an entity?", "P3 Conflict?", "P11 New resource?". Resultados: "200 OK" (duas vezes), "201 Created", "202 Accepted", "204 No Content", "300 Multiple Choices", "301 Moved Permanently", "303 See Other", "304 Not Modified", "307 Moved Temporarily", "400 Bad Request", "401 Unauthorized", "403 Forbidden", "404 Not Found", "405 Method Not Allowed", "406 Not Acceptable", "409 Conflict" (duas vezes), "410 Gone", "412 Precondition Failed" (duas vezes), "413 Request Entity Too Large", "414 Request URI Too Long", "415 Unsupported Media Type", "501 Not Implemented" (duas vezes), "503 Service Unavailable".](http-headers-status-v3.png)
