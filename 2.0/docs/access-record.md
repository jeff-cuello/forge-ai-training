# Access Record

### Allowed action
- Permission: edit = allow
- Resources: router.py and tests/test_router.py
- Result: Successfully edits the files

### Blocked action
- Permission: edit = deny, shell = deny
- Resources: all files except router.py and tests/test_router.py
- Result: Unable to edit files other than the allowed ones

### Access removal
- Initially allowed OpenCode to edit .md files
- Changed permission to deny
- Attempted the same file again
- Result: Edit was blocked