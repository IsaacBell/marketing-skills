---
name: hostinger-email
description: "Send and read email through the Hostinger mailbox API (api.mail.hostinger.com): find the mailbox id, send a message, list folders' messages. Use when wiring Hostinger email into a script, CRM or outreach tool, or when a send call fails. Covers what the API does not do and the cold-email sending rules a new domain has to follow."
version: 1.0.0
verified-against: "Hostinger mail API v1, October 2026. GET /me, POST send (204) and the inbox list were exercised live. Check the installed behavior before relying on a field."
---

# Hostinger email API

Hostinger's mailbox API sends mail from a mailbox you already host there, and reads the messages in it. It is a plain JSON API with bearer auth. It is not a bulk-mail service: it sends one message per call from one mailbox.

Check the current API reference for new endpoints. This skill records what was confirmed and what is easy to get wrong.

## Setup

- Base URL: `https://api.mail.hostinger.com`
- Auth: `Authorization: Bearer <API token>`. Create the token in Hostinger's panel. It is scoped to one order and the mailboxes under it. Keep it in a secret manager and inject it as an environment variable. Never put it in a repo, a config file or a command line.
- Every call takes a mailbox resource id (looks like `AC` plus letters and digits), not the email address.

## Find the mailbox id

There is no "list mailboxes" route. `GET /api/v1/mailboxes` returns 404. Use the account route:

```
GET /api/v1/me
```

It returns `data.orderResourceId` and `data.mailboxes[]`, each with `address` and `resourceId`. Pick the mailbox whose `address` matches your sender. Resolve it once and keep it in configuration, or resolve it on start-up.

## Send a message

```
POST /api/v1/mailboxes/{mailboxResourceId}/send
Content-Type: application/json
```

Body fields: `to`, `cc`, `bcc` (arrays of addresses; at least one is required), `subject`, `text`, `html`, `displayName`, `attachments[]` (`filename`, `content` base64, optional `contentType`, `cid`, `encoding`), and `inReplyTo` or `forwardOf` (an object with `folder` and `uid` of the source message; they are mutually exclusive).

What to expect:

- Set your own `User-Agent` header. A send made with a scripting library's default User-Agent came back `403` with an HTML page from the provider's edge network (no JSON envelope), while the same token worked from `GET /me`. A descriptive User-Agent fixed it. If you see a `403` that is HTML, this is the first thing to try; a real permission problem returns the JSON error envelope.
- Success is `204` with an empty body. There is no message id to store. Log the recipient, subject and time yourself.
- The message is copied to the mailbox's `INBOX.Sent` folder.
- `displayName` changes the name shown, not the sending address. The sender is always the mailbox the token is authorized for.
- Errors share one envelope: `{ "error": "...", "code": "ERR_...", "params": {...} }`. Branch on `code`, not on the text. `401` is a bad token, `403` is a mailbox the token cannot manage, `422` is a validation failure with the offending fields in `params`, `502` and `504` are upstream problems and are safe to retry later.
- There is no documented reply-to, custom header or unsubscribe-header field. Put the opt-out line in the body.

## Read messages

```
GET /api/v1/mailboxes/{mailboxResourceId}/folders/{folder}/messages?page=1&perPage=25&sort=-uid
```

`folder` is URL-encoded (`INBOX`, `INBOX.Sent`). `perPage` goes up to 100. Sort by `uid`, `date` or `size`, with a `-` prefix for descending. Each message carries `uid`, `messageId`, `inReplyTo`, `from`, `to`, `subject`, `date`, `flags`, `unseen` and attachment metadata, and the response has a `pagination` block. A reply to something you sent has your message's id in `inReplyTo`, which is how to match replies to sends. Bounces arrive in `INBOX` as ordinary messages from a mailer-daemon address. A send to an address that does not exist is still accepted with `204`, and the failure shows up in the inbox seconds later with the subject "Undelivered Mail Returned to Sender". The list call returns metadata only, so to read the failed address and the reason fetch the message: `GET .../messages/{uid}` returns metadata and attachment details, `GET .../messages/{uid}/text` returns the decoded body as JSON, `GET .../messages/{uid}/source` returns the raw message, and `GET .../messages/{uid}/attachments/{attachmentId}` returns an attachment (a bounce carries the returned original as a `message/rfc822` attachment).

What a bounce says is in the status code. `5.1.1`, `5.1.2` and `5.1.3` mean the address or domain does not exist: stop writing to it for good. `5.2.2` means the mailbox is full: try again later. `5.7.x`, or words like spam, policy or not authenticated, mean the other side is refusing you, not the address: stop sending and check SPF, DKIM and DMARC. `4.x.x`, or a "(Delay)" subject, means the server is still trying: do nothing yet. Use `POST .../search` (see the reference) to filter rather than paging through everything.

## Sending cold email from a new domain

The API does not protect your sender reputation. You do.

- Set up SPF, DKIM and DMARC on the sending domain before the first message, and check them with a mail tester.
- Start at a few messages a day and raise the volume over weeks. Cap the daily count in your own code. A new domain that sends a burst gets filtered.
- Send plain text, one recipient per message, no tracking pixels, no link shorteners.
- Include a real postal address and a clear way to opt out in every message, and keep a suppression list that the send step checks every time. US law (CAN-SPAM) and most other regimes require both for commercial email.
- Stop on a hard bounce and on a complaint. Do not retry a `422` or a bounced address.
- Do not email addresses you scraped from anywhere other than the recipient's own public business page.

## Writing the integration

- Keep the provider behind a small interface (`send(message) -> result`) so it can be swapped. Hostinger's `204`-with-no-id response is the main thing that differs from other providers.
- Read the token and mailbox id from the environment inside the adapter's factory, not inside the send call.
- Default to a dry run. A live send should need an explicit flag.
- Log every attempt (time, recipient, outcome) to an append-only file. Never log the token or the request headers.
