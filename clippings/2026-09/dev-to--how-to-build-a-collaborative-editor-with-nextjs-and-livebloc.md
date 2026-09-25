---
url: "https://dev.to/sachinchaurasiya/how-to-build-a-collaborative-editor-with-nextjs-and-liveblocks-389m?context=digest&ahoy_click=true&t=Gw7WG4OV11TDXZfKVc72nBTYWedUY7Ul&s=0PgIeu3PZ7umc4QQ0Ycnmq6aD9xWVQAnFw9tc_yMPWI&u=https%253A%252F%252Fdev.to%252Fsachinchaurasiya%252Fhow-to-build-a-collaborative-editor-with-nextjs-and-liveblocks-389m%253Fcontext%253Ddigest"
captured_at: "2026-09-25T00:54:01+01:00"
title: "How to Build a Collaborative Editor with Next.js and Liveblocks"
domain: "dev-to"
---

Collaborative applications are now essential in modern software, allowing multiple users to work on the same document, design, or codebase at the same time. Think of Google Docs, Figma, or multiplayer coding platforms these tools are powerful because they offer **real-time collaboration**, where every change is instantly visible to everyone.

In this guide, I'll show you how to build a collaborative text editor using **Next.js** and **Liveblocks**, a library that makes real-time collaboration easy. By the end, you'll have a working editor where multiple users can edit a document, see each other's changes in real-time, and track who is online and what they are doing.

## [](#what-to-expect-from-this-guide)**What to Expect from This Guide?**

### [](#part-1-understanding-collaborative-editors-and-the-role-of-liveblocks)**Part 1: Understanding Collaborative Editors and the Role of Liveblocks**

In the first part, we'll look at what collaborative editors are, how they work, and the technologies behind them. We'll focus on **WebSockets** for real-time updates and discuss how **Liveblocks** makes building these features easier.

### [](#part-2-building-the-collaborative-editor-stepbystep)**Part 2: Building the Collaborative Editor Step-by-Step**

In the second part, we'll start building the editor from scratch. We'll set up the project, integrate Liveblocks, and add features like real-time editing, user presence indicators, and managing document state. By the end, you'll have a live, shareable editor to show off.

Ready to get started? First, let's understand the basics of collaborative editors, the technology behind them, and why Liveblocks is perfect for building them.

## [](#what-is-a-collaborative-editor)What is a Collaborative Editor?

Imagine you're editing a document with a friend. You both see each other’s changes in real-time, making it feel like you're working on the same computer. That’s the magic of collaborative editors.

A collaborative editor is a software tool that lets multiple users work on the same document or file at the same time. Each user can make changes, and everyone sees these updates instantly. Examples include Google Docs, Notion, and Figma.

## [](#how-do-collaborative-editors-work)How Do Collaborative Editors Work?

Collaborative editors use **real-time communication** between users and a shared server. Here’s a simple overview of how it works

1.  When a user edits the document, the changes are sent to the server.
    
2.  The server processes these changes and sends them to all connected users.
    
3.  Everyone’s view updates instantly, showing the changes in real-time.
    

In scenarios where multiple users make changes simultaneously, the editor must effectively manage these updates to ensure consistency. This is where the technology that enables this real-time synchronization comes into play: **WebSockets**.

## [](#the-technology-behind-realtime-collaboration-websockets)The Technology Behind Real-Time Collaboration: WebSockets

Most traditional websites use HTTP requests to talk to servers. This works well for static pages but isn't quick enough for real-time apps like collaborative editors.

**WebSockets** fix this by allowing ongoing, two-way communication between the client and the server. Instead of sending separate requests for every update, a WebSocket connection stays **open**. This way, data can be sent and received instantly as changes occur.

Here's a simple explanation of how WebSocket communication works

