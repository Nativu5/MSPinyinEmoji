# MSPinyinEmoji

> 为微软拼音输入法添加 Emoji 候选功能😋

<img src="https://github.com/user-attachments/assets/878210f7-c355-4c93-8ccd-d92acf3723a7" alt="Emoji 候选展示" width="500"/>

## 使用方法

1. 下载 Release 中的词库文件（`.dat`）：

- 全拼：[Emojis.Quanpin.dat](https://github.com/Nativu5/MSPinyinEmoji/releases/download/v1.0.0/Emojis.Quanpin.dat)
- 小鹤双拼：[Emojis.Xiaohe.dat](https://github.com/Nativu5/MSPinyinEmoji/releases/download/v1.0.0/Emojis.Xiaohe.dat)

2. 在 Windows 任务栏中找到微软拼音输入法图标，右键点击“用户自定义短语”。
3. 点击“导入”按钮，选择下载的词库文件。
<img src="https://github.com/user-attachments/assets/67fe837e-9309-4c50-9163-19932a1163d4" alt="导入后的用户自定义短语列表" width="500"/>

4. 在输入法中输入某个词汇，对应的 Emoji 就会出现在候选字中。

**注意：**
- 如果您之前使用过自定义短语文件，建议先通过导出功能备份您的词库。
- Emoji 词库较大，可能造成性能影响。您可以通过自定义映射设置较小的词库。
- 如果导入词库后出现问题，可以删除 `%APPDATA%\Microsoft\InputMethod\Chs\ChsPinyinEUDPv1.lex` 文件，然后重新启动输入法。

## 自定义映射

本项目提供了一个 Python 脚本，用于生成微软拼音输入法的用户自定义短语文件（`.dat`）。您可以使用该脚本，生成任何按键映射（不仅限于 Emoji）。

首先，您需要准备一个 JSON 格式的映射文件，例如：

```json
[
    {
        "py": "a",
        "str": "😦",
        "rank": 2
    },
    {
        "py": "vx",
        "str": "微信",
        "rank": 1
    }
]
```

其中，`py` 为按键组合，`str` 为对应的字符串，`rank` 为该词的候选位置。

然后使用以下命令生成用户自定义短语文件：

```bash
python MSPinyinConverter.py -i YourPhrases.json -o YourPhrases.dat
```

## 参考资料

Emoji 中文映射：

- <https://github.com/yuhangch/zhmoji/>

词库转换：

- <https://github.com/studyzy/imewlconverter>
- <https://github.com/youmuyou/mschxudp>
