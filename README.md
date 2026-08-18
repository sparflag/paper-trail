# Paper Trail (`paper-trail`)

**Category:** osint · **Difficulty:** medium · **Points:** 250

A leaked document's metadata names an author whose handle is the key.

## Run it

```bash
docker build -t sparflag/paper-trail .
# `deca-ai start paper-trail` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is XOR-encrypted then base64-encoded. Discover the challenge key, then invert XOR+base64.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit paper-trail 'sparflag{...}'
```

## Hints

- Documents remember who made them.
- The author/creator field is the key; invert XOR+base64.
