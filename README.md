[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# スペクトル多変量解析

## 目的

$M$個の計測スペクトルデータ群$`\mathcal{Y}=\{\boldsymbol{y}_m\}_{m=1}^{M}`$を多変量解析するプログラム．

## こだわりポイント

本プログラムは，基準とするスペクトル$`\boldsymbol{s}`$からの距離（距離スペクトル）$`\boldsymbol{d}_m=D( \boldsymbol{s}, \boldsymbol{y}_m )`$を入力とすることがポイントである．

※ スペクトルデータをそのまま入力することもできる．

### 距離関数の設計
距離関数$`D(\boldsymbol{s}, \boldsymbol{y}_m)`$として，以下の関数を提供する：
- 残差二乗平方根 &nbsp; $`\boldsymbol{d}_m = \sqrt{(\boldsymbol{s} - \boldsymbol{y}_m)^2}`$
- 負のポアソン対数尤度 &nbsp; $`\boldsymbol{d}_m = -\ln{ \mathcal{P}(\boldsymbol{y}_m | \boldsymbol{s}) }`$

### 前処理の設計
スペクトルデータの多変量解析は，データ前処理方法が重要となる．
このプログラムはスペクトルデータに特化して，いくつかの前処理フローを提供している：このとき，前処理したデータ$`\boldsymbol{s}'=f(\boldsymbol{s})`$, $`\boldsymbol{y}'_m=f(h\boldsymbol{y}_m)`$を入力として，$`\boldsymbol{d}_m=D( \boldsymbol{s}', \boldsymbol{y}'_m )`$が多変量解析の入力行列となる．

- `is_log` 対数スケールへの変換 &nbsp; $`f(x)=\ln{x}`$　（※ 線形スケールの場合は，$`f(x)=x`$）
- `is_sign` 差分スペクトルの符号を反映 &nbsp; $`\boldsymbol{d}_m=\mbox{sign}(\boldsymbol{s} - \boldsymbol{y}_m) D( \boldsymbol{s}, \boldsymbol{y}_m )`$
- `is_scale` 強度スケールの補正 &nbsp; $`h\boldsymbol{y}_m`$ （※ 補正なしの場合は，$`h=1`$）

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

### テスト方法

### デプロイ方法

## 解析結果

![image](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/f8b0488b-9a4a-4f34-9d1e-fa4232d49c1e)

![image](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/16220edd-0587-4fca-b024-8d28f3cfd772)

## 著者
MURAKAMI Ryo
E-mail: MURAKAMI.Ryo@nims.go.jp
