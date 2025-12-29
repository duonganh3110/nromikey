[app]
title = NRO Online
package.name = nroonline
package.domain = org.mikey

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg,atlas

# Quan trọng: dùng pygame-ce (không dùng pygame)
requirements = python3,pygame-ce

# Quan trọng: trỏ tới local recipe
p4a.local_recipes = ./p4a-recipes
p4a.bootstrap = sdl2

android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.minapi = 21
android.ndk_api = 21

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
