---
url: "https://arpitbhayani.me/blogs/heartbeats-in-distributed-systems/?lid=4fnwkhygnsw8"
captured_at: "2026-07-07T00:22:59+01:00"
title: "Heartbeats in Distributed Systems"
domain: "arpitbhayani-me"
---

---
In distributed systems, one of the fundamental challenges is knowing whether a node or service is alive and functioning properly. Unlike monolithic applications, where everything runs in a single process, distributed systems span multiple machines, networks, and data centers. This becomes even glaring when the nodes are geographically separated. This is where heartbeat mechanisms come into play.

Imagine a cluster of servers working together to process millions of requests per day. If one server silently crashes, how quickly can the system detect this failure and react? How do we distinguish between a truly dead server and one that is just temporarily slow due to network congestion? These questions form the core of why heartbeat mechanisms matter.

## What are Heartbeat Messages

At its most basic level, a heartbeat is a periodic signal sent from one component in a distributed system to another to indicate that the sender is still alive and functioning. Think of it as a simple message that says “I am alive!”

Heartbeat messages are typically small and lightweight, often containing just a timestamp, a sequence number, or an identifier. The key characteristic is that they are sent regularly at fixed intervals, creating a predictable pattern that other components can monitor.

The mechanism works through a simple contract between two parties: the sender and the receiver. The sender commits to broadcasting its heartbeat at regular intervals, say every 2 seconds. The receiver monitors these incoming heartbeats and maintains a record of when the last heartbeat was received. If the receiver does not hear from the sender within an expected timeframe, it can reasonably assume something has gone wrong.

```
<span><span>class</span><span> HeartbeatSender</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, interval_seconds):  </span></span>
<span><span>        self</span><span>.interval </span><span>=</span><span> interval_seconds  </span></span>
<span><span>        self</span><span>.sequence_number </span><span>=</span><span> 0</span></span>
<span></span>
<span><span>    def</span><span> send_heartbeat</span><span>(self, target):  </span></span>
<span><span>        message </span><span>=</span><span> {  </span></span>
<span><span>            'node_id'</span><span>: </span><span>self</span><span>.get_node_id(),  </span></span>
<span><span>            'timestamp'</span><span>: time.time(),  </span></span>
<span><span>            'sequence'</span><span>: </span><span>self</span><span>.sequence_number  </span></span>
<span><span>        }  </span></span>
<span><span>        send_to(message, target)  </span></span>
<span><span>        self</span><span>.sequence_number </span><span>+=</span><span> 1</span></span>
<span></span>
<span><span>    def</span><span> run</span><span>(self):  </span></span>
<span><span>        while</span><span> True</span><span>:  </span></span>
<span><span>            self</span><span>.send_heartbeat(target_node)  </span></span>
<span><span>            time.sleep(</span><span>self</span><span>.interval)  </span></span>
```

When a node crashes, stops responding, or becomes isolated due to network partitions, the heartbeats stop arriving. The monitoring system can then take appropriate action, such as removing the failed node from a load balancer pool, redirecting traffic to healthy nodes, or triggering failover procedures.

## Core Components of Heartbeat Systems

The first component is the heartbeat sender. This is the node or service that periodically generates and transmits heartbeat signals. In most implementations, the sender runs on a separate thread or as a background task to avoid interfering with the primary application logic.

The second component is the heartbeat receiver or monitor. This component listens for incoming heartbeats and tracks when each heartbeat was received. The monitor maintains state about all the nodes it is tracking, typically storing the timestamp of the last received heartbeat for each node. When evaluating node health, the monitor compares the current time against the last received heartbeat to determine if a node should be considered failed.

