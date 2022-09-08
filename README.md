# mcsr regex
###### compiled and developed by **neal#0001**
#### multiple sets of regex patterns to answer some of the most commonly asked questions in mcsr twitch chat's, 
hopefully some of these can help you in your chat or a chat you moderate.

here is a list of all the sets i have worked on:
+ questions about
	+ [what the current world record is][wr]
	+ [what the broadcasters pb is][pb]
	+ [the pace of the current run][pace]
	+ [why all advancements overlay isn't enabled][aa-overlay]
	+ [what category being currently played][what-category]
+ mentions of
	+ [ads][ads]
	+ [view-count][view-count]
---

## usage
all of these sets of regex patterns are designed for use with fossabot keywords. 
each folder in the [data folder][data] listed above. 
each folder represents one keyword in fossabot dashboard. inside each folder there are two files:

`patterns.txt` (file linked above in full list of keywords)  
each line in this file represents a separate phrase group.
so far all of these regex only use one phrase per phrase group but that could change in future if it's needed.
don't forget to add `regex:` before each phrase to let fossabot know you are using regex.

`data.txt`  
these are all chat messages i've copy-pasted directly from twitch chats used to help me develop these regex patterns.

## additional resources
1) <https://regex101.com>  
this is where i write all the regex patterns and i would reccomend it to anyone who wants to modify these regex patterns or develop new ones.
2) <https://docs.fossabot.com/keywords>  
this is just the documentation for keywords for fossabot and is really helpful if you are struggling to get these regex stings to work for your fossabot.

## feedback, testing, and development
if you are using these regex patterns and notice a message does not get a proper response feel free to message me or open an issue [here][issues] on the github repository. 
i will add the message you've found to the testing data text file so it's checked every time i update these regex patterns in future. 
please do feel free to suggest new regex sets/keywords to be developed in future or any changes you would like to how this repository or how it is organized :)

## contributors
anyone who has developed anything from these regex patterns:

+ **calomena#0001**
+ **Isabel#7551**
+ **lizzie#0099**

[wr]: https://github.com/nealxm/mcsr-regex/blob/master/data/wr/patterns.txt
[pb]: https://github.com/nealxm/mcsr-regex/blob/master/data/pb/patterns.txt
[pace]: https://github.com/nealxm/mcsr-regex/blob/master/data/pace/patterns.txt
[aa-overlay]: https://github.com/nealxm/mcsr-regex/tree/master/data/aa%20overlay/patterns.txt
[what-category]: https://github.com/nealxm/mcsr-regex/blob/master/data/what%20category/patterns.txt
[ads]: https://github.com/nealxm/mcsr-regex/blob/master/data/ads/patterns.txt
[view-count]: https://github.com/nealxm/mcsr-regex/blob/master/data/view%20count/patterns.txt
[data]: https://github.com/nealxm/mcsr-regex/tree/master/data
[issues]: https://github.com/nealxm/mcsr-regex/issues