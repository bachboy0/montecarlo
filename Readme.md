日本語は英語の後に続きます。

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

