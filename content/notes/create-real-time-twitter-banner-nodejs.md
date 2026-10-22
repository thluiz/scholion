---
title: "Create Real-Time Twitter Banner using Node.js"
date: '2021-06-29T09:55:20-03:00'
category: webclip
summary: 'The post explains how to build a Twitter banner that updates with the three most recent followers, using Twitter API credentials, image downloading, Jimp compositing, and a looped update script.'
tags: ["nodejs", "twitter-api", "image-processing", "banner"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create Real-Time Twitter banner using Node.js"
    url: "https://blog.deveshb.me/create-a-real-time-twitter-banner"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/blog-deveshb-me--create-real-time-twitter-banner-nodejs.md"
    kind: repo
---

The post walks through building a Twitter banner that updates every 60 seconds with the profile images of the three most recent followers. It shows how to get Twitter API access, prepare a 1500x500 banner, fetch followers, download their images, composite them onto the banner, and upload the result back to Twitter.

## Reading notes

- Create a Twitter developer account, make a new app, switch the app to read and write, and collect the API key, API secret, access token, and access token secret.
- Prepare a 1500x500 banner image with Headers.me or Canva.
- Create an `index.js` file, run `npm init -y`, and install `twitter-api-client`, `fs`, `jimp`, and `axios`.
- Load the packages with `dotenv`, `twitter-api-client`, `axios`, `fs`, and `jimp`.
- Set up the Twitter client with the API key, API secret, access token, and access token secret.
- Test the connection by calling `followersList` with `screen_name` and `count: 3` and logging the returned users.
- Comment out the test code after confirming it works.
- Define a `download_image` function that uses `axios` to stream an image to a local file.
- Define a `drawImage` function that reads the banner and three follower images with Jimp, composites the avatars onto the banner, writes the final image, converts it to base64, and uploads it with `accountUpdateProfileBanner`.
- In `start()`, create an `image_url` array and a `lastDrawImage` timestamp.
- Fetch the latest three followers, unshift each profile image URL into the array, download the three images, and call `drawImage` when enough time has passed to avoid rate limits.
- Delete the downloaded images after updating the banner.
- Call `start()` once and repeat it with `setInterval(..., 6000)` so the process keeps running.
- The post says the code can be kept running or deployed on Heroku, and links a GitHub repo for reference.
