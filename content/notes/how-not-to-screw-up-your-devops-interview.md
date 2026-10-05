---
title: "How Not to Screw Up Your DevOps Interview"
date: '2017-06-10T15:10:33-03:00'
category: webclip
summary: 'The author says he was underprepared for a DevOps interview, then reviews basic web app infrastructure topics he needed to explain better: HTTP requests, load balancing, redundancy, and virtual IPs.'
tags: ["devops-interview", "load-balancing", "virtual-ips"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Not to Screw Up Your DevOps Interview"
    url: "https://dev.to/georgeoffley/how-not-to-screw-up-your-devops-interview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/dev-to--how-not-to-screw-up-your-devops-interview.md"
    kind: repo
---

The author describes going into a DevOps interview unprepared, especially for the technical part, and says the interview exposed gaps in his answers. He also says the interviewers helped him through fundamentals of web app infrastructure and administration, which left him with more knowledge for next time.

## Reading notes

- The author says he was not prepared for the technical portion of the interview and had gaps in basic DevOps topics.
- He says asking what an unclear question means can be a useful response when he does not know the answer.
- The interview covered how a web app is distributed across multiple servers.
- Uptime is presented as critical for an internet-based business because downtime can cost real money and customers.
- An HTTP request is described as going from the browser to DNS, then to the web server, usually on port 80 or 443.
- The response from a web server is described as including a status code such as 200 when the request succeeds.
- The text says static files can be served directly by a web server, while dynamic apps use routing or handlers.
- A load balancer is described as proxying connections to different servers in a cluster.
- Load balancing is presented as a way to serve one hostname and one IP across multiple servers and handle many requests.
- The post lists software and hardware load balancers and names NGINX, Kemp, Zen, and Windows Server load balancing.
- The article names round robin, least connections, IP hash, and historical analysis as load-balancing algorithms.
- It says a single routing server becomes a choke point and that redundancy needs a backup server.
- Virtual IPs are described as a way to spread traffic across servers while clients still see one public address.
- CARP is described as supporting redundancy by allowing another host to take over if one goes down.
- Proxy ARP is described as using tunneling to proxy incoming traffic.
- The conclusion says DevOps combines systems and development and that the interview helped the author learn more.
