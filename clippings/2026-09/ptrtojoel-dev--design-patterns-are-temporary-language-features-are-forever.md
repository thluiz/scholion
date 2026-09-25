---
url: "https://ptrtojoel.dev/posts/design-patterns-are-temporary/?ref=dailydev"
captured_at: "2026-09-25T20:16:10+01:00"
title: "Design Patterns Are Temporary, Language Features Are Forever"
domain: "ptrtojoel-dev"
---

Design patterns are these cool things that make you go 'hell yeah' because they make a certain problem easier to deal with. Whether it's applicable to all languages, or due to a language constraint, they're pretty nice. Of course, some people go crazy with them rather than doing the simple thing that works. Other times, you'll naturally do a design pattern without even knowing about it.

Every once in a while, I like to go through design patterns that are 'commonly applicable' to Java as a thought experiment to see:

*   Have I seen this in a codebase before?
*   Does this look like something that would've helped me with before?
*   Is this a solution to a problem which doesn't exist?

and so on.

A few times I have come across patterns such as 'visitor' and never truly grasped what it was solving, or why I would use it. Young Joel was unsure, probably due to poor explanations, which I think can be a big problem when it comes to concepts today. In jiujitsu, it's extremely evident when a concept or a technique is practical and not bullshido (if you go to a gym which competes at least in my anecdotal experience). But for the visitor pattern, explanations to me have always been:

\>"here's how the pattern works"

\>just randomly logs stuff

Not exactly helpful presenting how to use 'x' with an unrealistic use case.

When my son was born, I had decided to learn Rust since I was sleepless most of the time and I wanted to keep myself sharp during parental leave.

Can you imagine how mind blown I was when I saw this??:

```
let number = 13;

   match number {
       1 => println!("One!"),
       2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
       13..=19 => println!("A teen"),
       _ => println!("catch leftovers")
   }
```

And that's how Young Joel discovered pattern matching (and further exploration into FP (OCaml btw)).

After some time, I went back to the visitor pattern out of curiosity again to see if I could try to understand it once more. Now knowing about pattern matching, this is how I came to realise that the visitor pattern was pattern matching in an OO way. Of course, it's not 1:1 (I think), but it gives a familiar feel. I wouldn't try to pretend I understand completely the key details/downfalls of visitors, but now I had a better idea on how to use them.

At work I write a mix of Java, JavaScript, and Rust. Majority of my time is Java, but I don't like staying on a particular version for long because that's a major L and one of the worst characteristics of Java culture today in enterprise land.

