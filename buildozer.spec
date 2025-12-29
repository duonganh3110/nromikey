[app]
title = NRO Online
package.name = nroonline
package.domain = org.mikey
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg,atlas

# Nếu em dùng pygame-ce:
requirements = python3,pygame-ce
# Nếu không có recipe pygame-ce thì đổi dòng trên thành:
# requirements = python3,pygame

p4a.bootstrap = sdl2

android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.minapi = 21
android.api = 34

# Nếu em có folder p4a-recipes (local recipe) đặt cạnh main.py:
p4a.local_recipes = p4a-recipes

android.accept_sdk_license = True
log_level = 2
