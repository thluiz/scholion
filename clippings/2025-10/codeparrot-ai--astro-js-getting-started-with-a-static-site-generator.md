---
url: "https://codeparrot.ai/blogs/astrojs-getting-started-with-astrojs-static-site-generator"
captured_at: "2025-10-23T21:46:28+01:00"
title: "Astro.js Getting started with a static site generator"
domain: "codeparrot-ai"
---

# Astro.js Getting started with a static site generator

> Astro.js is a modern static site generator that has gained popularity among web developers for its simplicity, flexibility, and performance. It allows you to

Astro.js is a modern static site generator that has gained popularity among web developers for its simplicity, flexibility, and performance. It allows you to build fast websites using familiar technologies like HTML, CSS, and JavaScript, while also supporting various front-end frameworks.

## What is a Static Site?

A static site is a type of website that consists of pre-built HTML, CSS, and JavaScript files served directly to the user's browser without the need for server-side processing. Unlike dynamic websites that generate content on-the-fly, static sites are created in advance and remain unchanged until manually updated. This approach offers several advantages, including faster load times, improved security, and easier scalability. Static sites are particularly well-suited for content-driven websites such as blogs, portfolios, and documentation.

## What is a Static Site Generator?

A static site generator is a tool that helps create static websites. It takes content, usually written in a simple format, and turns it into HTML files. These files can then be uploaded to a web server. Static site generators automate the process of building a website, making it easier to manage and update content, often including templates that keep the design consistent across pages.

## Why use Astro?

Astro is designed to deliver high-performance websites by default, focusing on shipping only the necessary JavaScript to the browser, resulting in faster load times. It allows developers to use their preferred front-end frameworks (React, Vue, Svelte) within the same project, leveraging existing skills and component libraries while benefiting from Astro's optimized build process. Astro supports partial hydration, enabling interactivity only where needed.

Comparison with other static site generators:
- Performance: Astro.js excellent (minimal JS by default); Gatsby good but can be heavy (React); Next.js very good; Hugo excellent, known for build speed.
- Flexibility: Astro.js high (multiple frameworks); Gatsby moderate (React-based); Next.js good but React-focused; Hugo limited (Go templating).
- Learning curve: Astro.js relatively easy; Gatsby steeper (React + GraphQL); Next.js moderate; Hugo can be challenging without Go familiarity.
- Ecosystem: Astro.js growing rapidly; Gatsby extensive; Next.js strong within React; Hugo well-established themes/plugins.
- Build speed: Astro.js fast for small/medium sites; Gatsby can be slower for large sites (GraphQL layer); Next.js generally fast; Hugo extremely fast even at scale.

## Getting Started with Astro.js

Requires Node.js. Create a new project with `npm create astro@latest`, then run `npm run dev` to start a local server at `http://localhost:4321`.

### Creating a new page

Add a new file to `src/pages`, e.g. `about.astro`, with frontmatter for metadata followed by markup.

### Adding and using a component

Add a `.astro` file to `src/components` (e.g. `Button.astro`) defining a `Props` interface and using `Astro.props` to access passed props; import and use it in a page.

### Adding styles

Astro supports several approaches: inline styles via the `style` attribute, scoped styles within a component file (apply only to that component), global styles via a separate imported CSS file, CSS Modules (`.module.css` files), and built-in Tailwind CSS support.

## Writing Content with Astro.js

Markdown is built in for content-heavy pages: create a `.md` file in `src/pages`, add frontmatter metadata, write Markdown content — this generates a page automatically at the corresponding route.

### MDX Authoring

MDX extends Markdown with JavaScript expressions and components. Install via `npx astro add mdx`, create `.mdx` files in `src/pages`, mix Markdown and JSX (e.g. import and use a Button component within the content).

### Headless CMS Authoring

Astro works with headless CMS solutions — fetch content from a CMS API in the frontmatter script and render it in the page.

### Managing Content Pages

Three approaches: Page Files (Markdown/MDX in `src/pages` auto-generate routes), Local Content (files outside `src/pages` imported into Astro pages), and Content Collections (organize content in `src/content/` with `defineCollection` and Zod schemas for type-safe querying via `getCollection`).

### Showcasing Your Content

Example: `getStaticPaths` combined with `getCollection` to generate dynamic tag pages, filtering blog entries by tag.

## Building and Deploying

Build with `npm run build`, producing a `dist` directory with the static site, ready to upload to a web server. Deploy to Vercel (`vercel login`, `vercel build`, `vercel deploy`) or Netlify (`netlify login`, `netlify build`, `netlify deploy`) via their respective CLIs.

## Conclusion

Astro.js combines modern web development practices with strong performance, supporting multiple front-end frameworks, partial hydration, and minimal JavaScript shipping, with intuitive file-based routing, built-in Markdown support, and a growing integrations ecosystem.
