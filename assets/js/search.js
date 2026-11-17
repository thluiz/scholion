// Overrides themes/blowfish/assets/js/search.js.
// The theme loads the whole index.json (~19 MB, 16k entries) and runs Fuse.js on
// every keyup (~1 s per keystroke). This version keeps the theme's modal markup and
// keyboard behavior, but queries Pagefind, which downloads only the index chunks a
// query needs (tens of KB). The index is built by `pagefind --site public` in deploy.ps1.
var showButton = document.getElementById("search-button");
var showButtonMobile = document.getElementById("search-button-mobile");
var hideButton = document.getElementById("close-search-button");
var wrapper = document.getElementById("search-wrapper");
var modal = document.getElementById("search-modal");
var input = document.getElementById("search-query");
var output = document.getElementById("search-results");
var first = output.firstChild;
var last = output.lastChild;
var searchVisible = false;
var hasResults = false;

var pagefind = null;
var pagefindLoading = null;
var querySeq = 0;
var debounceTimer = null;
var MAX_RESULTS = 20;

var TYPE_LABELS = {
  nota: "Nota",
  pesquisa: "Pesquisa",
  local: "Local",
  podcast: "Podcast",
  quote: "Citação",
  comic: "Comic",
  etymology: "Etimologia",
  disciple: "Discípulo",
  movie: "Filme",
  walk: "Caminhada",
  webclip: "Webclip",
  tablature: "Tablatura",
  place: "Local",
};

// Listen for events
showButton ? showButton.addEventListener("click", displaySearch) : null;
showButtonMobile ? showButtonMobile.addEventListener("click", displaySearch) : null;
hideButton.addEventListener("click", hideSearch);
wrapper.addEventListener("click", hideSearch);
modal.addEventListener("click", function (event) {
  event.stopPropagation();
  event.stopImmediatePropagation();
  return false;
});
document.addEventListener("keydown", function (event) {
  // Forward slash to open search wrapper
  if (event.key == "/") {
    const active = document.activeElement;
    const tag = active.tagName;
    const isInputField = tag === "INPUT" || tag === "TEXTAREA" || active.isContentEditable;

    if (!searchVisible && !isInputField) {
      event.preventDefault();
      displaySearch();
    }
  }

  // Esc to close search wrapper
  if (event.key == "Escape") {
    hideSearch();
  }

  // Down arrow to move down results list
  if (event.key == "ArrowDown") {
    if (searchVisible && hasResults) {
      event.preventDefault();
      if (document.activeElement == input) {
        first.focus();
      } else if (document.activeElement == last) {
        last.focus();
      } else {
        document.activeElement.parentElement.nextSibling.firstElementChild.focus();
      }
    }
  }

  // Up arrow to move up results list
  if (event.key == "ArrowUp") {
    if (searchVisible && hasResults) {
      event.preventDefault();
      if (document.activeElement == input) {
        input.focus();
      } else if (document.activeElement == first) {
        input.focus();
      } else {
        document.activeElement.parentElement.previousSibling.firstElementChild.focus();
      }
    }
  }

  // Enter to get to results
  if (event.key == "Enter") {
    if (searchVisible && hasResults) {
      event.preventDefault();
      if (document.activeElement == input) {
        first.focus();
      } else {
        document.activeElement.click();
      }
    }
  }
});

// "input" instead of "keyup": arrows/Enter don't re-run the query, paste does.
input.addEventListener("input", function () {
  clearTimeout(debounceTimer);
  var term = this.value;
  debounceTimer = setTimeout(function () {
    executeQuery(term);
  }, 150);
});

function displaySearch() {
  loadPagefind();
  if (!searchVisible) {
    document.body.style.overflow = "hidden";
    wrapper.style.visibility = "visible";
    input.focus();
    searchVisible = true;
  }
}

function hideSearch() {
  if (searchVisible) {
    document.body.style.overflow = "visible";
    wrapper.style.visibility = "hidden";
    input.value = "";
    output.innerHTML = "";
    hasResults = false;
    querySeq++;
    document.activeElement.blur();
    searchVisible = false;
  }
}

function loadPagefind() {
  if (!pagefindLoading) {
    var baseURL = wrapper.getAttribute("data-url").replace(/\/?$/, "/");
    pagefindLoading = import(baseURL + "pagefind/pagefind.js").then(function (pf) {
      pagefind = pf;
      return pf.init().then(function () {
        return pf;
      });
    });
    pagefindLoading.catch(function (err) {
      console.error("[search] failed to load Pagefind", err);
      pagefindLoading = null;
    });
  }
  return pagefindLoading;
}

function escapeHTML(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderResult(data) {
  var tipo = data.filters && data.filters.tipo && data.filters.tipo[0];
  var label = TYPE_LABELS[tipo] || tipo || "";
  var meta = [label, data.meta.date].filter(Boolean).map(escapeHTML).join('<span class="px-2 text-primary-500">&middot;</span>');
  // data.excerpt is HTML produced by Pagefind: page text already escaped, matches wrapped in <mark>.
  return `<li class="mb-2">
          <a class="flex items-center px-3 py-2 rounded-md appearance-none bg-neutral-100 dark:bg-neutral-700 focus:bg-primary-100 hover:bg-primary-100 dark:hover:bg-primary-900 dark:focus:bg-primary-900 focus:outline-dotted focus:outline-transparent focus:outline-2"
          href="${escapeHTML(data.url)}" tabindex="0">
            <div class="grow">
              <div class="-mb-1 text-lg font-bold">${escapeHTML(data.meta.title)}</div>
              <div class="text-sm text-neutral-500 dark:text-neutral-400">${meta}</div>
              <div class="text-sm italic scholion-search-excerpt">${data.excerpt}</div>
            </div>
            <div class="ml-2 ltr:block rtl:hidden text-neutral-500">&rarr;</div>
            <div class="mr-2 ltr:hidden rtl:block text-neutral-500">&larr;</div>
          </a>
        </li>`;
}

function setResults(html, count) {
  output.innerHTML = html;
  hasResults = count > 0;
  if (hasResults) {
    first = output.firstChild.firstElementChild;
    last = output.lastChild.firstElementChild;
  }
}

function executeQuery(term) {
  var seq = ++querySeq;
  term = term.trim();
  if (!term) {
    setResults("", 0);
    return;
  }
  loadPagefind()
    .then(function (pf) {
      return pf.search(term);
    })
    .then(function (search) {
      if (seq !== querySeq || !search) return null;
      return Promise.all(
        search.results.slice(0, MAX_RESULTS).map(function (r) {
          return r.data();
        })
      );
    })
    .then(function (items) {
      if (seq !== querySeq || !items) return;
      // No whitespace between <li>s: arrow navigation walks nextSibling.
      setResults(items.map(renderResult).join(""), items.length);
    })
    .catch(function (err) {
      console.error("[search] query failed", err);
    });
}
