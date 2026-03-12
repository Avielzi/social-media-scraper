#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Start Example - Social Media Scraper
Simple examples for each platform
"""

from multi_platform_scraper import SocialMediaScraper
from pathlib import Path

def example_twitter():
    """Example: Scrape tweets - EASIEST TO START!"""
    print("=" * 70)
    print("🐦 TWITTER EXAMPLE - Recommended for beginners!")
    print("=" * 70)
    print()
    
    # Create scraper
    scraper = SocialMediaScraper('twitter', method='api')
    
    # Scrape tweets
    print("📥 Scraping tweets from @elonmusk (example)")
    print("💡 Replace with any public Twitter account")
    print()
    
    try:
        posts = scraper.scrape_posts(
            page_url='https://twitter.com/elonmusk',
            max_posts=10,  # Start small
            start_date='2024-01-01'
        )
        
        # Save to JSON
        output_file = scraper.save_to_json('twitter_example.json')
        
        print()
        print(f"✅ Success! Saved {len(posts)} tweets")
        print(f"📁 File: {output_file}")
        
        # Show sample
        if posts:
            print()
            print("📄 Sample tweet:")
            print(f"   Date: {posts[0]['date']}")
            print(f"   Text: {posts[0]['text'][:100]}...")
            print(f"   URL: {posts[0]['url']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("💡 Make sure you:")
        print("   1. Edited scraper_config.json")
        print("   2. Added your Twitter Bearer Token")
        print("   3. See AUTOMATION_GUIDE.md for help")


def example_facebook():
    """Example: Scrape Facebook page"""
    print()
    print("=" * 70)
    print("📘 FACEBOOK EXAMPLE")
    print("=" * 70)
    print()
    
    scraper = SocialMediaScraper('facebook', method='api')
    
    try:
        posts = scraper.scrape_posts(
            page_url='https://facebook.com/YourPageName',  # Replace!
            max_posts=50,
            start_date='2024-01-01',
            end_date='2026-03-11'
        )
        
        output_file = scraper.save_to_json('facebook_example.json')
        
        print(f"✅ Success! Saved {len(posts)} posts")
        print(f"📁 File: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("💡 Make sure you:")
        print("   1. Completed Facebook App setup")
        print("   2. Got Page Access Token")
        print("   3. Added token to scraper_config.json")


def example_linkedin():
    """Example: Scrape LinkedIn posts"""
    print()
    print("=" * 70)
    print("💼 LINKEDIN EXAMPLE")
    print("=" * 70)
    print()
    
    scraper = SocialMediaScraper('linkedin', method='api')
    
    try:
        posts = scraper.scrape_posts(
            page_url='https://linkedin.com/in/username',  # Replace!
            max_posts=30
        )
        
        output_file = scraper.save_to_json('linkedin_example.json')
        
        print(f"✅ Success! Saved {len(posts)} posts")
        print(f"📁 File: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("💡 LinkedIn API requires OAuth flow")
        print("   See AUTOMATION_GUIDE.md for complete setup")


def example_apify():
    """Example: Use Apify for any platform"""
    print()
    print("=" * 70)
    print("🔧 APIFY EXAMPLE - Works for ALL platforms!")
    print("=" * 70)
    print()
    
    # Choose platform
    platform = 'facebook'  # or 'linkedin', 'twitter'
    
    scraper = SocialMediaScraper(platform, method='third_party')
    
    print(f"📥 Scraping {platform} with Apify")
    print("⏳ This may take a few minutes...")
    print()
    
    try:
        posts = scraper.scrape_posts(
            page_url='https://facebook.com/YourPage',  # Replace!
            max_posts=100
        )
        
        output_file = scraper.save_to_json(f'{platform}_apify.json')
        
        print(f"✅ Success! Saved {len(posts)} posts")
        print(f"📁 File: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("💡 Make sure you:")
        print("   1. Signed up at apify.com")
        print("   2. Got API token")
        print("   3. Added to scraper_config.json")


def example_batch_scraping():
    """Example: Scrape multiple pages/accounts"""
    print()
    print("=" * 70)
    print("📦 BATCH SCRAPING EXAMPLE")
    print("=" * 70)
    print()
    
    # List of accounts to scrape
    accounts = [
        {'platform': 'twitter', 'url': 'https://twitter.com/elonmusk'},
        {'platform': 'twitter', 'url': 'https://twitter.com/BillGates'},
        {'platform': 'facebook', 'url': 'https://facebook.com/page1'},
        {'platform': 'facebook', 'url': 'https://facebook.com/page2'},
    ]
    
    all_posts = []
    
    for account in accounts:
        print(f"📥 Scraping: {account['url']}")
        
        try:
            scraper = SocialMediaScraper(account['platform'], method='auto')
            posts = scraper.scrape_posts(
                page_url=account['url'],
                max_posts=50
            )
            
            all_posts.extend(posts)
            print(f"   ✅ Got {len(posts)} posts")
            
        except Exception as e:
            print(f"   ❌ Failed: {e}")
        
        print()
    
    # Save all together
    import json
    with open('batch_all_posts.json', 'w', encoding='utf-8') as f:
        json.dump(all_posts, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Total: {len(all_posts)} posts from {len(accounts)} accounts")
    print(f"📁 File: batch_all_posts.json")


def example_incremental_scraping():
    """Example: Scrape in batches to avoid limits"""
    print()
    print("=" * 70)
    print("🔄 INCREMENTAL SCRAPING - For large archives")
    print("=" * 70)
    print()
    
    scraper = SocialMediaScraper('twitter', method='api')
    
    # Scrape in batches
    batch_size = 100
    total_wanted = 1000
    all_posts = []
    
    print(f"📥 Scraping {total_wanted} posts in batches of {batch_size}")
    print()
    
    for batch_num in range(0, total_wanted, batch_size):
        print(f"🔄 Batch {batch_num//batch_size + 1}")
        
        try:
            posts = scraper.scrape_posts(
                page_url='https://twitter.com/username',
                max_posts=batch_size
            )
            
            all_posts.extend(posts)
            
            # Save intermediate results
            import json
            with open(f'batch_{batch_num}.json', 'w', encoding='utf-8') as f:
                json.dump(all_posts, f, ensure_ascii=False, indent=2)
            
            print(f"   ✅ Total so far: {len(all_posts)}")
            
            # Stop if we got less than batch size (reached the end)
            if len(posts) < batch_size:
                print("   📍 Reached end of posts")
                break
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            break
    
    print()
    print(f"✅ Complete! Total posts: {len(all_posts)}")


def main():
    """Run examples"""
    print()
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "🚀 SOCIAL MEDIA SCRAPER EXAMPLES" + " " * 21 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    print("Choose an example to run:")
    print()
    print("1️⃣  Twitter (RECOMMENDED for beginners)")
    print("2️⃣  Facebook")
    print("3️⃣  LinkedIn")
    print("4️⃣  Apify (any platform)")
    print("5️⃣  Batch scraping (multiple accounts)")
    print("6️⃣  Incremental scraping (large archives)")
    print("0️⃣  Exit")
    print()
    
    choice = input("👉 Your choice: ").strip()
    
    if choice == '1':
        example_twitter()
    elif choice == '2':
        example_facebook()
    elif choice == '3':
        example_linkedin()
    elif choice == '4':
        example_apify()
    elif choice == '5':
        example_batch_scraping()
    elif choice == '6':
        example_incremental_scraping()
    elif choice == '0':
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice")
    
    print()
    print("=" * 70)
    print("📖 For detailed setup, see: AUTOMATION_GUIDE.md")
    print("🔧 Config file: scraper_config.json")
    print("=" * 70)


if __name__ == "__main__":
    main()
