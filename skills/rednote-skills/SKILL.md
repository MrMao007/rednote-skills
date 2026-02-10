---
name: rednote-skill
description: Comprehensive tool for interacting with rednote (xiaohongshu,小红书) platform. This skill enables users to search for posts by keyword, extract content from specific notes in markdown format, and perform interaction actions like liking, commenting, collecting, following, and publishing. Use this when users need to engage with content from xiaohongshu.com.
---

# Rednote Skill

This skill allows you to fully interact with the Xiaohongshu (Little Red Book) platform. You can search for posts by keyword and return results, extract content from specific notes to structured markdown format, and perform engagement actions like liking, commenting, collecting, following users, and more.

## Configuration and Preparation

### Requirements
- Python 3.7+
- Playwright (install with `pip install playwright`)
- Playwright drivers (install with `playwright install`)
- Configured browser environment

### Validate Xiaohongshu Login Status
Before using this skill, the system will verify your login status:
```
python scripts/validate_cookies.py
```

If the output is `True`, you have normal access and can proceed with search operations.

If the output is `False` or the login button is visible, the system will automatically execute the manual login procedure:

```
python scripts/manual_login.py
```
The system will launch the login interface in a browser window. You'll need to follow the instructions in the opened browser to complete the login process manually, then close the browser after completion.

## Usage Steps

### 1. Environment Setup

Before using this skill, ensure that:
1. The required dependencies are installed (Python 3.7+, Playwright)
2. The system will automatically handle the cookie saving via the manual login process when needed
3. Login status will be validated automatically using the validation utility

### 2. Using Search Functions

The skill provides several search and extraction functions:

- **Search Notes by Keyword**: `python scripts/search_note_by_key_word.py <KEYWORD> [--top_n TOP_N]`
- **Extract Note Content**: `python scripts/dump_note.py <NOTE_URL>`

### 3. Using Interaction Functions

The skill provides several interaction functions:

- **Like Note**: `python scripts/like_note.py <NOTE_URL>`
- **Collect Note**: `python scripts/collect_note.py <NOTE_URL>`
- **Comment on Note**: `python scripts/comment_note.py <NOTE_URL> <COMMENT_TEXT>`
- **Follow User**: `python scripts/follow_user.py <NOTE_URL>`
- **Publish Note**: `python scripts/publish_note.py [--title TITLE] [--content CONTENT] [--image_path IMAGE_PATH]`
- **Validate Login**: `python scripts/validate_cookies.py`
- **Manual Login**: `python scripts/manual_login.py`

### 4. Complete Workflow

1. Validate login status before starting interactions
2. Execute desired search functions if you need to find specific notes
3. Execute desired interaction functions with proper arguments
4. Monitor results for successful completion

## Function Descriptions

This skill provides the following functions for searching content on and interacting with the Xiaohongshu platform:

### Search Notes (`search_note_by_key_word.py`)
**Purpose**: Searches for Xiaohongshu notes using the provided keyword.

**Parameters**:
- `keyword` (string): The keyword to search for
- `--top_n` (integer, optional): Number of return notes (default is 5)

**Returns**: List of note URLs that match the keyword

**Behavior**: Launches browser, searches for the keyword on Xiaohongshu, returns matching note URLs.

### Extract Note Content (`dump_note.py`)
**Purpose**: Extracts specific note content and converts to formatted markdown.

**Parameters**:
- `note_url` (string): The URL of the note to extract content from

**Returns**: Structured markdown content including author, title, media, description, tags, and interaction data

**Behavior**: Launches browser, accesses the note, extracts content and formats to markdown.

### Like Note (`like_note.py`)
**Purpose**: Likes a specific note on Xiaohongshu using the note URL.

**Parameters**:
- `note_url` (string): The URL of the note to like

**Returns**: Success or error message indicating if the like was successful

**Behavior**: Launches browser, navigates to the note URL, clicks the like button, then closes the browser.

### Collect Note (`collect_note.py`)
**Purpose**: Collects (saves) a specific note to the user's collection.

**Parameters**:
- `note_url` (string): The URL of the note to collect

**Returns**: Success or error message indicating if the collection was successful

**Behavior**: Launches browser, navigates to the note URL, clicks the collect button, then closes the browser.

### Comment on Note (`comment_note.py`)
**Purpose**: Adds a comment to a specific note on Xiaohongshu.

**Parameters**:
- `note_url` (string): The URL of the note to comment on
- `comment_text` (string): The text content of the comment

