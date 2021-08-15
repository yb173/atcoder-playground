#!/.venv/bin/python
# -*- coding: utf-8 -*-
"""Python, C++ファイル監視＆テスト実行スクリプト

・ .py ファイルまたは .cpp ファイルの変更を検出します．
・ 変更されたファイルに対応するテストケースと期待値一覧を取得します
・ テストを実行します．
・ 実行結果を出力します

Todo:
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
# PATTERNS = ['abc*.py', 'abc*.cpp']
PATTERNS = ['*.py', '*.cpp']

### テストケースのインプットファイルのパターン
TEST_INPUT_PERTTERN = 'tests_*/*.in'

### テストケースのアウトプットファイルのパターン
TEST_OUTPUT_PERTTERN = 'tests_*/*.out'

### C++ 実行ファイル名
CPP_EXEC_FILENAME = 'main.out'

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

    def get_test_list(self, abs_problem_dir_path: str):
        """テスト情報一覧取得
        
        テスト情報の一覧を取得します．

        Args:
            abs_problem_dir_path (str): 問題ディレクトリ
        Returns:
            :obj:`list`: [テストケースファイル名の絶対パス, テストケース名, 期待値ありフラグ, 期待値] の配列
        Example:
            test_list[i][0]: '/Users/[USERNAME]/work/atcoder/atcoder-playground/abc/abc203/c/tests_abc203_c/sample-1.in'
            test_list[i][1]: 'sample-1.in'
            test_list[i][2]: True
            test_list[i][3]: '4'
        """

        # テストケースのファイル名一覧を取得
        in_list = glob.glob(abs_problem_dir_path + TEST_INPUT_PERTTERN)
        in_list.sort()
        
        # 期待値のファイル名一覧を取得
        out_name_list = glob.glob(abs_problem_dir_path + TEST_OUTPUT_PERTTERN)
        out_name_list.sort()

        # 期待値を抽出
        out_list = []
        for out in out_name_list:
            f = open(out)
            out_list.append(f.read().strip())
            f.close()

        # テスト情報のリストを作成
        test_list = []
        for i in range(len(in_list)):
            # テストケース名をテストケース名絶対パスから抽出
            matched = re.match(r'.+/([^/]+\.in)', in_list[i])
            test_case_name = matched.group(1)# 例) sample-1.in

            # 期待値が存在するか
            out_exists = True if out_list[i:i + 1] else False

            # 期待値
            out = out_list[i] if out_exists else ""
            
            # テスト情報を作成: [テストケースファイル名の絶対パス, テストケース名, 期待値ありフラグ, 期待値]
            test = [in_list[i], test_case_name, out_exists, out]
            
            test_list.append(test)
        
        return test_list
        
    def judge_python(self, abs_src_path: str, in_filename: str, test_case_name: str, out_exists: bool, out: str):
        """Pythonファイルのテスト実行＆ジャッジ
            
        テストを実行し，結果を期待値と比較して結果(AC or WA)を標準出力に出力します．
        期待値がなければ結果を出力します．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
            in_filename (str): テストケースのファイル名の絶対パス
            test_case_name (str): テストケース名
            out_exists (bool): 期待値存在フラグ
            out (str): 期待値
        """
        if out_exists:
            print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値あり） ----------")
        else:
            print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値なし） ----------")

        try:
            result_byte = subprocess.check_output(['python ' + abs_src_path + ' < ' + in_filename], shell=True)
            result = result_byte.decode().strip()
            
            # 期待値がない場合
            if not out_exists:
                print(result)
                print("")
                return

            if result == out:
                print(Decorate.BOLD + Color.GREEN + "[ AC ]" + Decorate.END)
            else:
                print(Decorate.BOLD + Color.RED + "[ WA ]" + Decorate.END)

            print(Decorate.BOLD + "Expected: " + Decorate.END)
            print(out)
            print(Decorate.BOLD + "Actual: " + Decorate.END)
            print(result)
            print("")

        except subprocess.CalledProcessError as e:
            print(e.output)
            
    def judge_cpp(self, abs_problem_dir_path: str, in_filename: str, test_case_name: str, out_exists: bool, out: str):
        """C++ ファイルのテスト実行＆ジャッジ
            
        テストを実行し，結果を期待値と比較して結果(AC or WA)を標準出力に出力します．
        期待値がなければ結果を出力します．

        Args:
            abs_problem_dir_path (str): 問題ディレクトリ
            in_filename (str): テストケースのファイル名の絶対パス
            test_case_name (str): テストケース名
            out_exists (bool): 期待値存在フラグ
            out (str): 期待値
        """
        if out_exists:
            print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値あり） ----------")
        else:
            print("---------- " + Decorate.BOLD + test_case_name + Decorate.END + " 実行結果（期待値なし） ----------")

        try:
            result_byte = subprocess.check_output([abs_problem_dir_path + '/' + CPP_EXEC_FILENAME + ' < ' + in_filename], shell=True)
            result = result_byte.decode().strip()
            
            # 期待値がない場合
            if not out_exists:
                print(result)
                print("")
                return
            
            if result == out:
                print(Decorate.BOLD + Color.GREEN + "[ AC ]" + Decorate.END)
            else:
                print(Decorate.BOLD + Color.RED + "[ WA ]" + Decorate.END)

            print(Decorate.BOLD + "Expected: " + Decorate.END)
            print(out)
            print(Decorate.BOLD + "Actual: " + Decorate.END)
            print(result)
            print("")

        except subprocess.CalledProcessError as e:
            print(e.output)
                             
    def run_test_python(self, abs_src_path: str, test_list):
        """Pythonテスト実行

        指定されたPythonファイルのテストを実行します．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
            test_list (ojb): テスト情報のリスト
        """
        # ジャッジを実行
        for i in range(len(test_list)):
            self.judge_python(abs_src_path, test_list[i][0], test_list[i][1], test_list[i][2], test_list[i][3])

    def run_test_cpp(self, abs_src_path: str, abs_problem_dir_path: str, test_list):
        """C++テスト実行

        指定された C++ ファイルのテストを実行します．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
            abs_problem_dir_path (str): 問題ディレクトリ
            test_list (ojb): テスト情報のリスト
        """
        # コンパイル
        try:
            print("■■■コンパイル開始")
            subprocess.check_output(['g++ -std=c++14 ' + abs_src_path + ' -o ' + abs_problem_dir_path + '/' + CPP_EXEC_FILENAME], shell=True)
            print("■■■コンパイル成功！")
        except subprocess.CalledProcessError as e:
            print("■■■コンパイル失敗... _(:3 」∠)_ _(┐「ε:)_")
            print(e.output)
            # 中断
            return

        # ジャッジを実行
        for i in range(len(test_list)):
            self.judge_cpp(abs_problem_dir_path, test_list[i][0], test_list[i][1], test_list[i][2], test_list[i][3])
                
    def run_test(self, abs_src_path: str):
        """テスト実行

        指定されたファイルを実行します．

        Args:
            abs_src_path (str): 変更があったファイルの絶対パス
        """
        print("■■■ 変更されたファイル: " + abs_src_path)

        # 変更されたファイル名などを絶対パスから抽出
        matched = re.match(r'(.+/[^/]+/[^/]+/)(([^/]+)\.(py|cpp))', abs_src_path)

        # 変更されたファイル名
        file_name = matched.group(2) # 例) 「a.py」 or 「a.cpp」
        # print("■■■ 変更されたファイル名: " + file_name)

        # 変更されたファイルの拡張子
        extension = matched.group(4) # 例) py or cpp
        # print("■■■ 変更されたファイルの拡張子: " + extension)

        # 問題ディレクトリ(a, b, c, d, e, f)
        abs_problem_dir_path = matched.group(1) # 例）/Users/[USERNAME]/atcoder-playground/abc/abc202/a/
        print("■■■ テストケースディレクトリ: " + abs_problem_dir_path)
                
        # テスト情報一覧を取得
        test_list = self.get_test_list(abs_problem_dir_path)
        print("■■■ テスト情報一覧：")
        for item in test_list:
            print(item)
        
        # テストケースが 0 件なら処理終了
        if len(test_list) == 0:
            print("■■■ テストケースが存在しないためテストを中断します．")
            return

        print("")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 実行ファイル: " + file_name)
        print("")

        if extension == 'py':
            # Python のテストを実行
            self.run_test_python(abs_src_path, test_list)
        elif extension == 'cpp':
            # C++ のテストを実行
            self.run_test_cpp(abs_src_path, abs_problem_dir_path, test_list)
        else:
            print("サポートされていない拡張子です．拡張子:", extension)
    
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
    
    print("■■■ ファイル監視を開始します．") 

    # 現在のディレクトリの絶対パスを取得
    current_directory = os.getcwd()
    print("■■■ watch.py 実行ディレクトリ: " + current_directory) 

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
        print("■■■ ファイル監視を終了します．")
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    print("■■■ メイン関数を実行します．")
    watch()
    print("■■■ メイン関数を終了します．")
