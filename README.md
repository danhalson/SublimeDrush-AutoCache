SublimeDrush-AutoCache
======================

Plugin for Drupal devs using Sublime Text 3 to clear the Drupal cache on every save.

This was originally going to be a fully blown Drush wrapper, however, since I started the plugin (a long while back now, been busy...) a decent alternative has appeared [https://github.com/vaanwd/sublime_drush]. Rather than waste my effort I'm presenting here what I perceive to be the most useful bit I'd developed, and a feature that doesn't yet exist in sublime_drush, a method to run drush cc all on every save to avoid the pain of forgetting to clear the cache and having to fling the command into the console on every save. Hope it's of use to someone, I'll do a little bit more on it I suspect in coming months, but it's mostly functional.

Installation:

Depends on Drush [https://github.com/drush-ops/drush] and obviously Drupal.

  1. cd ~/Library/Application Support/Sublime Text 3/Packages
  
  2. git clone <repo url>

Usage:

  1. Specify your drush path in the settings.
  
  2. Specify your drupal project dir in either your project folder (most uselful method) or in the main settings.
  
  Check the settings for other info.

Thanks.