The release of Java 21 saw a lot of fantastic features, one of them being: [Pattern Matching for switch](https://openjdk.org/jeps/441).

With pattern matching in switches and sealed types, the visitor pattern to me looks like a thing of the past (which is good!). I think if a language can improve in such a way, then the language itself becomes more enjoyable to use. For example, you can do this!:

![alt text](https://ptrtojoel.dev/posts/design-patterns-are-temporary/java-21-pattern-match.png)

Here is the Rust version:

```
enum WebEvent {
    PageLoad,
    PageUnload,
    KeyPress(char),
    Paste(String),
    Click { x: i64, y: i64 },
}

fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),
        WebEvent::Paste(s) => println!("pasted \"{}\".", s),
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}.", x, y);
        },
    }
}
```

Sealed types, records, switch expressions, switch pattern matching.. the list goes on. I really love modern Java, and the feature delivery is quality. Compared to Java <17 it feels like an entirely different language.

Coming back to the visitor pattern, here is some sample code I wrote during my son's nap times to get a feel on the pattern.

*   We model a filesystem where there is a Node which is either a BlobNode or a TreeNode.
*   There are two use cases: adding or deleting a BlobNode (the visitor pattern really shines because of how you can implement this)

```
package visitor;

import java.util.ArrayList;
import java.util.List;

abstract class Node {
    public final String name;

    public Node(String name) {
        this.name = name;
    }

    abstract public void accept(NodeVisitor visitor);

}

class BlobNode extends Node {
    public BlobNode(String name) {
        super(name);
    }

    @Override
    public void accept(NodeVisitor visitor) {
        visitor.visit(this);
    }

}

class TreeNode extends Node {
    public List<Node> children;

    public TreeNode(String name, List<Node> children) {
        super(name);
        this.children = children;
    }

    @Override
    public void accept(NodeVisitor visitor) {
        visitor.visit(this);
        children.forEach((c) -> c.accept(visitor));
    }

}

interface NodeVisitor {
    void visit(BlobNode node);

    void visit(TreeNode node);
}

class BlobNodeVisitor implements NodeVisitor {

    @Override
    public void visit(BlobNode node) {
        System.out.println("BlobNode: " + node.name);
    }

    @Override
    public void visit(TreeNode node) {
    }
}

class TreeNodeVisitor implements NodeVisitor {

    @Override
    public void visit(BlobNode node) {
    }

    @Override
    public void visit(TreeNode node) {
        System.out.println("TreeNode: " + node.name);
    }
}

class NodeAddVisitor implements NodeVisitor {

    private final String name;
    private final String directory;

    public NodeAddVisitor(String directory, String filename) {
        this.name = filename;
        this.directory = directory;
    }

    @Override
    public void visit(BlobNode node) {
    }

    @Override
    public void visit(TreeNode node) {
        if (node.name.equals(directory)) {
            System.out.println("\nAdding new file to '" + directory + "': " + name);
            node.children.add(new BlobNode(name));

        }
    }
}

class NodeDeleteVisitor implements NodeVisitor {

    private final String name;

    public NodeDeleteVisitor(String filename) {
        this.name = filename;
    }

    @Override
    public void visit(BlobNode node) {
    }

    @Override
    public void visit(TreeNode node) {
        // NOOOOOOOOOOOOOOOOO TAKE YOUR FP OUT OF MY OOP
        // REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        node.children = node.children.stream()
                .filter(n -> !n.name.equals(name))
                .toList();

    }
}
```

Here's it in action:

![alt text](https://ptrtojoel.dev/posts/design-patterns-are-temporary/chad-warden-visitor.png)

Honestly it's pretty cool you can achieve this, but still, for me:

*   Lots of code indirection (more use cases or concrete implementations might be harder to comprehend)
*   Double dispatch
*   New use case requires more 'visit' implementations (visit kinda sucks as a term as well)

The only valid point I think is double dispatch, the rest are just opinions.

Here's the modern Java version:

```
package visitor;

import java.util.ArrayList;
import java.util.List;
import visitor.FileNode.BlobNode;
import visitor.FileNode.TreeNode;
import visitor.FileNodeAction.Add;
import visitor.FileNodeAction.Delete;

sealed interface FileNode {
    String name();
    record BlobNode(String name) implements FileNode {};
    record TreeNode(String name, List<FileNode> children) implements FileNode {};
}

sealed interface FileNodeAction {
    String directory();
    record Add(FileNode node, String directory) implements FileNodeAction {};
    record Delete(FileNode node, String directory) implements FileNodeAction {};
}

public class NewStuff {
    public NewStuff() {};

    private void modifyFileNodes(List<FileNode> nodes, FileNodeAction action) {
        nodes.forEach(n -> {
            if (n instanceof TreeNode tn) {
                if (action.directory().equals(tn.name())) {
                    switch (action) {
                        case FileNodeAction.Add a -> tn.children().add(a.node());
                        case FileNodeAction.Delete d -> tn.children().remove(d.node());
                    }
                } else {
                    modifyFileNodes(tn.children(), action);
                }
            }
        });
    }
    //...
}
```

This even fits entirely on my screen:

![alt text](https://ptrtojoel.dev/posts/design-patterns-are-temporary/chad-warden-modern.png)

In this example, it's a lot nicer to follow and shifts the idea on being explicitly 'OO' to being more on the data itself.

Here's a side by side:

![alt text](https://ptrtojoel.dev/posts/design-patterns-are-temporary/side-by-side.png)

Visitors feel like an esoteric pattern I think, but now I have more appreciation for them.

Hopefully I'll never have to work on old Java projects but I got something up my sleeve now if I must.
