# Test Python Project for Renovate

This is a simple Python project created to test Renovate's dependency update functionality.

## Purpose

This project contains intentionally outdated dependencies in `requirements.txt` so that Renovate can:
1. Detect the outdated packages
2. Create pull requests to update them
3. Test the Renovate integration

## Files

- `requirements.txt` - Contains outdated package versions
- `app.py` - Simple Flask application using the dependencies
- `README.md` - This file

## How to Use

1. Push these files to your `packet-shark` repository
2. Wait for Renovate to scan the repository (15-30 minutes without webhooks)
3. Check for pull requests created by `metron-security-renovate[bot]`
4. Renovate should create PRs to update the outdated packages

## Expected Behavior

After pushing this to your repo, Renovate should:
- Detect `requirements.txt`
- Identify outdated packages
- Create pull requests like:
  - "Update dependency flask from 2.0.1 to latest"
  - "Update dependency requests from 2.26.0 to latest"
  - etc.

## Testing Locally (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Test endpoints
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/test-requests
```

## Note

This is a test project. Once Renovate is working, you can:
- Delete these files if not needed
- Or keep them as a simple example app
