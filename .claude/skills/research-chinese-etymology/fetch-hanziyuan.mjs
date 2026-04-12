// Usage: node fetch-hanziyuan.mjs <character>
import { chromium } from 'playwright';

const char = process.argv[2];
if (!char) { console.error('Usage: node fetch-hanziyuan.mjs <character>'); process.exit(1); }

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(`https://hanziyuan.net/#${char}`, { waitUntil: 'networkidle', timeout: 30000 });
await page.waitForTimeout(3000);
const text = await page.innerText('body');
await browser.close();
console.log(text);
