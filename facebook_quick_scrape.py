#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Facebook Quick Scraper - Ready to use!
Just edit config and run
"""

from multi_platform_scraper import SocialMediaScraper
import sys
from pathlib import Path

def scrape_facebook_simple():
    """Simplest Facebook scraping"""
    
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 20 + "📘 FACEBOOK QUICK SCRAPER" + " " * 23 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # קלט מהמשתמש
    print("📝 Facebook Page Details:")
    page_url = input("   Page URL (e.g., https://facebook.com/page): ").strip()
    
    if not page_url:
        print("❌ URL is required!")
        return
    
    print()
    max_input = input("   How many posts? (press Enter for all): ").strip()
    max_posts = int(max_input) if max_input else None
    
    print()
    print("🔧 Choose scraping method:")
    print()
    print("   1️⃣  Apify (Recommended - works immediately)")
    print("       ✅ 5 minutes setup")
    print("       ✅ $5 free credit")
    print("       ✅ ~500-1000 posts free")
    print()
    print("   2️⃣  Facebook Graph API (Free forever)")
    print("       ⏳ Requires approval (3-7 days)")
    print("       ✅ Unlimited posts")
    print("       ✅ Full data access")
    print()
    print("   3️⃣  Auto (Try all methods)")
    print("       🔄 Tries Apify → API → Scraping")
    print()
    
    choice = input("👉 Your choice (1/2/3): ").strip()
    
    method_map = {
        '1': 'third_party',
        '2': 'api',
        '3': 'auto'
    }
    
    method = method_map.get(choice, 'auto')
    method_names = {
        'third_party': 'Apify',
        'api': 'Facebook Graph API',
        'auto': 'Auto (all methods)'
    }
    
    print()
    print("=" * 70)
    print(f"🚀 Starting scrape with: {method_names[method]}")
    print("=" * 70)
    print()
    
    try:
        # צור scraper
        scraper = SocialMediaScraper('facebook', method=method)
        
        # הצג התקדמות
        if method == 'third_party':
            print("📡 Connecting to Apify...")
            print("⏳ This may take a few minutes...")
        elif method == 'api':
            print("📡 Connecting to Facebook Graph API...")
        else:
            print("🔄 Trying all available methods...")
        
        print()
        
        # שלוף פוסטים
        posts = scraper.scrape_posts(
            page_url=page_url,
            max_posts=max_posts
        )
        
        if not posts:
            print("⚠️  No posts found!")
            print()
            print("💡 Possible reasons:")
            print("   • Page is private")
            print("   • Wrong URL")
            print("   • API credentials not configured")
            print("   • Page has no posts")
            return
        
        # שמור לקובץ
        output_file = scraper.save_to_json()
        
        # הצלחה!
        print()
        print("╔" + "=" * 68 + "╗")
        print("║" + " " * 28 + "✅ SUCCESS!" + " " * 29 + "║")
        print("╚" + "=" * 68 + "╝")
        print()
        print(f"📊 Scraped posts: {len(posts)}")
        print(f"💾 Saved to: {output_file}")
        print()
        
        # הצג סטטיסטיקות
        print("📈 Statistics:")
        
        # ספור פוסטים עם קישורים/תמונות
        with_links = sum(1 for p in posts if p.get('links'))
        with_images = sum(1 for p in posts if p.get('images'))
        
        print(f"   • Posts with links: {with_links}")
        print(f"   • Posts with images: {with_images}")
        
        if posts and posts[0].get('likes') is not None:
            total_likes = sum(p.get('likes', 0) for p in posts)
            print(f"   • Total likes: {total_likes:,}")
        
        # הצג דוגמה
        print()
        print("📄 Sample post:")
        sample = posts[0]
        print(f"   Date: {sample.get('date', 'N/A')}")
        print(f"   Text: {sample.get('text', 'No text')[:150]}...")
        if sample.get('url'):
            print(f"   URL: {sample['url']}")
        
        print()
        print("=" * 70)
        print("💡 Next steps:")
        print("   1. Open the JSON file to see all posts")
        print("   2. Run: python load_posts.py " + output_file)
        print("   3. Get HTML/Excel/Markdown outputs!")
        print("=" * 70)
        
    except ValueError as e:
        # בעיית הגדרה
        print(f"❌ Configuration Error: {e}")
        print()
        print("💡 Fix:")
        
        if 'access token' in str(e).lower():
            print()
            print("📘 Facebook API Setup:")
            print("   1. Go to: https://developers.facebook.com")
            print("   2. Create an App")
            print("   3. Get Access Token")
            print("   4. Add to scraper_config.json")
            print()
            print("📖 See FACEBOOK_QUICK_START.md for detailed guide")
            
        elif 'apify' in str(e).lower():
            print()
            print("🔧 Apify Setup:")
            print("   1. Sign up: https://apify.com/sign-up")
            print("   2. Get API token: Settings → Integrations")
            print("   3. Add to scraper_config.json:")
            print('      "apify": {"api_token": "apify_api_YOUR_TOKEN"}')
            print()
            print("📖 See FACEBOOK_QUICK_START.md for detailed guide")
        
    except Exception as e:
        # שגיאה כללית
        print(f"❌ Error: {e}")
        print()
        print("💡 Troubleshooting:")
        print("   1. Check your internet connection")
        print("   2. Verify the Facebook page URL is correct")
        print("   3. Make sure scraper_config.json exists")
        print("   4. Check API credentials in config file")
        print()
        print("📖 Full documentation: AUTOMATION_GUIDE.md")


def check_config():
    """Check if config file exists and has required fields"""
    
    config_file = Path('scraper_config.json')
    
    if not config_file.exists():
        print("⚠️  scraper_config.json not found!")
        print()
        print("Creating default config file...")
        
        # הרץ את המנוע כדי ליצור config
        from multi_platform_scraper import SocialMediaScraper
        temp = SocialMediaScraper('facebook')
        
        print("✅ Created scraper_config.json")
        print()
        print("📝 Please edit the file and add your API credentials:")
        print("   • For Apify: Get token from apify.com")
        print("   • For Facebook API: See FACEBOOK_QUICK_START.md")
        print()
        return False
    
    # בדוק אם יש credentials
    import json
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    has_apify = bool(config.get('apify', {}).get('api_token'))
    has_facebook = bool(config.get('facebook', {}).get('access_token'))
    
    if not has_apify and not has_facebook:
        print("⚠️  No API credentials found in scraper_config.json")
        print()
        print("💡 You need at least one of:")
        print("   • Apify API token (recommended for quick start)")
        print("   • Facebook access token (free but needs setup)")
        print()
        print("📖 See FACEBOOK_QUICK_START.md for setup guides")
        print()
        
        proceed = input("Continue anyway? (y/n): ").strip().lower()
        return proceed == 'y'
    
    return True


def main():
    """Main entry point"""
    
    print()
    
    # בדוק הגדרות
    if not check_config():
        print()
        print("👋 Setup your credentials and run again!")
        return
    
    print()
    
    # הרץ scraper
    scrape_facebook_simple()
    
    print()


if __name__ == "__main__":
    main()