```
<span><span>class</span><span> HeartbeatMonitor</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, timeout_seconds):  </span></span>
<span><span>        self</span><span>.timeout </span><span>=</span><span> timeout_seconds  </span></span>
<span><span>        self</span><span>.last_heartbeats </span><span>=</span><span> {}  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> receive_heartbeat</span><span>(self, message):  </span></span>
<span><span>        node_id </span><span>=</span><span> message[</span><span>'node_id'</span><span>]  </span></span>
<span><span>        self</span><span>.last_heartbeats[node_id] </span><span>=</span><span> {  </span></span>
<span><span>            'timestamp'</span><span>: message[</span><span>'timestamp'</span><span>],  </span></span>
<span><span>            'sequence'</span><span>: message[</span><span>'sequence'</span><span>],  </span></span>
<span><span>            'received_at'</span><span>: time.time()  </span></span>
<span><span>        }  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> check_node_health</span><span>(self, node_id):  </span></span>
<span><span>        if</span><span> node_id </span><span>not</span><span> in</span><span> self</span><span>.last_heartbeats:  </span></span>
<span><span>            return</span><span> False</span><span>  </span></span>
<span><span>            </span></span>
<span><span>        last_heartbeat_time </span><span>=</span><span> self</span><span>.last_heartbeats[node_id][</span><span>'received_at'</span><span>]  </span></span>
<span><span>        time_since_heartbeat </span><span>=</span><span> time.time() </span><span>-</span><span> last_heartbeat_time  </span></span>
<span><span>        </span></span>
<span><span>        return</span><span> time_since_heartbeat </span><span>&lt;</span><span> self</span><span>.timeout  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> get_failed_nodes</span><span>(self):  </span></span>
<span><span>        failed_nodes </span><span>=</span><span> []  </span></span>
<span><span>        current_time </span><span>=</span><span> time.time()  </span></span>
<span><span>        </span></span>
<span><span>        for</span><span> node_id, data </span><span>in</span><span> self</span><span>.last_heartbeats.items():  </span></span>
<span><span>            if</span><span> current_time </span><span>-</span><span> data[</span><span>'received_at'</span><span>] </span><span>&gt;</span><span> self</span><span>.timeout:  </span></span>
<span><span>                failed_nodes.append(node_id)  </span></span>
<span><span>                </span></span>
<span><span>        return</span><span> failed_nodes  </span></span>
```

The third parameter is the heartbeat interval, which determines how frequently heartbeats are sent. This interval represents a fundamental trade-off in distributed systems. Sending heartbeats too frequently, we waste network bandwidth and CPU cycles. Send them too infrequently, and we will be slow to detect failures. Most systems use intervals ranging from 1 to 10 seconds, depending on the application requirements and network characteristics.

The fourth one is the timeout or failure threshold. This defines how long the monitor will wait without receiving a heartbeat before declaring a node as failed.

Note, the timeout must be carefully chosen to balance two competing concerns: fast failure detection versus tolerance for temporary network delays or processing pauses. A typical rule of thumb is to set the timeout to at least 2 to 3 times the heartbeat interval, allowing for some missed heartbeats before declaring failure.

## Deciding Heartbeat Intervals and Timeouts

When a system uses very short intervals, such as sending heartbeats every 500 milliseconds, it can detect failures quickly. However, this comes at a cost. Each heartbeat consumes network bandwidth, and in a large cluster with hundreds or thousands of nodes, the cumulative traffic can become significant. Additionally, very short intervals make the system more sensitive to transient issues like brief network congestion or garbage collection pauses.

Consider a system with 1000 nodes where each node sends heartbeats to a central monitor every 500 milliseconds. This results in 2000 heartbeat messages per second just for health monitoring. In a busy production environment, this overhead can interfere with actual application traffic.

Conversely, if the heartbeat interval is too long, say 30 seconds, the system becomes sluggish in detecting failures. A node could crash, but the system would not notice for 30 seconds or more. During this window, requests might continue to be routed to the failed node, resulting in user-facing errors.

Similarly, the timeout value must also account for network characteristics. In a distributed system spanning multiple data centers, network latency varies. A heartbeat sent from a node in California to a monitor in Virginia might take 80 milliseconds under normal conditions, but could spike to 200 milliseconds during periods of congestion.

Hence, if the timeout is set too aggressively, these transient delays trigger false alarms.

A practical approach is to measure the actual round-trip time in the network and use that as a baseline. Many systems follow the rule that the timeout should be at least 10 times the round-trip time. For example, if the average round-trip time is 10 milliseconds, the timeout should be at least 100 milliseconds to account for variance.