**Returns**: Success or error message indicating if the comment was published

**Behavior**: Launches browser, navigates to the note URL, fills in the comment text, clicks the send button, then closes the browser.

### Follow User (`follow_user.py`)
**Purpose**: Follows the user who created a specific note by visiting a note URL.

**Parameters**:
- `note_url` (string): The URL of a note by the user to follow

**Returns**: Success or error message indicating if the follow action was successful

**Behavior**: Launches browser, navigates to the note URL, clicks the follow button if available, then closes the browser.

### Validate Login Status (`validate_cookies.py`)
**Purpose**: Checks if the saved authentication tokens are valid and the user is logged in to Xiaohongshu.

**Parameters**: None

**Returns**: Boolean value indicating whether login is successful

**Behavior**: Launches browser, accesses Xiaohongshu homepage with stored credentials, checks for login state.

### Manual Login (`manual_login.py`)
**Purpose**: Assists in creating valid authentication cookies by opening the login interface.

**Parameters**: None

**Returns**: Success or error message after cookies are saved

**Behavior**: Launches browser, navigates to Xiaohongshu, allows user to log in manually, then saves cookies to storage file.

### Publish Note (`publish_note.py`)
**Purpose**: Publishes a new note to the user's Xiaohongshu account with provided content and options for image upload.

**Parameters**:
- `[--title TITLE]`: The title for the new note (optional, can also be entered during publishing)
- `[--content CONTENT]`: The main content text for the new note (optional, can also be entered during publishing)
- `[--image_path IMAGE_PATH]`: Path to image file(s) to upload with the note (optional, can add images interactively)

**Returns**: Success or error message indicating if the note was published successfully

**Behavior**: Launches browser, navigates to the Xiaohongshu publish page, fills in the note title, content, and uploads provided images, then clicks the publish button.

## Examples

### Basic Search and Content Extraction
```
# Validate login status
python scripts/validate_cookies.py

# Search for notes about "旅行攻略"
python scripts/search_note_by_key_word.py "旅行攻略" --top_n 3

# Extract content from a specific note
python scripts/dump_note.py "https://www.xiaohongshu.com/explore/some-note-id"
```

### Basic Liking and Collecting
```
# Like a specific note
python scripts/like_note.py "https://www.xiaohongshu.com/explore/some-note-id"

# Collect a specific note
python scripts/collect_note.py "https://www.xiaohongshu.com/explore/some-note-id"
```

### Commenting on a Note
```
# Add a comment to a specific note
python scripts/comment_note.py "https://www.xiaohongshu.com/explore/some-note-id" "Beautiful content! Thanks for sharing."
```

### Following a User
```
# Follow a user based on one of their posts
python scripts/follow_user.py "https://www.xiaohongshu.com/explore/some-note-by-user-id"
```

### Publishing a Note
```
# Publish a new note with title, content, and image
python scripts/publish_note.py --title "My New Post" --content "Check out this amazing discovery!" --image_path "/path/to/image.jpg"

# Publish a new note with interactive entry (without specifying parameters)
python scripts/publish_note.py
```

### Complete User Session
```
# 1. Validate login
python scripts/validate_cookies.py

# 2. Search for interesting content
python scripts/search_note_by_key_word.py "美食推荐" --top_n 5

# 3. Extract detailed content from a note
python scripts/dump_note.py "https://www.xiaohongshu.com/explore/note1"

# 4. Like interesting content
python scripts/like_note.py "https://www.xiaohongshu.com/explore/note1"

# 5. Collect useful content
python scripts/collect_note.py "https://www.xiaohongshu.com/explore/note2"

# 6. Engage with community
python scripts/comment_note.py "https://www.xiaohongshu.com/explore/note3" "Awesome tutorial!"

# 7. Follow good content creators
python scripts/follow_user.py "https://www.xiaohongshu.com/explore/note-by-creator"
```

## Implementation Guidelines

### Best Practices

1. **Validate Login First**: Login status will be automatically checked using `validate_cookies.py` before performing any interactions to ensure smooth operations.

2. **Rate Limiting**: To avoid account restrictions, implement appropriate delays between consecutive interactions. Avoid excessive rapid interactions.

3. **Error Handling**: Check the return values from the functions to ensure operations were successful before proceeding to the next action.

4. **User Intent**: Only engage with content that matches user interest and preferences. The skill should complement user decisions.

5. **Browser State Management**: The scripts manage browser opening and closing, so ensure system resources are available for these operations.

