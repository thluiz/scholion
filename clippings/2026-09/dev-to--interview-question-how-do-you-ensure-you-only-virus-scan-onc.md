---
url: "https://dev.to/miketalbot/interview-question-ensure-you-only-virus-scan-once-349j?"
captured_at: "2026-09-25T19:16:00+01:00"
title: "Interview Question: how do you ensure you only virus scan once?"
domain: "dev-to"
---

[![Cover image for Interview Question: how do you ensure you only virus scan once?](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2oispulophh52xyu9wkc.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2oispulophh52xyu9wkc.jpg)

[![Mike Talbot ⭐](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F388880%2Fbb28323e-d2d2-42a9-a95c-5147e7c3558f.jpeg)](https://dev.to/miketalbot)

I see a lot of interview questions being proposed that are around DSA and lower level algorithms that I don't really expect people to be writing in 2024.

Over the years I've interviewed thousands of developers and run teams of hundreds, so my team and I have developed questions that aim to test people's understanding of challenges they will face frequently.

## [](#example-interview-question)Example interview question

> You are writing a module that requires files to be uploaded to a server for processing. All uploaded files must be virus scanned. It is quite likely that users will upload the same file throughout their usage lifetime; multiple different users may also upload the same file. How do we minimise the time impact and cost of virus scanning the same file multiple times? If we need to store the file, can your solution optimise storage? How does your method affect the UX of the solution? How fault-tolerant is your method?

It's questions like this that I want my team to be able to reason out good answers to. A good solution will require an understanding of the tools that could be used and their performance and memory characteristics; I'd expect good answers to touch on services or tools that could be expected to help.

A suitable answer would be:

*   I would create a `name` for the file based on a V5 GUID, those kind of GUIDs are derived from the contents of the file. I'd check whether a file already existed with the `name` on my storage, and if it did, I'd see whether it was flagged as infected and report this immediately. If the `name` file did not exist, I'd virus scan the file and upload it with an indication of whether it was clean or infected. I only virus scan files once, and I only upload files once; this minimises the time taken and the cost of server resources while retaining a good UX.
*   **If we need to store the file multiple times?** My solution naturally stores the file only once and then uses the `name` as a reference. This has the added advantage that it's easy to find all the places where the same file is used.
*   **How does your method affect the UX of the solution?** Users can just upload files; they don't have to worry about anything, it minimises any impact on them.
*   **How fault-tolerant is your method?** It is pretty fault tolerant; although new viruses emerge and new detections are implemented, you could either record each filename and the version that was used to scan it, minimising rescan time, or you could change the namespace of the V5 GUID so that future uploaded files would be scanned again at the expense of duplicating storage.
*   **What tools would you use?** I'd store the `name` in a database for the user; I might use Redis to check file `name`s to improve performance.
*   **Why did you choose this method?** The lookup of the file is an O(1) operation after the `name` has been created, which is the optimal approach as the system scales. The creation of the `name` is an O(N) operation based on the size of the file being uploaded, but I have that file and need to process it anyway so reading it seems to be something that already needs to happen.

### [](#guiding-interviewees)Guiding interviewees

Suppose an interviewee started down a track of suggesting that the user should be responsible for ensuring a file existed only once. In that case, the key is to guide them into considering the poor UX this would give users. Some candidates can't get away from questions like these or challenges to the requirements, those people aren't the ones I'm looking for and if after guidance, they haven't found a solution that minimises costs and maximises UX, then I've got my answer.

## [](#conclusion)Conclusion

I think it's vital to see how people reason with real-world problems rather than parrot back algorithms that you can learn by rote.

There are, of course, many ways to solve this problem; it's by understanding the thought processes of the interviewee that you learn their style and their ways of reasoning. This is the vital thing for me.
