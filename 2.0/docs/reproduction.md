# Reproduction instructions

### Issue
The original routing function did not support the `critical` priority

### Original behavior
- urgent -> duty
- standard -> service
- critical -> raised an error with `unsupported priority`

### How to reproduce
1. Check out the original version of the routing function
2. Run the tests with `critical` as the priority
3. Observe the error raised

### Expected behavior
The `critical` priority should return duty