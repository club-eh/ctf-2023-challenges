# Pillowcode

Easy-to-medium difficulty Python reversing challenge by sudoBash418.

A simple Python script is provided (`source/generate.py`), along with a `static/result.png` generated from the script (with the flag as input).

## Solution

Solve script is available at `source/solve.py`

<details>
<summary>Spoiler</summary>

The naive solve is to directly reverse the operations from `encode()`:  
```python
flag[i] = (r & 0x70) | (g & 0x8a) | (b & 0x05)
```

A simpler solution is possible, however:
```python
flag[i] = r | g | b
```

</details>
