### What a "Session" Actually Is in Claude Code
A session = one continuous conversation context window.
```
It starts: when you open a new conversation in Claude Code
It ends:   when that conversation's context is cleared
           OR when you explicitly start a new conversation
```
### The Practical Reality in VS Code
```
Opening/closing the Claude Code TAB (sidebar panel)
  → Does NOT end the session
  → Context is preserved
  → Claude remembers everything from that conversation

Closing VS Code entirely
  → Depends on Claude Code's persistence settings
  → The conversation MAY still be there when you reopen
  → But treating it as a fresh session is safer

Starting a NEW conversation explicitly
  → This definitively ends the old session
  → Claude starts with zero context from before
  → Only CLAUDE.md and PROGRESS.md carry over automatically
```

### The Key Insight — Files Beat Memory
```
Don't rely on Claude remembering across sessions.
Rely on your files instead.

CLAUDE.md     → Claude reads this automatically every session
PROGRESS.md   → You reference it at session start manually

This means it doesn't matter whether the session
"technically" continued or reset.

The conversation that starts with:
  "Read PROGRESS.md and start Day 4"

...gives Claude identical context whether it's the
same session from yesterday or a brand new one.
```

### The Recommended Habit
```
END of each study session:
  1. Update PROGRESS.md (what was solid, shaky, needs retry)
  2. Close the conversation or just stop — doesn't matter which

START of next study session:
  1. Open Claude Code in VS Code
  2. Start a fresh conversation (safer than trusting continuity)
  3. First message: "Read PROGRESS.md and start Day 4"

That's it. The files are your session memory — not the tab.
```
> One fresh conversation per day is the cleanest pattern. Yesterday's long debugging tangent won't pollute today's focused teaching session.
