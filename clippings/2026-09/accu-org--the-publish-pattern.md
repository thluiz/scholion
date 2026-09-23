---
url: "https://accu.org/journals/overload/32/183/teodorescu/?ref=dailydev"
captured_at: "2026-09-23T17:30:10+01:00"
title: "The Publish Pattern"
domain: "accu-org"
---

The Publish Pattern - go to homepage
HOME
NEWS
CONFERENCES
VIDEOS
JOURNALS
REVIEWS
LOCAL GROUPS
JOIN!
LOG IN
The Publish Pattern

The Publish Pattern

By Lucian Radu Teodorescu

Overload, 32(183):16-19, October 2024

How do you minimise locking between producers and consumers? Lucian Radu Teodorescu describes a common, but currently undocumented, design pattern.

Design patterns can help us reason about code. They are like algorithms that are vaguely defined in the code. Once we recognise a pattern, we can easily draw conclusions about the behaviour of the code without looking at all the parts. Patterns also help us when designing software; they are known solutions to common problems.1

In this article, we describe a concurrency pattern that can't be found directly in any listing of concurrency patterns, and yet, it appears (in one way or another) in many codebases. It is useful when we have producers and consumers that run continuously, and we want to minimise the locking between them.

Problem description

Let's say we have an open-world game. As the player walks through the world, we load the data corresponding to the regions around the player. We have two types of workloads in our scenario: one for loading the data and another for displaying the loaded data. For the sake of our discussion, let's say that each of these two activities is bound to a thread.

