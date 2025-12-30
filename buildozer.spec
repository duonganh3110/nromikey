[app]
title = NRO Online
package.name = nroonline
package.domain = org.mikey
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg,atlas

# Game em import pygame => dùng pygame cho dễ build nhất
requirements = python3,pygame

p4a.bootstrap = sdl2

android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.minapi = 21
android.api = 34
android.accept_sdk_license = True
