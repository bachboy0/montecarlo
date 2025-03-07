# Monte Carlo Method for Pi Estimation

英語の後に日本語の説明が続きます。
영어, 일본어에 이어 한국어 설명이 있습니다.

## Overview

This project provides a simple simulation of the Monte Carlo method to estimate the value of π (pi). It works by randomly generating points within a unit square and calculating what fraction of those points fall within a quarter circle of radius 1.

## File Structure

The project consists of the following files:
- main.py: Entry point of the program
- monte_carlogic.py: Core logic for the Monte Carlo simulation
- monte_plot.py: Visualization functionality
- input_validation.py: User input handling and validation

## Visualization

The program offers visualization of the Monte Carlo simulation. When prompted, you can choose to generate a plot showing:
- A unit square (blue outline)
- A circle with radius 0.5 (green outline)
- Random points generated during simulation (red dots)

If the plotting functionality doesn't work in your environment, the plot will be saved as "monte_carlo_plot.png" in the current directory.

## How to Run

```bash
# Navigate to the project directory
cd /path/to/montecarlo

# Activate virtual environment (if created)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Run the program
python main.py
```

## Requirements

- Python 3.x
- NumPy
- Matplotlib

To install the required packages:

```bash
pip install numpy matplotlib
```

## Note

The maximum input value is limited to 16,777,216 (2^24) to prevent memory issues with large simulations.

---

# モンテカルロ法によるπの推定

## 概要

このプロジェクトは、モンテカルロ法を使用してπ（円周率）の値を推定する簡単なシミュレーションを提供します。単位正方形内にランダムな点を生成し、半径1の四分円内に落ちる点の割合を計算することで動作します。

## ファイル構成

このプロジェクトは以下のファイルで構成されています：
- main.py: プログラムのエントリーポイント
- monte_carlogic.py: モンテカルロシミュレーションのコアロジック
- monte_plot.py: 視覚化機能
- input_validation.py: ユーザー入力の処理とバリデーション

## 視覚化

このプログラムはモンテカルロシミュレーションの視覚化を提供します。プロンプトが表示されたら、以下を表示するプロットを生成するかどうかを選択できます：
- 単位正方形（青い輪郭）
- 半径0.5の円（緑の輪郭）
- シミュレーション中に生成されたランダムな点（赤い点）

お使いの環境でプロット機能が動作しない場合、プロットは現在のディレクトリに「monte_carlo_plot.png」として保存されます。

## 実行方法

```bash
# プロジェクトディレクトリに移動
cd /path/to/montecarlo

# 仮想環境を有効化（作成した場合）
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate  # Windows

# プログラムを実行
python main.py
```

## 必要条件

- Python 3.x
- NumPy
- Matplotlib

必要なパッケージをインストールするには：

```bash
pip install numpy matplotlib
```

## 注意

入力値の上限は16,777,216（2^24）に制限されています。これは、大規模なシミュレーションでのメモリ問題を防ぐためです。

---

# 몬테카를로 방식을 이용한 π 추정

## 개요

이 프로젝트는 몬테카를로 방식을 사용하여 π(파이) 값을 추정하는 간단한 시뮬레이션을 제공합니다. 단위 정사각형 내에서 무작위 점을 생성하고, 반지름 1의 사분원 안에 들어가는 점의 비율을 계산하는 방식으로 동작합니다.

## 파일 구조

이 프로젝트는 다음 파일들로 구성되어 있습니다:
- main.py: 프로그램의 진입점
- monte_carlogic.py: 몬테카를로 시뮬레이션의 핵심 로직
- monte_plot.py: 시각화 기능
- input_validation.py: 사용자 입력 처리 및 검증

## 시각화

이 프로그램은 몬테카를로 시뮬레이션의 시각화를 제공합니다. 메시지가 표시되면 다음을 보여주는 플롯을 생성할지 여부를 선택할 수 있습니다:
- 단위 정사각형(파란색 윤곽선)
- 반경 0.5의 원(초록색 윤곽선)
- 시뮬레이션 중 생성된 무작위 점(빨간색 점)

환경에서 플롯 기능이 작동하지 않는 경우, 플롯은 현재 디렉토리에 "monte_carlo_plot.png"로 저장됩니다.

## 실행 방법

```bash
# 프로젝트 디렉토리로 이동
cd /path/to/montecarlo

# 가상 환경 활성화(생성한 경우)
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows

# 프로그램 실행
python main.py
```

## 요구 사항

- Python 3.x
- NumPy
- Matplotlib

필요한 패키지 설치:

```bash
pip install numpy matplotlib
```

## 참고

입력값의 상한은 16,777,216(2^24)으로 제한되어 있습니다. 이는 대규모 시뮬레이션에서 메모리 문제를 방지하기 위함입니다.