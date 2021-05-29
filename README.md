# Atcoder Playground
🍆 AtCoder 作業用プロジェクトです．

## online-judge-tools のインストール
https://github.com/online-judge-tools/oj

```
$ pip3 install online-judge-tools
```

## atcoder-cli のインストール
https://github.com/Tatamo/atcoder-cli
```
$ npm install -g atcoder-cli
```

Python 用のコンフィグを修正する．
```
$ cd `acc config-dir`
$ touch PYTHON
$ ls
PYTHON
config.json
session.json
```

```
$ vim config.json
// config.json
{
    "oj-path": "/Users/[USERNAME]/.anyenv/envs/pyenv/shims/oj",
    "default-contest-dirname-format": "{ContestID}",
    "default-task-dirname-format": "{tasklabel}",
    "default-test-dirname-format": "tests",
    "default-task-choice": "inquire",
    "default-template": "PYTHON"
}
```

```
$ cd PYTHON
$ ll
main.py
template.json
```

```
$ cat template.json
{
  "task": {
    "program": [["main.py", "{TaskID}.py"]],
    "submit": "{TaskID}.py",
    "static": [],
    "testdir": "tests_{TaskID}",
    "cmd": "ls -l"
  },
  "contest": {
    "static": [],
    "cmd": "ls -l"
  }
}
```

## Python の仮想環境を作成する
`AtCoder` ディレクトリ配下で以下を実行します．
```
$ cd ./abc
$ pipenv install
```
すると，`abc` 配下に `Python` の仮想環境 `.venv` が生成されます．

## acc コマンドでコンテストディレクトリを作成
```
$ cd ./abc
$ acc new abc202
```

## ファイル監視＆テスト自動実行
`./abc` 配下でファイル監視スクリプト `../tools/watch.py` を実行します．
```
$ pwd
/xxx/xxx/abc/
$ pipenv run python ../tools/watch.py
```
`Pipfile` のスクリプトにショートカットを定義しているので，次のコマンドでも実行可能です．

```
$ pipevn run start
```

例えば `abc/abc202/a/` 配下の `abc202_a.py` ファイルを更新すると，それに対応するテストケースと期待値を検索してテストを実行します．以下は出力例です．
```
■■■ 変更されたファイル: /Users/[USERNAME]/atcoder-playground/abc/abc202/a/abc202_a.py
■■■ テストケース名一覧：
/Users/[USERNAME]/atcoder-playground/abc/abc202/a/tests_abc202_a/sample-1.in
/Users/[USERNAME]/atcoder-playground/abc/abc202/a/tests_abc202_a/sample-2.in
■■■ テストケースの期待値一覧：
13
6

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 実行ファイル: abc202_a.py

---------- sample-1.in 実行結果（期待値あり） ----------
[ AC ]
Expected: 13
Actual  : 13

---------- sample-2.in 実行結果（期待値あり） ----------
[ AC ]
Expected: 6
Actual  : 6
```

期待値(`*.out`)が見つからない場合は，AC or WA の判定はおこなわず，実行結果だけを出力します．
```
■■■ 変更されたファイル: /Users/[USERNAME]/atcoder-playground/abc/abc202/a/abc202_a.py
■■■ テストケース名一覧：
/Users/[USERNAME]/atcoder-playground/abc/abc202/a/tests_abc202_a/sample-1.in
/Users/[USERNAME]/atcoder-playground/abc/abc202/a/tests_abc202_a/sample-2.in
■■■ テストケースの期待値一覧：
13
6

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 実行ファイル: abc202_a.py

---------- sample-1.in 実行結果（期待値なし） ----------
13

---------- sample-2.in 実行結果（期待値なし） ----------
6
```

## AC 状況の markdown ファイルを出力する
`tools` に移動し，`ac_status.sh` を実行します．
```
$ cd ../tools/
$ ./ac_status.sh
```
同ディレクトリ内に `ac_status.md` が出力されます．