### Integration Considerations

1. **Session Management**: The skill maintains session state through cookies stored in `rednote_cookies.json`. Ensure this file is properly secured.

2. **Browser Automation**: The skill uses headless browsers for automation. Ensure the system has a compatible browser environment set up.

3. **URL Format**: The scripts expect properly formatted Xiaohongshu URLs. Ensure URLs are valid before passing to functions.

4. **Content Appropriateness**: Integrate this skill in a way that ensures interactions are appropriate and align with platform terms of service.

## Configuration and Preparation

### Advanced Setup

#### Cookie Management
- The skill stores authentication data in `rednote_cookies.json`
- This file is created automatically during the manual login process
- For security, protect this cookie file from unauthorized access

#### Environment Variables
- No specific environment variables are required
- The skill uses the default configuration files in the scripts directory

### Prerequisites Verification

Before using the rednote skill, verify:

1. **System Setup**:
   - Python 3.7 or above
   - Playwright installed (`pip install playwright`)
   - Browser drivers installed (`playwright install`)
   - Minimum available disk space for browser operation

2. **Xiaohongshu Access**:
   - Ability to access Xiaohongshu.com from your network
   - Compliance with Xiaohongshu's terms of service
   - Valid Xiaohongshu account credentials

3. **Security Setup**:
   - The system will handle automatic login when needed
   - Login status will be confirmed via validation script
   - Secured storage for authentication tokens

## Troubleshooting

### Common Issues

#### Login Error (`❌ 未找到 cookies 文件，请先登录小红书并保存 cookies`)
**Cause**: The `rednote_cookies.json` file doesn't exist or is not in the correct location.
**Solution**: The system will automatically execute `python scripts/manual_login.py` to perform manual login and save cookies. The user just needs to complete the login process in the opened browser window.

#### Login Session Expired (`❌ 未登录小红书，请先登录`)
**Cause**: Authentication tokens have expired or are invalid.
**Solution**: The system will re-verify login status and may execute `python scripts/manual_login.py` again to refresh tokens. The user just needs to complete the login process in the opened browser window if prompted.

#### Page Navigation Issues
**Cause**: Network connectivity issues or URL format errors.
**Solution**: Verify URL format is correct, ensure internet connection is stable, and check if Xiaohongshu is accessible.

#### Element Not Found During Interaction
**Cause**: Xiaohongshu's UI might have changed or the page hasn't loaded completely.
**Solution**: Retry the operation; if the issue persists, check for interface changes or wait before trying again.

### Debugging Steps

1. **Verify Prerequisites**: Ensure all requirements are installed and accessible
2. **Check Login Status**: Run the validation script before operations
3. **Review URL Format**: Ensure URLs are properly formatted Xiaohongshu links
4. **Monitor Browser Behavior**: Use non-headless mode to observe the automation process
5. **Check Storage Files**: Verify cookies file exists and is accessible

### Performance Considerations

- Browser automation is resource-intensive; ensure system has sufficient memory and CPU
- Network latency may affect operation timing; consider adding delays between operations
- Run validation scripts periodically to confirm stable authentication

## Limitations and Considerations

### Platform Limitations

- **Terms of Service**: This skill must be used in compliance with Xiaohongshu's terms of service and community guidelines
- **Rate Limiting**: Xiaohongshu may impose limits on the number of interactions per time period
- **UI Changes**: Xiaohongshu may update their interface, which could break element selectors used by the skill
- **Geographic Restrictions**: Some functionality may be limited based on geographic location

### Technical Limitations

- **Browser Dependence**: The skill relies on browser automation which may be slower than direct API calls
- **Stability**: Browser automation can be affected by network conditions and site changes
- **Resource Usage**: Each interaction launches a browser instance, consuming system resources
- **Headless Compatibility**: Some interactions may work better in non-headless mode

### Security Considerations

- **Authentication Storage**: Authentication credentials are stored in `rednote_cookies.json` and should be secured
- **Privacy**: Interactions performed with this skill will be visible to other users on Xiaohongshu
- **Data Handling**: The skill doesn't collect user data beyond session management for interaction

### Ethical Considerations

- **Authentic Engagement**: Use the skill to facilitate genuine engagement with content that users actually find interesting
- **Respect Content Creators**: Consider the impact of interactions on content creators and their audience
- **Anti-Spam Ethics**: Avoid using the skill for spam-like behavior or in ways that could harm the platform ecosystem