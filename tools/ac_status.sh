#!/bin/bash

### ========================================
### Python と C++ 別に AC 状況を可視化します.
###
### 使用方法
###     ./tools 配下で以下を実行
###     $ ./ac_status.sh
### ========================================

# ==================== 定数定義 ====================

### 最新のコンテスト番号
LATEST_CONTEST=204

### 大問名の配列
PARTS=()
PARTS[0]=a
PARTS[1]=b
PARTS[2]=c
PARTS[3]=d
PARTS[4]=e
PARTS[5]=f

### 大問ごとの Python のAC数
ac_py_count=()
ac_py_count[0]=0 # A の AC数
ac_py_count[1]=0 # B の AC数
ac_py_count[2]=0 # C の AC数
ac_py_count[3]=0 # D の AC数
ac_py_count[4]=0 # E の AC数
ac_py_count[5]=0 # F の AC数

### 大問ごとの C++ のAC数
ac_cpp_count=()
ac_cpp_count[0]=0 # A の AC数
ac_cpp_count[1]=0 # B の AC数
ac_cpp_count[2]=0 # C の AC数
ac_cpp_count[3]=0 # D の AC数
ac_cpp_count[4]=0 # E の AC数
ac_cpp_count[5]=0 # F の AC数

### 大問の問題数
sum=()
sum[0]=0 # A の 問題数
sum[1]=0 # B の 問題数
sum[2]=0 # C の 問題数
sum[3]=0 # D の 問題数
sum[4]=0 # E の 問題数
sum[5]=0 # F の 問題数

### AC 状況を可視化する markdown ファイル
AC_STATUS_FILE="./ac_status.md"



# ==================== markdown のテーブルを作成する処理 ====================

# markdown ファイルを再作成
rm -f ${AC_STATUS_FILE}
touch ${AC_STATUS_FILE}

# AC 状況の markdown テーブルを作成
TABLE=""
for i in `seq -w ${LATEST_CONTEST} 1` ; do
    # コンテストディレクトリ
    TARGET_DIR=../abc/abc${i}/
    # レコード
    RECORD="| ABC_${i} |"
    # 大問のループ
    for j in {0..5}; do
        # 大問ディレクトリ
        DIR=${TARGET_DIR}${PARTS[j]}/
        # Python, C++ ファイル名
        PY_FILE=${TARGET_DIR}${PARTS[j]}/abc${i}_${PARTS[j]}.py
        CPP_FILE=${TARGET_DIR}${PARTS[j]}/abc${i}_${PARTS[j]}.cpp
    
        # 大問ディレクトリが存在する場合
        if [ -d ${DIR} ]; then
            # 問題数合計をインクリメント
            sum[j]=$((++sum[j]))
        fi

        if [ ! -e ${PY_FILE} ]; then
            # Python ファイルが存在しなかった場合
            RECORD="${RECORD} ー"
        elif [ ! -s ${PY_FILE} ]; then
            # Python ファイルのサイズがゼロ場合
            RECORD="${RECORD} ×"
        elif [ -s ${PY_FILE} ]; then
            # Python ファイルのサイズがゼロよりおおきい場合（ACとみなす）
            RECORD="${RECORD} ●"
            # AC数合計をインクリメント
            ac_py_count[j]=$((++ac_py_count[j]))
        fi

        if [ ! -e ${CPP_FILE} ]; then
            # C++ ファイルが存在しなかった場合
            RECORD="${RECORD} ー"
        elif [ ! -s ${CPP_FILE} ]; then
            # C++ ファイルのサイズがゼロ場合
            RECORD="${RECORD} ×"
        elif [ -s ${CPP_FILE} ]; then
            # C++ ファイルのサイズがゼロよりおおきい場合（ACとみなす）
            RECORD="${RECORD} ★"
            # AC数合計をインクリメント
            ac_cpp_count[j]=$((++ac_cpp_count[j]))
        fi
        
        RECORD="${RECORD} |"

    done
    TABLE=${TABLE}${RECORD}$'\n'
done



# ==================== ファイルへ書き込み ====================

# ヘッダを書き込み
echo "# AtCoder AC 状況" >> ${AC_STATUS_FILE}

# AC サマリを書き込み
echo "## AC 状況サマリ" >> ${AC_STATUS_FILE}
echo "| Question | AC 数(py)/問題数 | AC 率(py) | AC 数(C++)/問題数 | AC 率(C++) |" >> ${AC_STATUS_FILE}
echo "| :----: | ----: | ----: | ----: | ----: |" >> ${AC_STATUS_FILE}
for i in {0..5}; do
    # AC 率
    ratio_py=`echo "scale=5; ${ac_py_count[i]} / ${sum[i]} * 100" | bc`
    ratio_py=`printf "%.2f" ${ratio_py}`
    ratio_cpp=`echo "scale=5; ${ac_cpp_count[i]} / ${sum[i]} * 100" | bc`
    ratio_cpp=`printf "%.2f" ${ratio_cpp}`
    # 例）A: 3/201 (0.015 %)
    echo "| ${PARTS[i]} | ${ac_py_count[i]}/${sum[i]} | ${ratio_py} % | ${ac_cpp_count[i]}/${sum[i]} | ${ratio_cpp} % " >> ${AC_STATUS_FILE}
done


# markdown テーブルを書き込み
echo "## AC 状況" >> ${AC_STATUS_FILE}
echo "### ●：Python AC, ★：C++ AC, ×：ファイルサイズゼロ, ー：ファイルなし" >> ${AC_STATUS_FILE}
echo "| Contest | A | B | C | D | E | F |" >> ${AC_STATUS_FILE}
echo "| :----: | :----: | :----: | :----: | :----: | :----: | :----: |" >> ${AC_STATUS_FILE}
echo "${TABLE}" >> ${AC_STATUS_FILE}

# 標準出力
head -n 10 ./ac_status.md
