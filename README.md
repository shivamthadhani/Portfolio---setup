# AI Tools Portfolio Setup

A short writeup of the portfolio assignment from 100Hires: install Cursor IDE, add the Claude Code and Codex extensions, set up a public GitHub repo, and document the process.

## What I installed

- **Cursor IDE** (https://cursor.com) — AI-native code editor, free plan
- **Claude Code extension** for Cursor (by Anthropic)
- **Codex extension** for Cursor (by OpenAI)
- **Git for Windows** (https://git-scm.com) — needed for Cursor to interact with GitHub
- **GitHub account** + this public repo

## Steps I completed

1. Downloaded and installed Cursor IDE for Windows
2. Created a GitHub account and a public repository for this project
3. Opened the Extensions panel in Cursor and installed Claude Code
4. Went through the Claude Code login flow
5. Installed the Codex extension and went through its login flow
6. Installed Git for Windows so Cursor could connect to GitHub
7. Opened this repo in Cursor using GitHub's "Open with Cursor" link
8. Wrote this README documenting the process
9. Committed and pushed to GitHub

## Issues I ran into and how I solved them

**1. Claude Code wouldn't let me log in on the free tier.**

The extension presented three login options: Claude.ai Subscription (needs paid Pro or Max), Anthropic Console (pay-per-use API credits), and enterprise cloud providers (Bedrock, Foundry, Vertex). I don't have a paid Claude subscription, so I went with Anthropic Console.

I created an account at console.anthropic.com and tried to generate an API key. The Console required adding credits before I could finish setup. I had read online that new accounts in some regions get $5 in free credits with phone verification, but that promo didn't apply to my India account. The minimum top-up shown was $5. I completed the signup, generated a key, and completed the OAuth handshake with Cursor's extension. The extension now shows as authenticated. Prompting still fails with a "credit balance too low" error since my balance is $0, but the login state is real and the install is complete.

**2. Codex required similar paid access.**

Same pattern as Claude Code. I installed the extension, opened the login flow, documented the auth requirements, and got the extension into a logged-in state I could verify in Cursor.

**3. Cursor's "Clone Repo" button did nothing.**

After installing Git for Windows, I expected Cursor's built-in clone button to work, but clicking it had no effect. I tried restarting Cursor, no change. Worked around it by going to my repo on github.com and clicking the "Open with Cursor" option from the Code dropdown, which opened the cloned repo directly in Cursor without using the in-app clone button.

## Reflections

The hard part of this task wasn't the technical setup. Cursor, GitHub, and Git installers are all straightforward. The hard part was figuring out how to satisfy "log in" when every login path led to a paywall, deciding which trade-off to make (spend money vs document the obstacle vs find a workaround), and making the call that fits the spirit of the assignment.

I chose to actually complete the auth handshake on a free-tier Anthropic Console account so the login state is real, rather than skipping the step. The extensions are installed and logged in. They just won't run prompts until I add credits.

Total time: about 20 minutes including the back-and-forth on the auth flow and getting Git working with Cursor.