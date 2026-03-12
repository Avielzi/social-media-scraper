#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load Posts - Quick loading and formatting of scraped posts.
"""

import json
import sys
from pathlib import Path

def load_and_display(filename: str):
    """Load posts from a JSON file and display them in a readable format."""
    file_path = Path(filename)
    
    if not file_path.exists():
        print(f"❌ Error: File {filename} not found!")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            posts = json.load(f)
        
        print(f"📊 Loaded {len(posts)} posts from {filename}")
        print("-" * 50)
        
        for i, post in enumerate(posts[:5], 1):
            print(f"Post #{i}:")
            print(f"   Date: {post.get('date', 'N/A')}")
            print(f"   Text: {post.get('text', 'No text')[:100]}...")
            print(f"   URL: {post.get('url', 'N/A')}")
            print("-" * 50)
            
        if len(posts) > 5:
            print(f"... and {len(posts) - 5} more posts.")
            
    except Exception as e:
        print(f"❌ Error loading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python load_posts.py <filename.json>")
    else:
        load_and_display(sys.argv[1])
