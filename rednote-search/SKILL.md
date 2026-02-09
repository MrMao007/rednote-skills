---
name: rednote-search
description: Search and extract content from rednote (xiaohongshu,小红书) platform. This skill enables users to search for posts by keyword and extract content from specific notes in markdown format. Use this when users need to find and access contents from xiaohongshu.com.
---

# Rednote Search Skill

This skill allows you to search and extract content from the Xiaohongshu (Little Red Book) platform. You can search for posts by keyword and return results, or convert content from specific notes to structured markdown format.

## Configuration and Preparation

### Requirements
- Python 3.7+
- Playwright (install with `pip install playwright`)
- Playwright drivers (install with `playwright install`)
- Configured browser environment

### Validate Xiaohongshu Login Status
Before using this skill, please verify your login status:
```
python scripts/validate_cookies.py
```

If the output is `True`, you have normal access and can proceed with search operations.

If the output is `False` or the login button is visible, please execute the manual login procedure:

```
python scripts/manual_login.py
```
Follow the instructions in the opened browser to complete the login, then close the browser after completion.

## Usage Steps

### Step 1: Content Search
Search Xiaohongshu notes by keyword:
```
python scripts/search_note_by_key_word.py <keyword> [--top_n TOP_N]
```
- `<keyword>`: Search keyword
- `--top_n TOP_N` (optional): Number of return notes (default is 5)

Output: A list of matching note URLs

### Step 2: Content Extraction
Extract note content to markdown format:
```
python scripts/dump_note.py <note_url>
```
- `<note_url>`: Complete URL of the Xiaohongshu note

Output: Structured markdown format with note content, including:
- Title and author
- User profile picture and nickname
- Media content (images or video)
- Body description
- Tags and interaction data (likes, saves, comments, shares)
- Publishing information (time, IP location, etc.)

## Script Details

| Script name | Usage | Output | Function |
|-------------|-------|--------|----------|
| `scripts/search_note_by_key_word.py` | `python scripts/search_note_by_key_word.py <keyword> [--top_n TOP_N]` | List of note URLs | Search Xiaohongshu notes using keywords |
| `scripts/dump_note.py` | `python scripts/dump_note.py <note_url>` | Markdown content | Extract specific note content and convert to markdown format |
| `scripts/validate_cookies.py` | `python scripts/validate_cookies.py` | Login status (True/False) | Check the validity of saved cookies |
| `scripts/manual_login.py` | `python scripts/manual_login.py` | Login guidance | Start interactive login interface and save cookies |

## Typical Use Cases

1. **Content Research**: Search specific topic posts on Xiaohongshu for market research or competitor analysis
2. **Information Collection**: Gather information on specific topics and format them for storage
3. **Data Mining**: Systematically obtain data and trend information from notes
4. **Content Analysis**: Perform in-depth analysis of user-generated content

## Notes and Limitations

1. **Comply with Platform Terms**: Please ensure compliance with Xiaohongshu's terms of service when using this skill
2. **Fair Usage**: Avoid high-frequency requests that might lead to IP blocking; consider adding appropriate request intervals
3. **Content Copyright**: Extracted content is copyrighted by original authors
4. **Data Accuracy**: In unstable network conditions, data loading errors may occur. Verification may be needed as appropriate

## Best Practices

- Before executing batch queries, validate the validity of cookies to ensure successful access
- Update cookies regularly to maintain access permissions
- If access problems are encountered, please re-execute the manual login procedure to update cookies

## Error Handling

If you encounter login expiration errors during operations:
- The script will return when detecting a need for login: "❌ Xiaohongshu not logged in, please log in first"
- In such cases, please run the manual login script to update your cookies


