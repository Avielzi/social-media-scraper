# 📘 Facebook Quick Start Guide

This guide will help you set up and run the Facebook scraper in minutes.

---

## 🚀 Choose Your Method

### 1️⃣ Method 1: Apify (Recommended - Works Immediately)
- ✅ **Setup Time**: 5 minutes
- ✅ **Cost**: $5 free credit (~500-1000 posts free)
- ✅ **No Approval Needed**: Works right away!

#### Steps:
1.  **Sign up for Apify**: [https://apify.com/sign-up](https://apify.com/sign-up)
2.  **Get API Token**: Go to **Settings** → **Integrations** → **Create API token**.
3.  **Add to `scraper_config.json`**:
    ```json
    {
      "apify": {
        "api_token": "apify_api_YOUR_TOKEN"
      }
    }
    ```
4.  **Run!**:
    ```bash
    python facebook_quick_scrape.py
    ```

---

### 2️⃣ Method 2: Facebook Graph API (Free Forever)
- ⏳ **Setup Time**: 30 minutes + 3-7 days waiting for approval
- ✅ **Cost**: Free
- ✅ **Full Data Access**: Unlimited posts and engagement metrics.

#### Steps:
1.  **Create Facebook App**: [https://developers.facebook.com](https://developers.facebook.com)
2.  **Get Access Token**: Use **Graph API Explorer** → **Generate Token**.
3.  **Add to `scraper_config.json`**:
    ```json
    {
      "facebook": {
        "access_token": "YOUR_TOKEN"
      }
    }
    ```
4.  **Run!**:
    ```bash
    python facebook_quick_scrape.py
    ```

---

## 📋 Summary of Files

### Core System:
- `multi_platform_scraper.py`: The main automation engine.
- `facebook_quick_scrape.py`: Ready-to-use script for Facebook.
- `scraper_config.json`: Your API credentials.

### Documentation:
- `AUTOMATION_GUIDE.md`: Full guide for all platforms (Facebook, Twitter, LinkedIn).
- `README.md`: General introduction and setup.
- `FACEBOOK_QUICK_START.md`: This guide!

---

## 🎯 Recommendation for Facebook

### 2-Step Plan:
1.  **Today (5 mins)**: Sign up for Apify, get $5 free, and scrape your first 500-1000 posts!
2.  **This Week (30 mins)**: Create a Facebook App, request permissions, and switch to the free API once approved.

---

## 💡 Troubleshooting
- **No posts found?** Check if the page is public and the URL is correct.
- **Configuration Error?** Ensure your token is correctly pasted in `scraper_config.json`.
- **Rate Limited?** Add `time.sleep(1)` between requests if scraping large amounts of data.

---

**Happy Scraping! 🚀**
