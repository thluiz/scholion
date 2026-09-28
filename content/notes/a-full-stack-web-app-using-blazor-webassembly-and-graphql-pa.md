---
title: "A Full-Stack Web App Using Blazor WebAssembly and GraphQL: Part 3"
date: '2022-06-08T20:55:07-03:00'
category: webclip
summary: 'This part adds edit and delete support for movies, server-side sorting and filtering, and client components for movie details, cards, genres, home page, and admin management.'
tags: ["blazor-webassembly", "graphql", "movie-management", "syncfusion"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Full-Stack Web App Using Blazor WebAssembly and GraphQL: Part 3"
    url: "https://www.syncfusion.com/blogs/post/a-full-stack-web-app-using-blazor-webassembly-and-graphql-part-3.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/syncfusion-com--a-full-stack-web-app-using-blazor-webassembly-and-graphql-pa.md"
    kind: repo
---

This part extends the movie app with edit and delete operations, plus sorting and filtering on the server and client. It also adds a movie details page, reusable rating, card, and genre components, a home page with sorting and genre filtering, and an admin panel for managing movies.

## Reading notes

- `IMovie` gains `GetAllMovies`, `UpdateMovie`, and `DeleteMovie` methods.
- `MovieDataAccessLayer` implements `GetAllMovies` with `AsNoTracking`, updates an existing movie by `MovieId`, and returns the poster path when deleting.
- `MovieQueryResolver` adds `GetMovieList` with `[UseSorting]` and `[UseFiltering]`.
- `EditMovie` checks whether `PosterPath` is a base64 string, saves a new poster file when needed, and then updates the movie.
- `DeleteMovie` removes the movie and deletes its poster file unless it is the default poster.
- `Program.cs` registers GraphQL filtering and sorting.
- The client adds GraphQL queries and mutations for fetching, filtering, sorting, editing, and deleting movies.
- The app is configured to use Bootstrap and Font Awesome, and later adds Syncfusion Toast support.
- `MovieRating` is a reusable component that displays the rating with custom styling.
- `MovieDetails` loads a movie by `MovieID`, shows the poster, title, overview, language, genre, rating, and formats duration as hours and minutes.
- `MovieCard` shows poster, title, genre, and rating, and links to the details page.
- `MovieGenre` loads genres and navigates to `/category/{genreName}` for filtering.
- `Home` supports `/` and `/category/{GenreName}`, loads sorted movies by default, filters by genre, and sorts by title, rating, or duration.
- `AddEditMovie` loads movie data when `MovieID` is set and uses edit or add mutations depending on whether the movie already exists.
- `ManageMovies` lists movies in an admin table, opens a delete confirmation modal, and shows a toast after deletion.
- The navigation bar is updated to link to the admin panel instead of the add movie link.
- The article ends by noting that the next part will cover authentication, authorization, login, registration, and client-side state management.
