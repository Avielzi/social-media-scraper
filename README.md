# 🚀 Multi-Platform Social Media Scraper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/your-username/social-media-scraper/graphs/commit-activity)

A powerful, flexible, and easy-to-use tool for scraping posts from **Facebook**, **LinkedIn**, and **Twitter/X**. Support for multiple scraping methods including official APIs, third-party services (Apify), and automated fallbacks.

---

## ✨ Key Features

- 📘 **Facebook Scraper**: Extract posts, likes, comments, and media from public pages.
- 💼 **LinkedIn Scraper**: Gather insights from personal profiles and organization pages.
- 🐦 **Twitter/X Scraper**: Fetch tweets and engagement metrics using API v2.
- 🔄 **Multi-Method Support**:
  - **Official APIs**: Stable and reliable (Graph API, Twitter v2).
  - **Apify Integration**: Quick start with no approval needed (~500-1000 posts free).
  - **Auto-Fallback**: Automatically tries the best available method.
- 📊 **Data Export**: Save results in structured JSON format for easy analysis.
- 🔄 **Universal Aggregator**: Dynamic content collector for any social media page.
- 📂 **Post Loader**: Quick loading and formatting of scraped posts.
- 🛠️ **Quick Start Scripts**: Ready-to-use scripts for immediate results.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/social-media-scraper.git
cd social-media-scraper
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Configure API Keys
Edit `scraper_config.json` and add your credentials:
```json
{
  "apify": {
    "api_token": "YOUR_APIFY_TOKEN"
  },
  "facebook": {
    "access_token": "YOUR_FB_ACCESS_TOKEN"
  }
}
```

### 4. Run the Scraper
For a quick Facebook scrape:
```bash
python facebook_quick_scrape.py
```

---

## 📖 Documentation

Detailed guides for each platform and method:

- [**Full Automation Guide**](AUTOMATION_GUIDE.md) - Step-by-step setup for all APIs.
- [**Facebook Quick Start**](FACEBOOK_QUICK_START.md) - Specific guide for Facebook scraping.
- [**Usage Examples**](quick_start_examples.py) - Code snippets for various use cases.

---

## 🛠️ Supported Methods

| Platform | Official API | Apify (Recommended) | Web Scraping |
| :--- | :---: | :---: | :---: |
| **Facebook** | ✅ | ✅ | ⚠️ |
| **LinkedIn** | ✅ | ✅ | ⚠️ |
| **Twitter/X** | ✅ | ✅ | ⚠️ |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## ⭐ Show Your Support

If you find this project useful, please consider giving it a star on GitHub! Your support helps us grow and improve this tool for everyone. 🙏

[![Star on GitHub](https://img.shields.io/github/stars/Avielzi/social-media-scraper?style=social)](https://github.com/Avielzi/social-media-scraper/stargazers)

---

## 📞 Support & Community

For issues, questions, or feature requests, please open an [Issue](https://github.com/Avielzi/social-media-scraper/issues).

Join our community to discuss features, get help, and share your scraping insights!


---

**Developed with ❤️ for the Automation Community.**

`#SocialMediaScraper` `#FacebookScraping` `#LinkedInAPI` `#TwitterAPI` `#PythonAutomation` `#DataExtraction` `#Apify`
