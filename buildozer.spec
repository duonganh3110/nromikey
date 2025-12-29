[app]
title = NRO Online
package.name = nroonline
package.domain = org.mikey
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg,atlas
source.exclude_dirs = .git,.github,__pycache__,.venv,venv,build,dist

# ✅ ĐỪNG dùng pygame -> dùng pygame-ce
requirements = python3,pygame-ce

# ✅ Local recipe (bắt buộc nếu dùng pygame-ce kiểu này)
p4a.local_recipes = ./p4a-recipes
p4a.bootstrap = sdl2

# (thỉnh thoảng cần) p4a.branch = develop :contentReference[oaicite:2]{index=2}
p4a.branch = develop

android.archs = arm64-v8a,armeabi-v7a
android.minapi = 21
android.ndk_api = 21
android.api = 34
android.permissions = INTERNET
android.accept_sdk_license = True

# ✅ ép dùng SDK có sẵn của runner để không thiếu build-tools/aidl
android.sdk_path = /usr/local/lib/android/sdk
