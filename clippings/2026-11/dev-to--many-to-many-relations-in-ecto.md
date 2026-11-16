---
url: "https://dev.to/ceyhunkerti/many-to-many-relations-in-ecto-33n4"
captured_at: "2026-11-16T01:16:24+00:00"
title: "Many to Many Relations in Ecto"
domain: "dev-to"
---

I believe this post will be helpful to the ones, searching for a many to many relationship implementation in phoenix/ecto.

I can't express enough my thoughts about elixir and surrounding ecosystem like [phoenix](https://www.phoenixframework.org/) and [ecto](https://hexdocs.pm/ecto/Ecto.html), all i can say is it's a great pleasure to learn and be the part of the community even as a beginner. I have additional info about the community and resources at the end of the post, so let's get straight to the point and try to implement a many-to-many relation.

Suppose we have the classical blog application and our model is like;

[![blog model](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu65na64qezrwov2zox8d.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu65na64qezrwov2zox8d.png)

Sure we have other columns like username, name etc.. in users or comment body in comments. I've skipped these additional attributes for the sake of simplicity.

Our migrations will look like this;  

```
# users

defmodule MyApp.Repo.Migrations.AddUsersTable do
  use Ecto.Migration

  def change do
    create table(:users) do
      add :name, :string
      add :username, :string, null: false
      add :password_hash, :string, null: false
      add :email, :string, null: false

      timestamps()
    end

    create unique_index(:users, [:username])
    create unique_index(:users, [:email])

  end
end
```

Enter fullscreen mode Exit fullscreen mode

```
# posts

defmodule MyApp.Repo.Migrations.CreatePosts do
  use Ecto.Migration

  def change do
    create table(:posts) do
      add :title, :string
      add :owner_id, references(:users, on_delete: :nothing), null: true

      timestamps()
    end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

```
# comments

defmodule MyApp.Repo.Migrations.CreateComments do
  use Ecto.Migration

  def change do
    create table(:comments) do
      add :body, :string
      add :post_id, references(:posts, on_delete: :delete_all)
      add :owner_id, references(:users, on_delete: :nothing), null: true

      timestamps()
    end

  end
end
```

Enter fullscreen mode Exit fullscreen mode

```
# comment_likes

defmodule MyApp.Repo.Migrations.AddCommnetLikeTable do
  use Ecto.Migration

  def change do
    create table(:comment_likes, primary_key: false) do
      add(:comment_id, references(:comments, on_delete: :delete_all), primary_key: true)
      add(:user_id, references(:users, on_delete: :delete_all), primary_key: true)

      timestamps()
    end

    create(
      unique_index(:comment_likes, [:comment_id, :user_id], name: :comment_id_user_id_unique_index)
    )
  end
end
```

Enter fullscreen mode Exit fullscreen mode

Now we add the schema definitions;  

```
# User.ex

 schema "users" do
    field :name, :string
    field :password, :string, virtual: true
    field :password_hash, :string
    field :username, :string
    field :email, :string
    many_to_many :liked_comments, Comment, join_through: CommentLike, on_replace: :delete

    timestamps()
  end
```

Enter fullscreen mode Exit fullscreen mode

```
# User.ex

 schema "users" do
    field :name, :string
    field :password, :string, virtual: true
    field :password_hash, :string
    field :username, :string
    field :email, :string
    many_to_many :liked_comments, Comment, join_through: CommentLike, on_replace: :delete

    timestamps()
  end
```

Enter fullscreen mode Exit fullscreen mode

```
# Comment.ex

  schema "comments" do
    field :body, :string
    belongs_to :post, Post, references: :id
    belongs_to :owner, User, references: :id
    many_to_many :liked_by, User, join_through: CommentLike, on_replace: :delete

    timestamps()
  end
```

Enter fullscreen mode Exit fullscreen mode

```
# Post.ex

  schema "posts" do
    field :title, :string
    belongs_to :owner, User, references: :id
    has_many :comments, Comment

    timestamps()
  end
```

Enter fullscreen mode Exit fullscreen mode

finally we must also have a schema for the relation itself, i have skipped this part while i was first implementing it, just because i thought it was auto done, and no need for it but this was a mistake and I've learned it is actually necessary. So lets create it like;  

```
# comment_like.ex

  @primary_key false
  schema "comment_likes" do
    belongs_to :user, User
    belongs_to :comment, Comment

    timestamps()
  end
```

Enter fullscreen mode Exit fullscreen mode

OK the model is set, and the rest is easy; I'll give a sample implementation for liking a comment and getting comment list along with the attribute, `is_liked` which is if the current user is liked the comment or not.

Liking a comment;  

```
# comment_controller.ex

def like(conn, %{"comment_id" => comment_id}) do
    case Context.like_comment(conn.assigns.current_user, comment_id) do
      {:ok, _} -> json conn, :ok
      {:error, _} -> json conn, :error
    end
  end
```

Enter fullscreen mode Exit fullscreen mode

```
# context.ex


  def like_comment(current_user, comment_id) do
    current_user
    |> Repo.preload(:liked_comments)
    |> Ecto.Changeset.change
    |> Ecto.Changeset.put_assoc(:liked_comments, [get_comment!(comment_id)])
    |> Repo.update()
  end
```

Enter fullscreen mode Exit fullscreen mode

Getting the list of comments for the post;  

```
# context.ex

 def get_commnets(current_user_id, post_id) do
    query = from p in Post,
      join: c in assoc(p, :comments),
      left_join: cl in CommentLike,
      on: c.id == cl.comment_id,
      left_join: u in User,
      on: cl.user_id == u.id and u.id == ^current_user_id,
      where: p.id == ^post_id,
      select: %{comment: c, is_liked: not is_nil(u.id)}

    Repo.all(query)
  end
```

Enter fullscreen mode Exit fullscreen mode

That's it.

I strongly suggest `iex`(elixir interactive shell) for trying, learning or debugging your ecto models. Just issue `iex -S mix` in your project folder and you are ready to go, you can interact with your application in console.

Lastly, elixir has a welcoming community. I've learned a lot from the posts and [discord channel](https://discord.gg/u62wMu).

Here are a few resources for learning elixir and phoenix.

*   [Elixir home page](https://elixir-lang.org/)
*   [Elixir school](https://elixirschool.com/en/)
*   [Elixir blog](https://elixirforum.com/t/elixir-blog-posts/150)
*   [Elixir repository](https://github.com/elixir-lang/elixir)
*   [Phoenix](https://www.phoenixframework.org/)
*   [Ecto docs](https://hexdocs.pm/ecto/Ecto.html)
*   [Elixir casts](https://elixircasts.io/)
*   [Discord channel](https://discord.gg/u62wMu)

Thanks for reading i hope it'll help.
