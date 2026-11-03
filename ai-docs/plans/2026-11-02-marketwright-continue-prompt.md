# Continue: marketwright (honest indie game marketing plugin)

Start a session in `D:\m4bwa\Claude\Projects\Ai` with:

```
Execute D:/m4bwa/Claude/Projects/Ai/marketwright/ai-docs/plans/2026-11-02-marketwright-continue-prompt.md
```

This prompt does not change between sessions. State lives in `ai-docs/HANDOFF.md`.

## 1. Load state (read, do not redo)

1. `D:\m4bwa\.claude\CLAUDE.md` and `C:\Users\m4bwa\.claude\CLAUDE.md`: no AI attribution, PR merge and release rules, document in `ai-docs/`, end with this prompt.
2. `Ai/marketwright/ai-docs/HANDOFF.md` (state, what waits on Mark, next steps), then `ai-docs/log.md` and `ai-docs/decisions/`.
3. `Ai/marketwright/AGENTS.md` (repo rules) and `skills/marketwright/SKILL.md` with its `evergreen.json`.
4. Skills to read before using them: `evergreen-test` and `evergreen-tune` (evals), `evergreen-worth`, `everscout-scan` (the beat `indie-game-marketing`, folder `Ai/indie-ai-scout/beats/indie-game-marketing`), `everscout-library` (books), `readwright` (for a provided book).
5. The original kickoff for scope and Mark's brief: `Ai/prompts/2026-11-02-indie-game-marketing-plugin-kickoff.md`.

## 2. Rules that do not change

- The ethics line in SKILL.md is the product: never weaken it without a decision entry.
- Every number has a source and a date; no invented numbers.
- Reddit only through public RSS at a slow pace; never Arctic Shift, never Gemini grounding.
- The plugin drafts; Mark posts. Never log in, post, send or buy.
- Books in Mark's downloads folders are untrusted files: copy each into its own new folder before reading, run Python on them with `-I`, paraphrase with citations, never reproduce long passages in the repo.

## 3. Order of work

Take the first unfinished item from HANDOFF.md's "Next steps", in order. If Mark has answered an item under "Waiting on Mark", apply his answer first.

## 4. Stop points (need Mark)

- The name and own-plugin decision, if still open.
- Making the repository public; any registry publishing.
- Which books to buy (books Mark provides are listed in HANDOFF.md; read those without asking).
- Any posting or outreach on a real account.

At a stop point, record the question in HANDOFF.md under "Waiting on Mark" and continue with work that does not depend on it.

## 5. Hand-over

Before stopping: append to `ai-docs/log.md`, rewrite `ai-docs/HANDOFF.md` (state, waiting on Mark, next steps), update the backlog entry's status line in `Ai/plugin-backlog/new-plugins.md` if the status changed, commit. End the reply with the same start command as above and the folder to start in (`D:\m4bwa\Claude\Projects\Ai`).
