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
LATEST_CONTEST=202

### 大問名の配列
PARTS=()
PARTS[0]=a
PARTS[1]=b
PARTS[2]=c
PARTS[3]=d
PARTS[4]=e
PARTS[5]=f

### 大問ごとの AC数
ac_count=()
ac_count[0]=0 # A の AC数
ac_count[1]=0 # B の AC数
ac_count[2]=0 # C の AC数
ac_count[3]=0 # D の AC数
ac_count[4]=0 # E の AC数
ac_count[5]=0 # F の AC数

### 大問の問題数
# sum=()
# sum[0]=0 # A の 問題数
# sum[1]=0 # B の 問題数
# sum[2]=0 # C の 問題数
# sum[3]=0 # D の 問題数
# sum[4]=0 # E の 問題数
# sum[5]=0 # F の 問題数

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
        # python ファイル名
        PY_FILE=${TARGET_DIR}${PARTS[j]}/abc${i}_${PARTS[j]}.py
        
        if [ ! -e ${PY_FILE} ]; then
            # ファイルが存在しなかった場合
            RECORD="${RECORD} ー |"
        elif [ ! -s ${PY_FILE} ]; then
            # ファイルサイズがゼロの場合
            RECORD="${RECORD} × |"
            # 問題数合計をインクリメント
            # sum[j]=$((++sum[j]))
        else
            # ファイルサイズがゼロでない場合（ACしているとみなす）
            RECORD="${RECORD} ● |"
            # 問題数合計をインクリメント
            # sum[j]=$((++sum[j]))
            # AC数合計をインクリメント
            ac_count[j]=$((++ac_count[j]))
        fi
    done
    TABLE=${TABLE}${RECORD}$'\n'
done



# ==================== ファイルへ書き込み ====================

# ヘッダを書き込み
echo "# AtCoder AC 状況" >> ${AC_STATUS_FILE}

# AC サマリを書き込み
# echo "## AC 状況サマリ" >> ${AC_STATUS_FILE}
# echo "| Question | AC 数/問題数 | AC 率 |" >> ${AC_STATUS_FILE}
# echo "| :----: | ----: | ----: |" >> ${AC_STATUS_FILE}
# for i in {0..5}; do
#     # AC 率
#     ratio=`echo "scale=5; ${ac_count[i]} / ${sum[i]} * 100" | bc`
#     ratio=`printf "%.2f" ${ratio}`
#     # 例）A: 3/201 (0.015 %)
#     echo "acカウント ${ac_count[i]}"
#     echo "sum ${sum[i]}"
#     echo "| ${PARTS[i]} | ${ac_count[i]}/${sum[i]} | ${ratio} % |" >> ${AC_STATUS_FILE}
# done
echo "## AC 状況サマリ" >> ${AC_STATUS_FILE}
echo "| Question | AC 数 |" >> ${AC_STATUS_FILE}
echo "| :----: | ----: |" >> ${AC_STATUS_FILE}
for i in {0..5}; do
    echo "| ${PARTS[i]} | ${ac_count[i]} |" >> ${AC_STATUS_FILE}
done

# markdown テーブルを書き込み
echo "## AC 状況" >> ${AC_STATUS_FILE}
echo "| Contest | A | B | C | D | E | F |" >> ${AC_STATUS_FILE}
echo "| :----: | :----: | :----: | :----: | :----: | :----: | :----: |" >> ${AC_STATUS_FILE}
echo "${TABLE}" >> ${AC_STATUS_FILE}

# 標準出力
head -n 10 ./ac_status.md
