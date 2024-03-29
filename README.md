# club.eh 2023 CTF - Challenge Repository

This repo contains the challenges released during club.eh's 2023 CTF: Hacker's Odyssey.

**We have archived our CTF website: [https://ctf-2023.clubeh.ca/](https://ctf-2023.clubeh.ca/)**  
Please note that our dynamic challenges have been taken down; however, you can still host them yourself using the files from this repo.

---

## Description

This repo is meant to be deployed to a CTFd instance using [sudoBash418's ctf-challenge-toolkit](https://github.com/club-eh/ctf-challenge-toolkit).

We used a modified version of CTFd during the event, which can be found [here](https://github.com/club-eh/CTFd/tree/ctf-2023-deploy).  
Our CTFd theme can be found [here](https://github.com/club-eh/ctfd-theme/tree/hackers-odyssey).

The infrastructure used to host our CTF can be found [here](https://github.com/club-eh/ctf-2023-infrastructure).


### Flag Format

Example: `clubeh{some_l33t_speak_here_5731c3a0}`  
Regex: `clubeh\{[\w]{8,64}\}`

If a challenge does not follow this flag format, its description must clearly indicate that.


## Repository Layout

The outer repository layout consists of:

- A `challenge-repository.toml` file.
  Defines challenge categories.
- Multiple directories, one for each challenge.
  These directories should follow the [challenge layout](#challenge-layout)


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
- A `healthcheck/` subdirectory ~~(required if `dynamic` is present)~~.  
  ~~This directory will be used for healthcheck scripts (details TBD).~~  
  We ran out of time to properly implement this.

Additionally, a subdirectory named `source` may be present as well. This is meant for any extra files that aren't relevant to deployment, but are otherwise useful to challenge development.  
For example, a binary reversing challenge would have the binary's source code in `source/`.

Files that should be made available for players to download include files under `static/`, along with any files specified in the relevant `challenge.toml`.
