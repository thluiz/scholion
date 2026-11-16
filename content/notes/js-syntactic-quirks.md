---
title: "JS syntactic quirks"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The page catalogs JavaScript syntax quirks that complicate parsing, from ambiguous grammar and ASI to conditional keywords, strict mode, slashes, lazy compilation, and cover grammars.'
tags: ["javascript", "parsing", "syntax", "ecmascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "jsparagus/js-quirks.md at master · mozilla-spidermonkey/jsparagus"
    url: "https://github.com/mozilla-spidermonkey/jsparagus/blob/master/js-quirks.md"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--js-syntactic-quirks.md"
    kind: repo
---

JavaScript is hard to parse because its grammar mixes formal rules with prose, contextual keywords, line-break sensitivity, and special cases that affect both lexing and parsing. The page walks through the main trouble spots for an implementation built from scratch.

## Reading notes

- Dangling else is resolved by attaching each else to the nearest unmatched if, and recursive descent parsers can implement that directly.
- The lexical grammar uses longest-match scanning, but several productions also need lookahead restrictions to enforce maximum munch inside the grammar.
- Annex B adds ambiguities for regular expressions and legacy octal escapes, and implementations must switch behavior based on context and strict mode.
- Unicode identifiers have exceptions such as $, _, zero-width joiner and non-joiner, and FEFF counts as whitespace.
- Legacy octal literals and escape sequences behave differently in non-strict code, with digits 8 and 9 changing how a leading-zero number is interpreted.
- Strict mode changes parsing and semantics, including reserved words, binding names, duplicate parameters, delete on identifiers, and with statements.
- Many keywords are conditional, especially yield, await, let, static, async, of, get, set, target, and the strict-mode-only reserved words.
- Escape sequences can appear in identifiers and property names, but not in keywords when they are acting as keywords.
- Early errors enforce many context-sensitive rules, including name restrictions, template-string validity, super call placement, and several parser shortcuts.
- Some nonterminals carry boolean parameters that a parser generator must track at run time.
- ASI inserts semicolons in limited situations, depends on whitespace, and interacts with restricted productions and slash ambiguity.
- Restricted productions cover cases like return, throw, yield, and postfix ++ or -- where line breaks change parsing.
- Slash can start either a division operator or a regular expression literal, so the lexer needs parser context to choose correctly.
- Lazy compilation forces parsers to track scope while skimming function bodies, including tricky arrow-function and Annex B function-scoping cases.
- Cover grammars let the spec accept ambiguous-looking syntax first and reject invalid interpretations later with early errors.
- The concluding lesson is that writing a JavaScript parser is full of awkward special cases.
