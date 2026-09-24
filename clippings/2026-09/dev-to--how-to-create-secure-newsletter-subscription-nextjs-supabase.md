---
url: "https://dev.to/madza/how-to-create-a-secure-newsletter-subscription-with-nextjs-supabase-nodemailer-and-arcjet-3ll7?context=digest"
captured_at: "2026-09-25T00:33:15+01:00"
title: "How to Create a Secure Newsletter Subscription with NextJS, Supabase, Nodemailer and Arcjet 🔐💯"
domain: "dev-to"
---

In today's digital age, newsletters are a powerful tool for engaging with your audience, driving traffic, and building a loyal community around your brand.

Enterprise options can be costly for large lists, while free solutions often face spam sign-ups, poor email validation, and inadequate bot protection.

In this tutorial, we will build a custom email subscription app from scratch and solve the common challenges associated with existing solutions by integrating robust security measures and validation techniques.

Here’s an overview of the tech stack and features:

*   [NextJS](https://nextjs.org/)\-based user interface and API for capturing user emails with a sleek and responsive design;
    
*   [Supabase](https://supabase.com/)\-powered backend to store and manage subscriber data securely;
    
*   [Nodemailer](https://nodemailer.com/) transporter for sending confirmation emails, enabling a smooth double opt-in process;
    
*   [Arcjet](https://arcjet.com/) integration for shield protection, bot detection, rate limiting, and email validation.
    

By the end of this guide, you'll have a fully functional and secure newsletter subscription form. I hope this tutorial will be useful for you, and that you'll learn a few security-related concepts along the way.

Thanks to the Arcjet team for sponsoring this article! They contacted me to ask if I would like to try their beta and paid me for my time but did not influence the content.

* * *

## [](#what-is-arcjet)What is Arcjet?

[Arcjet](https://arcjet.com/) is a security solution designed to empower developers by providing robust application protection with minimal effort.

Arcjet is seamlessly integrated into your application as a dependency, requiring no additional agents or complex infrastructure.

With Arcjet, you can easily implement critical security features such as rate limiting, bot protection, email validation, and defenses against common web attacks.

[![Arcjet](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvhdj2l84t9wjp5351t7k.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvhdj2l84t9wjp5351t7k.png)

Currently, Arcjet is optimized for the JavaScript ecosystem, offering robust support for Bun, NextJS, Node.js, and SvelteKit applications.

The team is also working on expanding support to other popular frameworks, including Django, Ruby on Rails, and Laravel, which will be available in the future.

Also, Arcjet is available on [GitHub](https://github.com/arcjet), so feel free to check them out and give it a ⭐ star if you liked the project.

## [](#how-are-we-going-to-use-arcjet)How are we going to use Arcjet?

We'll leverage Arcjet to implement four major security features:

**1\. Validating Email Format**

We will use email format validation to make sure only correctly formatted email addresses can be added to our subscriber list.

Arcjet’s email validation feature will be used server-side to check for common issues like invalid formats, disposable emails, and emails without MX records.

**2\. Adding Rate Limit**

We will implement rate limiting on our API to manage the server load via Arcjet’s rate-limiting rules, such as a fixed window.

For example, we will restrict the number of submissions per IP address within a certain time frame, preventing abuse and reducing the server load.

**3\. Detecting Bots**

We will also protect the subscription form from automated sign-ups via Arcjet’s bot detection feature to distinguish between human users and bots.

This will help us block or challenge suspicious requests, ensuring that the mailing list consists of genuine subscribers.

**4\. Enabling Attack Protection**

To protect the app against common web attacks, such as DDoS or brute force, we’ll use Arcjet’s attack protection mechanisms.

This includes features like IP blocking, request filtering, and anomaly detection.

## [](#planning-the-user-interface)Planning the User Interface

There will be four UI views that will be switched between the subscription state: the landing screen, pending screen, error screen, and confirmation screen:

**1\. Landing screen**

The landing screen will serve as the initial entry point with a simple form featuring an email text field and a submit button.

[![Landing screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9hdt8xoc9sf27l2rpqif.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9hdt8xoc9sf27l2rpqif.png)

The design will be designed to encourage users to subscribe to the newsletter.

**2\. Pending screen**

Once users submit their email addresses, they will be redirected to the pending screen. It will reassure users that the subscription process is in progress.

[![Pending screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fahckvtarhi82had0l0pl.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fahckvtarhi82had0l0pl.png)

This page will notify them to check their email.

**3\. Error screen**

In the event of an issue during the subscription process, such as an invalid email or a rate limit, users will be presented with an error view.

[![Error screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9fbyprsjz6sp7n1455kb.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9fbyprsjz6sp7n1455kb.png)

This page will display a message indicating that the subscription has failed.

**4\. Confirmation screen**

Upon successful subscription, users will be re-directed to the confirmation screen, with a message that their email has been registered.

[![Confirmation screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F67wxbgacelxw9dgkeoz9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F67wxbgacelxw9dgkeoz9.png)

This will let the users know that the subscription process is complete.

## [](#setting-up-the-nextjs-app)Setting up the NextJS app

Open your terminal and run `npx create-next-app@latest`.

This will launch the built-in setup wizard. Give your project a name `arcjet-demo` and configure the rest of the options as shown below:

[![NextJS wizard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbbjmfzfiobbp0zmnx5qj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbbjmfzfiobbp0zmnx5qj.png)

Change the working directory to the newly created project by running the command `cd arcjet-demo`.

Start the developer server by running `npm run dev`.

Click on the link provided in the terminal. It should open the NextJS welcome screen in your default web browser.

You should presented with something like this:

[![NextJS welcome screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3ff4jfrc2zal2xuspurs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3ff4jfrc2zal2xuspurs.png)

If your app screen does not open from the terminal link, you can open it in your browser manually by navigating to [http://localhost:3000](http://localhost:3000/).

## [](#adding-media-assets)Adding media assets

For this tutorial, you will need 5 icons.

Four will represent the newsletter app state for the unsubscribed, approval, subscribed, and error state and the fifth will represent the loading state.

I recommend using static PNG files with a transparent background and an animated GIF to improve the UX while switching through the states.

Name the files `unsubsribed.png`, `approval.png`, `subscribed.png`, `error.png` and `loading.gif` so it would be easier to follow along with the tutorial.

You can pick any icons that fit your style and app design. For reference, I used assets available on [Flaticon](https://www.flaticon.com/packs/email-24?word=envelope) and [Loading.io](http://loading.io/).

Download them and add them to the `public` folder in your NextJS project.

## [](#creating-the-arcjet-account)Creating the Arcjet account

Visit the [Arcjet](https://arcjet.com/) website and create a [free account](https://app.arcjet.com/auth/signin).

You can sign up via GitHub or Google.

[![Arcjet sign-up](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvgjhr02xhgotu4ma30cb.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvgjhr02xhgotu4ma30cb.png)

Create a new project, by clicking on the "+ New site" at the profile dashboard.

[![Arcjet New project](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0jbheg767ioq5doz577n.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0jbheg767ioq5doz577n.png)

Enter the project name `arcjet-demo` and click "Create".

[![Arcjet dashboard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc0fgmix8m7blp55api6m.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc0fgmix8m7blp55api6m.png)

You should now be presented with the Arcjet API key.

Copy it to your clipboard, since we will need it in a few minutes.

[![Arcjet API Key](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs59g429e4zleh26lgmjg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs59g429e4zleh26lgmjg.png)  

## [](#adding-arcjet-to-nextjs)Adding Arcjet to NextJS

Switch to your NextJS project in the code editor and navigate to the root.

Install Arcjet by running `npm i @arcjet/next` in your terminal.

Create a new file called `.env.local` in the root of your project and include the Arcjet API key as shown below:

`ARCJET_KEY=yourarcjetapikeygoeshere`

Next, we will create an Arcjet configuration file so it will be easier to work with Arcjet later in the tutorial.

Make a new folder `lib` in the `app` folder.

Create a new file `arcjet.tsx` inside the newly created `lib` folder.

Include the following code in the `arcjet.tsx` file:

```


import arcjet, {
  shield,
  detectBot,
  fixedWindow,
  validateEmail,
} from "@arcjet/next";

export default arcjet({
  key: process.env.ARCJET_KEY!,
  rules: [
    shield({ mode: "LIVE" }),
    detectBot({
      mode: "LIVE",
      allow: [],
    }),
    fixedWindow({
      mode: "LIVE",
      match: "/api/submit",
      window: "2m",
      max: 3,
    }),
    validateEmail({
      mode: "LIVE",
      block: ["DISPOSABLE", "INVALID", "NO_MX_RECORDS"],
    }),
  ],
});


```

Enter fullscreen mode Exit fullscreen mode

First, we imported `arcjet` library and protection-related functions `shield`, `detectBot`, `validateEmail`, `fixedWindow` from the `@arcjet/next` package.

Then we set the `key` variable using the `ARCJET_KEY` from the `.env.local` file.

Next, we configured the Arcjet rules as follows:

*   `shield` to protect against general threats;
    
*   `detectBot` to detect and block automated bot traffic;
    
*   `fixedWindow` to limit the number of requests to `/api/submit` within a specific time window (max 3 requests in 2 minutes);
    
*   `validateEmail` to block requests with disposable, invalid, or emails without MX records.
    

We configured each instance to be used in the `LIVE` mode to block the requests if the warnings are detected. If you want them to be logged into the console, you can use `DRY_RUN` mode, which is recommended for testing or debugging.

## [](#setting-up-nodemailer-transporter)Setting up Nodemailer transporter

Install the Nodemailer by running `npm i nodemailer && npm i @types/nodemailer --save-dev` in your terminal.

To work with Nodemailer, we must first add and configure the following SMTP keys in our `local.env` in the project root as follows:

```


SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_SECURE=true
SMTP_USER=yourusername
SMTP_PASS=yourpassword
BASE_URL=http://localhost:3000 # or your production URL


```

Enter fullscreen mode Exit fullscreen mode

We will use [Gmail](https://gmail.com/) as an SMTP provider for this tutorial, but if you use a different provider check their docs.

For the `SMTP_USER` key provide your Gmail email address.

For the `SMTP_PASS` visit your [Google account](https://myaccount.google.com/) for app keys and create a new password for this demo. You can access the configuration page [here](https://myaccount.google.com/apppasswords).

To keep the configuration logic separate from the API routes, we will include the configuration file in a seperate library, just like we did for Arcjet before.

Navigate to your `lib` folder and create a new file `nodemailer.tsx` inside of it.

Include the following code in the `nodemailer.tsx` file:

```


import nodemailer from "nodemailer";

export const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST!,
  port: parseInt(process.env.SMTP_PORT!, 10),
  secure: process.env.SMTP_SECURE === "true",
  auth: {
    user: process.env.SMTP_USER!,
    pass: process.env.SMTP_PASS!,
  },
});

export const sendOptInEmail = async (email: string, token: string) => {
  const mailOptions = {
    from: '"Newsletter-subscription" <noreply@youremail.com>',
    to: email,
    subject: "Confirm Your Subscription",
    html: `<h1 style="font-size: 1.5rem; font-weight: 700;">Thanks for signing up!</h1></p>
           <p style="font-size: 1.125rem; color: #4a5568;">Please confirm your subscription by clicking on the link below:</p>
           <p><a href="${process.env.BASE_URL}/api/confirm?token=${token}" style="display: block; width: 100%; font-size: 16px; background-color: #38b2ac; color: #ffffff; padding: 0.5rem; border-radius: 0.25rem; text-align: center; text-decoration: none; transition: background-color 0.2s;">Confirm Subscription</a></p>`,
  };

  await transporter.sendMail(mailOptions);
};


```

Enter fullscreen mode Exit fullscreen mode

First, we imported the `nodemailer` package that will handle the logic for sending the emails to provide the double opt-in for our newsletter demo app.

Then we created the `transporter` object, which holds all of the configuration data from the `.local.env` file to initialize the `nodemailer`.

Next, we defined the `sendOptInEmail` function that will hold the email structure of the double opt-in confirmation email sent to the subscriber.

The `sendOptInEmail` takes in two variables `email` and `token`. We will pass those after we import the library in the API route.

We also used a simple HTML structure for the body of the email with some CSS styling so it would look similar to our app design.

## [](#creating-supabase-tables)Creating Supabase tables

Navigate to the [Supabase](https://supabase.com/) website and [log in](https://supabase.com/dashboard/sign-in).

[![Supabase sign-up](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr2p78t9t5n9vrk4diuk1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr2p78t9t5n9vrk4diuk1.png)

Click "New project" in the user dashboard.

[![Supabase New project](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqr21qk9ant0s55pxhkkh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqr21qk9ant0s55pxhkkh.png)

Give your app a name `arcjet-demo`, provide a strong password, and select a region closest to the location of your users for optimal performance.

[![Supabase configuration](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqn4mafxj762vxdhhn6m6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqn4mafxj762vxdhhn6m6.png)

Next, we will create a couple of tables to store the data.

The first table will store the unique token that will be used to identify the user once the user clicks on the verification link for the double opt-in.

Navigate to the "Database" section on the left navigation sidebar and click "New table" on the right of the dashboard to create a new database.

[![Supabase database](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F68ci898bcvemmefojm7e.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F68ci898bcvemmefojm7e.png)

We will call the first table `pending_subscriptions` to temporarily store the email addresses that have been submitted but have not been approved.

We will create three columns in the table.

The first column will store the user `token` with the type of `uuid`, the default value of `get_random_uuid()`, and serve as the primary key.

The second column will store the `email` address with the type of `text`.

The third column will store `link_sent_at` data with the type of `timestamptz`. Select the default value to be set as `now()`. It will detect when the confirmation email is sent.

[![Supabase table](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuztqjyia202edzrndztv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuztqjyia202edzrndztv.png)

Now let's create the second table that will store the confirmed email addresses of users. We will move the user to it upon successful confirmation.

While on the "Database" page click "New table" again and this time we will call the table `subscribers`.

We will create two columns for this table.

The first column will be called `email`. Set the `text` type for this column, and make it a primary column. It will store all of the confirmed email addresses.

The second column will be called `confirmed_at`. Set the type of it as `timestamptz`. Also, select the default value to be set as `now()`. This will store the time when the user completes the subscription process.

[![Supabase table #2](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffo789uujnnhue72n0btr.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffo789uujnnhue72n0btr.png)  

## [](#adding-supabase-to-nextjs)Adding Supabase to NextJS

Switch back to your NextJS project and run the following command in your terminal to install Supabase: `npm i @supabase/supabase-js`.

Also, install a UUID library to generate the unique tokens that we will need for email confirmation by running `npm i uuid && npm i @types/uuid --save-dev`.

Next, add the following variables to `.env.local` file:

```


NEXT_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY


```

Enter fullscreen mode Exit fullscreen mode

To find these variables, visit the Supabase website, open the main dashboard of your project, click "Settings" at the bottom left, and select "API".

[![Supabase API Key](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsfv1vqa5bzuf34bhtwo8.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsfv1vqa5bzuf34bhtwo8.png)

Switch back to your NextJS project and create a new file called `supabase.tsx` inside the `lib` folder. We will use it to create a dedicated client for the configuration setup.

Include the following code in the `supabase.tsx` file:

```


import { SupabaseClient } from "@supabase/supabase-js";

const supabase = new SupabaseClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_KEY!
);

export default supabase;


```

Enter fullscreen mode Exit fullscreen mode

We first imported `SupabaseClient` from the `@supabase/supabase-js` package.

To initialize the client, we provided the Supabase project link and the API key from the `.local.env` file and then exported the client so we could later use it when handling the API route logic.

## [](#creating-a-submit-api-route)Creating a Submit API route

This route will handle the logic of the user request after the email has been entered in the input area and the submit button has been pressed.

First, navigate to the `app` directory in your NextJS project.

Next, create a new `api` folder, and within it, add another folder called `submit`. Then, open the `submit` folder and create a new file named `route.tsx`.

Include the following code in the `route.tsx`:

```


import { NextRequest, NextResponse } from "next/server";
import arcjet from "@/lib/arcjet";
import { sendOptInEmail } from "@/lib/nodemailer";
import supabase from "@/lib/supabase";
import { v4 as uuidv4 } from "uuid";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const email = searchParams.get("email")!;

  const decision = await arcjet.protect(req, { email });
  if (decision.isDenied()) {
    if (decision.reason.isShield()) {
      console.log("Suspicious action detected!");
      return NextResponse.json(
        { error: "Suspicious action detected!" },
        { status: 403 }
      );
    }
    if (decision.reason.isBot()) {
      console.log("Looks like you might be a bot!");
      return NextResponse.json(
        { error: "Looks like you might be a bot!" },
        { status: 403 }
      );
    }
  }
  return NextResponse.json({ data: "Hello World!" });
}

export async function POST(req: NextRequest) {
  const data = await req.json();
  const email = data.email;

  const decision = await arcjet.protect(req, { email });

  if (decision.isDenied()) {
    if (decision.reason.isRateLimit()) {
      const resetTime = decision.reason.resetTime;
      if (!resetTime) {
        return NextResponse.json(
          { error: "Too many requests. Try again later." },
          { status: 429 }
        );
      }

      const remainingTime = Math.max(
        0,
        Math.floor((resetTime.getTime() - Date.now()) / 1000)
      );
      const timeUnit = remainingTime > 60 ? "minutes" : "seconds";
      const timeValue =
        timeUnit === "minutes" ? Math.ceil(remainingTime / 60) : remainingTime;

      return NextResponse.json(
        { error: `Too many requests. Try again in ${timeValue} ${timeUnit}.` },
        { status: 429 }
      );
    }
    if (decision.reason.isEmail()) {
      const errorType = decision.reason.emailTypes;
      if (errorType.includes("INVALID")) {
        return NextResponse.json(
          { error: "Invalid email format. Check your spelling." },
          { status: 400 }
        );
      } else if (errorType.includes("DISPOSABLE")) {
        return NextResponse.json(
          { error: "Disposable email address. Check your spelling." },
          { status: 400 }
        );
      } else if (errorType.includes("NO_MX_RECORDS")) {
        return NextResponse.json(
          { error: "Email without an MX record. Check your spelling." },
          { status: 400 }
        );
      } else {
        return NextResponse.json(
          { error: "Invalid email. Check your spelling." },
          { status: 400 }
        );
      }
    }
  }
  const checkEmailExists = async (email: string) => {
    const { data, error } = await supabase
      .from("subscribers")
      .select("*")
      .eq("email", email);

    if (error) {
      console.error("Error checking email:", error);
      return false;
    }

    return data.length > 0;
  };

  const handleEmailSubmission = async (email: string) => {
    const emailExists = await checkEmailExists(email);

    if (emailExists) {
      return NextResponse.json(
        { error: "This email has already been registered." },
        { status: 500 }
      );
    } else {
      const token = uuidv4();

      const { error } = await supabase
        .from("pending_subscriptions")
        .insert([{ email, token }]);

      if (error) {
        return NextResponse.json({ error: "Database error" }, { status: 500 });
      }

      await sendOptInEmail(email, token);
      return NextResponse.json({ data: "Success" }, { status: 200 });
    }
  };

  return await handleEmailSubmission(email);
}


```

Enter fullscreen mode Exit fullscreen mode

First, we imported `NextRequest` and `NextResponse` to handle requests and responses in our API route. Then, we imported the `arcjet` client from the `lib` folder.

We also imported `sendOptInEmail` for sending verification emails, `supabase` for database interaction, and `uuid` for generating unique tokens.

Next, we handled incoming `GET` requests to check if the request was suspicious. If it was denied, we logged this action and returned a `403` response.

Then, we checked if the request came from a bot. If the request was denied, we logged this and returned a `403` response.

After that, we handled incoming `POST` requests. We first parsed the request body to extract the received email address.

We then checked rate limits. If the request was denied due to too many attempts, we extracted the `resetTime` and calculated the remaining time before the user could retry.

Next, we validated the email address. If the email was invalid, disposable, or lacked MX records, we checked the specific error type `emailTypes` and returned a `400` response.

Then, we created an async function `checkEmailExists` to verify if the email was already in our `subscribers` database. If an error occurred, we logged it and returned `false`.

Finally, we created a function `handleEmailSubmission` to handle the confirmation emails. We generated a unique token with UUID, inserted it into the `pending_subscriptions` table with Supabase, and sent an opt-in email using Nodemailer.

## [](#creating-the-confirmation-api-route)Creating the Confirmation API route

This route will handle email confirmation by validating the token provided in the query parameters of the verification URL and will forward the user to the confirmation screen.

Navigate to the `lib` folder in your NextJS project and create a new `confirm` folder. Next, create a `route.tsx` file inside it.

Include the following code in `route.tsx`:

```


import { NextRequest, NextResponse } from "next/server";
import supabase from "@/lib/supabase";

export async function GET(req: NextRequest) {
  const token = req.nextUrl.searchParams.get("token");

  if (!token) {
    console.log("Invalid token");
    return NextResponse.json({ error: "Invalid token" }, { status: 400 });
  }

  const { data: record, error } = await supabase
    .from("pending_subscriptions")
    .select("*")
    .eq("token", token)
    .single();

  if (error || !record) {
    console.log("Token not found");
    return NextResponse.json({ error: "Token not found" }, { status: 400 });
  }

  await supabase.from("subscribers").insert([{ email: record.email }]);

  await supabase.from("pending_subscriptions").delete().eq("token", token);

  return NextResponse.redirect(`${process.env.BASE_URL}/?approved=true`);
}


```

Enter fullscreen mode Exit fullscreen mode

First, we imported `NextRequest` and `NextResponse` from `"next/server"`. We also imported the `supabase` client to work with the database.

Next, we exported an async function for `GET` requests. We retrieved the `token` from the URL query parameters using `req.nextUrl.searchParams`. If the token was not present in the request, we returned a `400` response.

After that, we validated the token by querying the `pending_subscriptions` table. If an error occurred or the record was not found, we returned a `400` response. If the record was found, we marked the email as confirmed.

We then deleted the token record from the `pending_subscriptions` table to clean up the database. Note that this is optional, and you could keep those records if you need to access them to see when the confirmation links were sent.

Finally, we redirected the user to the confirmation view with a `approved=true` query parameter. This confirmed the verification to the user.

## [](#building-the-user-interface)Building the User Interface

In our previous sections, we created the backend for the application or the logic of how the app will handle the user requests and send the responses.

Now we will create a frontend or the the visual part of the application.

We will start by resetting the default styling.

Open the `globals.css` file in your `app` folder and remove all of the styling rules except for the Tailwind imports, so the file now looks like this:

```


@tailwind  base;
@tailwind  components;
@tailwind  utilities;


```

Enter fullscreen mode Exit fullscreen mode

Next, open the `page.tsx` file in your `app` folder and include the following code:

```


"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Image from "next/image";

export default function Home() {
  const [isLoading, setIsLoading] = useState(false);
  const [inputValue, setInputValue] = useState("");
  const [isEmailSubmitted, setIsEmailSubmitted] = useState(false);
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [isErrorState, setIsErrorState] = useState(false);
  const [infoMessage, setInfoMessage] = useState(
    "Sent out weekly on Sundays. Always free."
  );

  const searchParams = useSearchParams();

  useEffect(() => {
    const queryParam = searchParams.get("approved");

    if (queryParam === "true") {
      setIsSubscribed(true);
      setInfoMessage("See you soon in the email! Best for now!");
    }
    setIsLoading(false);
  }, [searchParams]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const response = await fetch("/api/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: inputValue }),
      });

      const result = await response.json();
      if (result.data === "Success") {
        setIsEmailSubmitted(true);
        setInfoMessage("The link should be in your email shortly.");
        setIsLoading(false);
      } else {
        setIsErrorState(true);
        setInfoMessage(result.error || "An error occurred.");
        setIsLoading(false);
      }
    } catch (error) {
      setInfoMessage("An unexpected error occurred.");
      setIsLoading(false);
    }
  };

  return (
    <main className="flex items-center justify-center min-h-screen ">
      {isLoading ? (
        <Image
          className="w-auto"
          src={"/loading.gif"}
          alt="loading"
          width={80}
          height={80}
        ></Image>
      ) : (
        <div className="flex flex-col items-center justify-center text-center max-w-[650px] min-h-[350px] p-10 space-y-6">
          <Image
            className="w-auto"
            src={
              isSubscribed
                ? "/subscribed.png"
                : isEmailSubmitted
                ? "/approval.png"
                : isErrorState
                ? "/error.png"
                : "/unsubscribed.png"
            }
            alt="logo"
            width={100}
            height={100}
          />
          <h1 className="text-2xl font-bold">
            {isSubscribed
              ? "You are all set! Thank you!"
              : isEmailSubmitted
              ? "Verification email sent!"
              : isErrorState
              ? "Subscription failed!"
              : "Subscribe to My Newsletter"}
          </h1>
          <p className="text-lg text-gray-700">
            {isSubscribed
              ? "The verification was successful and I'm sure this is a great beginning for something special."
              : isEmailSubmitted
              ? "Double opt-in ensures that only valid and genuinely interested subscribers are added to my mailing list."
              : isErrorState
              ? "Unfortunately, your email was not added to the newsletter list due to reason in the warning message."
              : "Join the subscribers list to get the latest news, updates, and special offers delivered directly to your inbox."}
          </p>
          {!isEmailSubmitted && !isSubscribed && !isErrorState ? (
            <form
              className="flex flex-col sm:flex-row w-full px-4 space-y-2 sm:space-y-0 sm:space-x-2"
              onSubmit={handleSubmit}
            >
              <input
                type="text"
                placeholder="Enter your email"
                className="flex-grow border border-gray-300 p-2 sm:w-8/12 rounded focus:outline-none"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                required
              />
              <button
                className="w-full sm:w-4/12 bg-teal-500 text-white p-2 hover:bg-teal-600 rounded"
                type="submit"
              >
                Subscribe
              </button>
            </form>
          ) : (
            <button
              className="w-full bg-teal-500 text-white p-2 hover:bg-teal-600 rounded"
              type="button"
              onClick={() => {
                setIsSubscribed(false);
                setIsEmailSubmitted(false);
                setIsErrorState(false);
                setInfoMessage("Sent out weekly on Sundays. Always free.");
              }}
            >
              {isErrorState ? "Let me try again" : "Back to start"}
            </button>
          )}
          {!isErrorState ? (
            <p className="text-md text-gray-700">{infoMessage}</p>
          ) : (
            <p className="text-md text-red-500">{infoMessage}</p>
          )}
        </div>
      )}
    </main>
  );
}


```

Enter fullscreen mode Exit fullscreen mode

First, we declared `use client` at the top of the file, indicating that this is a client-side NextJS component.

Next, we brought in `useEffect` and `useState` to manage states and side effects. We also imported `useSearchParams` to access URL query parameters and the `Image` component to handle images.

Then we defined the `Home` component, which was exported as the default export of the module. Inside it, we declared several state variables using the `useState` hook:

*   `isLoading` to track the loading state;
    
*   `inputValue` to store the user's email input;
    
*   `isEmailSubmitted` to indicate if the email has been successfully submitted;
    
*   `isSubscribed` to track if the user has successfully subscribed;
    
*   `isErrorState` to indicate if there was an error during the process;
    
*   `infoMessage` to store a message displayed to the user, initialized with a default message.
    

Next, we utilized the `useEffect` hook to handle side effects when the component renders to see if the request is the initial request.

We then defined an async `handleSubmit` function, which handles the form submission when the user tries to subscribe.

In the return statement, we defined the UI for the component using JSX.

The email `input` form consists of an input field and a `submit` button and is shown only if the user hasn't yet submitted their email or has not encountered an error.

If the user has already subscribed, submitted their email, or encountered an error, we rendered a "Back to start" or "Let me try again" button that resets the relevant states.

Finally, we displayed the `infoMessage` text based on whether it was informational or indicated an error.

## [](#testing-attacks-from-the-terminal)Testing attacks from the terminal

Now let's test the security of our application.

First, make sure your developer server is still running. If it is not, run `npm run dev` to start it again.

We will first simulate the attacks from the terminal via `curl`. We will not see any warnings on the app UI, but they will still be logged in our console.

### [](#1-attack-protection)1\. Attack protection

Open a new terminal, besides the one running the developer server.

Execute the command `curl -v -H "x-arcjet-suspicious: true" http://localhost:3000/api/submit`.

Check your terminal response. You should get a warning message indicating suspicious activity has been detected.

[![Suspicious activity](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F73dxtmlbxrnbpxvys2vv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F73dxtmlbxrnbpxvys2vv.png)

Now switch over to your Arcjet project dashboard. The log will be displayed, indicating which protection reason blocked the request.

[![Arcjet project dashboard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc4z7bik9stygph9ij7r2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc4z7bik9stygph9ij7r2.png)

Shield detects suspicious behavior, such as SQL injection and cross-site scripting attacks.

### [](#2-bot-detection)2\. Bot detection

Now let's see if our application is safe from bots. Again we will use a `curl` command to simulate the attack.

Execute the command `curl -v http://localhost:3000/api/submit`.

Check your terminal and you should see a message that the request has been blocked and Arcject has identified a bot activity.

[![Bot activity](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcj9poqfvb1xaxzoe7p22.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcj9poqfvb1xaxzoe7p22.png)

Now, switch to the Arcject dashboard. Again, you should see the blocked request and the reason for it.

[![Arcject dashboard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9dkfc72ym87nrw3yonad.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9dkfc72ym87nrw3yonad.png)

Remember we set the `LIVE` protection mode for the Arcjet instances in the `lib` folder meaning that this would block the requests.

You can always enable `DRY_RUN` mode so the results would be only logged.

## [](#testing-errors-from-the-ui)Testing errors from the UI

Now let's use the user interface to test our app.

Click on the developer server link in your primary terminal window or open your web browser and navigate to [http://localhost:3000](http://localhost:3000/) to open the app.

### [](#1-email-protection)1\. Email protection

First, let’s test our app by trying to register with an invalid email address.

For example, `info@website` is not a valid email address format since it is missing the domain to ensure proper routing and delivery of messages.

[![Invalid email](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fta36lkrpl14ko1pxvfm6.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fta36lkrpl14ko1pxvfm6.gif)

Next, we’ll attempt to use a disposable email address.

For example, `user123@mytemp.email` is a disposable email, that would usually come from a provider that offers temporary, short-term email addresses.

[![Disposable email](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fao663mlw9hebzhw2psrd.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fao663mlw9hebzhw2psrd.gif)

Finally, we’ll input an email address that appears valid but lacks MX records.

For example, `support@missingmx.com` is valid in format and domain but cannot receive emails due to the absence of MX records.

[![Email lacks MX records](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwp21fsmagjwk8v37r3g.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwp21fsmagjwk8v37r3g.gif)

In each of the above cases, the registration attempts were denied, and error messages were properly displayed, preventing the submission.

Behind the scenes, Arcjet blocked invalid, disposable, or non-functional emails before they could be processed, ensuring that only reliable emails were accepted.

### [](#2-rate-limiting)2\. Rate limiting

Now, let’s test the rate-limiting feature by attempting to submit an email multiple times in a short time.

We set the rate limit to allow only 3 requests within a 2-minute window. We should hit the rate limit if we submit more than three times rapidly.

[![Rate limit](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fd7zy5w5b8wg5lgbrhk3m.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fd7zy5w5b8wg5lgbrhk3m.gif)

As expected, additional requests were blocked once the limit was reached.

The UI responded by switching to an error view, displaying the warning message indicating that further submissions are temporarily restricted.

Let’s wait for a minute and try submitting the email again.

[![Rate limit reset](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8ts4tov06kd97fc5fug9.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8ts4tov06kd97fc5fug9.gif)

You'll notice that the UI continuously updates the warning message with the remaining time for the rate-limiting block, keeping the user informed.

This real-time feedback ensures a smoother user experience while protecting your server from excessive requests.

### [](#3-checking-double-emails)3\. Checking double emails

Next, we will check against the existing records in the table since you do not want repeated emails in your subscriber database.

For this test, I have purposely entered an already existing email in the `subscribers` database, so we could get an error when trying to submit it.

[![Checking double emails](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdwzjbf48ho3e1snhidoh.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdwzjbf48ho3e1snhidoh.gif)

Behind the scenes, a `POST` request was sent to the server when the form was submitted. The `submit` API route checked if the email already existed.

Since the email was found in the database, the server returned an error, and the client-side UI responded by displaying a warning message indicating the duplication.

This feature helps ensure that your mailing list remains free of redundant entries.

## [](#testing-successful-double-optin)Testing successful double opt-in

Finally, let's walk through the complete process of successfully subscribing to the newsletter.

First, enter a valid email address and submit it.

[![Testing successful double opt-in](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fngwh0i9z7pzfwywrkhnw.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fngwh0i9z7pzfwywrkhnw.gif)

Arcjet passed all security checks and the app transitioned to the pending screen. Behind the scenes, the email was added to the `pending_subscriptions` table in Supabase.

Next, Nodemailer sent a confirmation email to the provided address. Wait a few seconds for the confirmation email to arrive in your inbox, and click on the confirmation link.

[![Arcjet passed all security checks](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1y8ht420xqtfd5nu8mkc.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1y8ht420xqtfd5nu8mkc.gif)

This initiated Supabase to remove the user data from `pending_subscriptions` table and add the email to the main `subscribers` table.

Finally, the user was redirected to the confirmation screen indicating the successful subscription.

Congratulations, you have created a fully functional newsletter subscription application!

## [](#conclusion)Conclusion

By using NextJS, Supabase, Nodemailer, and Arcjet, you can build a robust solution that processes emails effectively and ensures a high level of security.

Arcjet plays a crucial role in this setup by providing useful protection mechanisms such as bot detection, rate limiting, and email validation.

Supabase and Nodemailer complemented this by offering seamless database management and reliable email delivery.

I hope the article was helpful and you learned how to build a secure newsletter subscription system for your future projects!

* * *

Writing has always been my passion and it gives me pleasure to help and inspire people. If you have any questions, feel free to reach out!

Make sure to receive the best resources, tools, productivity tips, and career growth tips I discover by subscribing to [my newsletter](https://madzadev.substack.com/)!

Also, connect with me on [Twitter](https://twitter.com/madzadev), [LinkedIn](https://www.linkedin.com/in/madzadev/), and [GitHub](https://github.com/madzadev)!
