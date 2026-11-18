---
title: "How to build a web crawler with Node"
date: '2019-12-30T08:21:05+00:00'
category: webclip
summary: 'The article shows how to build a Node.js crawler with Axios, Cheerio, worker threads, and Firebase. It fetches exchange-rate HTML, extracts table data, and stores it in Firestore.'
tags: ["nodejs", "web-crawler", "worker-threads", "firebase"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to build a web crawler with Node"
    url: "https://dev.to/bnevilleoneill/how-to-build-a-web-crawler-with-node-3hn2"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-build-a-web-crawler-with-node.md"
    kind: repo
---

The article explains a simple Node.js web crawler that fetches the HTML of the IBAN exchange-rates page, parses the table with Cheerio, and sends the formatted results to a worker thread. The worker stores the crawled exchange-rate data in Firestore and sends a confirmation message back.

## Reading notes

- A web crawler systematically browses the internet, mainly for web indexing, and can also be used for web scraping.
- The tutorial uses Node workers because scraping can be CPU-intensive depending on the site structure and the amount of data extracted.
- The setup requires Node.js, Yarn or NPM, and a Node version 10.5.0 or higher.
- The project installs Axios, Cheerio, and firebase-admin.
- A worker is created with the worker_threads module.
- isMainThread is used to distinguish the main thread from a worker thread.
- The example shows bidirectional messaging with worker.postMessage() and parentPort.postMessage().
- The crawler workflow is to fetch HTML, extract it, traverse the DOM, format the table rows, send the data to a worker, receive it in the worker, and store it in Firestore.
- In main.js, Axios requests https://www.iban.com/exchange-rates and Cheerio selects the table rows under .table.table-bordered.table-hover.downloads > tbody > tr.
- The table text is split and cleaned before being formatted into an object.
- In dbWorker.js, Firebase is initialized, the current date is used as the document key, and the crawled data is saved under the Rates collection.
- The article notes that web crawling can be illegal if it is used for copyright infringement and advises checking a site’s crawling policy first.
- It also says worker threads do not guarantee faster performance, but can reduce pressure on the main thread by handling CPU-intensive tasks.
