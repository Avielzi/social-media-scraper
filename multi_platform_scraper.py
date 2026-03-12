#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Platform Social Media Scraper
Supports: Facebook, LinkedIn, Twitter/X
Methods: Graph API, Web Scraping, Third-party APIs
"""

import json
import os
import requests
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path
import time

class SocialMediaScraper:
    """Universal scraper supporting multiple platforms and methods"""
    
    def __init__(self, platform: str, method: str = "auto"):
        """
        Initialize scraper
        
        Args:
            platform: 'facebook', 'linkedin', 'twitter'
            method: 'api', 'scraping', 'third_party', or 'auto'
        """
        self.platform = platform.lower()
        self.method = method
        self.posts = []
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """Load API keys and configuration"""
        config_file = Path('scraper_config.json')
        
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default config
            default_config = {
                "facebook": {
                    "app_id": "",
                    "app_secret": "",
                    "access_token": "",
                    "api_version": "v18.0"
                },
                "linkedin": {
                    "client_id": "",
                    "client_secret": "",
                    "access_token": ""
                },
                "twitter": {
                    "api_key": "",
                    "api_secret": "",
                    "bearer_token": "",
                    "access_token": "",
                    "access_token_secret": ""
                },
                "apify": {
                    "api_token": ""
                },
                "scraping": {
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "timeout": 30,
                    "retry_attempts": 3
                }
            }
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2)
            
            print(f"✅ Created config file: {config_file}")
            print(f"📝 Please fill in your API credentials")
            
            return default_config
    
    def scrape_posts(self, page_url: str, max_posts: int = None, 
                    start_date: str = None, end_date: str = None) -> List[Dict]:
        """
        Main scraping method - automatically chooses best approach
        
        Args:
            page_url: URL of the page/profile to scrape
            max_posts: Maximum number of posts (None = all)
            start_date: Filter posts from this date (YYYY-MM-DD)
            end_date: Filter posts until this date (YYYY-MM-DD)
        """
        print(f"🚀 Starting scrape: {self.platform}")
        print(f"📍 URL: {page_url}")
        print(f"📊 Max posts: {max_posts or 'All'}")
        
        if self.method == "auto":
            # Try methods in order of reliability
            methods = ['api', 'third_party', 'scraping']
        else:
            methods = [self.method]
        
        for method in methods:
            try:
                print(f"\n🔧 Trying method: {method}")
                
                if method == "api":
                    return self._scrape_via_api(page_url, max_posts, start_date, end_date)
                elif method == "third_party":
                    return self._scrape_via_third_party(page_url, max_posts)
                elif method == "scraping":
                    return self._scrape_via_web(page_url, max_posts)
                    
            except Exception as e:
                print(f"⚠️  Method {method} failed: {e}")
                continue
        
        print("❌ All methods failed!")
        return []
    
    def _scrape_via_api(self, page_url: str, max_posts: int, 
                        start_date: str, end_date: str) -> List[Dict]:
        """Scrape using official APIs"""
        
        if self.platform == "facebook":
            return self._facebook_api_scrape(page_url, max_posts, start_date, end_date)
        elif self.platform == "linkedin":
            return self._linkedin_api_scrape(page_url, max_posts)
        elif self.platform == "twitter":
            return self._twitter_api_scrape(page_url, max_posts, start_date, end_date)
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
    
    def _facebook_api_scrape(self, page_url: str, max_posts: int,
                            start_date: str, end_date: str) -> List[Dict]:
        """Scrape Facebook using Graph API"""
        
        config = self.config.get('facebook', {})
        access_token = config.get('access_token')
        
        if not access_token:
            raise ValueError("Facebook access token not configured")
        
        # Extract page ID from URL
        page_id = self._extract_facebook_page_id(page_url)
        
        api_version = config.get('api_version', 'v18.0')
        base_url = f"https://graph.facebook.com/{api_version}/{page_id}/posts"
        
        params = {
            'access_token': access_token,
            'fields': 'id,message,created_time,permalink_url,attachments{media,url},likes.summary(true),comments.summary(true)',
            'limit': min(max_posts or 100, 100)  # Max 100 per request
        }
        
        if start_date:
            params['since'] = start_date
        if end_date:
            params['until'] = end_date
        
        all_posts = []
        next_url = base_url
        
        while next_url and (max_posts is None or len(all_posts) < max_posts):
            print(f"📥 Fetching batch... (current: {len(all_posts)})")
            
            response = requests.get(next_url, params=params if next_url == base_url else {})
            response.raise_for_status()
            
            data = response.json()
            posts = data.get('data', [])
            
            for post in posts:
                formatted_post = {
                    'id': post.get('id'),
                    'date': self._format_date(post.get('created_time')),
                    'text': post.get('message', ''),
                    'url': post.get('permalink_url', ''),
                    'likes': post.get('likes', {}).get('summary', {}).get('total_count', 0),
                    'comments': post.get('comments', {}).get('summary', {}).get('total_count', 0),
                    'images': self._extract_fb_images(post.get('attachments', {})),
                    'platform': 'facebook'
                }
                all_posts.append(formatted_post)
                
                if max_posts and len(all_posts) >= max_posts:
                    break
            
            # Get next page
            next_url = data.get('paging', {}).get('next')
            
            # Reset params for pagination
            params = {}
            
            # Rate limiting
            time.sleep(0.5)
        
        print(f"✅ Fetched {len(all_posts)} Facebook posts")
        self.posts = all_posts
        return all_posts
    
    def _linkedin_api_scrape(self, page_url: str, max_posts: int) -> List[Dict]:
        """Scrape LinkedIn using API"""
        
        config = self.config.get('linkedin', {})
        access_token = config.get('access_token')
        
        if not access_token:
            raise ValueError("LinkedIn access token not configured")
        
        # LinkedIn API endpoint
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        # Extract organization/person URN from URL
        urn = self._extract_linkedin_urn(page_url)
        
        url = f"https://api.linkedin.com/v2/ugcPosts"
        params = {
            'q': 'authors',
            'authors': f'List({urn})',
            'count': min(max_posts or 50, 50)
        }
        
        all_posts = []
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        posts = data.get('elements', [])
        
        for post in posts:
            formatted_post = {
                'id': post.get('id'),
                'date': self._format_date_from_timestamp(post.get('created', {}).get('time')),
                'text': post.get('specificContent', {}).get('com.linkedin.ugc.ShareContent', {}).get('shareCommentary', {}).get('text', ''),
                'url': f"https://www.linkedin.com/feed/update/{post.get('id')}",
                'platform': 'linkedin'
            }
            all_posts.append(formatted_post)
        
        print(f"✅ Fetched {len(all_posts)} LinkedIn posts")
        self.posts = all_posts
        return all_posts
    
    def _twitter_api_scrape(self, page_url: str, max_posts: int,
                           start_date: str, end_date: str) -> List[Dict]:
        """Scrape Twitter using API v2"""
        
        config = self.config.get('twitter', {})
        bearer_token = config.get('bearer_token')
        
        if not bearer_token:
            raise ValueError("Twitter bearer token not configured")
        
        # Extract username
        username = self._extract_twitter_username(page_url)
        
        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }
        
        # First, get user ID
        user_url = f"https://api.twitter.com/2/users/by/username/{username}"
        user_response = requests.get(user_url, headers=headers)
        user_response.raise_for_status()
        user_id = user_response.json()['data']['id']
        
        # Get tweets
        tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        params = {
            'max_results': min(max_posts or 100, 100),
            'tweet.fields': 'created_at,public_metrics,attachments',
            'expansions': 'attachments.media_keys',
            'media.fields': 'url'
        }
        
        if start_date:
            params['start_time'] = f"{start_date}T00:00:00Z"
        if end_date:
            params['end_time'] = f"{end_date}T23:59:59Z"
        
        all_posts = []
        next_token = None
        
        while max_posts is None or len(all_posts) < max_posts:
            if next_token:
                params['pagination_token'] = next_token
            
            print(f"📥 Fetching tweets... (current: {len(all_posts)})")
            
            response = requests.get(tweets_url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            tweets = data.get('data', [])
            
            for tweet in tweets:
                formatted_post = {
                    'id': tweet.get('id'),
                    'date': self._format_date(tweet.get('created_at')),
                    'text': tweet.get('text', ''),
                    'url': f"https://twitter.com/{username}/status/{tweet.get('id')}",
                    'likes': tweet.get('public_metrics', {}).get('like_count', 0),
                    'retweets': tweet.get('public_metrics', {}).get('retweet_count', 0),
                    'replies': tweet.get('public_metrics', {}).get('reply_count', 0),
                    'platform': 'twitter'
                }
                all_posts.append(formatted_post)
                
                if max_posts and len(all_posts) >= max_posts:
                    break
            
            next_token = data.get('meta', {}).get('next_token')
            if not next_token:
                break
            
            time.sleep(0.5)
        
        print(f"✅ Fetched {len(all_posts)} tweets")
        self.posts = all_posts
        return all_posts
    
    def _scrape_via_third_party(self, page_url: str, max_posts: int) -> List[Dict]:
        """Scrape using Apify or similar services"""
        
        config = self.config.get('apify', {})
        api_token = config.get('api_token')
        
        if not api_token:
            raise ValueError("Apify API token not configured")
        
        # Apify actor IDs for different platforms
        actors = {
            'facebook': 'apify/facebook-pages-scraper',
            'linkedin': 'apify/linkedin-posts-scraper',
            'twitter': 'apify/twitter-scraper'
        }
        
        actor_id = actors.get(self.platform)
        if not actor_id:
            raise ValueError(f"No Apify actor for {self.platform}")
        
        print(f"🔄 Using Apify actor: {actor_id}")
        
        # Start the actor
        run_url = f"https://api.apify.com/v2/acts/{actor_id}/runs"
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }
        
        input_data = {
            'startUrls': [{'url': page_url}],
            'maxPosts': max_posts or 1000
        }
        
        response = requests.post(run_url, headers=headers, json=input_data)
        response.raise_for_status()
        
        run_id = response.json()['data']['id']
        print(f"▶️  Run started: {run_id}")
        
        # Wait for completion
        status_url = f"https://api.apify.com/v2/acts/{actor_id}/runs/{run_id}"
        
        while True:
            status_response = requests.get(status_url, headers=headers)
            status_data = status_response.json()['data']
            status = status_data['status']
            
            print(f"⏳ Status: {status}")
            
            if status == 'SUCCEEDED':
                break
            elif status in ['FAILED', 'ABORTED', 'TIMED-OUT']:
                raise Exception(f"Apify run {status}")
            
            time.sleep(5)
        
        # Get results
        dataset_id = status_data['defaultDatasetId']
        results_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
        
        results_response = requests.get(results_url, headers=headers)
        results_response.raise_for_status()
        
        raw_posts = results_response.json()
        
        # Format posts
        formatted_posts = []
        for post in raw_posts:
            formatted_posts.append(self._format_third_party_post(post))
        
        print(f"✅ Fetched {len(formatted_posts)} posts via Apify")
        self.posts = formatted_posts
        return formatted_posts
    
    def _scrape_via_web(self, page_url: str, max_posts: int) -> List[Dict]:
        """Scrape using direct web scraping"""
        
        print("⚠️  Web scraping is limited due to anti-bot measures")
        print("💡 Recommendation: Use API or third-party service instead")
        
        # This is a placeholder - full implementation would need:
        # - Selenium/Playwright for JavaScript rendering
        # - Cookie/session management
        # - CAPTCHA solving
        # - IP rotation
        
        raise NotImplementedError(
            "Direct web scraping requires additional setup. "
            "Please use API or third-party methods instead."
        )
    
    # Helper methods
    
    def _extract_facebook_page_id(self, url: str) -> str:
        """Extract page ID from Facebook URL"""
        # Simplified - would need more robust parsing
        if '/pages/' in url:
            return url.split('/pages/')[1].split('/')[1]
        else:
            return url.rstrip('/').split('/')[-1]
    
    def _extract_linkedin_urn(self, url: str) -> str:
        """Extract URN from LinkedIn URL"""
        # Simplified extraction
        return url.rstrip('/').split('/')[-1]
    
    def _extract_twitter_username(self, url: str) -> str:
        """Extract username from Twitter URL"""
        return url.rstrip('/').split('/')[-1].replace('@', '')
    
    def _format_date(self, date_str: str) -> str:
        """Format ISO date to readable format"""
        if not date_str:
            return ""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%d/%m/%Y')
        except:
            return date_str
    
    def _format_date_from_timestamp(self, timestamp: int) -> str:
        """Format timestamp to readable date"""
        if not timestamp:
            return ""
        dt = datetime.fromtimestamp(timestamp / 1000)
        return dt.strftime('%d/%m/%Y')
    
    def _extract_fb_images(self, attachments: Dict) -> List[str]:
        """Extract image URLs from Facebook attachments"""
        images = []
        data = attachments.get('data', [])
        for item in data:
            media = item.get('media', {})
            if media.get('image'):
                images.append(media['image'].get('src', ''))
        return images
    
    def _format_third_party_post(self, post: Dict) -> Dict:
        """Format post from third-party scraper"""
        # Generic formatting - adjust based on actual response
        return {
            'date': post.get('date', ''),
            'text': post.get('text', ''),
            'url': post.get('url', ''),
            'platform': self.platform
        }
    
    def save_to_json(self, output_file: str = None):
        """Save posts to JSON file"""
        if not output_file:
            output_file = f"{self.platform}_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.posts, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Saved {len(self.posts)} posts to {output_file}")
        return output_file


def main():
    """Example usage"""
    print("=" * 70)
    print("🚀 Multi-Platform Social Media Scraper")
    print("=" * 70)
    print()
    
    # Example: Facebook scraping
    print("📘 Example: Facebook")
    fb_scraper = SocialMediaScraper('facebook', method='auto')
    
    # This will try API first, then fallback to other methods
    # posts = fb_scraper.scrape_posts(
    #     page_url='https://facebook.com/YourPage',
    #     max_posts=100
    # )
    
    print()
    print("💡 To use this scraper:")
    print("   1. Edit scraper_config.json with your API credentials")
    print("   2. Choose your platform: 'facebook', 'linkedin', 'twitter'")
    print("   3. Run: scraper.scrape_posts(page_url, max_posts)")
    print()
    print("📖 See AUTOMATION_GUIDE.md for detailed setup instructions")


if __name__ == "__main__":
    main()
