---
url: "https://substack.com/home/post/p-169730157"
captured_at: "2026-08-24T17:50:20+01:00"
title: "Day 1: Event-Driven Architecture Fundamentals - by Systems"
domain: "substack.com"
---
### What We're Building Today

By the end of this lesson, a complete event-driven social media platform that processes thousands of events per second: an event taxonomy with 10 distinct event types, a real-time Kafka producer/consumer architecture, a FastAPI backend with event processing endpoints, an interactive React dashboard with live event visualization, and a testing suite for production readiness.

### The Problem with Request-Response

Traditional web applications work like phone calls - every action requires waiting for a response. When Sarah likes a post, the system must immediately update counters, notify followers, trigger recommendations, and log analytics. This creates a bottleneck where one slow operation blocks everything else. Real-world pain points cited: Instagram's like button freezing during high traffic, Twitter's timeline delays during viral events, LinkedIn's connection requests timing out.

### Event-Driven Architecture Solution

Events transform synchronous operations into asynchronous streams. Instead of waiting for each operation, the system publishes events that flow through independently. Think of events as notifications broadcasted to anyone interested. When Sarah likes a post, the system emits a `user_interaction` event. Multiple services consume this event simultaneously - analytics tracks engagement, notifications alert the author, and recommendations update Sarah's feed.

### StreamSocial Event Taxonomy

The example platform needs three event categories:

1. User Actions (6 events): user_registration, user_login, user_profile_update, user_follow, user_post_create, user_post_delete
2. Content Interactions (3 events): content_like, content_comment, content_share
3. System Events (1 event): system_notification

### Core Architecture Components

**Event Producer**: captures user actions and publishes structured events to Kafka topics. Each event contains metadata like timestamp, user_id, and action-specific data.

**Event Consumer**: services that subscribe to relevant event streams. The notification service consumes content_like events, while analytics consumes everything.

**Event Store (Kafka)**: a distributed log that persists events in ordered topics. Events remain available for replay, enabling new services to process historical data.

### System Design Context

Event-driven architecture enables: decoupling (services operate independently without blocking each other), scalability (each service scales based on its specific load patterns), resilience (failed services don't affect event publishing), flexibility (new features consume existing event streams without system changes).

### Real-World Applications

- Netflix: video play events trigger recommendation updates, billing calculations, and content popularity tracking
- Uber: ride requests create events consumed by driver matching, pricing, and analytics services
- Slack: message events update multiple clients, trigger notifications, and index content for search

### Production Benefits

Event-driven systems handle traffic spikes gracefully. During viral content, like counts update asynchronously without blocking user interactions. Failed operations retry automatically through event replay. The distributed nature means global scaling - events published in Asia get consumed by services in America with minimal latency.

### Hands-On Implementation

The lesson walks through a full local build: project structure, a Python virtual environment, Pydantic event models (`EventType` enum covering the ten event types plus a `StreamSocialEvent` schema with event_id, event_type, timestamp, user_id, session_id and a data payload), a Kafka + Zookeeper docker-compose cluster, a `StreamSocialEventProducer`/`StreamSocialEventConsumer` pair using kafka-python, a FastAPI server exposing `/events/user/register` and `/events/recent`, and a React dashboard polling the API every 2 seconds to show live stats (total events, user registrations, content interactions). Unit and integration tests are included (pytest for the event model, a requests-based check for the registration endpoint).

### Today's Challenge: Event Type Definition

Design the 10 event types considering user lifecycle events (registration, authentication, profile changes), content interaction events (likes, comments, shares, saves), and system-generated events (notifications, recommendations, moderation). Each event should be atomic (representing one specific action) and contain sufficient context for downstream processing.

### Next Steps

The next lesson deploys a 3-broker Kafka cluster with Docker Compose, transforming the single-node setup into a production-ready distributed system capable of handling millions of events per second. Assignment: extend the event taxonomy with 5 additional event types for features like direct messaging, content moderation, or user analytics, considering how each event would be consumed by different services.
