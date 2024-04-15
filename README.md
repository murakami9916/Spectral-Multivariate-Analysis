[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# スペクトル多変量解析

## 目的

$M$個の計測スペクトルデータ群$`\mathcal{Y}=\{\boldsymbol{y}_m\}_{m=1}^{M}`$を多変量解析するプログラム．

## こだわりポイント

本プログラムは，基準とするスペクトルからの距離（距離スペクトル）$`\boldsymbol{d}_m=D(\boldsymbol{s}, \boldsymbol{y}_m)`$を入力とすることがポイントである．

距離関数$`D(\boldsymbol{s}, \boldsymbol{y}_m)`$として，以下の関数を提供する：
- 残差二乗平方根
$$\boldsymbol{d}_m = \sqrt{(\boldsymbol{s}-\boldsymbol{y}_m)^2}$$

スペクトルデータの多変量解析は，データ前処理方法が重要となる．
このプログラムはスペクトルデータに特化して，いくつかの前処理フローを提供している．
- 対数スケールへの変換
- 差分スペクトルの符号を反映

## 使い方
### インストール方法
### テスト方法
### デプロイ方法

## 解析結果

![image](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/f8b0488b-9a4a-4f34-9d1e-fa4232d49c1e)

![image](https://github.com/murakami9916/Spectral-Multivariate-Analysis/assets/34080190/16220edd-0587-4fca-b024-8d28f3cfd772)