[![websocket-flow](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmtx30i439ew5ieap7q5w.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmtx30i439ew5ieap7q5w.png)

1.  User 1 makes an edit.
    
2.  The server gets the edit and sends it to both User 1 and User 2.
    
3.  User 2 makes an edit, and the server sends it to both users again.
    

This way, everyone sees the same document version in real-time.

## [](#liveblocks-simplifying-realtime-collaboration)Liveblocks: Simplifying Real-Time Collaboration

Building a collaborative editor from scratch is possible, but handling real-time sync, conflict resolution, and user presence can be tricky. This is where **Liveblocks** helps.

**Liveblocks** is a powerful library that makes building collaborative apps easier. Instead of writing all the WebSocket and state management code yourself, you can use Liveblocks’ built-in features, such as

*   **Presence**: Track who is online and what they are doing.
    
*   **Storage**: Share and sync documents, drawings, or any content.
    
*   **Room Management**: Manage connections and permissions for multiple users.
    

Here’s why using Liveblocks can save you a lot of time:

1.  **Built-in Presence**: See who’s editing, where their cursors are, and what they’re typing all in real-time.
    
2.  **Conflict Handling**: Easily manage updates when multiple users make changes at the same time.
    
3.  **Simple Integration**: It works seamlessly with popular frontend frameworks like Next.js, making it easier to build and scale.
    

By using Liveblocks, you can focus on building the core features of your editor without worrying about low-level communication details.

## [](#project-setup)Project Setup

Let's start by creating a new Next.js project.  

```
npx create-next-app@latest collaborative-editor --typescript
```

Enter fullscreen mode Exit fullscreen mode

After creating the project install the Liveblocks dependencies  

```
npm install @liveblocks/client @liveblocks/node @liveblocks/react @liveblocks/yjs @tiptap/extension-collaboration @tiptap/extension-collaboration-cursor @tiptap/pm @tiptap/react @tiptap/starter-kit yjs
```

Enter fullscreen mode Exit fullscreen mode

Next, create a Liveblocks config to set up the types for the user information and to display the cursor in the editor.  

```
// liveblocks.config.ts

declare global {
  interface Liveblocks {
    Presence: { cursor: { x: number; y: number } | null };
    UserMeta: {
      id: string;
      info: {
        name: string;
        color: string;
        picture: string;
      };
    };
  }
}

export {};
```

Enter fullscreen mode Exit fullscreen mode

Go to [https://liveblocks.io/](https://liveblocks.io/) and sign up for a free account. After signing up, you'll be taken to the dashboard where you will see two projects created for you. Select the first project, go to the `API keys` section on the left panel, and get the secret key.

[![liveblocks-dashboard1](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsi0o7qs3a4v2b3t398ed.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsi0o7qs3a4v2b3t398ed.png)

[![liveblocks-dashboard2](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F53j9r80bmjjmrkwhp6oq.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F53j9r80bmjjmrkwhp6oq.png)

Create a `.env` file and add `LIVEBLOCKS_SECRET_KEY` environment variable and secret key you copied from the API keys dashboard.  

```
LIVEBLOCKS_SECRET_KEY=sk_dev_xxxxxxxxxx_xxxxxxx_xxx_xxxxx_x
```

Enter fullscreen mode Exit fullscreen mode

Alright, the project setup is done. In the next section, we will create components for our editor.

## [](#create-components-for-the-editor)Create components for the editor

Let's start by creating a toolbar component and adding the following code. We will use Tiptap to build the editor because it is one of my favorite tools for creating rich text and collaborative editors.  

```
// components/Toolbar.tsx

import { Editor } from "@tiptap/react";
import styles from "./Toolbar.module.css";

type Props = {
  editor: Editor | null;
};

export function Toolbar({ editor }: Props) {
  if (!editor) {
    return null;
  }

  return (
    <div className={styles.toolbar}>
      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleBold().run()}
        data-active={editor.isActive("bold") ? "is-active" : undefined}
        aria-label="bold"
      >
        <BoldIcon />
      </button>
      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleItalic().run()}
        data-active={editor.isActive("italic") ? "is-active" : undefined}
        aria-label="italic"
      >
        <ItalicIcon />
      </button>
      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleStrike().run()}
        data-active={editor.isActive("strike") ? "is-active" : undefined}
        aria-label="strikethrough"
      >
        <StrikethroughIcon />
      </button>

      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleBlockquote().run()}
        data-active={editor.isActive("blockquote") ? "is-active" : undefined}
        aria-label="strikethrough"
      >
        <BlockQuoteIcon />
      </button>

      <button
        className={styles.button}
        onClick={() => editor.chain().focus().setHorizontalRule().run()}
        data-active={undefined}
        aria-label="horizontal-line"
      >
        <HorizontalLineIcon />
      </button>

      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleBulletList().run()}
        data-active={editor.isActive("bulletList") ? "is-active" : undefined}
        aria-label="bullet-list"
      >
        <BulletListIcon />
      </button>

      <button
        className={styles.button}
        onClick={() => editor.chain().focus().toggleOrderedList().run()}
        data-active={editor.isActive("orderedList") ? "is-active" : undefined}
        aria-label="number-list"
      >
        <OrderedListIcon />
      </button>
    </div>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Here we are using the Tiptap editor and its formatting options like italic, bold, and lists.

Next, let's create an Avatars component to display all the online users in the room.  

```
// components/Avatars.tsx

import { useOthers, useSelf } from "@liveblocks/react/suspense";
import styles from "./Avatars.module.css";

export function Avatars() {
  const users = useOthers();
  const currentUser = useSelf();

  return (
    <div className={styles.avatars}>
      {users.map(({ connectionId, info }) => {
        return (
          <Avatar key={connectionId} picture={info.picture} name={info.name} />
        );
      })}

      {currentUser && (
        <div className="relative ml-8 first:ml-0">
          <Avatar
            picture={currentUser.info.picture}
            name={currentUser.info.name}
          />
        </div>
      )}
    </div>
  );
}

export function Avatar({ picture, name }: { picture: string; name: string }) {
  return (
    <div className={styles.avatar} data-tooltip={name}>
      <img
        src={picture}
        className={styles.avatar_picture}
        data-tooltip={name}
      />
    </div>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Here we are using two hooks:

*   `useOthers`: to get the list of other users connected to the same room I'm in.
    
*   `useSelf`: to get the info of my own user
    

Now let's create an `ErrorListener` component to catch any errors happening inside the Liveblocks provider. most important one is the `4001` when user is trying to connect the room which they don’t have access to.  

```
// components/ErrorListener.tsx

"use client";

import { useErrorListener } from "@liveblocks/react/suspense";

import React from "react";

import styles from "./ErrorListener.module.css";
import { Loading } from "./Loading";

const ErrorListener = () => {
  const [error, setError] = React.useState<string | undefined>();

  useErrorListener((error) => {
    switch (error.code) {
      case -1:
        setError("Could not connect to Liveblocks");

        break;

      case 4001:
        // Could not connect because you don't have access to this room
        setError("You don't have access to this room");

        break;

      default:
        setError("An unexpected error occurred");

        break;
    }
  });

  return error ? (
    <div className={styles.container}>
      <div className={styles.error}>{error}</div>
    </div>
  ) : (
    <Loading />
  );
};

export default ErrorListener;
```

Enter fullscreen mode Exit fullscreen mode

Thanks to Liveblocks for making things easier with the `useErrorListener` hook, which handles all the error-catching logic in our collaborative application.

Next is the `ConnectToRoom` component, which shows the initial UI where the user enters the room name they want to join. Then, it redirects to the room page using the entered name as the roomId.  

```
// components/ConnectToRoom.tsx

"use client";

import React from "react";
import styles from "./ConnectToRoom.module.css";

import { useRouter } from "next/navigation";

const ConnectToRoom = () => {
  const router = useRouter();

  const inputRef = React.useRef<HTMLInputElement>(null);

  const connectToRoom = async () => {
    const roomId = inputRef.current?.value;
    if (roomId && roomId.length > 0) {
      await (async () => router.push(`/room?roomId=${roomId}`))();
    }
  };

  return (
    <div className={styles.container}>
      <h1>Connect to a room</h1>
      <p>Connect to a room to start collaborating with others.</p>
      <input
        ref={inputRef}
        type="text"
        placeholder="Room ID"
        className={styles.input}
      />
      <button className={styles.button} onClick={connectToRoom}>
        Connect
      </button>
    </div>
  );
};

export default ConnectToRoom;
```

Enter fullscreen mode Exit fullscreen mode

Since we will get the roomId from the URL, let's create a custom hook.  

```
// hooks/useRoomId.ts

import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export const useRoomId = () => {
  const searchParams = useSearchParams();

  const [roomId, setRoomId] = useState<string | null>(
    searchParams.get("roomId")
  );

  useEffect(() => {
    setRoomId(searchParams.get("roomId"));
  }, [searchParams]);

  return roomId;
};
```

Enter fullscreen mode Exit fullscreen mode

Lastly, there's the Editor component, which works together with Tiptap and Liveblocks to create some of the magic.  

```
// components/Editor.tsx

"use client";

import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import Collaboration from "@tiptap/extension-collaboration";
import CollaborationCursor from "@tiptap/extension-collaboration-cursor";
import * as Y from "yjs";
import { LiveblocksYjsProvider } from "@liveblocks/yjs";
import { useRoom, useSelf } from "@liveblocks/react/suspense";
import { useEffect, useState } from "react";
import { Toolbar } from "./Toolbar";
import styles from "./Editor.module.css";
import { Avatars } from "@/components/Avatars";

export function Editor() {
  const room = useRoom();
  const [doc, setDoc] = useState<Y.Doc>();
  const [provider, setProvider] = useState<any>();

  useEffect(() => {
    const yDoc = new Y.Doc();
    const yProvider = new LiveblocksYjsProvider(room, yDoc);
    setDoc(yDoc);
    setProvider(yProvider);

    return () => {
      yDoc?.destroy();
      yProvider?.destroy();
    };
  }, [room]);

  if (!doc || !provider) {
    return null;
  }

  return <TiptapEditor doc={doc} provider={provider} />;
}

type EditorProps = {
  doc: Y.Doc;
  provider: any;
};

function TiptapEditor({ doc, provider }: EditorProps) {
  const userInfo = useSelf((me) => me.info);

  const editor = useEditor({
    editorProps: {
      attributes: {
        class: styles.editor,
      },
    },
    extensions: [
      StarterKit.configure({
        history: false,
      }),
      Collaboration.configure({
        document: doc,
      }),
      CollaborationCursor.configure({
        provider: provider,
        user: userInfo,
      }),
    ],
  });

  return (
    <div className={styles.container}>
      <div className={styles.editorHeader}>
        <Toolbar editor={editor} />
        <Avatars />
      </div>
      <EditorContent editor={editor} className={styles.editorContainer} />
    </div>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

[![liveblocks-with-tiptap-editor](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiam2dfn8kpuy4ovyj98a.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiam2dfn8kpuy4ovyj98a.png)

Liveblocks gives us a YJS provider that helps define and store the editor content. Plus, Tiptap supports collaboration extensions, making it easy to set up collaboration.

Great, our editor is ready, but for collaboration, we need to set up the Liveblocks provider and RoomProvider. This will allow users to authenticate themselves and create a session for the room they want to join.

In the next section, we will discuss rooms and how Liveblocks enable real-time collaboration.

## [](#set-up-liveblocks-provider-and-room-provider)Set Up Liveblocks Provider and Room Provider

Before writing the code let's first understand how Liveblocks work with the diagram.

[![liveblock-flow-diagram](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fispb9zr9urbpxnyuj2lw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fispb9zr9urbpxnyuj2lw.png)

*   When a user opens the app, it sends a request to find out which room they want to join. The room ID is obtained using the useRoomId hook.
    
*   After getting the roomId, the LiveblocksProvider is set up.
    
*   An authentication request is sent to `/api/liveblocks-auth` (we will set this up soon) with the roomId to check the user's access.
    
*   If the authentication is successful, the room setup starts. This includes creating a new collaborative document instance (Y.Doc) and setting up a provider (LiveblocksYjsProvider) to handle synchronization with the Liveblocks backend.
    
*   The LiveblocksYjsProvider opens a WebSocket connection with Liveblocks, joining the specified room.
    
*   The initial presence state (like cursor position and user activity) is shared with other participants in the room.
    
*   **User Presence**: When a user joins, their presence is updated and shared with everyone in the room.
    
*   **Cursor Tracking**: Their cursor position is tracked and shared instantly using the CollaborationCursor extension.
    
*   **Document Synchronization**: Any changes a user makes are sent to the Liveblocks server, which updates the shared document for all users.
    
*   If **User A** edits the document, these changes are sent to Liveblocks as updates.
    
*   Liveblocks sends these changes to all users, keeping the document in sync.
    
*   When **User B** joins, their cursor and presence are shared with everyone.
    
*   When a user leaves, the Y.Doc instance and provider are removed, and the WebSocket connection is closed.
    
*   This starts a cleanup process to remove the user’s presence and updates from the room.
    

I hope the explanation above helps you understand how Liveblocks works.

As mentioned, Liveblocks needs an endpoint to verify the user and start a session for the room they want to join. So, let's create an API endpoint called `liveblocks-auth`.  

```
// app/api/liveblocks-auth/route.ts

import { Liveblocks } from "@liveblocks/node";
import { NextRequest } from "next/server";

const liveblocks = new Liveblocks({
  secret: process.env.LIVEBLOCKS_SECRET_KEY!,
});

export async function POST(request: NextRequest) {
  const userId = Math.floor(Math.random() * 10) % USER_INFO.length;

  const roomId = request.nextUrl.searchParams.get("roomId");

  const session = liveblocks.prepareSession(`session-${userId}`, {
    userInfo: USER_INFO[userId],
  });

  session.allow(roomId!, session.FULL_ACCESS);

  const { body, status } = await session.authorize();
  return new Response(body, { status });
}

const USER_INFO = [
  {
    name: "Sachin Chaurasiya",
    color: "#D583F0",
    picture: "https://github.com/Sachin-chaurasiya.png",
  },
  {
    name: "Mislav Abha",
    color: "#F08385",
    picture: "https://liveblocks.io/avatars/avatar-2.png",
  },
  {
    name: "Tatum Paolo",
    color: "#F0D885",
    picture: "https://liveblocks.io/avatars/avatar-3.png",
  },
  {
    name: "Anjali Wanda",
    color: "#85EED6",
    picture: "https://liveblocks.io/avatars/avatar-4.png",
  },
  {
    name: "Jody Hekla",
    color: "#85BBF0",
    picture: "https://liveblocks.io/avatars/avatar-5.png",
  },
  {
    name: "Emil Joyce",
    color: "#8594F0",
    picture: "https://liveblocks.io/avatars/avatar-6.png",
  },
  {
    name: "Jory Quispe",
    color: "#85DBF0",
    picture: "https://liveblocks.io/avatars/avatar-7.png",
  },
  {
    name: "Quinn Elton",
    color: "#87EE85",
    picture: "https://liveblocks.io/avatars/avatar-8.png",
  },
];
```

Enter fullscreen mode Exit fullscreen mode

Here, we are using fake user data, but in a real product, you would get the user data from the database and then create the session.

This line lets the user access the room with full permissions, which are `room:read` and `room:write`. This is just for demo purposes, but in real situations, access will depend on the user's role.  

```
session.allow(roomId!, session.FULL_ACCESS);
```

Enter fullscreen mode Exit fullscreen mode

Next, Let's create a `Provider` component and use it in the `RootLayout`.  

```
// app/Providers.tsx

"use client";

import { useRoomId } from "@/hooks/useRoomId";
import { LiveblocksProvider } from "@liveblocks/react";
import { type PropsWithChildren } from "react";

export function Providers({ children }: PropsWithChildren) {
  const roomId = useRoomId();

  return (
    <LiveblocksProvider
      key={roomId}
      authEndpoint={`/api/liveblocks-auth?roomId=${roomId}`}
    >
      {children}
    </LiveblocksProvider>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Update the root layout and wrap the children with the providers.  

```
// app/layout.tsx
import { Providers } from "./Providers";
...

return (
    ...
    <body>
      <Providers>{children}</Providers>
    </body>
    ...
)
```

Enter fullscreen mode Exit fullscreen mode

Alright, the providers are set up. Now, let's create a Room component using `RoomProvider`.  

```
// app/Room.tsx

"use client";

import { ReactNode } from "react";
import { RoomProvider } from "@liveblocks/react/suspense";
import { ClientSideSuspense } from "@liveblocks/react";
import ErrorListener from "@/components/ErrorListener";
import { useRoomId } from "@/hooks/useRoomId";

export function Room({ children }: { children: ReactNode }) {
  const roomId = useRoomId();

  return (
    <RoomProvider
      id={roomId ?? ""}
      initialPresence={{
        cursor: null,
      }}
      key={roomId}
    >
      <ClientSideSuspense fallback={<ErrorListener />}>
        {children}
      </ClientSideSuspense>
    </RoomProvider>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Here, `RoomProvider` uses two props: `roomId` and `initialPresence` for the user's cursor, which is just the x, y position of the cursor.

We use `ClientSideSuspense` with the `ErrorListener` component as a fallback. If there's an error, it will show the error; otherwise, it will display a loader, meaning the providers are still loading.

Next, create the Room page and add the following code. It's straightforward: use the Room component to wrap the Editor so that the editor gets all the connections in that specific room.  

```
// app/room/page.tsx
"use client";

import { Room } from "@/app/Room";
import { Editor } from "@/components/Editor";

export default function RoomPage() {
  return (
    <main>
      <Room>
        <Editor />
      </Room>
    </main>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Finally, update the Home page, which is `app/page.tsx`.  

```
import ConnectToRoom from "@/components/ConnectToRoom";

export default function Home() {
  return (
    <main>
      <ConnectToRoom />
    </main>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Alright, Liveblocks providers are set up correctly. Now, let's move on to the most exciting part: testing our collaborative editor. Are you excited? I am too! Let's test it in the next section.

## [](#testing)Testing

Start the dev server by running the following command  

```
npm run dev
```

Enter fullscreen mode Exit fullscreen mode

The server will start on localhost:3000, and you will see the "Connect to Room" interface.

[![connect-to-room-page](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwx0qzveyjtt7pzra67ki.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwx0qzveyjtt7pzra67ki.png)

Enter the room ID, and you will be taken to the room page where you can work with other users in real time.

Here is an example of two users connecting to the same room, `local-room`.

![demo-gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdianrjif9d74qrxaa40o.gif)

Great job, and congratulations on building the editor with real-time collaboration.

Thanks for reading to the end. If you don't want to miss interesting topics and project-building content, subscribe to the [Dev Buddy newsletter](https://devbuddyweekly.substack.com/).

## [](#conclusion)Conclusion

In this guide, we explore the power of collaborative applications, focusing on building a real-time collaborative text editor using Next.js and Liveblocks.

We break down the process into understanding the role of collaborative editors and setting up a project with features like real-time editing, user presence tracking, and document state management.

## [](#resources)Resources

*   [GitHub Repo](https://github.com/Sachin-chaurasiya/collaborative-editor)
    
*   Thanks to Liveblocks for creating different examples [here](https://github.com/liveblocks/liveblocks/tree/main/examples)
