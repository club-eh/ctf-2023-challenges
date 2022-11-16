# 2023 CTF challenge monorepo

Contains challenge files and associated configuration.

### Flag Format

Example: `clubeh{some_l33t_speak_here_5731c3a0}`  
Regex: `clubeh{[\w]{8,64}}`

If a challenge does not follow this flag format, its description must clearly indicate that.


## Repository Layout

The outer repository layout consists of:

- A `challenge-repository.toml` file.
  Defines challenge categories.
- Multiple directories, one for each challenge.
  These directories follow the [challenge layout](#challenge-layout)


```
repo/
├─ challenge-monorepo.toml
├─ barebones/
│  └─ challenge.toml
├─ some-static-challenge/
│  ├─ challenge.toml
│  └─ static/
│     └─ hidden-message.png
├─ sql-injection/
│  ├─ challenge.toml
│  └─ dynamic/
│     ├─ docker-compose.yaml
│     ├─ Containerfile
│     └─ src/
│        └─ index.php
├─ <challenge-id>/
│  ├─ challenge.toml
│  ├─ [dynamic/]
│  │  └─ [files...]
│  └─ [static/]
│     └─ [files...]
...
```


## Challenge Layout

Each challenge directory follows the given format:

- A `challenge.toml` file (required).  
  This file defines important aspects of the challenge, including metadata and deployment info.  
  A barebones challenge may only require this file (ex. "decode this base64 string").
- A `static/` subdirectory (optional).  
  If this directory exists, all contents will be made available to players as downloadable files.
- A `dynamic/` subdirectory (optional).  
  If this directory exists, the contents will be deployed on the challenge server according to the `[dynamic.*]` section(s) of the `challenge.toml`.
- A `healthcheck/` subdirectory (required if `dynamic` is present).  
  This directory will be used for healthcheck scripts (details TBD).

Additionally, a subdirectory named `source` may be present as well. This is meant for any extra files that aren't relevant to deployment, but are otherwise useful to challenge development.  
For example, a binary reversing challenge would have the binary's source code in `source/`.
