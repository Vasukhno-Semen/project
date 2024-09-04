[app]

title = PaperLab
package.name = testapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,Pillow,babel,kivy-garden.mapview,kivycalendar3,sqlite3

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
android.permissions = INTERNET, ACCESS_NETWORK_STATE
source.main = main.py
source.dir = .
android.api = 31
android.minapi = 21
android.sdk = 31
android.debug = True
# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