```
<span><span>def</span><span> calculate_timeout</span><span>(round_trip_time_ms, heartbeat_interval_ms):  </span></span>
<span><span>    # Timeout is 10x the RTT  </span></span>
<span><span>    rtt_based_timeout </span><span>=</span><span> round_trip_time_ms </span><span>*</span><span> 10</span><span>  </span></span>
<span><span>    </span></span>
<span><span>    # Timeout should also be at least 2-3x the heartbeat interval  </span></span>
<span><span>    interval_based_timeout </span><span>=</span><span> heartbeat_interval_ms </span><span>*</span><span> 3</span><span>  </span></span>
<span><span>    </span></span>
<span><span>    # Use the larger of the two  </span></span>
<span><span>    return</span><span> max</span><span>(rtt_based_timeout, interval_based_timeout)  </span></span>
```

Another important consideration is the concept of multiple missed heartbeats before declaring failure. Rather than marking a node as dead after a single missed heartbeat, systems wait until several consecutive heartbeats are missed. This approach reduces false positives caused by packet loss or momentary delays.

For instance, if we send heartbeats every 2 seconds and require 3 missed heartbeats before declaring failure, a node would need to be unresponsive for at least 6 seconds before being marked as failed. This provides a good balance between quick failure detection and tolerance for transient issues.

## Push vs Pull Heartbeat Models

Heartbeat mechanisms can be implemented using two different communication models: push and pull.

In a push model, the monitored node actively sends heartbeat messages to the monitoring system at regular intervals. The node takes responsibility for broadcasting its own health status. The monitored service simply runs a background thread that periodically sends a heartbeat message.

```
<span><span>class</span><span> PushHeartbeat</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, monitor_address, interval):  </span></span>
<span><span>        self</span><span>.monitor_address </span><span>=</span><span> monitor_address  </span></span>
<span><span>        self</span><span>.interval </span><span>=</span><span> interval  </span></span>
<span><span>        self</span><span>.running </span><span>=</span><span> False</span><span>  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> start</span><span>(self):  </span></span>
<span><span>        self</span><span>.running </span><span>=</span><span> True</span><span>  </span></span>
<span><span>        self</span><span>.heartbeat_thread </span><span>=</span><span> threading.Thread(</span><span>target</span><span>=</span><span>self</span><span>._send_loop)  </span></span>
<span><span>        self</span><span>.heartbeat_thread.daemon </span><span>=</span><span> True</span><span>  </span></span>
<span><span>        self</span><span>.heartbeat_thread.start()  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> _send_loop</span><span>(self):  </span></span>
<span><span>        while</span><span> self</span><span>.running:  </span></span>
<span><span>            try</span><span>:  </span></span>
<span><span>                self</span><span>._send_heartbeat()  </span></span>
<span><span>            except</span><span> Exception</span><span> as</span><span> e:  </span></span>
<span><span>                logging.error(</span><span>f</span><span>"Failed to send heartbeat: </span><span>{</span><span>e</span><span>}</span><span>"</span><span>)  </span></span>
<span><span>            time.sleep(</span><span>self</span><span>.interval)  </span></span>
<span><span>            </span></span>
<span><span>    def</span><span> _send_heartbeat</span><span>(self):  </span></span>
<span><span>        message </span><span>=</span><span> {  </span></span>
<span><span>            'node_id'</span><span>: </span><span>self</span><span>.get_node_id(),  </span></span>
<span><span>            'timestamp'</span><span>: time.time(),  </span></span>
<span><span>            'status'</span><span>: </span><span>'alive'</span><span>  </span></span>
<span><span>        }  </span></span>
<span><span>        requests.post(</span><span>self</span><span>.monitor_address, </span><span>json</span><span>=</span><span>message)  </span></span>
```

The push model works well in many scenarios, but it has limitations. If the node itself becomes completely unresponsive or crashes, it obviously cannot send heartbeats. Additionally, in networks with strict firewall rules, the monitored nodes might not be able to initiate outbound connections to the monitoring system.

-   Kubernetes Node Heartbeats
-   Hadoop YARN NodeManagers push heartbeats to the ResourceManager
-   Celery and Airflow workers push heartbeats to the schedule

In a pull model, the monitoring system actively queries the nodes at regular intervals to check their health. Instead of waiting for heartbeats to arrive, the monitor reaches out and asks, “Are you alive?” The monitored services expose a health endpoint that responds to these queries.

