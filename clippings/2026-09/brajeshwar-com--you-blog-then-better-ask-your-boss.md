---
url: "https://brajeshwar.com/2003/you-blog-then-better-ask-your-boss/"
captured_at: "2026-09-24T20:23:16+01:00"
title: "You blog? then better ask your boss"
domain: "brajeshwar-com"
---

Wed, Oct 29, 2003

Open in

[](https://chatgpt.com/?q=Read%20https%3A%2F%2Fbrajeshwar.com%2F2003%2Fyou-blog-then-better-ask-your-boss.md%20%E2%80%94%20I%20have%20questions%20about%20this%20post%20%28%22You%20blog%3F%20then%20better%20ask%20your%20boss%22%29. "Open in OpenAI")[](https://claude.ai/new?q=Read%20https%3A%2F%2Fbrajeshwar.com%2F2003%2Fyou-blog-then-better-ask-your-boss.md%20%E2%80%94%20I%20have%20questions%20about%20this%20post%20%28%22You%20blog%3F%20then%20better%20ask%20your%20boss%22%29. "Open in Claude")[](https://brajeshwar.com/2003/you-blog-then-better-ask-your-boss.md "View as Markdown")

Do you blog? And are you employed? Be careful your boss may not like what you blog, this guy got fired ([read actual thread](https://www.michaelhanscom.com/eclecticism/2003/10/of_blogging_and.html)) because he [wrote something](https://www.michaelhanscom.com/eclecticism/2003/10/even_microsoft_.html) on his blog that his company do not like. Similarly, better be careful with your blog content and follow your web-host’s rules and regulation. I got a warning of “Abuse-Copyright Infringement” because of some of the comments on this blog. I had to spend half a day reading all comments and deleting many of them. Right now, I am following the Tip No. 6 of of the seven quick steps to spam-free blog.

For the archive sack, here is the Step No. 6.

**Reasoning** : One of the reasons that comment spam is such a pain is that it takes several clicks through MT’s interface to get rid of a single post. If you could kill a spam easily as soon as it appeared, their effectiveness would be reduced dramatically, with the hopeful aim of deterring spammers entirely.

**The fix** : This is another Perl insert, this time into the file lib/MT/App/Comments.pm (about line 150):

```
$Text::Wrap::cols = 72;
$body = Text::Wrap::wrap('', '', $body) . "\n$link_url\n\n" .
   $app->translate('IP Address:') . ' ' . $comment->ip . "\n" .
   $app->translate('Name:') . ' ' . $comment->author . "\n" .
   $app->translate('Email Address:') . ' ' . $comment->email . "\n" .
   $app->translate('URL:') . ' ' . $comment->url . "\n\n" .
   $app->translate('Comments:') . "\n\n" . $comment->text . "\n";
$body .= "\nTo delete this comment, click this link:\n".
   $app->{cfg}->CGIPath . "mt.cgi?__mode=delete_confirm&" .
   "_type=comment&id=".$comment->id ."&blog_id=" . $blog->id ."\n";
MT::Mail->send(\%head, $body);
```

It inserts a link into the mail that, when followed, jumps straight to the “Delete comment? \[Yes/No\]” page in MT (though, irritatingly, this page will close the browser window after you’ve hit the button, so you’ll want to ensure the page appears in a spare/new window when you click on the link).
