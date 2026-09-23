// Usage: node fetch-webclip.mjs <url>
// Prints JSON {title, text} to stdout. Non-zero exit on navigation failure.
import { chromium } from 'playwright';

const url = process.argv[2];
if (!url) { console.error('Usage: node fetch-webclip.mjs <url>'); process.exit(1); }

const browser = await chromium.launch();
try {
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });

  // Dismiss common cookie-consent walls (OneTrust, MSN, etc.) that block
  // the real content until accepted.
  const consentPattern = /^(I Accept|Accept All|Accept Cookies|Agree|Accept)$/i;
  try {
    const btn = page.getByRole('button', { name: consentPattern }).first();
    if (await btn.isVisible({ timeout: 3000 })) {
      await btn.click({ timeout: 3000 });
      await page.waitForLoadState('networkidle', { timeout: 10000 }).catch(() => {});
    }
  } catch { /* no consent wall present — fine */ }

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
