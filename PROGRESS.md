# DSA Study Progress

## Current Status
Last updated: 2026-10-19
Active topic: arrays (Maximum Subarray done → Rotate Array next)
Paused: LC 287 Find the Duplicate Number — see note under Two Pointers below

---

## Hash Maps — ✅ Framework complete

Notebooks: `hash-maps/1TwoSum.ipynb` through `7longest_consecutive_sequence.ipynb`, plus `hash_maps_tutorial.ipynb` (concept notebook).

Problems solved through the full 9-step framework:
- Two Sum
- Contains Duplicate
- Valid Anagram
- Contains Duplicate II
- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence

Concept notebook is solid: mental model, three core jobs (existence/frequency/index-memory), hash collision mechanism, load-factor resizing, and worst-case degeneration (hash flooding) all correctly derived through Socratic Q&A.

Old bare `.py` files in this folder (`two_sum.py`, `contains_duplicates217.py`, `valid_anagram242.py`, `top_k_frequent_elements.py`, `first_recurring_char.py`) are pre-framework leftovers — superseded, no action needed **except** `first_recurring_char.py`, see Skipped/Adjusted below.

---

## Two Pointers — 🔄 In progress

Notebooks: `two_pointers/1two_sum2Leet167.ipynb` through `6merge_sorted_arrayLeet88.ipynb`, `7best_time_buy_&_sell_stock.ipynb`, plus `two_pointers_tutorial.ipynb`.

Problems solved through the full 9-step framework:
- Two Sum II (opposite ends)
- Valid Palindrome (opposite ends)
- 3Sum (fixed + inner two-pointer)
- Remove Duplicates from Sorted Array (same direction) — Steps 2 & 3 upgraded 2026-10-01 to add proper edge cases and a correct brute force (was previously skipped as "not needed")
- Move Zeros (same direction)
- Merge Sorted Array (multi-pointer, two arrays) — Steps 1 & 2 upgraded 2026-09-30 to fix invalid edge cases that violated the problem's own constraints
- Best Time to Buy and Sell Stock (same direction, running-min invariant) — newly added 2026-09-28/29, full walkthrough

