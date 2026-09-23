#!/usr/bin/env python3
import os
import re
import shutil
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    print("=== Applying branding overlay for Listen to Sadhu ===")

    # 1. Android native string resources
    android_src = os.path.join(repo_root, "branding", "android", "res")
    android_dst = os.path.join(repo_root, "shruti", "modules", "apps", "mobile", "android", "app", "src", "main", "res")
    if os.path.exists(android_src) and os.path.exists(android_dst):
        print("Applying Android resources...")
        shutil.copytree(android_src, android_dst, dirs_exist_ok=True)

    # 2. iOS native string resources
    ios_src = os.path.join(repo_root, "branding", "ios")
    ios_dst = os.path.join(repo_root, "shruti", "modules", "apps", "mobile", "ios", "App", "App")
    if os.path.exists(ios_src) and os.path.exists(ios_dst):
        print("Applying iOS resources...")
        shutil.copytree(ios_src, ios_dst, dirs_exist_ok=True)

    # 3. i18n locale brand names
    locales_dir = os.path.join(repo_root, "shruti", "modules", "apps", "mobile", "shruti", "i18n", "locales")
    if os.path.exists(locales_dir):
        print("Applying i18n brand names...")
        brand_names = {
            "ru": "Слушай Садху",
            "uk": "Слухай Садху",
            "sr-Cyrl": "Слушај Садхуа",
            "sr-Latn": "Slušaj Sadhu",
            "en": "Listen to Sadhu",
            "de": "Listen to Sadhu",
            "es": "Listen to Sadhu",
            "fr": "Listen to Sadhu",
            "it": "Listen to Sadhu",
            "pl": "Listen to Sadhu",
            "pt": "Listen to Sadhu",
            "hu": "Listen to Sadhu",
            "hi": "Listen to Sadhu",
            "bn": "Listen to Sadhu",
        }
        for lang, brand_name in brand_names.items():
            app_ts_path = os.path.join(locales_dir, lang, "app.ts")
            if os.path.exists(app_ts_path):
                with open(app_ts_path, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content = re.sub(r'(\bname:\s*["\'`])[^"\'`]+(["\'`])', rf'\g<1>{brand_name}\g<2>', content)
                with open(app_ts_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Set app.name for {lang} -> {brand_name}")

    print("=== Branding overlay applied successfully ===")

if __name__ == "__main__":
    main()
