# Finance Analysis

Pythonを用いて株価データ・企業財務データを取得し、投資判断に活用するための分析ツール。

## Overview

本プロジェクトの目的は以下の3点である。

1. Pythonの学習
2. 株式分析の自動化
3. AIを活用した投資判断支援

株価データは主にYahoo Finance（yfinance）から取得し、企業情報・財務情報はJ-Quantsから取得する。

将来的にはChatGPT APIと連携し、自動で分析レポートを生成することを目指す。

---

## Features

現在実装済み

- [ ] yfinanceによる株価取得
- [ ] 株価データのCSV保存
- [ ] テクニカル指標の計算
- [ ] J-Quants連携
- [ ] AI分析レポート生成

---

## Technology Stack

- Python 3.14
- VSCode
- Git / GitHub
- pandas
- yfinance
- J-Quants API（予定）
- OpenAI API（予定）

---

## Development Policy

- 学習目的のため、可能な限り自分で実装する
- AIは補助的に利用する
- 実運用前に取得データの妥当性を確認する
- 投資判断は最終的に自身で行う

---

## Roadmap

### Phase 1

- yfinanceで株価取得
- CSV保存

### Phase 2

- 移動平均線
- RSI
- MACD

### Phase 3

- J-Quants連携
- 財務データ取得

### Phase 4

- ChatGPT連携
- 自動分析レポート生成

### Phase 5

- ポートフォリオ分析
- ダッシュボード化

---

## License

Private Project
