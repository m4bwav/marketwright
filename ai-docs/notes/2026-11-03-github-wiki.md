# GitHub wiki: marketwright

Written 2026-11-03 for 0.1.1. Working copy: `Ai/marketwright.wiki` (branch master). The wiki repository was created by saving GitHub's default Home page in the browser, then pages were pushed.

Pages: Home, Getting-Started, Commands, The-Ethics-Line, Numbers-and-Sources, FAQ, Versions-and-Upgrading, Development, _Sidebar, _Footer.

Verification: every output block on Commands and Getting-Started was printed by `mkw.py` 0.1.1 on Windows, Python 3.14, on 2026-11-03 (inputs on the page). Not a registry package, so no published-package run; the release zip holds the same files. `wikiwright.py check` 0 errors, `live` 8 pages 0 failures, everwrite tells 0 strong.

Found while writing: the ethics scan missed "leave a review in exchange for a free key" (reward named after the review). Fixed in 0.1.1 (PR #2) with a test.

Update procedure for a release: rerun each command on Commands with the same inputs, paste the new output, bump the version on Getting-Started, Commands, Versions-and-Upgrading and _Footer, add a Versions row, then `wikiwright.py check` and `live`.
