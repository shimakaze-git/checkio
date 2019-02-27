import re


def checkio(text: str) -> str:

    # 空白を消す
    text_rsplit = text.rsplit()

    # 文字列を結合
    text_join = "".join(text_rsplit)
    text_lower = text_join.lower()

    # 記号と数字を除去
    clean_text = re.sub(r"[!-/:-@[-`{-~\d+]", "", text_lower)

    text_dict = {}
    for word in clean_text:
        text_dict[word] = clean_text.count(word)

    # 辞書内の値の数値が最大値(max)と最小値(min)が一致している
    # という事は、辞書内の数値が全て一緒ということになる。
    if max(text_dict.values()) == min(text_dict.values()):

        # 辞書内のキーの最小値を取り出す
        # アルファベットの最小値を取り出す
        min_word = min(text_dict)
        return min_word
    else:
        # 数が多い文字を抽出
        count = 0
        target_key = None
        for key in text_dict:
            if text_dict[key] >= count:
                count = text_dict[key]
                target_key = key
        return target_key

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")