```
<span><span>class</span><span> PullHeartbeat</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, nodes, interval):  </span></span>
<span><span>        self</span><span>.nodes </span><span>=</span><span> nodes  </span><span># List of nodes to monitor  </span></span>
<span><span>        self</span><span>.interval </span><span>=</span><span> interval  </span></span>
<span><span>        self</span><span>.health_status </span><span>=</span><span> {}  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> start</span><span>(self):  </span></span>
<span><span>        self</span><span>.running </span><span>=</span><span> True</span><span>  </span></span>
<span><span>        self</span><span>.poll_thread </span><span>=</span><span> threading.Thread(</span><span>target</span><span>=</span><span>self</span><span>._poll_loop)  </span></span>
<span><span>        self</span><span>.poll_thread.daemon </span><span>=</span><span> True</span><span>  </span></span>
<span><span>        self</span><span>.poll_thread.start()  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> _poll_loop</span><span>(self):  </span></span>
<span><span>        while</span><span> self</span><span>.running:  </span></span>
<span><span>            for</span><span> node </span><span>in</span><span> self</span><span>.nodes:  </span></span>
<span><span>                self</span><span>._check_node(node)  </span></span>
<span><span>            time.sleep(</span><span>self</span><span>.interval)  </span></span>
<span><span>            </span></span>
<span><span>    def</span><span> _check_node</span><span>(self, node):  </span></span>
<span><span>        try</span><span>:  </span></span>
<span><span>            response </span><span>=</span><span> requests.get(</span><span>f</span><span>"http://</span><span>{</span><span>node</span><span>}</span><span>/health"</span><span>, </span><span>timeout</span><span>=</span><span>2</span><span>)  </span></span>
<span><span>            if</span><span> response.status_code </span><span>==</span><span> 200</span><span>:  </span></span>
<span><span>                self</span><span>.health_status[node] </span><span>=</span><span> {  </span></span>
<span><span>                    'alive'</span><span>: </span><span>True</span><span>,  </span></span>
<span><span>                    'last_check'</span><span>: time.time()  </span></span>
<span><span>                }  </span></span>
<span><span>            else</span><span>:  </span></span>
<span><span>                self</span><span>.mark_node_unhealthy(node)  </span></span>
<span><span>        except</span><span> Exception</span><span> as</span><span> e:  </span></span>
<span><span>            self</span><span>.mark_node_unhealthy(node)  </span></span>
```

The pull model provides more control to the monitoring system and can be more reliable in some scenarios. Since the monitor initiates the connection, it works better in environments with asymmetric network configurations. However, it also introduces additional load on the monitor, especially in large clusters where hundreds or thousands of nodes need to be polled regularly.

-   Load balancers actively probe backend servers
-   Prometheus pulls metrics endpoints on each target
-   Redis Sentinel monitors and polls Redis instances with PING

By the way, many real-world systems use a hybrid approach that combines elements of both models. For example, nodes might send heartbeats proactively (push), but the monitoring system also periodically polls critical nodes (pull) as a backup mechanism. This redundancy improves overall reliability.

## Failure Detection Algorithms

While basic heartbeat mechanisms are effective, they struggle with the challenge of distinguishing between actual failures and temporary slowdowns. This is where more sophisticated failure detection algorithms come into play.

The simplest failure detection algorithm uses a fixed timeout. If no heartbeat is received within the specified timeout period, the node is declared failed. While easy to implement, this binary approach is inflexible and prone to false positives in networks with variable latency.

```
<span><span>class</span><span> FixedTimeoutDetector</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, timeout):  </span></span>
<span><span>        self</span><span>.timeout </span><span>=</span><span> timeout  </span></span>
<span><span>        self</span><span>.last_heartbeats </span><span>=</span><span> {}  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> is_node_alive</span><span>(self, node_id):  </span></span>
<span><span>        if</span><span> node_id </span><span>not</span><span> in</span><span> self</span><span>.last_heartbeats:  </span></span>
<span><span>            return</span><span> False</span><span>  </span></span>
<span><span>        </span></span>
<span><span>        elapsed </span><span>=</span><span> time.time() </span><span>-</span><span> self</span><span>.last_heartbeats[node_id]  </span></span>
<span><span>        return</span><span> elapsed </span><span>&lt;</span><span> self</span><span>.timeout  </span></span>
```

