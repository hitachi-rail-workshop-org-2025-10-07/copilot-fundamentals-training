# 🛡️ Emergency Log Triage Demo

## 🚀 What You'll Build

In this short lab you'll use **GitHub Copilot** to transform a bare‑bones skeleton into a working Python utility that:

1. Streams either plain or gzipped access‑log files.  
2. Filters entries by **date range** (`--from`/`--to`) or **last *N* minutes** (`--minutes`).  
3. Tallies `(HTTP‑status, endpoint)` pairs.  
4. Prints a compact Markdown‑style histogram.

The goal isn't perfect code—it's to **see Copilot's UI and autocompletion magic in action**. You'll prompt Copilot from comment blocks, accept (or finesse) its suggestions, and watch it generate production‑style boilerplate in seconds. 🪄

---

## 🗂️ Repository Layout

| Path | Purpose |
|------|---------|
| `triage.py` | The starter script with **function stubs** and embedded Copilot prompts. |
| `sample_access.log.gz` | A 1 000‑line gzipped access‑log spanning the last hour, containing a mix of 2xx/4xx/5xx, plus custom `499` and `321` errors for testing. |
| `README.md` | The instructions for this demo. |

---

## 🛠️ Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.8 + | Standard library only—no external packages required. |
| VS Code | Latest | Any IDE that supports GitHub Copilot will work, but the steps below assume VS Code. |
| GitHub Copilot | Enabled | Make sure the extension is signed‑in and working (check for 💡 suggestions). |

---

## 🧑‍💻 Hands‑On Walkthrough

### 1. Clone & Open

```bash
git clone https://github.com/ps-copilot-sandbox/copilot-fundamentals-training.git
cd demos/copilot-essentials/
code .
```

### 2. Explore the Skeleton

Open **`triage.py`** and familiarize yourself with the structure:

- **5 empty functions** with `pass` statements that need implementation
- **Detailed prompts** at the **top of the file** (lines 15-45) with exact instructions for each function
- **Function signatures** already defined with proper type hints

Example function structure:

```python
def read_lines(file_path: Path) -> Iterable[str]:
    """Open plain or gzipped log file and yield each line (stripped)."""
    pass  # ← Copilot will fill this in
```

### 3. Find the Prompts 📜

**Look at the top** of `triage.py` (lines 15-45) to find the **Copilot prompts section**:

```python
# 📝 Updated Copilot prompts with improvements and date range support
# read_lines prompt:
#   "Implement read_lines(file_path) to transparently handle .log or .log.gz files..."
# parse_line prompt: 
#   "Use a compiled regex for common/combined log format; extract timestamp..."
# ... etc
```

**💡 Pro Tip:** Consider **copying these prompts to the top** of each function for easier access!

### 4. Implement with Copilot ✨

For **each function** (`read_lines`, `parse_line`, `triage`, `render`, `main`):

1. **Read the corresponding prompt** at the top of the file
2. **Position your cursor** on the `pass` statement
3. **Type or paste the prompt** as a comment above `pass`
4. **Hit Tab** to trigger Copilot suggestions
5. **Review and accept** the generated code
6. **Test incrementally** - you can run the script after implementing `main()` to see argument parsing

**Alternative approach:**
- **Copy the entire prompt** from the top
- **Paste it as a comment** right above the `pass` statement  
- **Delete the `pass`** and let Copilot generate the implementation

> 💡 **Debugging Tip:** If Copilot doesn't suggest anything, try typing the first line yourself (e.g., `if file_path.suffix == ".gz":`) to give it context.

### 5. Test Your Implementation 🧪

**First, check if argument parsing works:**

```bash
python triage.py --help
```

**Using date range (recommended for this demo):**

```bash
python triage.py sample_access.log.gz --from 2025-07-15 --status 499,321 --top 10
```

**Using time window (sliding from now):**

```bash
python triage.py sample_access.log.gz --minutes 15 --status 499,321 --top 10
```

