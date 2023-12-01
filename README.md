# mcsr regex
###### *compiled and developed by @nealxm on discord*
#### a collection of regex patterns enabling automatic responses to some of the most commonly asked questions in mcsr twitch chats. i hope that some of these can help you in your chat, or a chat you moderate.

here are a list of all the keywords provided in this repository:
+ questions about
	+ [why all advancements overlay is not enabled][aa-overlay]
	+ [the current category being played][category]
	+ [what hdm stands for in aa speedruns][hdm]
	+ [what keyboard the broadcaster is using][keyboard]
	+ [the pace of the current run][pace]
	+ [what the broadcasters pb is][pb]
	+ [what playlist is currently being used][playlist]
	+ [any interesting runs so far in the stream][runs]
	+ [the current song][song]
	+ [what texture pack is being used][texture-pack]
	+ [where the timer is][timer]
	+ [the version being currently played][version]
	+ [what the current world record is][wr]
+ mentions of
	+ [ads][ads]
	+ [view count][view-count]
---

## usage
these sets of regex patterns are designed for use with fossabot keywords. 
each folder in the [data folder][data] listed at the top of this page represents one keyword in fossabot dashboard.
inside each folder there are two files:

`patterns.txt` (this file is linked above in full list of keywords)  
each line in this file represents a single *separate* phrase group.
so far, these regex patterns only use **one phrase per phrase group** but that could change in future if it is needed.
don't forget to add the response you want fossabot to give and add `regex:` before each phrase to signify to fossabot that you are using regex

`data.txt`  
these are all chat messages copy-pasted directly from twitch chats used to help develop these regex patterns.
along with development, keeping these tests helps ensure future changes do not break any old functionality.

## additional resources
1) <https://regex101.com>  
this is where i write all the regex patterns, and i would recommend it to anyone who wants to modify these regex patterns or develop new ones.
2) <https://docs.fossabot.com/keywords>  
here is the documentation for keywords for fossabot and is helpful if you are struggling to get these regex stings to work for your fossabot.

## feedback, testing, and development
if you are using these regex patterns and notice a message does not get a proper response feel free to message me or open an issue [here][issues] directly on the github repository. 
after helping fix the problem, i will also add the message you have found to the testing data text file so that it is checked every time i update these regex patterns in the future. 
please do feel free to suggest new regex patterns/keywords to be developed in future or any changes you would like to how this repository or how it is organized :)

## contributors
anyone who has developed anything from these regex patterns: (all discord usernames)

+ **@calomena**
+ **@isabelcoolaf**
+ **@eiizie**
+ **@pacmanmvc**

[aa-overlay]: https://github.com/nealxm/mcsr-regex/blob/master/data/aa-overlay/patterns.txt
[category]: https://github.com/nealxm/mcsr-regex/blob/master/data/category/patterns.txt
[hdm]: https://github.com/nealxm/mcsr-regex/blob/master/data/hdm/patterns.txt
[keyboard]: https://github.com/nealxm/mcsr-regex/blob/master/data/keyboard/patterns.txt
[pace]: https://github.com/nealxm/mcsr-regex/blob/master/data/pace/patterns.txt
[pb]: https://github.com/nealxm/mcsr-regex/blob/master/data/pb/patterns.txt
[playlist]: https://github.com/nealxm/mcsr-regex/blob/master/data/playlist/patterns.txt
[runs]: https://github.com/nealxm/mcsr-regex/blob/master/data/runs/patterns.txt
[song]: https://github.com/nealxm/mcsr-regex/blob/master/data/song/patterns.txt
[texture-pack]: https://github.com/nealxm/mcsr-regex/blob/master/data/texture-pack/patterns.txt
[timer]: https://github.com/nealxm/mcsr-regex/blob/master/data/timer/patterns.txt
[version]: https://github.com/nealxm/mcsr-regex/blob/master/data/version/patterns.txt
[wr]: https://github.com/nealxm/mcsr-regex/blob/master/data/wr/patterns.txt

[ads]: https://github.com/nealxm/mcsr-regex/blob/master/data/ads/patterns.txt
[view-count]: https://github.com/nealxm/mcsr-regex/blob/master/data/view-count/patterns.txt

[data]: https://github.com/nealxm/mcsr-regex/tree/master/data
[issues]: https://github.com/nealxm/mcsr-regex/issues