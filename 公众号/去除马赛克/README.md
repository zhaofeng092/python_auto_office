<div align="center">
    <a href="https://github.com/zhaofeng092/python_auto_office"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://t.cn/A6Gkrbzw"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkyMzIwOTgzMA==&action=getalbum&album_id=1861970403066249218&scene=173&from_msgid=2247484814&from_itemidx=1&count=3&nolastread=1#wechat_redirect"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

# Depix

Depix is a tool for recovering passwords from pixelized screenshots.

This implementation works on pixelized images that were created with a linear box filter.

In [this article](https://www.linkedin.com/pulse/recovering-passwords-from-pixelized-screenshots-sipke-mellema) I cover background information on pixelization and similar research.

## Example

`python depix.py -p images/testimages/testimage3_pixels.png -s images/searchimages/debruinseq_notepad_Windows10_closeAndSpaced.png -o output.png`

![image](docs/img/Recovering_prototype_latest.png)

## Usage

* Cut out the pixelated blocks from the screenshot as a single rectangle.
* Paste a [De Bruijn sequence](https://damip.net/article-de-bruijn-sequence) with expected characters in an editor with the same font settings (text size, font, color, hsl).
* Make a screenshot of the sequence. If possible, use the same screenshot tool that was used to create the pixelized image.
* Run `python depix.py -p [pixelated rectangle image] -s [search sequence image] -o output.png`

## Algorithm

The algorithm uses the fact that the linear box filter processes every block separately. For every block it pixelizes all blocks in the search image to check for direct matches.

For most pixelized images Depix manages to find single-match results. It assumes these are correct. The matches of surrounding multi-match blocks are then compared to be geometrically at the same distance as in the pixelized image. Matches are also treated as correct. This process is repeated a couple of times.

After correct blocks have no more geometrical matches, it will output all correct blocks directly. For multi-match blocks, it outputs the average of all matches.

## Misc

### Usage issues

* **Dependency Issues** See: https://github.com/beurtschipper/Depix/issues/12
* 
