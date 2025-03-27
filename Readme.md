# Monte Carlo Method for Pi Estimation

## Overview

This project simulates the estimation of π (Pi) using the Monte Carlo method.
It randomly generates points and evaluates them against a circle to approximate π.

## File Structure

The project is composed of the following files:

- **main.py**:  
  The entry point for the application. It manages user interaction, gathers input, and runs the simulation.
  
- **monte_carlogic.py**:  
  Contains the core logic for running the Monte Carlo simulation and evaluating the results.
  
- **monte_plot.py**:  
  Provides visualization for the simulation by plotting points, a square, and a circle.
  
- **input_validation.py**:  
  Handles user input and validation of numerical values and the circle’s radius.

## Visualization

Users can visualize the simulation process and results. The generated plots display:
- A square and a circle for reference.
- Points generated during simulation.

If interactive display is not available, the plot will be saved as "monte_carlo_plot.png" in the current directory.

## How to Run

```bash
# Navigate to the project directory
cd /path/to/your/montecarlo

# Activate virtual environment (if created)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Run the main program
python main.py
```

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required packages with:

```bash
pip install numpy matplotlib
```

---

# モンテカルロ法によるπの推定

## 概要

このプロジェクトは、モンテカルロ法を使用してπ（円周率）の推定を行います。
ランダムな点を生成し、円と比較することでπの近似値を求めます。

## ファイル構成

プロジェクトは以下のファイルで構成されています：

- **main.py**:  
  アプリケーションのエントリーポイント。ユーザーとの対話、入力の取得、およびシミュレーションの実行を管理します。
  
- **monte_carlogic.py**:  
  モンテカルロ法によるシミュレーションのコアロジックと、結果の評価を含む機能を提供します。
  
- **monte_plot.py**:  
  シミュレーション結果の視覚化を行うため、点、正方形、円をプロットで表示します。
  
- **input_validation.py**:  
  ユーザー入力の処理と、数値や円の半径のバリデーションを担当します。

## 視覚化

シミュレーションの過程とその結果を視覚化できます。生成されるプロットは以下の要素を含みます：
- 参照用の正方形と円
- シミュレーション中に生成された点

インタラクティブな表示が利用できない場合、プロットはカレントディレクトリ内に「monte_carlo_plot.png」として保存されます。

## 実行方法

```bash
# プロジェクトディレクトリに移動
cd /path/to/your/montecarlo

# 仮想環境を有効化（作成済みの場合）
source venv/bin/activate  # Linux/Mac用
# または
venv\Scripts\activate  # Windows用

# プログラムの実行
python main.py
```

## 必要条件

- Python 3.x
- NumPy
- Matplotlib

以下のコマンドで必要パッケージをインストールしてください：

```bash
pip install numpy matplotlib
```

---

# 몬테카를로 방식을 이용한 π 추정

## 개요

이 프로젝트는 몬테카를로 방식을 사용하여 π (파이)를 추정합니다.
무작위로 점을 생성하고, 원과 비교하여 π의 근사값을 계산합니다.

## 파일 구조

프로젝트는 다음 파일들로 구성되어 있습니다:

- **main.py**:  
  프로그램의 진입점으로, 사용자와의 상호작용, 입력 처리 및 시뮬레이션 실행을 담당합니다.
  
- **monte_carlogic.py**:  
  몬테카를로 시뮬레이션의 핵심 로직과 결과 평가 기능을 포함합니다.
  
- **monte_plot.py**:  
  시뮬레이션 결과를 시각화하기 위해 점, 정사각형, 원을 플롯합니다.
  
- **input_validation.py**:  
  사용자 입력 처리와 숫자, 원의 반지름에 대한 유효성 검사를 수행합니다.

## 시각화

사용자는 시뮬레이션 과정과 결과를 시각화할 수 있습니다. 생성된 플롯에는 다음 요소가 포함됩니다:
- 기준이 되는 정사각형과 원
- 시뮬레이션 중 생성된 무작위 점들

만약 인터랙티브한 표시가 불가능할 경우, 플롯은 현재 디렉토리에 "monte_carlo_plot.png" 파일로 저장됩니다.

## 실행 방법

```bash
# 프로젝트 디렉토리로 이동
cd /path/to/your/montecarlo

# 가상 환경 활성화(생성된 경우)
source venv/bin/activate  # Linux/Mac용
# 또는
venv\Scripts\activate  # Windows용

# 프로그램 실행
python main.py
```

## 요구 사항

- Python 3.x
- NumPy
- Matplotlib

필요한 패키지는 다음 명령어로 설치할 수 있습니다:

```bash
pip install numpy matplotlib
```