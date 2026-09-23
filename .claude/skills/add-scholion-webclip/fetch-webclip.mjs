// Usage: node fetch-webclip.mjs <url>
// Prints JSON {title, text} to stdout. Non-zero exit on navigation failure.
import { chromium } from 'playwright';

const url = process.argv[2];
if (!url) { console.error('Usage: node fetch-webclip.mjs <url>'); process.exit(1); }

const browser = await chromium.launch();
try {
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  const title = await page.title();
  const text = await page.evaluate(() => {
    const el = document.querySelector('article') || document.querySelector('main') || document.body;
    return el.innerText;
  });
  console.log(JSON.stringify({ title, text }));
} catch (err) {
  console.error(String(err));
  process.exit(1);
} finally {
  await browser.close();
}
