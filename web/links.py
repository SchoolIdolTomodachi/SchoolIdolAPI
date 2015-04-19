 # -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

def get_links(current_en, current_jp):
    return [
        {
            'name': _('Download'),
            'link': 'download',
            'idol': 'Kousaka Honoka',
            'links': [
                {
                    'name': 'iOs: English Version',
                    'url': 'https://itunes.apple.com/us/app/school-idol-festival/id834030294?mt=8',
                    'language': 'english',
                },
                {
                    'name': 'Android: English Version',
                    'url': 'https://play.google.com/store/apps/details?id=klb.android.lovelive_en',
                    'language': 'english',
                },
                {
                    'name': 'iOs: Japanese Version',
                    'url': 'https://itunes.apple.com/jp/app/raburaibu!sukuruaidorufesutibaru/id626776655?mt=8',
                    'language': 'japanese',
                },
                {
                    'name': 'Android: Japanese Version',
                    'url': 'https://play.google.com/store/apps/details?id=klb.android.lovelive&hl=en',
                    'language': 'japanese',
                },
                {
                    'name': _('How to install Japanese apps?'),
                    'description': _('Follow this tutorial to play the Japanese version of the game. You\'ll be able to download it directly from the App Store or Play Store!'),
                    'url': 'https://github.com/SchoolIdolTomodachi/SchoolIdolAPI/wiki/How-to-install-Japanese-apps%3F',
                    'language': 'japanese',
                },
                {
                    'name': _('APKs and Links'),
                    'description': _('If none of the Android links worked, that\'s what you\'re searching for.'),
                    'url': 'http://platinumdis.co/lovelive',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': _('Other Android APKs mirror'),
                    'url': 'https://ll.idolactiviti.es/apk/',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': _('Play on a rooted Android'),
                    'description': _('"Illegal access detected!"? Here is the solution.'),
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/wiki/rooting',
                    'type': 'tutorial',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': _('Play on a PC'),
                    'url': 'http://pastebin.com/gx0a1mEY',
                    'type': 'tutorial',
                    'language': 'world',
                    'size': 'small',
                },
            ],
        },
        {
            'name': _('Get Started'),
            'link': 'getstarted',
            'idol': 'Yazawa Nico',
            'links': [
                {
                    'name': _('Beginner\'s guide'),
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/wiki/guide',
                    'size': 'big',
                    'type': 'tutorial',
                    'language': 'world',
                },
                {
                    'name': _('Menu\'s Translation'),
                    'description': _('Useful if you play on the Japanese version.'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Menus',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('GamePlay'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Gameplay',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Frequently Asked Questions'),
                    'description': 'Reddit Version.',
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/wiki/faq',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Frequently Asked Questions'),
                    'description': 'Decaf Wiki Version.',
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=FAQ',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('List of Items'),
                    'description': _('In game points and virtual money.'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Items',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Save your Transfer Code'),
                    'description': _('First thing to do! In case you lose your device, it will allow you to retrieve your precious account.'),
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/wiki/passcode',
                    'type': 'tutorial',
                    'language': 'world',
                },
                {},
                {
                    'name': 'Japanese Bushimo Love Live! Festival Wiki',
                    'url': 'http://www59.atwiki.jp/lovelive-sif/',
                    'type': 'info',
                    'language': 'japanese',
                    'size': 'small',
                },
                {
                    'name': 'Japanese Love Live! Festival Gamerch Wiki',
                    'url': 'http://xn--eck5eb7eb.gamerch.com/',
                    'type': 'info',
                    'language': 'japanese',
                    'size': 'small',
                },
                {
                    'name': 'Chinese MoeGirl Wiki',
                    'url': 'http://zh.moegirl.org/LoveLive!',
                    'type': 'info',
                    'language': 'japanese',
                    'size': 'small',
                },
                {
                    'name': _('Points required to rank up'),
                    'url': 'http://www59.atwiki.jp/lovelive-sif/pages/23.html',
                    'type': 'info',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': _('Edit your "about me" section in the game'),
                    'url': 'https://yefta.com/llsif/proedit.html',
                    'type': 'tool',
                    'language': 'world',
                    'size': 'small',
                },
            ],
        },
        {
            'name': _('News & Updates'),
            'link': 'tutorials',
            'idol': 'Ayase Eli',
            'links': [
                {
                    'name': _('Game Facebook Page'),
                    'url': 'https://www.facebook.com/schoolidolfestival',
                    'description': _('Official page with news about the game.'),
                    'type': '',
                    'language': 'english',
                },
                {
                    'name': 'Love Live Facebook Page',
                    'url': 'https://www.facebook.com/LoveLive.Muse',
                    'description': '',
                    'type': '',
                    'language': 'english',
                },
                {
                    'name': 'Twitter @LLSIF_english',
                    'url': 'https://twitter.com/LLSIF_english',
                    'type': '',
                    'language': 'english',
                },
                {
                    'name': 'Official Twitter @lovelive_staff',
                    'url': 'https://twitter.com/lovelive_staff',
                    'type': '',
                    'language': 'japanese',
                },
                {
                    'name': 'Official Twitter @lovelive_SIF',
                    'url': 'https://twitter.com/lovelive_SIF',
                    'type': '',
                    'language': 'japanese',
                },
                {
                    'name': 'Twitter School Idol Tomodachi',
                    'url': 'https://twitter.com/schoolidolu',
                    'size': 'big',
                    'description': _('Updates about the cards and the community (this website!).'),
                    'type': '',
                    'language': 'english',
                },
                {
                    'name': 'Twitter @loveliveconfess',
                    'url': 'https://twitter.com/loveliveconfess',
                    'type': '',
                    'description': _('Funny quotes from frustrated players.'),
                    'language': 'english',
                    'size': 'small',
                },
                {
                    'name': _('English In Game Updates'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=English_Version_Info',
                    'type': 'info',
                    'language': 'english',
                },
                {
                    'name': _('Japanese In Game Updates'),
                    'description': _('Translated in English.'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Updates',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('Official News about LoveLive! Franchise'),
                    'url': 'http://news.lovelive-anime.jp/app-def/S-102/news/',
                    'language': 'japanese',
                    'type': 'info',
                },
            ],
        },
        {
            'name': _('Communities'),
            'link': 'communities',
            'idol': 'Toujou Nozomi',
            'links': [
                {
                    'name': 'Reddit',
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/',
                    'size': 'big',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': 'Facebook Group',
                    'url': 'https://www.facebook.com/groups/293090280852174/',
                    'description': _('Mainly casual gamers but very active community.'),
                    'size': 'big',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': _('School Idol Tomodachi'),
                    'description': _('Discuss with players using comments on their pages or on the cards.'),
                    'url': '/users/',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': 'Otonokizaka Forum',
                    'url': 'http://otonokizaka.org/',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': 'Crunchyroll Forum',
                    'url': 'http://www.crunchyroll.com/forumtopic-855485/love-live-school-idol-festival-app-game?pg=0',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': 'MyAnimeList Forum',
                    'url': 'http://myanimelist.net/forum/?topicid=635035',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': 'Fuwanovel Forum',
                    'url': 'http://forums.fuwanovel.org/index.php?/topic/5034-love-live-school-idol-festival-thread/',
                    'type': '',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': 'AnimeSuki Forum',
                    'url': 'http://forums.animesuki.com/showthread.php?t=126816',
                    'type': '',
                    'language': 'world',
                    'size': 'small',
                },
            ],
        },
        {
            'name': _('Collect Cards'),
            'link': 'cards',
            'idol': 'Koizumi Hanayo',
            'links': [
                {
                    'name': _('Browse Cards'),
                    'description': _('Search for cards using smart filters and ordering.'),
                    'url': '/cards',
                    'type': 'info',
                    'language': 'world',
                    'size': 'big',
                },
                {
                    'name': _('Track your Cards'),
                    'url': '/cards',
                    'description': _('Helps you fill your album in the game - and brag about your cards ;)'),
                    'type': 'tool',
                    'language': 'world',
                },
                {
                    'name': _('Recruitment Simulator'),
                    'url': 'http://scfes.mnyk.info/',
                    'type': 'tool',
                    'language': 'japanese',
                },
                {
                    'name': _('Cards you can get from songs'),
                    'url': 'http://xn--eck5eb7eb.gamerch.com/%E3%83%A9%E3%82%A4%E3%83%96%E5%A0%B1%E9%85%AC',
                    'description': _('Sometimes you can get an R at the end of some songs.'),
                    'type': 'info',
                    'language': 'world',
                    'size': 'small',
                },
                {
                    'name': _('Trade Accounts on Facebook'),
                    'url': 'https://www.facebook.com/groups/348965238597534/',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': _('Trade Accounts on Reddit'),
                    'url': 'http://www.reddit.com/r/SIFTrades',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': _('Starter Accounts Giveaways with UR on Facebook'),
                    'url': 'https://www.facebook.com/groups/732282656879803/',
                    'type': '',
                    'size': 'small',
                    'language': 'world',
                },
                {
                    'name': _('Experience required to level up a card'),
                    'url': 'http://www59.atwiki.jp/lovelive-sif/pages/32.html',
                    'type': 'info',
                    'language': 'world',
                },
            ],
        },
        {
            'name': _('Play Songs & Watch Stories'),
            'link': 'songs',
            'idol': 'Nishikino Maki',
            'links': [
                {
                    'name': _('Scoring Guide'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Scoring',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('List of songs'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Songs',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Android Traning App Sukutore'),
                    'description': _('Train your fingers without wasting your LPs!'),
                    'url': 'http://apps.evozi.com/apk-downloader/?id=siy.sukutore',
                    'size': 'big',
                    'type': 'tool',
                    'language': 'world',
                },
                {
                    'name': _('Assist Guides for each songs'),
                    'url': 'https://www.youtube.com/user/OktopazOfficial',
                    'description': _('Songs are slowed down, showed with and without hands, with a beatmania-like representation and good sound feedback.)'),
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Advanced Scoring Guide'),
                    'url': 'http://www.reddit.com/r/SchoolIdolFestival/comments/2r5nx6/guide_advanced_scoring_guide/',
                    'type': 'tutorial',
                    'language': 'world',
                },
               {},
                {
                    'name': _('Watch all the English Side Stories'),
                    'size': 'big',
                    'description': _('Click on a card, scroll down and play the video!'),
                    'url': '/cards/?is_world=True',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Watch all the main story'),
                    'url': 'https://www.youtube.com/playlist?list=PLpXLEE3mSzRjyKa6nEH0CXm-bJcOXpKjU',
                    'type': 'info',
                    'language': 'english',
                },
                {
                    'name': _('Main Story Translation'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Story',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('All Characters Stories Translation'),
                    'url': 'http://decaf.kouhi.me/lovelive/',
                    'description': _('Go to each characters page from the list on the left.'),
                    'type': 'info',
                    'language': 'japanese',
                    'size': 'small',
                },
            ],
        },
        {
            'name': _('Join Events'),
            'link': 'events',
            'idol': 'Minami Kotori',
            'links': [
                {
                    'name': _('Types of Events & How to Play'),
                    'url': 'http://decaf.kouhi.me/lovelive/index.php?title=Gameplay#Events',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': ('Current' if current_en.is_world_current() else 'Latest') + ' Event English Version',
                    'description': current_en.english_name,
                    'url': '/event/' + current_en.japanese_name + '/',
                    'size': 'big',
                    'type': 'info',
                    'language': 'english',
                },
                {
                    'name': ('Current' if current_en.is_japan_current() else 'Latest') + ' Event Japanese Version',
                    'description': current_jp.japanese_name,
                    'url': '/event/' + current_jp.japanese_name + '/',
                    'size': 'big',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('English Event Tracker'),
                    'description': _('Track statistics about the current English event.'),
                    'url': 'https://sites.google.com/site/llsifeneventtracker/',
                    'type': 'info',
                    'language': 'english',
                },
                {
                    'name': _('Japanese Event Tracker'),
                    'description': _('Track statistics about the current Japanese event.'),
                    'url': 'http://atsites.jp/llborder/',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('Events Rank Calculator'),
                    'url': 'https://yefta.com/llsif/',
                    'description': _('A tool to calculate the required loveca and time you will need to get a certain position in the global ranking.'),
                    'size': 'big',
                    'type': 'tool',
                    'language': 'world',
                },
                {
                    'name': _('Japanese Events Tier 2 Cutoff Predictor'),
                    'url': 'http://www.usagi.org/doi-bin/llcutoff.pl',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('List of all events'),
                    'url': '/events/',
                    'size': 'big',
                    'description': _('Events information + Hall of fame of all scores of the players from the School Idol Tomodachi community.'),
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('Event Cards'),
                    'url': '/cards/?is_event=on&ordering=release_date&reverse_order=on',
                    'type': 'info',
                    'language': 'world',
                },
            ],
        },
        {
            'name': _('Fall in love with idols'),
            'link': 'love',
            'idol': 'Hoshizora Rin',
            'links': [
                {
                    'name': _('All the characters in the game'),
                    'url': '/idols/',
                    'description': _('Get all the facts about your favorite idols, as well as their cards.'),
                    'size': 'big',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': _('Vote for the BEST GIRL'),
                    'url': '/contest/',
                    'description': _('Vote for your favorite cards on School Idol Contest, the Facemash.'),
                    'size': 'big',
                    'type': '',
                    'language': 'world',
                },
                {
                    'name': _('Personal Idols Ranking Generator'),
                    'url': 'http://kouhi.me/idol/',
                    'description': _('Check "Love Live!" and press "Music Start!".'),
                    'type': 'tool',
                    'language': 'world',
                },
            ],
        },
        {
            'name': 'LoveLive! Franchise',
            'link': 'other',
            'idol': 'Sonoda Umi',
            'links': [
                {
                    'name': _('Official Website'),
                    'url': 'http://www.lovelive-anime.jp/',
                    'language': 'japanese',
                    'type': 'info',
                    'size': 'big',
                },
                {
                    'name': _('Information about the anime'),
                    'url': 'http://myanimelist.net/anime/15051/Love_Live!_School_Idol_Project',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('General Wiki about LoveLive!'),
                    'url': 'http://love-live.wikia.com/wiki/Main_Page',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('LoveLive! Discography'),
                    'url': 'http://love-live.wikia.com/wiki/Category:Discography',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': _('LoveLive! The Manga'),
                    'url': 'http://love-live.wikia.com/wiki/Love_Live!_School_idol_project_(Manga)',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': 'LoveLive! School Idol Paradise',
                    'description': 'PS Vita Game',
                    'url': 'http://love-live.wikia.com/wiki/Love_Live!_School_idol_paradise',
                    'type': 'info',
                    'language': 'world',
                },
                {
                    'name': 'Youtube Channel μ\'s（ラブライブ！） by Lantis',
                    'url': 'https://www.youtube.com/playlist?list=PLmgGL3shzkGM9akfMoobnVhE3XCP42lHb',
                    'type': 'info',
                    'language': 'japanese',
                },
                {
                    'name': _('Buy music on iTunes'),
                    'url': 'https://itunes.apple.com/jp/artist/ms/id411582529?l=en',
                    'type': 'info',
                    'language': 'japanese',
                },
                 {
                    'name': _('Love Live music on videos'),
                     'description': _('by the Reddit /r/LoveLive community'),
                     'url': 'https://vimeo.com/lovelivereddit',
                     'type': 'info',
                     'language': 'world',
                 },
            ],
        },
    ]