**With specific date/time range:**

```bash
python triage.py sample_access.log.gz --from "2025-07-15 16:00:00" --to "2025-07-15 18:00:00" --status 499,321
```

Expected output (truncated):

```
| Rank | Status | Path               | Hits |
|------|--------|--------------------|------|
| 1    | 321    | /reports/summary   | 13   |
| 2    | 499    | /static/app.js     | 11   |
| ...  | ...    | ...                | ...  |
```

**💡 Pro tip:** Since the sample log contains data from July 2025, use `--from 2025-07-15` to see results. Feel free to omit `--status` to see **all** codes, or change `--top` for more/fewer results.

### 6. Experiment

- **Change prompts** to ask for a progress bar or CSV export—then re‑run Copilot.  
- **Break the log format** in a few lines and see if your `parse_line` gracefully skips invalid entries.  
- **Swap in real logs** from your dev stack (keep them in `.log` or `.log.gz`).  

---

## 🔍 Inside `sample_access.log.gz`

* Format: **Apache/Nginx "combined" access log** (`ip – – [timestamp] "METHOD path HTTP/x.y" status size ...`).  
* Time span: past 60 minutes, randomised per run.  
* Status codes: normal 2xx & 3xx, plus plenty of `400`, `404`, `499`, `500`, `503` and a handful of **custom `321`**.  
* Endpoints: typical REST routes (`/api/v1/*`), static assets, health checks.

> 🗒️ **Why gzipped?** Real systems rotate & compress logs; beginners learn to handle both transparently.

---

## 🎯 Learning Objectives

| ✅ Skill | Demonstrated by |
|----------|------------------|
| Prompt‑driven code generation | Turning comment blocks into working Python functions. |
| Incremental acceptance | Reviewing, refining, or rejecting Copilot suggestions. |
| Code explanation & learning | Using Copilot Chat to understand WHY code works, not just WHAT it does. |
| Neighboring Tab Suggestions (NES) | Experiencing how Copilot learns from your patterns within the same file. |
| Error resolution | Using `/fix` command to automatically resolve coding issues. |
| Log processing patterns | Lazy file streaming, regex parsing, `collections.Counter`. |
| Advanced CLI design | Using `argparse` with mutually exclusive groups and date parsing. |
| Date/time handling | Converting log timestamps and working with timezone-aware datetimes. |

---

## 💬 Common Questions

| Q | A |
|---|---|
| "Why not use pandas?" | The lab is designed to stay in standard lib so no installs block your flow. |
| "Does Copilot always nail it first try?" | No—guide it! Move the cursor, tighten the prompt, or type the first line yourself. |
| "How big can the log be?" | Reading line‑by‑line uses constant memory; size is limited only by disk space. |

---

## 🧩 Stretch Challenges

1. **Add a `--dry‑run` flag** that prints how many lines *would* be processed without running the regex.  
2. **Output CSV** with `status,path,hits` so analysts can import it.  
3. **Relative date parsing**: Accept "--from yesterday" or "--from '2 hours ago'" using natural language.  
4. **Timezone support**: Handle logs with different timezones (not just UTC).  
5. **Threaded version**: parallel‑parse multiple log files in a directory.  
6. **Unit tests**: stub a tiny log sample and verify counter outputs with different date ranges.

---

## 📚 Further Reading

* [GitHub Copilot Docs → "Prompt Tips & Tricks"](https://docs.github.com/en/copilot)  
* Python docs: [`datetime`](https://docs.python.org/3/library/datetime.html), [`re`](https://docs.python.org/3/library/re.html), [`argparse`](https://docs.python.org/3/library/argparse.html)  
* Real‑world inspiration: [Nginx Log Formats](https://nginx.org/en/docs/http/ngx_http_log_module.html)

---

### 🎉 You're Done!

Fire up Copilot, generate the code, and impress your team with a **one‑off script** that would normally take an hour—now built in minutes. Happy triaging! 🤓