### Phi Accrual Failure Detection

A more sophisticated approach is the [phi accrual failure detector](https://arpitbhayani.me/blogs/phi-accrual), originally developed for the Cassandra database. Instead of providing a binary output (alive or dead), the phi accrual detector calculates a suspicion level on a continuous scale. The higher the suspicion value, the more likely it is that the node has failed.

The phi value is calculated using statistical analysis of historical heartbeat arrival times. The algorithm maintains a sliding window of recent inter-arrival times and uses this data to estimate the probability distribution of when the next heartbeat should arrive. If a heartbeat is late, the phi value increases gradually rather than jumping immediately to a failure state.

The phi value represents the confidence level that a node has failed. For example, a phi value of 1 corresponds to approximately 90% confidence, a phi of 2 corresponds to 99% confidence, and a phi of 3 corresponds to 99.9% confidence.

## Gossip Protocols for Heartbeats

As distributed systems grow in size, centralized heartbeat monitoring becomes a bottleneck. A single monitoring node responsible for tracking thousands of servers creates a single point of failure and does not scale well. This is where gossip protocols come into play.

Gossip protocols distribute the responsibility of failure detection across all nodes in the cluster. Instead of reporting to a central authority, each node periodically exchanges heartbeat information with a randomly selected subset of peers. Over time, information about the health of every node spreads throughout the entire cluster, much like gossip spreads in a social network.

The basic gossip algorithm: each node maintains a local membership list containing information about all known nodes in the cluster, including their heartbeat counters. Periodically, the node selects one or more random peers and exchanges its entire membership list with them. When receiving a membership list from a peer, the node merges it with its own list, keeping the most recent information for each node.

```
<span><span>class</span><span> GossipNode</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, node_id, peers):  </span></span>
<span><span>        self</span><span>.node_id </span><span>=</span><span> node_id  </span></span>
<span><span>        self</span><span>.peers </span><span>=</span><span> peers  </span></span>
<span><span>        self</span><span>.membership_list </span><span>=</span><span> {}  </span></span>
<span><span>        self</span><span>.heartbeat_counter </span><span>=</span><span> 0</span><span>  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> update_heartbeat</span><span>(self):  </span></span>
<span><span>        self</span><span>.heartbeat_counter </span><span>+=</span><span> 1</span><span>  </span></span>
<span><span>        self</span><span>.membership_list[</span><span>self</span><span>.node_id] </span><span>=</span><span> {  </span></span>
<span><span>            'heartbeat'</span><span>: </span><span>self</span><span>.heartbeat_counter,  </span></span>
<span><span>            'timestamp'</span><span>: time.time()  </span></span>
<span><span>        }  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> gossip_round</span><span>(self):  </span></span>
<span><span>        # Update own heartbeat  </span></span>
<span><span>        self</span><span>.update_heartbeat()  </span></span>
<span><span>        </span></span>
<span><span>        # Select random peers to gossip with  </span></span>
<span><span>        num_peers </span><span>=</span><span> min</span><span>(</span><span>3</span><span>, </span><span>len</span><span>(</span><span>self</span><span>.peers))  </span></span>
<span><span>        selected_peers </span><span>=</span><span> random.sample(</span><span>self</span><span>.peers, num_peers)  </span></span>
<span><span>        </span></span>
<span><span>        # Send membership list to selected peers  </span></span>
<span><span>        for</span><span> peer </span><span>in</span><span> selected_peers:  </span></span>
<span><span>            self</span><span>._send_gossip(peer)  </span></span>
<span><span>            </span></span>
<span><span>    def</span><span> _send_gossip</span><span>(self, peer):  </span></span>
<span><span>        try</span><span>:  </span></span>
<span><span>            response </span><span>=</span><span> requests.post(  </span></span>
<span><span>                f</span><span>"http://</span><span>{</span><span>peer</span><span>}</span><span>/gossip"</span><span>,  </span></span>
<span><span>                json</span><span>=</span><span>self</span><span>.membership_list  </span></span>
<span><span>            )  </span></span>
<span><span>            received_list </span><span>=</span><span> response.json()  </span></span>
<span><span>            self</span><span>._merge_membership_list(received_list)  </span></span>
<span><span>        except</span><span> Exception</span><span> as</span><span> e:  </span></span>
<span><span>            logging.error(</span><span>f</span><span>"Failed to gossip with </span><span>{</span><span>peer</span><span>}</span><span>: </span><span>{</span><span>e</span><span>}</span><span>"</span><span>)  </span></span>
<span><span>            </span></span>
<span><span>    def</span><span> _merge_membership_list</span><span>(self, received_list):  </span></span>
<span><span>        for</span><span> node_id, info </span><span>in</span><span> received_list.items():  </span></span>
<span><span>            if</span><span> node_id </span><span>not</span><span> in</span><span> self</span><span>.membership_list:  </span></span>
<span><span>                self</span><span>.membership_list[node_id] </span><span>=</span><span> info  </span></span>
<span><span>            else</span><span>:  </span></span>
<span><span>                # Keep the entry with the higher heartbeat counter  </span></span>
<span><span>                if</span><span> info[</span><span>'heartbeat'</span><span>] </span><span>&gt;</span><span> self</span><span>.membership_list[node_id][</span><span>'heartbeat'</span><span>]:  </span></span>
<span><span>                    self</span><span>.membership_list[node_id] </span><span>=</span><span> info  </span></span>
<span><span>                    </span></span>
<span><span>    def</span><span> detect_failures</span><span>(self, timeout_seconds):  </span></span>
<span><span>        failed_nodes </span><span>=</span><span> []  </span></span>
<span><span>        current_time </span><span>=</span><span> time.time()  </span></span>
<span><span>        </span></span>
<span><span>        for</span><span> node_id, info </span><span>in</span><span> self</span><span>.membership_list.items():  </span></span>
<span><span>            if</span><span> node_id </span><span>!=</span><span> self</span><span>.node_id:  </span></span>
<span><span>                time_since_update </span><span>=</span><span> current_time </span><span>-</span><span> info[</span><span>'timestamp'</span><span>]  </span></span>
<span><span>                if</span><span> time_since_update </span><span>&gt;</span><span> timeout_seconds:  </span></span>
<span><span>                    failed_nodes.append(node_id)  </span></span>
<span><span>                    </span></span>
<span><span>        return</span><span> failed_nodes  </span></span>
```

The gossip protocol eliminates single points of failure since every node participates in failure detection. It scales well because the number of messages each node sends remains constant regardless of cluster size. It is also resilient to node failures since information continues to spread as long as some nodes remain connected.

However, gossip protocols also introduce complexity. Because information spreads gradually, there can be a delay before all nodes learn about a failure. This eventual consistency model means that different nodes might temporarily have different views of the cluster state. The protocol also generates more total network traffic since information is duplicated across many gossip exchanges, though this is usually acceptable since gossip messages are small.

Many production systems use gossip-based failure detection. Cassandra, for example, uses a gossip protocol where each node gossips with up to three other nodes every second. Nodes track both heartbeat generation numbers and version numbers to handle various failure scenarios. The protocol also includes mechanisms to handle network partitions and prevent split-brain scenarios.

## Implementation Considerations

One important implementation consideration is the transport protocol.

Should heartbeats use TCP or UDP? TCP provides reliable delivery and guarantees that messages arrive in order, but it also introduces overhead and can be slower due to connection establishment and acknowledgment mechanisms.

UDP is faster and more lightweight, but packets can be lost or arrive out of order. Many systems use UDP for heartbeat messages because occasional packet loss is acceptable, the receiver can tolerate missing a few heartbeats without declaring a node dead.

However, TCP is often preferred when heartbeat messages carry critical state information that must not be lost.

Another consideration is network topology. In systems spanning multiple data centers, network latency and reliability vary significantly between different paths. A heartbeat between two nodes in the same data center might have a round-trip time of 1 millisecond, while a heartbeat crossing continents might take 100 milliseconds or more. Systems should account for these differences, potentially using different timeout values for local versus remote nodes.

```
<span><span>class</span><span> AdaptiveHeartbeatConfig</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self):  </span></span>
<span><span>        self</span><span>.configs </span><span>=</span><span> {}  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> configure_for_node</span><span>(self, node_id, location):  </span></span>
<span><span>        if</span><span> location </span><span>==</span><span> 'local'</span><span>:  </span></span>
<span><span>            config </span><span>=</span><span> {  </span></span>
<span><span>                'interval'</span><span>: </span><span>1000</span><span>,  </span><span># 1 second  </span></span>
<span><span>                'timeout'</span><span>: </span><span>3000</span><span>,   </span><span># 3 seconds  </span></span>
<span><span>                'protocol'</span><span>: </span><span>'UDP'</span><span>  </span></span>
<span><span>            }  </span></span>
<span><span>        elif</span><span> location </span><span>==</span><span> 'same_datacenter'</span><span>:  </span></span>
<span><span>            config </span><span>=</span><span> {  </span></span>
<span><span>                'interval'</span><span>: </span><span>2000</span><span>,  </span><span># 2 seconds  </span></span>
<span><span>                'timeout'</span><span>: </span><span>6000</span><span>,   </span><span># 6 seconds  </span></span>
<span><span>                'protocol'</span><span>: </span><span>'UDP'</span><span>  </span></span>
<span><span>            }  </span></span>
<span><span>        else</span><span>:  </span><span># remote_datacenter  </span></span>
<span><span>            config </span><span>=</span><span> {  </span></span>
<span><span>                'interval'</span><span>: </span><span>5000</span><span>,  </span><span># 5 seconds  </span></span>
<span><span>                'timeout'</span><span>: </span><span>15000</span><span>,  </span><span># 15 seconds  </span></span>
<span><span>                'protocol'</span><span>: </span><span>'TCP'</span><span>  </span></span>
<span><span>            }  </span></span>
<span><span>            </span></span>
<span><span>        self</span><span>.configs[node_id] </span><span>=</span><span> config  </span></span>
<span><span>        return</span><span> config  </span></span>
```

Another important implementation consideration is to ensure that we do not have blocking operations in the heartbeat processing path. Heartbeat handlers should execute quickly and defer any expensive operations to separate worker threads.

Resource management is also critical. In a system with thousands of nodes, maintaining separate threads or timers for each node can exhaust system resources. We should prefer event-driven architectures or thread pools to efficiently manage concurrent heartbeat processing. Connection pooling would also reduce the overhead of establishing new connections for each heartbeat message.

## Network Partitions and Split-brain

A network partition occurs when network connectivity is disrupted, splitting a cluster into two or more isolated groups. Nodes within each partition can communicate with each other but cannot reach nodes in other partitions.

During a partition, nodes on each side will stop receiving heartbeats from nodes on the other side. This creates an ambiguous situation where both sides might believe the other has failed. If not handled carefully, this can lead to split-brain scenarios where both sides continue operating independently, potentially leading to data inconsistency or resource conflicts.

Consider a database cluster with three nodes spread across two data centers. If the network connection between data centers fails, the nodes in each data center will form separate partitions. Without proper safeguards, both partitions might elect their own leader, accept writes, and diverge from each other.

To handle network partitions correctly, systems often use quorum-based approaches. A quorum is the minimum number of nodes that must agree before taking certain actions. For example, a cluster of five nodes might require a quorum of three nodes to elect a leader or accept writes.

During a partition, only the partition containing at least three nodes can continue operating normally. The minority partition recognizes it has lost quorum and stops accepting writes.

```
<span><span>class</span><span> QuorumBasedFailureHandler</span><span>:  </span></span>
<span><span>    def</span><span> __init__</span><span>(self, total_nodes, quorum_size):  </span></span>
<span><span>        self</span><span>.total_nodes </span><span>=</span><span> total_nodes  </span></span>
<span><span>        self</span><span>.quorum_size </span><span>=</span><span> quorum_size  </span></span>
<span><span>        self</span><span>.reachable_nodes </span><span>=</span><span> set</span><span>()  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> update_reachable_nodes</span><span>(self, node_list):  </span></span>
<span><span>        self</span><span>.reachable_nodes </span><span>=</span><span> set</span><span>(node_list)  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> has_quorum</span><span>(self):  </span></span>
<span><span>        return</span><span> len</span><span>(</span><span>self</span><span>.reachable_nodes) </span><span>&gt;=</span><span> self</span><span>.quorum_size  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> can_accept_writes</span><span>(self):  </span></span>
<span><span>        return</span><span> self</span><span>.has_quorum()  </span></span>
<span><span>        </span></span>
<span><span>    def</span><span> should_step_down_as_leader</span><span>(self):  </span></span>
<span><span>        return</span><span> not</span><span> self</span><span>.has_quorum()  </span></span>
```

## Real-world Applications

Each node in a Kubernetes cluster runs a kubelet agent that periodically sends node status updates to the API server. By default, kubelets send updates every 10 seconds. If the API server does not receive an update within 40 seconds, it marks the node as NotReady.

Kubernetes also implements liveness and readiness probes at the pod level. A liveness probe checks whether a container is running properly, and if the probe fails repeatedly, Kubernetes restarts the container. A readiness probe determines whether a container is ready to accept traffic, and failing readiness probes cause the pod to be removed from service endpoints.

```
<span><span>apiVersion</span><span>: </span><span>v1</span><span>  </span></span>
<span><span>kind</span><span>: </span><span>Pod</span><span>  </span></span>
<span><span>metadata</span><span>:  </span></span>
<span><span>  name</span><span>: </span><span>example-pod</span><span>  </span></span>
<span><span>spec</span><span>:  </span></span>
<span><span>  containers</span><span>:  </span></span>
<span><span>  - </span><span>name</span><span>: </span><span>app</span><span>  </span></span>
<span><span>    image</span><span>: </span><span>myapp:latest</span><span>  </span></span>
<span><span>    livenessProbe</span><span>:  </span></span>
<span><span>      httpGet</span><span>:  </span></span>
<span><span>        path</span><span>: </span><span>/healthz</span><span>  </span></span>
<span><span>        port</span><span>: </span><span>8080</span><span>  </span></span>
<span><span>      initialDelaySeconds</span><span>: </span><span>15</span><span>  </span></span>
<span><span>      periodSeconds</span><span>: </span><span>10</span><span>  </span></span>
<span><span>      timeoutSeconds</span><span>: </span><span>2</span><span>  </span></span>
<span><span>      failureThreshold</span><span>: </span><span>3</span><span>  </span></span>
<span><span>    readinessProbe</span><span>:  </span></span>
<span><span>      httpGet</span><span>:  </span></span>
<span><span>        path</span><span>: </span><span>/ready</span><span>  </span></span>
<span><span>        port</span><span>: </span><span>8080</span><span>  </span></span>
<span><span>      initialDelaySeconds</span><span>: </span><span>5</span><span>  </span></span>
<span><span>      periodSeconds</span><span>: </span><span>5</span><span>  </span></span>
<span><span>      timeoutSeconds</span><span>: </span><span>2</span><span>  </span></span>
```

Cassandra, a distributed NoSQL database, uses gossip-based heartbeats to maintain cluster membership. Each Cassandra node gossip with up to three other random nodes every second. The gossip messages include heartbeat generation numbers that increment whenever a node restarts and heartbeat version numbers that increment with each gossip round.

Cassandra uses the phi accrual failure detector to determine when nodes are down. The default phi threshold is 8, meaning a node is considered down when the algorithm is about 99.9999% confident it has failed. This adaptive approach allows Cassandra to work reliably across diverse network environments.

etcd, a distributed key-value store used by Kubernetes, implements heartbeats as part of its Raft consensus protocol. The Raft leader sends heartbeat messages to followers every 100 milliseconds by default. If a follower does not receive a heartbeat within the election timeout (typically 1000 milliseconds), it initiates a new leader election.

Heartbeats are essential to distributed systems. From simple periodic messages to sophisticated adaptive algorithms, heartbeats enable systems to maintain awareness of component health and respond to failures quickly.

The key to effective heartbeat design lies in balancing competing concerns. Fast failure detection requires frequent heartbeats and aggressive timeouts, but this increases network overhead and sensitivity to transient issues. Slow detection reduces resource consumption and false positives but leaves the system vulnerable to longer outages.

As we design distributed systems, consider heartbeat mechanisms early in the architecture process. The choice of heartbeat intervals, timeout values, and failure detection algorithms significantly impacts system behavior under failure conditions.

No matter what we are building, heartbeats remain an essential tool for maintaining reliability.
