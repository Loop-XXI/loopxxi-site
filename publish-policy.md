# LoopXXI — Public Brand Statement Publish Gate

Every public-facing brand statement published to Nostr, social media, or any external
channel **must** pass a 3-point self-check before being sent. If any check fails,
the post is blocked — do not send, do not repurpose, stop.

## The three checks

### 1. Every factual claim independently verified
If the post states a fact about LoopXXI — location, headcount, revenue, product
status, metrics, timelines — that fact must be traceable to a source you can cite
before you hit publish.

*Examples of failure:* "Building from Los Angeles" (incorrect — entity is an
Illinois LLC based in Chicago). "Trusted by 15+ industry leaders" (fabricated).
"Live since 2026" (true but unhelpful — see check 3).

### 2. No fabricated social proof
Do not invent users, customers, investors, advisors, team members, or endorsements.
If the post references people (avatars, names, logos, testimonials, "trusted by"),
every referenced entity must be real and have a verifiable relationship with
LoopXXI.

*This includes:* avatar stacks, customer logos, testimonial quotes, partner badges,
"backed by" claims, "also used by" mentions.

### 3. The post plausibly advances sats accumulation
A post should move a needle that matters. Before posting, ask: *does this
plausibly generate a new user, partner, customer, or sats?*

Internal milestones ("we shipped a redesign", "we refactored the stack") default
to **not posting** — they fail check 3. Exceptions require explicit approval from
Josh.

## Exemptions

- **Prod static-site deploys** (loopxxi.com, brand.html): execute-first.
  Trivially revertible. Not a brand statement.

- **Direct reply to an inbound inquiry**: if someone asks a question, answer it
  factually. Checks 1 and 2 still apply to the answer.

## Enforcement

This file is the authoritative gate. Before every publish action:
1. Read this file.
2. Run the 3 checks against the proposed content.
3. If any check fails, do NOT publish. Log the block reason.

The gate binds all Hermes agents (current and future) operating under this repo.
It survives context resets, model swaps, and tool changes.
