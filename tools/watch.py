#!/.venv/bin/python
# -*- coding: utf-8 -*-
"""Pythonファイル監視＆テスト実行スクリプト

* *.py ファイルが変更されたら検出します
* 変更されたファイルに対応するテストケース一覧を取得します
* 変更されたファイルに対応するテストケースの期待値一覧を取得します
* 変更された .py ファイルを実行します
* 実行結果を出力します

Todo:
    * README を記述する
"""

import glob
import os
import sys
import time
import subprocess
import re
from datetime import datetime, timedelta 
from typing import Union
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileModifiedEvent, DirModifiedEvent
from watchdog.observers import Observer

### 監視＆実行されるファイルのパターン
PATTERNS = ['abc*.py']

### テストケースのインプットファイルのパターン
TEST_INPUT_PERTTERN = 'tests_*/*.in'

### テストケースのアウトプットファイルのパターン
TEST_OUTPUT_PERTTERN = 'tests_*/*.out'

class Color:
    """文字色クラス
    
    標準出力用の文字色の定数を保持するクラスです．

    """
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    WHITE = "\033[37m"
    END = "\033[39m" # 文字色のみの終了コード
class Decorate:
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    INVISIBLE = "\033[08m"
    REVERSE = "\033[07m"
    END = "\033[0m" # 全ての色指定や装飾の終了コード
class BgColor:
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    BLUE = "\033[44m"
    WHITE = "\033[47m"
    END = "\033[49m" # 背景色のみの終了コード

