[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# スペクトル多変量解析

## 目的

$M$個の計測スペクトルデータ群$`\mathcal{Y}=\{{y}_m\}_{m=1}^{M}`$を多変量解析するプログラム．

## こだわりポイント

本プログラムは，基準とするスペクトル$`{s}`$からの距離（距離スペクトル）$`{d}_m=D( {s}, {y}_m )`$を入力とすることがポイントである．

※ スペクトルデータをそのまま入力することもできる．

### 距離関数の設計
距離関数$`D({s}, {y}_m)`$として，以下の関数を提供する：
- 残差二乗平方根 &nbsp; $`{d}_m = \sqrt{({s} - {y}_m)^2}`$
- 負のポアソン対数尤度 &nbsp; $`{d}_m = -\ln{ \mathcal{P}({y}_m | {s}) }`$

### 前処理の設計
スペクトルデータの多変量解析は，データ前処理方法が重要となる．
このプログラムはスペクトルデータに特化して，いくつかの前処理フローを提供している：このとき，前処理したデータ$`{s}'=f({s})`$, $`{y}'_m=f(h {y}_m)`$を入力として，$`{d}_m=D( {s}', {y}'_m )`$が多変量解析の入力行列となる．

- `is_log` 対数スケールへの変換 &nbsp; $`f(x)=\ln{x}`$　（※ 線形スケールの場合は，$`f(x)=x`$）
- `is_sign` 差分スペクトルの符号を反映 &nbsp; $`{d}_m=\mbox{sign}({s} - {y}_m) D( {s}, {y}_m )`$
- `is_scale` 強度スケールの補正 &nbsp; $`h{y}_m`$ （※ 補正なしの場合は，$`h=1`$）

## 使い方

### 構成
- data
  - サンプルデータ(XPSサーベイデータ)
- sample
  - チュートリアルのノートブック
- src
  - スペクトル多変量解析ライブラリ

### 必要なライブラリ
- numpy==1.4.2
- pandas==2.2.2
- scipy==1.13.0
- matplotlib==3.8.4
- scikit-learn==1.4.2

## デモ用のデータ

Si基板上に厚さ$`T`$[nm]の酸化インジウムを成膜した試料のXPSサーベイシミュレーションデータ

![input_data](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/cceb39aa-4c12-4f72-864f-57340ee3fe27)

## 解析結果

### 獲得された基底関数

![basis](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/4c285323-e849-4e10-a5e8-e93b25dd55b8)

### 係数と物理パラメータの関係

![result](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/e86b5101-ad3f-4dc4-8316-72f067a504e9)

## 著者
MURAKAMI Ryo

E-mail: MURAKAMI.Ryo@nims.go.jp
