[app]
title = NRO Online
package.name = nroonline
package.domain = org.mikey
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg,atlas
source.exclude_dirs = venv,.venv,__pycache__,.git,.github,build,dist,.buildozer

requirements = python3,pygame

orientation = landscape

android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk_api = 21

android.accept_sdk_license = True
android.skip_update = True

p4a.bootstrap = sdl2
