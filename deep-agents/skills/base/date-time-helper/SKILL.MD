---
name: date-time-helper
description: Get current date/time and calculate relative dates for accurate time-based responses
license: MIT
allowed-tools: get_current_datetime
---

# Date & Time Helper Skill

## When to Use
- User asks about "today", "tomorrow", "next week", etc.
- You need to include current date in reports or research
- You must calculate deadlines, durations, or historical dates
- Any time-sensitive query requires precise date handling

## How It Works
1. Call `get_current_datetime()` to get ISO-formatted current datetime
2. Use Python's `datetime` module logic for calculations (described below)
3. Format dates as "Mon Jan 25, 2026" for user-facing responses

## Date Calculation Logic
- "Tomorrow" = today + 1 day
- "Next Monday" = next Monday after today
- "3 days ago" = today - 3 days
- Always use UTC to avoid timezone confusion

## Example Usage
User: "What's the date tomorrow?"
→ Call `get_current_datetime()`
→ Calculate tomorrow = today + timedelta(days=1)
→ Respond: "Tomorrow is Tue Jan 26, 2026"