---
url: "https://x.com/milan_milanovic/status/1742576659067191706?s=20"
captured_at: "2024-01-03T16:00:25+00:00"
title: "Dr Milan Milanović (@milan_milanovic) on X"
domain: "x-com"
---

𝗦𝘆𝘀𝘁𝗲𝗺 𝗗𝗲𝘀𝗶𝗴𝗻: 𝗛𝗼𝘄 𝘁𝗼 𝗗𝗲𝘀𝗶𝗴𝗻 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺

In this post, we continue with the system design series. Let's first discuss the requirements:

𝟭. 𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗺𝗲𝗻𝘁𝘀:

Functional requirements:

- Upload images from a mobile client
- Users follow other users
- Generate a feed of images
- Scale: 10 million users / upload 2 photos per month, wherever photo have 5MB -> 100TB month -> 1.2PB per year

Non-functional Requirements: Our system should be available. In the case of any web service, it’s a mandatory rule. The system should also be reliable, which means any uploaded photo by users should never be lost.

𝟮. 𝗗𝗲𝘀𝗶𝗴𝗻 𝗱𝗮𝘁𝗮 𝘀𝘁𝗼𝗿𝗮𝗴𝗲

First, we create three tables to hold users, photos, and followers:

- User (name, email, location, lastLoginTime)
- Photo (user_id, title, location, URL, creationDate)
- UserFollow (from, to)

𝟯. 𝗗𝗲𝘀𝗶𝗴𝗻 𝘀𝘆𝘀𝘁𝗲𝗺

The next step is to design the system. The first flow is when we have uploaded the image. From the mobile device, we hit the API gateway (single entry point for all clients), which then hit Load Balancer before going to the write App server. The load balancer is here to distribute the user traffic to many servers. 

Here, we keep many copies of the component to remove the single point of failure in the system, making it highly available. This server writes the image metadata to the Metadata DB, while the image is written to the Azure Blob/ AWS S3 or similar service. 

To support millions of users, we need to partition our database to divide and store our data into different DB servers. We can use database sharding for metadata. If we partition metadata DB based on ‘UserID,’ we may keep all the user photos in the same shard. One User seems to have almost 3 TB of data. If one DB shard is 1TB, we will need three data shards for each User.

Reading the images from the system is done via the App server (read), which reuses the cache (e.g., Redis), which reads metadata from the Metadata DB and returns it to the client, which then reads the image itself from the Blob/S3, or do this via CDN close to him.

The third option is a feed of images the user sees in the app. Here, we can use the Feed Generation service, which reads data from the Cache or Metadata DB. Users can get the latest newsfeed from the server using two approaches:

- 𝘗𝘶𝘭𝘭-𝘉𝘢𝘴𝘦𝘥 𝘈𝘱𝘱𝘳𝘰𝘢𝘤𝘩. In this approach, each User may poll the server after a regular interval to check if any friend has a new update. The server has to find all the user connections and check for each friend to create a new post. If there are new posts, the database’s query will get all the recent posts created by a user’s connections.

- 𝘗𝘶𝘴𝘩-𝘉𝘢𝘴𝘦𝘥 𝘈𝘱𝘱𝘳𝘰𝘢𝘤𝘩. In this approach, servers can push new data to the users as soon as it is available. Users must maintain a long polling request with the server to receive the updates.

#softwarearchitecture #systemdesign #programming
