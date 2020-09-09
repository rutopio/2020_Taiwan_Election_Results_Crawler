# 2020 台灣選舉結果爬蟲：以不分區政黨票為例

## 這是什麼？

這是一個針對2020年台灣選舉結果，透過中選會，簡單使用python的爬蟲小東東。

裡面用了python，所以你要先有pythonㄛ，怎麼裝自己查。

還用了像是`bs4`, `requests`, `selenium`, `pandas`, `html5lib`等package，如果你沒有要先安裝這些東東也要裝ㄛ

```{terminal}
$ pip install <package name>
# 可能需要加sudo
```

## 怎麼用？

下載 Party-list_proportional_representation/count_votes.py 到你開心的地方，然後透過terminal切換到該目錄之下，接著在terminal裡輸入

```{terminal}
$ python count_votes.py 
```

然後照著上面的步驟走就好惹。

最後就會得到以下的結果ㄌ，我這裡用記事本開這個肥滋滋ㄉcsv

![](https://i.imgur.com/DGFJCv0.png)


## 怎麼做的？

可以看我寫的東西，[在這裡](http://chingru.me/code/2020-01-16-python%E7%AD%86%E8%A8%98-2020%E5%8F%B0%E7%81%A3%E9%81%B8%E8%88%89%E7%B5%90%E6%9E%9C%E7%88%AC%E8%9F%B2%E4%BB%A5%E4%B8%8D%E5%88%86%E5%8D%80%E6%94%BF%E9%BB%A8%E7%A5%A8%E7%82%BA%E4%BE%8B/)。