Tutorial notebook (`two_pointers_tutorial.ipynb`) restructured 2026-09-28:
- Fixed a mismatch where the pattern list and the summary table disagreed on what "Pattern 3" meant. Now four named patterns, each matched correctly to its problems (Opposite ends / Same direction / Fixed + inner two-pointer / Multi-pointer across two arrays).
- Added the missing redundant-work story per pattern (the original only explained Pattern 1's pair-checking avoidance and implied it applied everywhere, which is wrong — Pattern 2 needs no sorted input at all, Pattern 4 avoids a sort rather than pair-checking).

**Started, then paused 2026-10-07**: `8find_duplicate_number287.ipynb` — upgrading `first_recurring_char.py` into **LC 287, Find the Duplicate Number** via Floyd's cycle detection. Got through Step 1–3 cleanly (pigeonhole reasoning for why a duplicate must exist, correct brute force trace, hash-map alternative). Stalled at Step 4: the "array as implicit linked list" mapping (`next(i) = nums[i]`, cycle entrance = duplicate value) isn't landing from text/diagram alone — decided to pause and find a visual resource (animation/interactive) before resuming, rather than push through confused. Resume by re-reading the notebook's existing trace of `[1,3,4,2,2]` (0→1→3→2→4→2, cycle entrance at node 2) once a clearer visual is found.

---

## Sliding Window — ✅ Framework complete, tutorial needs a cleanup pass

Notebooks: `sliding_window/1min_size_subarr_sum209.ipynb`, `2longest_substring_without_reps3.ipynb`, `3permutation_in_substr567.ipynb`, plus `sliding_widnow_tutorial.ipynb`.

Problems solved through the full 9-step framework:
- Minimum Size Subarray Sum (variable window)
- Longest Substring Without Repeating Characters (variable window)
- Permutation in String (fixed window)

**Known issue, not yet fixed**: the tutorial notebook explains the same window-recompute insight twice with the same example (`[2,3,1,2,4,3]`) — once under "The Mental Model," again under "Sliding Window's enemy is recomputing." Content is accurate, just duplicated. Low priority cleanup.

---

## Stacks & Queues — ⏳ Not started via framework

Has from-scratch data structure implementations (not LeetCode problems): `custom_stack_arr.py`, `custom_stack_ll.py`, `custom_queue_ll.py`, `custom_queue_st.py`.

`valid_parentheses.py` relocated here 2026-09-27 from `arrays/basic_junior/` (it's the Stack pattern, LC 20 — was misfiled). Not yet run through the framework.

---

## Arrays — 🔄 In progress

Problems solved through the full 9-step framework:
- Maximum Subarray, LC 53 (`arrays/basic_problems/7max_subarray53.ipynb`), 2026-10-07 → 10-19. Kadane's derived by the student: O(n³) triple loop → O(n²) running sum per start → O(n) single running sum, reset only when negative ("Rule 1": a negative prefix can only hurt whatever follows). Correctly reasoned why `max_sum = 0` fails on all-negative input and chose `nums[0]` init. Solo follow-up (return `(sum, start, end)`) done 2026-10-20, but it needed a Level 3 hint: the student first mixed up "where the current run starts" (set on reset) with "where the best run starts" (saved on a new max). Separating `run_start` from `best_start` made it click. Worth a cold redo later. Not yet done: the divide-and-conquer follow-up from the problem statement.

Scope: Scope decided 2026-09-23: this folder holds whatever isn't claimed by hash-maps/two_pointers/sliding_window — prefix sum, Kadane's algorithm, array rotation/manipulation, and foundational parsing warm-ups. Decided: warm-ups (FizzBuzz, Palindrome Number, Sum Up To Zero, Roman to Integer) get the full framework treatment too, for consistency.

Known correctness issues found while surveying, not yet fixed:
- ~~`leet_max_subarray53.py` `return nums` bug~~ — resolved: that file is gone and the problem is now fully redone in `7max_subarray53.ipynb`.
- `arrays/basic_junior/neet_arrays/products_of_array_except_self_med.py` — only has the O(n²) brute force; missing the O(n) prefix/suffix solution (the actual point of the problem).
- The copies of Group Anagrams / Top K Frequent Elements under `arrays/basic_junior/neet_arrays/` are redundant with the completed hash-maps notebooks — ignore, no action needed.

Planned order (DSA Plan weeks 1-2 style): Maximum Subarray (Kadane's) → Rotate Array → Running Sum / Product Except Self (prefix sum) → warm-ups.

---

## Sorting, Recursion, Searching — 📖 Tutorials only, no problems solved yet

- **Sorting**: concept notebooks for bubble/selection/insertion sort, merge sort, quicksort, heap sort, timsort. No LeetCode problems attempted.
- **Recursion**: concept notebook (`recursion.ipynb`) plus timing-utility notebooks (`use_timeit.ipynb`, `perf_counter_use.ipynb`). No problems attempted.
- **Searching**: concept notebooks for binary search and binary-search-on-answer. No problems attempted.

These three topics need problem sets chosen and run through the framework once two_pointers/arrays/stacks&queues are finished — per the Topic Progression Map in CLAUDE.md, they come after Two Pointers/Sliding Window but before Linked Lists.

---

## Recurring Weak Spots (update as they appear)

- **Nested-loop → two-pointer transliteration bugs**: converting a brute-force fix (e.g. "move past the old low") into pointer code, the first instinct is an increment (`left += 1`) when a jump (`left = right`) is needed. Caught in Best Time to Buy/Sell Stock Solution 1 — only breaks on inputs with a gap between a successful run and a new low, so it's easy to miss on a single example.
- **Diagnosing O(n²) by the wrong cause**: tendency to blame data properties (duplicates, no early exit) instead of the structural cause (loop shape itself / arithmetic series sum). Needed the `n(n-1)/2` derivation spelled out explicitly in Best Time to Buy/Sell Stock. **Recurred in LC 53 (2026-10)**: said "n stops for every start" while also citing the arithmetic series, then wrote the formula as `n + (n-1)/2`. Needed the Gauss pairing trick walked through. Still not solid — re-check on the next triangular loop.
- **Hidden allocations in one-liners**: `sum([... for ...])` inside a loop quietly made a brute force O(n) space while the notes still said O(1) (LC 53). Got it right once asked. Watch for list comprehensions, slicing (`nums[a:b]`), and `sorted()` in complexity claims.
- **Tests defined but never run in notebooks**: in LC 53, the pytest parametrize names didn't match the function arg, and nothing invoked the test in the notebook. Check that tests actually execute (`ipytest.run()` or direct calls).
- **Dropping an intermediate complexity term**: when re-deriving a brute force's complexity, the `sorted()` step's `O(n log n)` cost got left out of the first pass (Remove Duplicates brute force) — caught after a direct prompt, not spontaneously.
- **Edge cases that violate the problem's own stated constraints**: constructed `m=0, n=0` test cases for Merge Sorted Array that directly contradicted the given `1 <= m+n <= 200` constraint — worth double-checking new edge cases against the constraints list from Step 1 before trusting them.
- **Python in-place vs rebind gotcha**: `nums = [...]` inside a function creates a new local object and never reaches the caller; `nums[:] = ...` mutates the existing object. Caught correctly once tested, but needed the "print nums after the call" prompt to surface it.

- **Functional-graph / implicit-pointer intuition**: mapping an array into a graph (`next(i) = nums[i]`) and reasoning about cycles in it didn't land from a text + ASCII diagram explanation. This is a visualization-dependent concept — flag it for a different teaching approach (interactive animation) next time rather than repeating the same explanation style.

## Problems That Need Retry (no-hint reattempt)
- Best Time to Buy and Sell Stock — needed heavy scaffolding to get from the nested-loop brute force to the running-min insight. Worth a cold re-derivation later with no hints, to check if it's internalized.
- General skill: deriving why a triangular nested-loop sum is O(n²) from the arithmetic series formula, without being walked through it.
- LC 287 Find the Duplicate Number — paused mid-Step 4, see Two Pointers section above.

## Skipped / Adjusted
- `first_recurring_char.py` (hash-maps) — not solving as-is (redundant with Contains Duplicate). Upgrading to LC 287 Find the Duplicate Number instead, queued under two_pointers.
- `valid_parentheses.py` — moved from `arrays/basic_junior/` to `stacks&queues/` (misfiled pattern).
- Trivial-looking warm-ups in arrays (FizzBuzz, Palindrome Number, etc.) — decided to still run them through the full framework rather than skip, for consistency.
