# AI Tools Portfolio Setup

Documentation of the 100Hires portfolio assignment: install Cursor IDE, add the Claude Code and Codex extensions, set up a public GitHub repo, and write up the process.

![Cursor with Claude Code and Codex extensions installed](cursor-extensions.png)

## What I installed

- **Cursor IDE** (https://cursor.com) — AI-native code editor, free plan
- **Claude Code extension** for Cursor (by Anthropic)
- **Codex extension** for Cursor (by OpenAI)
- **Git for Windows** (https://git-scm.com) — needed for Cursor to interact with GitHub
- **GitHub account** + this public repo

## Steps I completed

1. Downloaded and installed Cursor IDE for Windows
2. Created a GitHub account and this public repository
3. Opened the Extensions panel in Cursor and installed Claude Code
4. Went through the Claude Code login flow
5. Installed the Codex extension (loaded into Cursor without any login friction)
6. Installed Git for Windows so Cursor could connect to GitHub
7. Opened this repo in Cursor using GitHub's "Open with Cursor" link
8. Wrote this README documenting the process
9. Committed and pushed to GitHub

## Issues I ran into and how I solved them

**1. Claude Code wouldn't let me log in on the free tier.**

The extension presented three login options: Claude.ai Subscription (needs paid Pro or Max), Anthropic Console (pay-per-use API credits), and enterprise cloud auth (Bedrock, Foundry, Vertex). I don't have a paid Claude subscription.

I created a new Anthropic Console account at console.anthropic.com. I had read that new accounts in some regions get $5 in free credits with phone verification, but that promo didn't apply to my India signup. The Console required a credit top-up before key generation worked. I completed the signup, generated an API key, and went through the OAuth flow with Cursor's extension. The extension now shows as authenticated. Actually running a prompt returns a "credit balance too low" error since my balance is $0, but the install is complete and the login state is real.

**2. Cursor's Clone Repo button did nothing.**

After installing Git for Windows, I expected Cursor's built-in clone button to work, but clicking it had no effect. I tried restarting Cursor, confirmed `git --version` ran fine in PowerShell, and reinstalled Git. The button still wouldn't respond. I worked around it by going to my repo on github.com, clicking the Code dropdown, and using the "Open with Cursor" option from there. That opened the cloned repo directly in Cursor and let me skip the in-app clone button entirely.

Codex installed without any of these issues. The extension loaded directly in Cursor and was ready to use, no paywall, no auth flow blocking the install.
