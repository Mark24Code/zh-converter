# 中文简体繁体互译


# 安装

Linux/Mac OS

`./install.sh` 安装依赖

Windows

`pip3 install requirements.txt`


# 执行

`python3 zh-converter.py  -h` 获取帮助

`-t` type 翻译的目标类型，默认是cn

```
cn 大陆简体
tw 台灣正體
hk 香港繁體
sg 马新简体（无词汇表，需要手工指定）
hans 简体
hant 繁體
```

`python3 zh-converter.py -t cn   -w <单词>` 查单词 

`python3 zh-converter.py -t tw -f <文件>` 翻译文件，本地目录生成 translated.txt 
