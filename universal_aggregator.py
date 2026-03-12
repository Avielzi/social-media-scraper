#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Aggregator - Dynamic content collector for any social media page.
"""

import json
from typing import List, Dict
from multi_platform_scraper import SocialMediaScraper

class UniversalAggregator:
    """Aggregates data from multiple platforms into a unified format."""
    
    def __init__(self):
        self.scrapers = {
            'facebook': SocialMediaScraper('facebook'),
            'linkedin': SocialMediaScraper('linkedin'),
            'twitter': SocialMediaScraper('twitter')
        }
        self.all_data = []

    def aggregate(self, platform: str, url: str, max_posts: int = 100) -> List[Dict]:
        """Scrape and aggregate data from a specific platform."""
        if platform not in self.scrapers:
            raise ValueError(f"Unsupported platform: {platform}")
            
        print(f"🌐 Aggregating data from {platform}: {url}")
        posts = self.scrapers[platform].scrape_posts(url, max_posts=max_posts)
        self.all_data.extend(posts)
        return posts

    def save_all(self, filename: str = "aggregated_posts.json"):
        """Save all aggregated data to a single JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved {len(self.all_data)} total posts to {filename}")

if __name__ == "__main__":
    # Example usage
    aggregator = UniversalAggregator()
    print("Universal Aggregator initialized.")
