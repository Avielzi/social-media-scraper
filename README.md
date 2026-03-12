# 🚀 Multi-Platform Social Media Scraper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Avielzi/social-media-scraper/graphs/commit-activity)
[![Stars](https://img.shields.io/github/stars/Avielzi/social-media-scraper?style=social)](https://github.com/Avielzi/social-media-scraper/stargazers)

--- 

## 🌟 Unlock Social Media Insights with Ease

This project provides a **powerful, flexible, and easy-to-use Python-based solution** for extracting valuable data from major social media platforms: **Facebook**, **LinkedIn**, and **Twitter/X**. Designed for developers, data analysts, and researchers, it offers multiple scraping methods, including official APIs and robust third-party integrations, ensuring reliable and comprehensive data collection.

--- 

## ✨ Key Features & Capabilities

-   **📘 Facebook Scraper**: Effortlessly extract posts, comments, likes, and media from public Facebook pages. Ideal for sentiment analysis, trend monitoring, and competitive intelligence.
-   **💼 LinkedIn Scraper**: Gather professional insights from LinkedIn profiles and organization pages, supporting lead generation, market research, and talent acquisition efforts.
-   **🐦 Twitter/X Scraper**: Fetch tweets, engagement metrics (likes, retweets, replies), and user data using the official Twitter API v2, perfect for social listening and campaign analysis.
-   **🔄 Multi-Method Support**: Our intelligent system automatically selects the best available scraping method:
    -   **Official APIs**: Leverage stable and reliable direct integrations (Facebook Graph API, Twitter API v2, LinkedIn API) for high-fidelity data.
    -   **Apify Integration**: Get started instantly with a powerful third-party service. Apify offers a generous free tier (~500-1000 posts) and handles complex anti-bot measures, making it ideal for quick setups and large-scale projects.
    -   **Auto-Fallback**: The scraper intelligently attempts different methods, ensuring maximum data retrieval even if one method fails.
-   **📊 Data Export & Management**:
    -   **Structured JSON Output**: All scraped data is saved in a clean, easy-to-parse JSON format, ready for immediate use in your applications or databases.
    -   **Universal Aggregator (`universal_aggregator.py`)**: Consolidate data from various platforms into a single, unified dataset for holistic analysis.
    -   **Post Loader (`load_posts.py`)**: Quickly load and display your scraped data, providing immediate insights and verification.
-   **🛠️ Developer-Friendly**: Includes ready-to-use scripts (`facebook_quick_scrape.py`, `quick_start_examples.py`) and comprehensive documentation for rapid deployment and customization.

--- 

## 🚀 Quick Start Guide

Get your social media scraper up and running in minutes!

### 1. Clone the Repository

```bash
git clone https://github.com/Avielzi/social-media-scraper.git
cd social-media-scraper
```

### 2. Install Dependencies

```bash
pip install requests
```

### 3. Configure API Keys

Edit the `scraper_config.json` file to include your API credentials. You can use either Apify (recommended for quick setup) or official API tokens:

```json
{
  "apify": {
    "api_token": "YOUR_APIFY_TOKEN" 
  },
  "facebook": {
    "access_token": "YOUR_FB_ACCESS_TOKEN"
  },
  "linkedin": {
    "client_id": "YOUR_LINKEDIN_CLIENT_ID",
    "client_secret": "YOUR_LINKEDIN_CLIENT_SECRET",
    "access_token": "YOUR_LINKEDIN_ACCESS_TOKEN"
  },
  "twitter": {
    "api_key": "YOUR_TWITTER_API_KEY",
    "api_secret": "YOUR_TWITTER_API_SECRET",
    "bearer_token": "YOUR_TWITTER_BEARER_TOKEN",
    "access_token": "YOUR_TWITTER_ACCESS_TOKEN",
    "access_token_secret": "YOUR_TWITTER_ACCESS_TOKEN_SECRET"
  }
}
```

### 4. Run the Scraper

Execute the `facebook_quick_scrape.py` script for an interactive Facebook scraping experience:

```bash
python facebook_quick_scrape.py
```

For more advanced usage and examples, refer to `quick_start_examples.py`.

--- 

## 📖 Comprehensive Documentation

Dive deeper into the project with our detailed guides:

-   [**Full Automation Guide**](AUTOMATION_GUIDE.md): A complete walkthrough for setting up and utilizing all supported APIs across different platforms.
-   [**Facebook Quick Start**](FACEBOOK_QUICK_START.md): A dedicated guide for getting started specifically with Facebook data extraction.
-   [**Usage Examples**](quick_start_examples.py): Practical code snippets demonstrating various scraping scenarios and configurations.

--- 

## 🛠️ Supported Methods at a Glance

| Platform    | Official API | Apify (Recommended) | Web Scraping (Limited) |
| :---------- | :----------: | :-----------------: | :--------------------: |
| **Facebook**  |      ✅      |         ✅          |           ⚠️           |
| **LinkedIn**  |      ✅      |         ✅          |           ⚠️           |
| **Twitter/X** |      ✅      |         ✅          |           ⚠️           |

*⚠️ Web scraping is generally not recommended due to platform anti-bot measures and frequent layout changes. Official APIs or Apify provide more reliable and stable solutions.*

--- 

## 🤝 Contributing to the Project

We welcome contributions from the community! If you have ideas for new features, improvements, or bug fixes, please follow these steps:

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

--- 

## 📄 License

Distributed under the MIT License. See the `LICENSE` file for more information.

--- 

## ⭐ Show Your Support

If this project helps you unlock valuable social media insights, please consider giving it a star on GitHub! Your support fuels our development and helps us reach a wider audience. Thank you! 🙏

[![Star on GitHub](https://img.shields.io/github/stars/Avielzi/social-media-scraper?style=social)](https://github.com/Avielzi/social-media-scraper/stargazers)

--- 

## 📞 Support & Community

For any issues, questions, or feature requests, please open an [Issue](https://github.com/Avielzi/social-media-scraper/issues) on GitHub. Join our growing community to discuss best practices, share your scraping insights, and get assistance.

--- 

**Developed with ❤️ for the Automation Community.**

`#SocialMediaScraper` `#FacebookScraping` `#LinkedInScraping` `#TwitterScraping` `#PythonAutomation` `#DataExtraction` `#OSINT` `#Apify` `#SocialMediaAnalytics` `#WebScraping` `#APIIntegration` `#Python` `#OpenSource`
