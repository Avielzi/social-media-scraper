# 🤖 מדריך אוטומציה מלא - AI Posts Scraper

## 📋 תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [שיטה 1: Facebook Graph API](#שיטה-1-facebook-graph-api)
3. [שיטה 2: LinkedIn API](#שיטה-2-linkedin-api)
4. [שיטה 3: Twitter API](#שיטה-3-twitter-api)
5. [שיטה 4: Apify (צד שלישי)](#שיטה-4-apify-צד-שלישי)
6. [שיטה 5: Web Scraping](#שיטה-5-web-scraping)
7. [השוואה בין השיטות](#השוואה-בין-השיטות)

---

## 🎯 סקירה כללית

המערכת תומכת ב-**3 פלטפורמות** ו-**5 שיטות איסוף**:

### פלטפורמות:
- ✅ **Facebook** - דפי עסקים וקבוצות
- ✅ **LinkedIn** - פרופילים אישיים וארגוניים
- ✅ **Twitter/X** - כל חשבון ציבורי

### שיטות:
1. **Graph API** (רשמי, דורש אישור)
2. **LinkedIn API** (רשמי, דורש אישור)
3. **Twitter API v2** (רשמי, יש גרסה חינמית)
4. **Apify** (צד שלישי, מהיר)
5. **Web Scraping** (לא מומלץ)

---

## 🔵 שיטה 1: Facebook Graph API

### יתרונות:
- ✅ רשמי ויציב
- ✅ גישה למידע מלא (לייקים, תגובות)
- ✅ תומך בפגינציה (כל הפוסטים)
- ✅ חינמי עד 200 בקשות/שעה

### חסרונות:
- ❌ דורש אישור מפייסבוק (3-7 ימים)
- ❌ תהליך רישום מורכב
- ❌ מוגבל לדפי עסקים ציבוריים

### 📝 הגדרה צעד אחר צעד:

#### שלב 1: יצירת אפליקציה
```
1. גש ל-https://developers.facebook.com
2. לחץ על "My Apps" → "Create App"
3. בחר "Business" כסוג האפליקציה
4. מלא פרטים:
   - App Name: "AI Posts Scraper"
   - App Contact Email: המייל שלך
   - Business Account: צור חשבון עסקי אם אין
```

#### שלב 2: קבלת Access Token
```
1. בתפריט צד, לחץ "Tools" → "Graph API Explorer"
2. בחר את האפליקציה שלך
3. לחץ "Generate Access Token"
4. בקש הרשאות:
   ✅ pages_read_engagement
   ✅ pages_read_user_content
   ✅ public_profile
```

#### שלב 3: הפיכת Token לקבוע
```bash
# Token זמני פג תוקף אחרי שעה. להפוך לקבוע:
curl -X GET "https://graph.facebook.com/v18.0/oauth/access_token" \
  -d "grant_type=fb_exchange_token" \
  -d "client_id=YOUR_APP_ID" \
  -d "client_secret=YOUR_APP_SECRET" \
  -d "fb_exchange_token=YOUR_SHORT_LIVED_TOKEN"
```

#### שלב 4: קבלת Page Access Token
```bash
# אם אתה בעל הדף:
curl -X GET "https://graph.facebook.com/v18.0/me/accounts" \
  -d "access_token=YOUR_USER_ACCESS_TOKEN"

# תקבל רשימת דפים. שמור את page_access_token
```

#### שלב 5: בדיקה
```bash
# בדוק שהכל עובד:
curl -X GET "https://graph.facebook.com/v18.0/PAGE_ID/posts" \
  -d "access_token=PAGE_ACCESS_TOKEN" \
  -d "fields=id,message,created_time" \
  -d "limit=5"
```

#### שלב 6: הגדרה בקוד
ערוך את `scraper_config.json`:
```json
{
  "facebook": {
    "app_id": "YOUR_APP_ID",
    "app_secret": "YOUR_APP_SECRET",
    "access_token": "YOUR_PAGE_ACCESS_TOKEN",
    "api_version": "v18.0"
  }
}
```

#### שימוש:
```python
from multi_platform_scraper import SocialMediaScraper

scraper = SocialMediaScraper('facebook', method='api')
posts = scraper.scrape_posts(
    page_url='https://facebook.com/YourPage',
    max_posts=None,  # כל הפוסטים
    start_date='2024-01-01',
    end_date='2026-03-11'
)
scraper.save_to_json('facebook_posts.json')
```

---

## 💼 שיטה 2: LinkedIn API

### יתרונות:
- ✅ רשמי ויציב
- ✅ גישה לפוסטים אישיים וארגוניים
- ✅ חינמי

### חסרונות:
- ❌ דורש אישור מ-LinkedIn
- ❌ תהליך רישום ארוך
- ❌ מוגבל ל-50 פוסטים לבקשה

### 📝 הגדרה:

#### שלב 1: יצירת אפליקציה
```
1. גש ל-https://www.linkedin.com/developers
2. לחץ "Create App"
3. מלא פרטים:
   - App name: "AI Posts Scraper"
   - LinkedIn Page: צור/בחר דף
   - Privacy policy URL: הכן מדיניות פרטיות
   - App logo: העלה לוגו
```

#### שלב 2: הגדרת Scopes
```
1. בלשונית "Auth", אשר redirect URL
2. בקש הרשאות (Products):
   ✅ Sign In with LinkedIn
   ✅ Share on LinkedIn
   ✅ Marketing Developer Platform (אם זמין)
```

#### שלב 3: OAuth 2.0 Flow
```python
# צריך לממש OAuth flow להשגת access token
# הנה דוגמה פשוטה:

import requests

# Step 1: Get authorization code
auth_url = f"https://www.linkedin.com/oauth/v2/authorization"
params = {
    'response_type': 'code',
    'client_id': 'YOUR_CLIENT_ID',
    'redirect_uri': 'http://localhost:8000/callback',
    'scope': 'r_liteprofile r_emailaddress w_member_social'
}
# פתח בדפדפן: auth_url + params

# Step 2: Exchange code for token
token_url = "https://www.linkedin.com/oauth/v2/accessToken"
data = {
    'grant_type': 'authorization_code',
    'code': 'CODE_FROM_CALLBACK',
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET',
    'redirect_uri': 'http://localhost:8000/callback'
}
response = requests.post(token_url, data=data)
access_token = response.json()['access_token']
```

#### שלב 4: הגדרה בקוד
```json
{
  "linkedin": {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN"
  }
}
```

---

## 🐦 שיטה 3: Twitter API v2

### יתרונות:
- ✅ **יש גרסה חינמית!**
- ✅ קל יחסית להגדרה
- ✅ תיעוד מצוין
- ✅ עד 10,000 tweets/חודש (Free tier)

### חסרונות:
- ❌ גרסה חינמית מוגבלת
- ❌ Basic tier: $100/חודש ל-50,000 tweets

### 📝 הגדרה (הכי קלה!):

#### שלב 1: יצירת Developer Account
```
1. גש ל-https://developer.twitter.com
2. לחץ "Sign up for Free Account"
3. מלא את הטופס (מטרת השימוש, תיאור)
4. אשר מייל
```

#### שלב 2: יצירת Project & App
```
1. לחץ "Create Project"
2. שם: "AI Posts Scraper"
3. Use case: "Exploring the API"
4. Project description: "Collecting social media posts"
5. יצירת App בתוך הפרויקט
```

#### שלב 3: קבלת Keys
```
אחרי יצירת App, תקבל:
- API Key
- API Secret Key
- Bearer Token ⭐ (זה מה שאתה צריך!)
- Access Token
- Access Token Secret

💾 שמור את כולם במקום בטוח!
```

#### שלב 4: הגדרה בקוד
```json
{
  "twitter": {
    "api_key": "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
    "bearer_token": "YOUR_BEARER_TOKEN",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
  }
}
```

#### שימוש:
```python
scraper = SocialMediaScraper('twitter', method='api')
posts = scraper.scrape_posts(
    page_url='https://twitter.com/elonmusk',
    max_posts=100,
    start_date='2024-01-01'
)
```

#### מגבלות Free Tier:
- ✅ 10,000 tweets/חודש
- ✅ 1 App
- ✅ גישה בסיסית ל-API v2
- ❌ ללא גישה להיסטוריה מלאה

---

## 🔧 שיטה 4: Apify (מומלץ!)

### יתרונות:
- ✅ **עובד מיד ללא אישורים!**
- ✅ תומך בכל הפלטפורמות
- ✅ פשוט להגדרה
- ✅ טיפול אוטומטי בחסימות
- ✅ יש תוכנית חינמית

### חסרונות:
- ❌ תוכנית חינמית מוגבלת ($5 קרדיט)
- ❌ מחיר: $49/חודש לשימוש רציני

### 📝 הגדרה (הכי מהירה!):

#### שלב 1: הרשמה
```
1. גש ל-https://apify.com
2. הרשם (יש גרסה חינמית!)
3. קבל $5 קרדיט חינם
```

#### שלב 2: קבלת API Token
```
1. לחץ על הפרופיל שלך
2. Settings → Integrations
3. לחץ "Create API Token"
4. שם: "Posts Scraper"
5. העתק את ה-Token
```

#### שלב 3: הגדרה בקוד
```json
{
  "apify": {
    "api_token": "YOUR_APIFY_TOKEN"
  }
}
```

#### שימוש:
```python
# Facebook
scraper = SocialMediaScraper('facebook', method='third_party')
posts = scraper.scrape_posts(
    page_url='https://facebook.com/YourPage',
    max_posts=500
)

# LinkedIn
scraper = SocialMediaScraper('linkedin', method='third_party')
posts = scraper.scrape_posts(
    page_url='https://linkedin.com/in/profile',
    max_posts=200
)

# Twitter
scraper = SocialMediaScraper('twitter', method='third_party')
posts = scraper.scrape_posts(
    page_url='https://twitter.com/username',
    max_posts=1000
)
```

#### מחירון Apify:
- 🆓 **Free**: $5 קרדיט (כ-500-1000 פוסטים)
- 💰 **Starter**: $49/חודש
- 💎 **Team**: $499/חודש

---

## 🌐 שיטה 5: Web Scraping

### ⚠️ לא מומלץ!

Web scraping ישיר קשה מאוד כי:
- ❌ פייסבוק/לינקדין/טוויטר חוסמים bots
- ❌ צריך Selenium/Playwright (כבד)
- ❌ צריך לפתור CAPTCHA
- ❌ צריך IP rotation
- ❌ תוכן דינמי (JavaScript)
- ❌ מבנה משתנה כל הזמן

**המלצה: השתמש ב-API או Apify במקום!**

---

## 📊 השוואה בין השיטות

| שיטה | פלטפורמות | עלות | קלות הגדרה | מהירות | אמינות |
|------|-----------|------|-----------|--------|---------|
| **Facebook API** | Facebook | חינם | 🟡 בינוני | 🟢 מהיר | 🟢 גבוהה |
| **LinkedIn API** | LinkedIn | חינם | 🔴 קשה | 🟢 מהיר | 🟢 גבוהה |
| **Twitter API** | Twitter | חינם/משלם | 🟢 קל | 🟢 מהיר | 🟢 גבוהה |
| **Apify** | הכל | $5-$49 | 🟢 מאוד קל | 🟢 מהיר | 🟢 גבוהה |
| **Web Scraping** | הכל | חינם | 🔴 מאוד קשה | 🔴 איטי | 🔴 נמוכה |

---

## 🚀 המלצות לפי מקרה שימוש

### אם אתה מתחיל:
1. **Twitter API** (הכי קל!) - $0
2. **Apify** ($5 חינם) - מהיר ופשוט
3. **Facebook API** - אם מוכן לחכות לאישור

### אם אתה רוצה כל הפלטפורמות:
1. **Apify** - פתרון all-in-one ($49/חודש)
2. או: Twitter API + Facebook API + Apify לLinkedIn

### אם אתה רוצה חינם לגמרי:
1. Twitter API (10K tweets/חודש)
2. Facebook API (אחרי אישור)
3. העתקה ידנית עם הכלי שבניתי

---

## 💡 טיפים חשובים

### 1. שמור על Rate Limits
```python
# הוסף המתנות בין בקשות
import time
time.sleep(1)  # 1 שנייה בין בקשות
```

### 2. טיפול בשגיאות
```python
try:
    posts = scraper.scrape_posts(url, max_posts=100)
except Exception as e:
    print(f"Error: {e}")
    # נסה שיטה אחרת
```

### 3. גיבוי תכוף
```python
# שמור כל 100 פוסטים
if len(posts) % 100 == 0:
    scraper.save_to_json(f'backup_{len(posts)}.json')
```

### 4. שימוש ב-Auto Mode
```python
# תנסה את כל השיטות אוטומטית
scraper = SocialMediaScraper('facebook', method='auto')
posts = scraper.scrape_posts(url)
```

---

## 🎯 תוכנית פעולה מומלצת

### שבוע 1: התחלה
```
יום 1: הרשם ל-Twitter Developer (5 דקות)
יום 2: קבל Bearer Token ובדוק (10 דקות)
יום 3: שלוף 100 tweets ראשונים (5 דקות)
יום 4-5: הרשם ל-Apify ונסה (30 דקות)
```

### שבוע 2: הרחבה
```
יום 1-2: הגש בקשה ל-Facebook API
יום 3-5: חכה לאישור
יום 6-7: בדוק Facebook API
```

### שבוע 3: ייעול
```
- בנה אוטומציה מלאה
- הוסף תזמון יומי
- בנה דשבורד לניטור
```

---

## 📞 עזרה ותמיכה

יש בעיות? קרה תקלה?
- 📧 support@aviel.ai
- 💬 פתח Issue ב-GitHub
- 📖 תיעוד מלא: docs.apify.com

---

**נוצר ב-🤖 Claude & 💼 AVIEL.AI**