class MyHandler(PatternMatchingEventHandler):
    """ファイル変更のイベントハンドラクラス
    
    ファイルの変更イベントを処理する関数や属性値を保持するクラスです．
    
    Attributes
        last_runned (datatime): テストが最後に実行された時刻
        file_name(str): 監視＆実行される py ファイル
    """
    def __init__(self):
        super(MyHandler, self).__init__(patterns=PATTERNS)
        self.last_runned = datetime.now()

    def get_test_filename_list(self, test_dir: str):
        """テストケースファイル名一覧取得
        
        テストケースのファイル名の一覧を取得します．

        Args:
            test_dir (str): テストケースがあるディレクトリ
        Returns:
            str: テストケースのファイル名一覧を取得する
        """

        # ファイル名一覧を取得
        in_list = glob.glob(test_dir + TEST_INPUT_PERTTERN)
        in_list.sort()

        return in_list
    
    def get_out_list(self, test_dir: str):
        """テストケースの出力一覧取得
        
        テストケースの出力一覧を取得します．

        Args:
            test_dir (str): テストケースがあるディレクトリ

        Returns
            out_list(str): テスト出力名のリスト
        """

        # テストケース一覧を取得 
        out_name_list = glob.glob(test_dir + TEST_OUTPUT_PERTTERN)
        out_name_list.sort()
        out_list = []
        for out in out_name_list:
            f = open(out)
            out_list.append(f.read().strip())
            f.close()
        return out_list
    
    def judge_with_out(self, abs_src_path: str, in_filename: str, out: str):
        """出力ケースありの場合のテスト実行＆ジャッジ
            
        テストを実行し，結果を出力ケースを比較して結果(AC or WA)を標準出力に出力します

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
            in_filename(str): テストケースのファイル名
            out(str): テストケースのアウトプットの内容
        """
        try:
            # NOTE: subprocess で呼び出される python は親プロセスが実行されている python になる
            result_byte = subprocess.check_output(['python ' + abs_src_path + ' < ' + in_filename], shell=True)
            result = result_byte.decode().strip()
            if result == out:
                print(Decorate.BOLD + Color.GREEN + "[ AC ]" + Decorate.END)
            else:
                print(Decorate.BOLD + Color.RED + "[ WA ]" + Decorate.END)
            print("Expected: " + out)
            print("Actual  : " + result)
        except subprocess.CalledProcessError as e:
            print(e.output)

    def judge_without_out(self, abs_src_path: str, in_filename: str):
        """出力ケースなしの場合のテスト実行＆ジャッジ
        
        テストを実行し，結果を標準出力に出力します．出力ケースがないため，AC or WA の判断はおこないません．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
            in_filename(str): テストケースのファイル名
        """
        try:
            # NOTE: subprocess で呼び出される python は親プロセスが実行されている python になる
            subprocess.call(['python ' + abs_src_path + ' < ' + in_filename], shell=True)
        except subprocess.CalledProcessError as e:
            print(e.output)

    def run_test(self, abs_src_path: str):
        """テスト実行

        指定されたファイルを実行します．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
        """

        print("■■■ 変更されたファイル: " + abs_src_path)

        # 変更されたファイル名などを絶対パスから抽出
        matched = re.match(r'(.+/[^/]+/[^/]+/)(([^/]+)\.py)', abs_src_path)

        # 変更されたファイル名
        file_name = matched.group(2) # 例) a.py
        # print("■■■ 変更されたファイル名: " + file_name)

        # テストディレクトリがあるディレクトリ
        test_dir = matched.group(1) # 例）/Users/[USERNAME]/atcoder-playground/abc/abc202/a/
        # print("■■■ テストケースディレクトリ: " + test_dir)
        
        # テスト入力ケース名一覧を取得
        in_list = self.get_test_filename_list(test_dir)
        print("■■■ テストケース名一覧：")
        for item in in_list:
            print(item)
        
        # テスト期待値一覧を取得
        out_list = self.get_out_list(test_dir)
        print("■■■ テストケースの期待値一覧：")
        for item in out_list:
            print(item)

        # テストケースが 0 件なら処理終了
        if len(in_list) == 0:
            print("■■■ テストケースが存在しないためテストを中断します．")
            return

        print("")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 実行ファイル: " + file_name)
        print("")

        for i in range(len(in_list)):
            # 期待値（outファイル）存在フラグ
            out_exists = out_list[i:i + 1]
            
            # テストケース名をテストケース名絶対パスから抽出
            matched = re.match(r'.+/([^/]+\.in)', in_list[i])
            test_case_name = matched.group(1)# 例) sample-1.in

            if out_exists:
                # 期待値が存在する場合
                print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値あり） ----------")
                self.judge_with_out(abs_src_path, in_list[i], out_list[i])
                print("")
            else:
                # 期待値が存在しない場合
                print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値なし） ----------")
                self.judge_without_out(abs_src_path, in_list[i])
                print("")
    
    def on_modified(self, event: Union[FileModifiedEvent, DirModifiedEvent]):
        """ファイル変更イベントハンドラ

        ファイル変更イベントの検知して処理をおこないます．

        Args:
            event (Union[FileModifiedEvent, DirModifiedEvent]): ファイル変更イベント
        """
        
        # コマンドが最後に実行された時刻から1秒も過ぎていなかったら何もしない
        if datetime.now() - self.last_runned < timedelta(seconds=1):
            return
        else:
            # コマンド最終実行時刻を更新
            self.last_runned = datetime.now()
            # 変更されたファイルの絶対パスを取得
            abs_src_path = event.src_path
            # テストを実行
            self.run_test(abs_src_path)

def watch():
    """監視
    
    ファイル変更イベントを監視し，ハンドリングします．
    """
    
    print("■■ ファイル監視を開始します．") 

    # 現在のディレクトリの絶対パスを取得
    current_directory = os.getcwd()
    print("■■ watch.py 実行ディレクトリ: " + current_directory) 

    # インスタンス生成
    event_handler = MyHandler()
    observer = Observer()

    # ファイル監視をスケジュールする
    observer.schedule(event_handler, current_directory, recursive=True)

    # 監視の開始
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # スレッド停止命令
        observer.stop()
        # スレッドが終了するまで待機
        observer.join()
        print("■■ ファイル監視を終了します．")
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    print("■ メイン関数を実行します．")
    watch()
    print("■ メイン関数を終了します．")
