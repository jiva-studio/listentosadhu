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
            lang_dir = os.path.join(locales_dir, lang)
            if not os.path.exists(lang_dir):
                continue

            # app.ts
            app_ts = os.path.join(lang_dir, "app.ts")
            if os.path.exists(app_ts):
                with open(app_ts, "r", encoding="utf-8") as f:
                    content = f.read()
                content = re.sub(r'(\bname:\s*["\'`])[^"\'`]+(["\'`])', rf'\g<1>{brand_name}\g<2>', content)
                with open(app_ts, "w", encoding="utf-8") as f:
                    f.write(content)

            # onboarding.ts
            onboarding_ts = os.path.join(lang_dir, "onboarding.ts")
            if os.path.exists(onboarding_ts):
                with open(onboarding_ts, "r", encoding="utf-8") as f:
                    content = f.read()
                content = re.sub(r'(\bappName:\s*["\'`])[^"\'`]+(["\'`])', rf'\g<1>{brand_name}\g<2>', content)
                with open(onboarding_ts, "w", encoding="utf-8") as f:
                    f.write(content)

            # settings.ts
            settings_ts = os.path.join(lang_dir, "settings.ts")
            if os.path.exists(settings_ts):
                with open(settings_ts, "r", encoding="utf-8") as f:
                    content = f.read()
                if lang == "ru":
                    content = content.replace("«Shruti»", f"«{brand_name}»")
                elif lang == "uk":
                    content = content.replace("«Shruti»", f"«{brand_name}»")
                elif lang in ("sr-Cyrl", "sr-Latn"):
                    content = content.replace("„Shruti“", f"„{brand_name}“")
                else:
                    content = content.replace('"Shruti"', f'"{brand_name}"').replace("'Shruti'", f"'{brand_name}'")
                with open(settings_ts, "w", encoding="utf-8") as f:
                    f.write(content)

            # home.ts
            home_ts = os.path.join(lang_dir, "home.ts")
            if os.path.exists(home_ts):
                with open(home_ts, "r", encoding="utf-8") as f:
                    content = f.read()
                if lang == "ru":
                    content = content.replace("«Shruti»", f"«{brand_name}»")
                elif lang == "uk":
                    content = content.replace("«Shruti»", f"«{brand_name}»")
                elif lang in ("sr-Cyrl", "sr-Latn"):
                    content = content.replace("Shruti", brand_name)
                else:
                    content = content.replace("Shruti", brand_name)
                with open(home_ts, "w", encoding="utf-8") as f:
                    f.write(content)

            # chat.ts
            chat_ts = os.path.join(lang_dir, "chat.ts")
            if os.path.exists(chat_ts):
                with open(chat_ts, "r", encoding="utf-8") as f:
                    content = f.read()
                if lang == "ru":
                    content = content.replace("«Shruti Pro»", f"«{brand_name} Pro»")
                    content = content.replace('"Shruti Pro"', f'"{brand_name} Pro"')
                    content = content.replace("Обновите Shruti", f"Обновите {brand_name}")
                elif lang == "uk":
                    content = content.replace("«Shruti Pro»", f"«{brand_name} Pro»")
                    content = content.replace('"Shruti Pro"', f'"{brand_name} Pro"')
                    content = content.replace("Оновіть Shruti", f"Оновіть {brand_name}")
                else:
                    content = content.replace("Shruti Pro", f"{brand_name} Pro")
                    content = content.replace("Shruti", brand_name)
                with open(chat_ts, "w", encoding="utf-8") as f:
                    f.write(content)

            print(f"Set branding for {lang} -> {brand_name}")

    print("=== Branding overlay applied successfully ===")

if __name__ == "__main__":
    main()
