# Automated Product Comedy Shorts Generator (Pure GitHub Actions)

This repository contains the full source code for generating automated YouTube Shorts using pure GitHub Actions workflow.

## Environment Variables / GitHub Secrets Required:
- `GEMINI_API_KEY`: Gemini API key
- `GROQ_API_KEY`: Groq API key
- `YT_CLIENT_ID` & `YT_CLIENT_SECRET`: YouTube API credentials

*(Note: No image/media API keys required! Media is fetched automatically via direct high-definition media sources).*

## Execution:
Trigger manually via GitHub Actions tab using `workflow_dispatch`.