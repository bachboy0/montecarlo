英語版の後に日本語版がございます。
영어판, 일본어판 뒤에 한국어판이 있습니다.

# Calculating π using the Monte Carlo Method

This project is a Python program that estimates the value of pi (π) using the Monte Carlo method.

## Overview

The Monte Carlo method is a technique that uses probabilistic simulations for numerical calculations. In this implementation, random points are generated within a unit square, and the ratio of points falling within a unit circle is used to estimate the value of π.

## How it Works

1. Random (x,y) coordinates are generated in the range from 0 to 1
2. The program determines whether the point is inside a circle with center (0.5,0.5) and radius 0.5
3. After simulating a sufficient number of points, π is estimated from the ratio of points inside the circle

## Usage

1. Run the program
2. Enter the number of points (a natural number) to be generated in the simulation
3. Enter 0 to exit the program

## Requirements

- Python 3.x
- NumPy library

## Installation

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install required libraries
pip install numpy
```

## Example Output

```
Welcome to Monte Carlo
This is a simulation to find Pi using the Monte Carlo Method.
Please enter any natural number to see how the Monte Carlo Method works!
If you would like to quit, enter number 0.

Enter natural number: 1000000

Attempts: 1000000
Points inside the circle: 785398
Points outside the circle: 214602
Probability of points inside the circle: 0.7854
Area of the circle: 0.7854
Approximate value of Pi derived from the Monte Carlo Method: 
3.14159200
Pi from Python numpy: 
3.14159265
Error between Pi from Python numpy and Pi from the Monte Carlo Method: 
6.5e-07
```

## Notes

The maximum input value is limited to 16777216. Larger values might take too much time to compute.



# モンテカルロ法によるπの計算

このプロジェクトは、モンテカルロ法を使って円周率（π）の値を推定するPythonプログラムです。

## 概要

モンテカルロ法は確率的なシミュレーションを用いて数値計算を行う手法です。この実装では、単位正方形内にランダムな点を生成し、その中で単位円内に入る点の割合からπの値を推定します。

## 仕組み

1. 0から1までの範囲でランダムな(x,y)座標を生成します
2. 点が中心(0.5,0.5)、半径0.5の円の内側にあるかを判定します
3. 十分な数の点をシミュレーションした後、円内の点の割合から円周率πを推定します

## 使い方

1. プログラムを実行します
2. シミュレーションで生成する点の数（自然数）を入力します
3. 0を入力するとプログラムを終了します

## 必要条件

- Python 3.x
- NumPy ライブラリ

## インストール方法

```bash
# 仮想環境の作成（推奨）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate  # Windows

# 必要ライブラリのインストール
pip install numpy
```

## 実行例

```
Welcome to Monte Carlo
This is a simulation to find Pi using the Monte Carlo Method.
Please enter any natural number to see how the Monte Carlo Method works!
If you would like to quit, enter number 0.

Enter natural number: 1000000

Attempts: 1000000
Points inside the circle: 785398
Points outside the circle: 214602
Probability of points inside the circle: 0.7854
Area of the circle: 0.7854
Approximate value of Pi derived from the Monte Carlo Method: 
3.14159200
Pi from Python numpy: 
3.14159265
Error between Pi from Python numpy and Pi from the Monte Carlo Method: 
6.5e-07
```

## 注意事項

入力値の上限は16777216です。それ以上の値を入力すると、計算に時間がかかりすぎる可能性があります。



# 몬테카를로 방식을 이용한 π 계산

이 프로젝트는 몬테카를로 방식을 사용하여 원주율(π)의 값을 추정하는 파이썬 프로그램입니다.

## 개요

몬테카를로 방식은 확률적 시뮬레이션을 사용하여 수치 계산을 수행하는 기법입니다. 이 구현에서는 단위 정사각형 내에 무작위 점을 생성하고, 그 중 단위 원 내에 들어가는 점의 비율로부터 π 값을 추정합니다.

## 작동 원리

1. 0에서 1 사이의 범위에서 무작위 (x,y) 좌표를 생성합니다
2. 점이 중심(0.5,0.5), 반경 0.5인 원 안에 있는지 판정합니다
3. 충분한 수의 점을 시뮬레이션한 후, 원 안에 있는 점의 비율로부터 원주율 π를 추정합니다

## 사용법

1. 프로그램을 실행합니다
2. 시뮬레이션에서 생성할 점의 수(자연수)를 입력합니다
3. 0을 입력하면 프로그램을 종료합니다

## 필요 조건

- Python 3.x
- NumPy 라이브러리

## 설치 방법

```bash
# 가상 환경 생성(권장)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows

# 필요한 라이브러리 설치
pip install numpy
```

## 실행 예시

```
Welcome to Monte Carlo
This is a simulation to find Pi using the Monte Carlo Method.
Please enter any natural number to see how the Monte Carlo Method works!
If you would like to quit, enter number 0.

Enter natural number: 1000000

Attempts: 1000000
Points inside the circle: 785398
Points outside the circle: 214602
Probability of points inside the circle: 0.7854
Area of the circle: 0.7854
Approximate value of Pi derived from the Monte Carlo Method: 
3.14159200
Pi from Python numpy: 
3.14159265
Error between Pi from Python numpy and Pi from the Monte Carlo Method: 
6.5e-07
```

## 주의사항

입력값의 상한은 16777216입니다. 그 이상의 값을 입력하면 계산에 너무 많은 시간이 걸릴 수 있습니다.

