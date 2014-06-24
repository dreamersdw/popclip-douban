# coding:utf8
import sys
import json
import urllib2

def main():
    title = sys.stdin.readline().strip()
    search_api = "http://api.douban.com//v2/movie/search?q=%s" % title
    data = json.load(urllib2.urlopen(search_api))

    if not data["subjects"]:
        response = "哎呦, 找不到叫 %s 的电影" % title
    else:
        rating = data["subjects"][0]["rating"]["average"]
        full_title = data["subjects"][0]["title"]
        response = "%s 评分 %s" % (full_title.encode("utf8"), rating)

    print response

if __name__ == '__main__':
    main()
