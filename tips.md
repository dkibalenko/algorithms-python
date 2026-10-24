`CLAUDE.md` stays exactly as built — pure teaching instructions.

`PROGRESS.md `is a living document you update daily. Claude reads it at the start of each session to know your current position, what's done, what's shaky, and what's next. No manual context-setting needed.

---

**The `PROGRESS.md` Structure**

# SQL Study Progress

## Current Status
Day: 3 / 14
Date: 2025-05-23
Next session focus: One-to-One + Self-Referential JOINs

## Completed Days

### Day 1 — 1-to-Many JOINs ✅
Solid: LEFT JOIN, parent duplication concept, COUNT(*) vs COUNT(col)
Shaky: COALESCE on LEFT JOIN NULLs — keep revisiting
Hard problem: Needed a hint on "users with no orders show 0"
Index finding: orders.user_id index dropped cost 4x on EXPLAIN

### Day 2 — Many-to-Many ✅
Solid: Junction table pattern, two-JOIN traversal
Shaky: "Orders with BOTH tag A AND tag B" — got it after hint
       The double-filter pattern doesn't feel automatic yet
Hard problem: Solved independently ✅
ORM: prefetch_related clicked finally

## Recurring Weak Spots (update as they appear)
- COALESCE after LEFT JOIN — keep seeing NULLs where I expect 0
- HAVING with aliased columns — keep trying to use alias

## Problems That Need Retry (no-hint reattempt)
- Day 2 Medium: "Orders with BOTH tag 'urgent' AND 'vip'"
- Day 1 Hard: Full user stats with COALESCE

## Skipped / Adjusted
- None yet

---

**How Claude Uses It Each Session**

At the start of every Claude Code session just say:

> "Read PROGRESS.md and start Day 4."

Claude will:

- See exactly where you are
- Know your recurring weak spots
- Know which problems to retry first
- Pick up the day's topic without you re-explaining anything

---

**The One Rule for `PROGRESS.md`**

**Update it at the END of every session** — not the next morning.

While the session is fresh, write:
- □ What was solid
- □ What was shaky
- □ Which problems needed hints
- □ What surprised you

That honest log is what makes the next session precise.

A vague "Day 3 done ✅" tells Claude **nothing useful**.

This setup means your two-week plan lives as the **structure** in your head and the **daily reality** in `PROGRESS.md` — not as a static file Claude blindly follows.
