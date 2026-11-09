**session init** — model `claude-sonnet-5-5`, MCP servers [{'name': 'prompt-history', 'status': 'connected', 'source': 'dynamic'}, {'name': 'claude-in-chrome', 'status': 'connected', 'source': 'dynamic'}], 

**TOOL CALL → `Read`** `{"file_path": "/home/claude/demo/rosetta/rosetta/db.py"}`

<details><summary>tool result</summary>

```
1	"""The persistent Chroma store: two collections holding the same ids.
2	
3	`literal` embeds each idiom's own words; `meaning` embeds its gloss. Every
4	search is a query against one or both of them.
5	"""
6	
7	import re
8	import threading
9	import uuid
10	from pathlib import Path
11	from typing import Callable
12	
13	from .embed import embedding_function, models_label
14	
15	ROOT = Path(__file__).resolve().parent.parent
16	DB_PATH = ROOT / "chroma_db"
17	BATCH_SIZE = 256
18	# Below this cosine …[7708 chars trimmed]
```
</details>

**ASSISTANT:** I read `rosetta/db.py` and changed nothing. I didn't run any of it, so the Chroma-behavior points are things to verify, not confirmed failures.

**Likely bugs**

1. **`stats()` counts keys that `_metadata` never writes (lines 215-216).** It counts `meaning_pinyin` and `idiom_en`, but `_metadata` only stores `pinyin`. Unless some enrichment step patches those fields in via `update_metadata`, `zh_pinyin` and `zh_english` will always be 0.

2. **`lookup_key` strips punctuation before collapsing whitespace (lines 82-83).** `"break a leg ."` becomes `"break a leg "` after `rstrip`, and the regex then collapses the trailing space to one space instead of removing it. The key keeps a trailing space and won't match the stored `"break a leg"`. Fix by collapsing and stripping last. The docstring also says quotes don't matter, but only `’` is normalized. `‘ ’ “ ”` and the Chinese `。！？` are not.

3. **`update_metadata` fails when none of a batch's ids exist (lines 141-144).** `meaning().get` returns no ids, and `update(ids=[])` raises in Chroma, which rejects empty id lists. Unknown ids are otherwise dropped silently. Patching `idiom` also leaves `key` stale, because `key` is only computed in `_metadata`.

4. **`build` crashes on duplicate ids in `records` (lines 108-114).** Duplicates within one batch raise a `DuplicateIDError` from Chroma. Also, "already-stored ids are skipped" means edited records never update, so a rebuild with corrected glosses does nothing.

**Worth checking**

5. **The model-mismatch guard may never fire (lines 54-61).** It relies on `get_or_create_collection` leaving an existing collection's metadata untouched. If your Chroma version overwrites it with the passed `metadata`, `built_with` always equals the current label. Chroma may also raise its own embedding-function conflict first, before your friendlier `ModelMismatch`. A more robust approach is to call `get_collection` first, check its metadata, and only create if it's missing.

6. **`add` isn't atomic (lines 131-132).** If the `meaning().add` fails after `literal().add` succeeds, you get an orphan id in `literal`. Later `build` treats it as not stored, but `add` never retries. Other points:
   - `add` doesn't validate `lang`, so a bad value later raises `KeyError` in `equiv` (`OTHER[...]`).
   - It doesn't reject an empty idiom or gloss.
   - It doesn't call the duplicate check, so every caller has to remember `nearest_meanings` and `DUPLICATE_THRESHOLD`.

7. **`_vector` raises a bare `IndexError` for an unknown id (line 159).** `equiv` and `compare` hit this if the record's id is missing from either collection, for example after the partial write in point 6.

**Minor**

- `detect_lang` only covers U+4E00–U+9FFF (the basic CJK block), so rare characters in the Extension A block (U+3400–U+4DBF) are classed as English.
- `stats()` pulls every zh metadata row into memory just to count two fields, which will be slow on a large store.
- `find` and `compare` ask for `k` or `k+1` results without checking the collection size. Chroma only warns when it's smaller, so this is harmless.


---
*result: success, turns=2, cost=$0.09, 24s*
