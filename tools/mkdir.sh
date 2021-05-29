#!/bin/bash

### atcoder/cli を使っているため，こちらは現在は使用していない

# 大問名の配列
PARTS=()
PARTS[0]=A
PARTS[1]=B
PARTS[2]=C
PARTS[3]=D

for i in `seq -w 1 125` ; do
    # コンテストディレクトリ
    TARGET_DIR=ABC_${i}/
    # コンテストディレクトリを生成
    mkdir -p ${TARGET_DIR}

    for e in ${PARTS[@]}; do
        # python ファイルを生成
        touch ${TARGET_DIR}${e}.py
        # テストケースディレクトリ
        TEST_CASE_DIR=${TARGET_DIR}${e}_TestCases/
        # テストケースディレクトリを生成
        mkdir -p ${TEST_CASE_DIR}
        # テストケースを生成
        touch ${TEST_CASE_DIR}${e}_1.in
        touch ${TEST_CASE_DIR}${e}_2.in
        touch ${TEST_CASE_DIR}${e}_3.in
    done
done

PARTS[4]=E
PARTS[5]=F

for i in `seq -w 126 250` ; do
    # コンテストディレクトリ
    TARGET_DIR=ABC_${i}/
    # コンテストディレクトリを生成
    mkdir -p ${TARGET_DIR}

    for e in ${PARTS[@]}; do
        # python ファイルを生成
        touch ${TARGET_DIR}${e}.py
        # テストケースディレクトリ
        TEST_CASE_DIR=${TARGET_DIR}${e}_TestCases/
        # テストケースディレクトリを生成
        mkdir -p ${TEST_CASE_DIR}
        # テストケースを生成
        touch ${TEST_CASE_DIR}${e}_1.in
        touch ${TEST_CASE_DIR}${e}_2.in
        touch ${TEST_CASE_DIR}${e}_3.in
    done
done