The problem we are trying to solve is how to structure the passing of data (let's call this document) from the loading thread (producer) to the rendering thread (consumer). This is analogous to the classical producer-consumer problem [Wikipedia-1], but it has some interesting twists. Let's try to outline the requirements of the problem:

(R1) The producer is constantly producing new versions of the document.
(R2) The consumer is constantly consuming document data.
(R3) The consumer will use the latest version of the document.

Please note that we are discussing multiple versions of the document. In our example, the loading thread will produce different documents depending on the position of the player, and the rendering thread will display the latest document, corresponding to the player's most recent position.

A naïve implementation for this problem might look like the code in Listing 1. Here, we have two functions, produce() and consume(), that are called multiple times from the appropriate threads. They both work on a shared document, current_document, so they need something to protect concurrent access to this object. We use a mutex to ensure that we are not reading the document while modifying it.2

struct document_t {...};

void produce_unprotected(document_t& d);
void consume_unprotected(const document_t& d);

document_t current_document;
std::mutex document_bottleneck;

void produce() {
  std::lock_guard<std::mutex>
    lock{document_bottleneck};
  produce_unprotected(current_document);
}

void consume() {
  std::lock_guard<std::mutex>
    lock{document_bottleneck};
  consume_unprotected(current_document);
}

Listing 1

This implementation meets our requirements, but it likely has performance issues. If producing the document takes a long time (which is often the case when loading data from disk), then rendering might be blocked until the operation completes. This is completely unacceptable for this type of application. Moreover, considering the potential usage of the data, this is also suboptimal, as we are often loading data that is far from the player, thereby blocking rendering for data that we might not even need.

This means we need to add a new requirement:

(R4) Consuming the data should not be delayed by delays in producing the data.

With this new requirement, the naïve implementation from Listing 1 no longer works. Let's explore how we can improve it.

The Publish Pattern

We need to find a way to decouple the production and consumption of the document. The consumer needs to use the latest version of the published document but doesn't necessarily need to wait for the producer to complete if production is currently happening. Similarly, the production of the document doesn't need to wait until the latest version of the document is consumed. This is the essence of what I call the Publish Pattern.

Similar to the mutex implementation, we still have three parts:

The latest published document
A way to update the published document (without blocking the consumers)
A way to consume the published document (without preventing the publishing of new versions of the document)

The code that implements this might resemble what is shown in Listing 2, and the definition of the published template may look like the one in Listing 3. The interaction between the producer and the consumer occurs through a published_document object that is thread-safe. The producer takes the current document, makes a copy of it, and then edits this copy; when the new document is ready, it is published to the shared published_document object. The consumer simply takes the latest version from published_document (which is a std::shared_ptr<const document_t>) and uses the object freely.

struct document_t {...};

void produce_unprotected(document_t& d);
void consume_unprotected(const document_t& d);

published<document_t> published_document;

void produce() {
  // Make a copy of the currently published
  // document.
  document_t new_version(
    *published_document.get());
  // Perform the needed updates.
  produce_unprotected(new_version);
  // Publish the new version.
  published_document.publish(
    std::move(new_version));
}

void consume() {
  auto current = published_document.get();
  consume_unprotected(*current);
  // The current document is kept alive until
  // the end of the function.
}

Listing 2
template <typename T>
class published {
public:
  void publish(T&& doc) {
    std::lock_guard<std::mutex>
      lock(small_bottleneck_);
    published_document_ =
      std::make_shared<const T>(std::move(doc));
  }

  std::shared_ptr<const T> get() {
    std::lock_guard<std::mutex>
      lock(small_bottleneck_);
    return published_document_;
  }

private:
  std::shared_ptr<const T> published_document_;
  std::mutex small_bottleneck_;
};

Listing 3

The published template provides two basic thread-safe operations on an inner std::shared_ptr<const T> object. The first operation is to update the content of this object, and the second is to simply return a copy of the shared pointer.

The key element is the internal type: std::shared_ptr<const T>. Because the inner object of the shared pointer is const, nobody can change it after it's created.

This means that copies of the std::shared_ptr<const T> object can be passed around and safely shared across threads; we don't have race conditions on the inner object.

When we want to update the document, we update just the master copy of the object, the one embedded in the published<T> class; we do this under a lock to prevent copies being made while we update the master copy. All the copies we've already made are still valid, and they don't become invalidated by updating the master copy.

This means that the consumers, on whichever threads they run, can continue to use their versions of the document regardless of how many times we publish a new document. Thus, we fulfil all four requirements we had.

Analysis
Performance

For most problems, using this pattern is relatively cheap. We have just 2, potentially 3, heavy operations:

a memory allocation each time we publish a new document
small synchronisation when we publish and when we get the latest version of the document
(potentially) copying of the document

If the producing and the consuming operation are expensive (which is the main use case for this pattern), then a memory allocation for publishing a new document should be a very small cost.

Similarly, the contention on accessing the latest published document inside the published<T> class should be very small. We are doing very little inside the lock, and the lock is taken infrequently (twice while producing and once while consuming). Depending on the platform, the lock can be improved by using a spin-lock, but I would argue that for most cases, this won't be necessary; anyways, we should measure first.

Finally, we are making a copy of the document. Depending on the document type, this may be an expensive operation. If the documents are hard to copy, there may be ways of improving the copying type. We will provide some tips later.

Thread safety

An instance of published<T> can be safely shared across threads and called from multiple threads. The content of the std::shared_ptr<const T> objects obtained from a published<T> can also be freely used across different threads. The inner objects are marked as const, so we can only have read-only access to them. In the absence of a writer to this object, there is no data race when accessing it.

This immediately implies that we can have multiple consumers running at the same time. They can all view the same document (i.e., the latest version), or they may be viewing different versions of the document if there was at least one publish call during the execution of a consumer job.

Strictly speaking, from a thread safety perspective, it's also acceptable to have multiple producers running at the same time. They may overwrite the documents that the other producers generate, but this doesn't pose a thread safety issue.

This approach manages to retain thread safety while dramatically reducing the scope of the locks.

Functionality

Let's now analyse the proposed pattern from a functional point of view. One can easily see that requirements (R1) and (R2) are fulfilled. Nothing prevents the two threads from continuously producing and consuming documents. Requirement (R4) is also satisfied, as the consumers are not affected by the duration of the producer operation. If producing the document takes longer, consumers will see new versions of the document less frequently, but they are not prevented from running at the same pace.

Requirement (R3) is slightly more interesting. When a consumer starts its job, the first thing it does is retrieve the latest published version of the document. From this perspective, we can say that (R3) is satisfied. But this is not the complete story. During the consumer's work, the producer may publish a new version of the document; it's even possible for more than one version of the document to be published. That is, the fact that when the consumer job started, it had the latest version of the published document doesn't mean that by the time the job is finished, it still has the latest version of the document. This is an important functional aspect that the user needs to account for.

On the other hand, this technique ensures that once we start consuming a version of the document, the inner parts of the document don't change. We get 100% consistency when consuming the document. This technique linearises the producer and consumer operations [Wikipedia-2].

From a safety perspective, we can have multiple producers running at the same time. But from a functional perspective, that would be a bug. The problem is that one producer may completely overwrite the changes made by another producer. There are ways to fix this, but this is outside the pattern laid out by Listing 2.

Memory consumption

One of the things that the user may need to pay attention to is memory (and, in general, resource) consumption. If we have many long-running consumers, we may end up with multiple versions of the document. If the documents consume a significant amount of memory, this might be a problem.

The Publish pattern doesn't guarantee an upper bound to the number of documents that may be in flight at a given time.

This is a downside of having the possibility of multiple independent consumers, which also run independently from the producer(s). If we had used locking, we would implicitly guarantee that there is only one version of the document available.

Variants and improvements

The term the Publish pattern is something I coined to describe a behaviour that I implemented to solve a problem similar to the one described here (at that time, I was working on navigation software). The idea seemed to be applicable in multiple contexts; indeed, since then, I've applied it multiple times in various contexts. I took inspiration for this technique from a presentation by Herb Sutter on implementing atomic linked lists, in which he advocated for std::atomic<std::shared_ptr<T>> [Sutter14].

In essence, this pattern is a form of double-buffering or, more generally, multiple-buffering [Wikipedia-3]. One can use the Publish pattern to implement double-buffering; conversely, one can use double-buffering techniques in places where the Publish pattern could be applied. Compared to the typical double-buffering technique, I appreciate the simplicity and generality of the Publish pattern.

From a different perspective, we can consider this to be a variant of the read-copy-update (RCU) synchronisation mechanism [Wikipedia-4]. While RCU is a low-level technique, the Publish pattern is something that we can apply to complex documents.

Handling multiple producers

As previously mentioned, the code from Listing 2 doesn't work if we have multiple producers running at the same time. One of the producers might overwrite the data produced by the others.

To solve this, we may employ an optimistic locking scheme [Wikipedia-5]. We publish a new version of the document only if a new version hasn't been published while we were computing the new version to publish. Otherwise, we can retry the publish operation.

This can be implemented with code similar to Listing 4. When trying to publish, we check if nothing else has been published in the meantime; if we have the same document, we can publish directly. Otherwise, we get the latest version of the document, reapply the updates, and retry.

template <typename T> class published {
public:
  bool try_publish(std::shared_ptr<const T>& old,
  T&& doc) {
    std::lock_guard<std::mutex>
      lock(small_bottleneck_);
    if (published_document_ != old) {
      // tell the caller which is the current
      // document
      old = published_document_;
      return false;
    }
    published_document_ =
      std::make_shared<const T>(std::move(doc));
    return true;
  }
  ...
};

void apply_updates(const document_t& base,
  document_t& doc);

void produce_with_retry() {
  auto current = published_document.get();
  // Make a copy of the currently published
  // document.
  document_t new_version(*current);
  // Perform the needed updates.
  produce_unprotected(new_version);
  // Publish the new version.
  while (!published_document.try_publish(current,
         std::move(new_version))) {
    // 'current' is now the latest version;
    // reapply the updates, and retry.
    apply_updates(*current, new_version);
  }
}

Listing 4

One downside of this algorithm is that we don't have an upper bound on how many times we can retry publishing a document. If applying some updates takes a long time, we may constantly get new versions of the document published in the meantime, which would keep the retry process running endlessly. As the reader might have guessed, there are techniques for detecting long retry chains and failing the entire update after a certain number of retries. One can imagine more complex strategies for dealing with these cases, but that is outside the scope of this article.

Merging the latest version of the document with the changes local to the producer may not be a trivial task, but it's doable.

The bottom line is that the Publish pattern can be easily adapted to work in contexts where multiple producers are needed.

Monotonic updates

My friend, Dimi Racordon, wanted to speed up the Hylo compiler [Hylo] by introducing concurrency into the type checker. Oversimplifying, the activity of a type checker can be seen as building a graph (for the most part, it's a tree) and evaluating the validity of each node. Different declarations and type evaluations will typically generate different nodes in the graph. Many nodes in the graph can be processed in parallel, even if sometimes they need to intersect (e.g., different declarations depend on the same type).

The implementation that Dimi chose for speeding up the type checker closely resembles the Publish pattern with multiple producers. A producer type-checks a set of nodes, and after a while, publishes the results obtained so far, so that others can see the progress. However, in her case, the way the document is updated has a special property: all the updates are monotonic. That is, once we add some information to the document, we can never remove it.

Having guaranteed monotonic updates may make merging the documents much easier. All the updates to the documents are additions, so merging involves placing our additions on top of those in the base document.

This strategy may allow us to break the producer's job into two parts: determining additions and committing the additions. This may look like the code from Listing 5. This approach reduces the lifetime of the current version of the document; after all, the main activity is producing the updates. This implies that the chances of other documents being produced while we apply the updates are reduced. In this way, we reduce the overall time needed to publish a new version of the document.

void produce_monotonic() {
  // Produce the additions
  auto additions = produce_additions();
  // Publish a new version of the document.
  auto current = published_document.get();
  while (true) {
    document_t new_version(*current);
    update_document(new_version, additions);
    if (published_document.try_publish(current,
        std::move(new_version)))
      break;
  }
}

Listing 5
Large documents

We mentioned earlier that the Publish pattern may not be very efficient when dealing with large documents, as producing a new version of the document requires copying it. The copying process can take significant time and may lead to high memory consumption.

Two techniques come to mind that we can apply to improve this:

Persistent data structures [Wikipedia-6]
Using aggregation instead of composition for document subparts and sharing the subparts between document versions.

In the first case, persistent data structures allow us to reuse the previous version of the document while adding new information to it (or removing information from it). For example, adding an element to the front of a list doesn't change any of the elements already existing. Thus, we can make the new list share data with the previous list. The act of copying the document is cheap, as the subparts of the document are not actually copied. Tree structures are also good examples of persistent data structures.

The second technique depends on the type of document, so let's describe it with an example. Let's say that the document is defined as

  using document_t =
    std::unordered_map<location_t, tile_data_t>

(we load a tile's worth of data for the positions around the player). Let's also assume that, once tile data is loaded for a location, it will never change. Copying tile_data_t objects might be expensive, so copying the entire document is expensive. However, if we change the document to be

  std::unordered_map<location_t,
    std::shared_ptr<const tile_data_t>>

then copying the document is cheap. We are not copying the tile data; we are just copying the map. Multiple document versions will share the same tile data subobjects.

Conclusions

The Publish pattern can be a valuable tool in one's toolkit. It can be used in many scenarios where we want to reduce contention between threads and have a producer-consumer type of problem.

The pattern works well when there are multiple consumers of the document. In its basic form, the pattern works with only one producer, but it can be easily extended to accommodate multiple producers.

The pattern is easy to implement and can be very efficient, depending on the problem. However, like any software solution, it has downsides; in this case, extra memory allocations and copying the document. Being aware of these downsides helps users tailor the pattern to the problem at hand.

I hope you find this pattern as useful as I did. Please let me know about your experience with it.

References

[Hylo] The Hylo Programming Language, https://www.hylo-lang.org/

[Sutter14] Herb Sutter, Lock-Free Programming (or, Juggling Razor Blades), Part II, CppCon 2014, https://youtu.be/CmxkPChOcvw

[Wikipedia-1] 'Producer–consumer problem': https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem, accessed August 2024.

[Wikipedia-2] 'Linearizability': https://en.wikipedia.org/wiki/Linearizability, accessed August 2024.

[Wikipedia-3] 'Multiple buffering': https://en.wikipedia.org/wiki/Multiple_buffering, accessed August 2024.

[Wikipedia-4] 'Read-copy-update': https://en.wikipedia.org/wiki/Read-copy-update, accessed August 2024.

[Wikipedia-5] 'Optimistic concurrency control': https://en.wikipedia.org/wiki/Optimistic_concurrency_control, accessed August 2024.

[Wikipedia-6] 'Persistent data structure': https://en.wikipedia.org/wiki/Persistent_data_structure, accessed August 2024.

Footnotes
When we talk about design patterns, we often emphasise their importance for design, while not giving enough credit to how we read and reason about the code. As we reason about the code more often than we design it, maybe we should shift the focus. Just a thought…
Every mutex is a bottleneck; by design, it prevents a thread that has resources from doing meaningful work.

Lucian Radu Teodorescu has a PhD in programming languages and is a Staff Engineer at Garmin. He likes challenges; and understanding the essence of things (if there is one) constitutes the biggest challenge of all.
