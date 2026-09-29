<p align="center">
  <img src="assets/seedance-25-hero.png" alt="画像、動画、音声、カメラ、連続性のリファレンスを一つの完成ショットへ統合する映画的な Seedance 2.5 ディレクションコンソール" width="100%">
</p>

<h1 align="center">Seedance 2.5 Director</h1>

<p align="center">
  <strong>シーンを演出し、リファレンスを結び、状態をつなぐ。</strong><br>
  アイデア、脚本、マルチモーダル素材を制作に使える Seedance 2.5 プロンプトへ変換する Agent Skill。
</p>

<p align="center">
  <img alt="Seedance 2.5" src="https://img.shields.io/badge/Seedance-2.5-7c5cff?style=flat-square">
  <img alt="Agent Skill" src="https://img.shields.io/badge/Agent-Skill-45c8ff?style=flat-square">
  <img alt="ドキュメント言語：日本語" src="https://img.shields.io/badge/Docs-Japanese-1f9d8a?style=flat-square">
  <img alt="プロンプトリンター同梱" src="https://img.shields.io/badge/Prompt_Linter-Included-f2a750?style=flat-square">
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>日本語</strong>
</p>

<p align="center">
  <a href="#このリポジトリが必要な理由">目的</a> ·
  <a href="#この-skill-でできること">機能</a> ·
  <a href="#ここから始める">はじめに</a> ·
  <a href="#インストール">インストール</a> ·
  <a href="#skill-の使い方">使い方</a> ·
  <a href="#プロンプトリンター">Lint</a> ·
  <a href="#公式情報の境界">情報源</a>
</p>

---

## このリポジトリが必要な理由

Seedance 2.5 はテキスト、画像、動画、音声を入力できます。しかし、入力を増やすだけで制御性が高まるわけではありません。複雑な生成は、主に次のような構造上の理由で失敗します。

- 複数のリファレンスが同じ出力要素の主導権を奪い合う。
- キャラクター、プロップ、台詞が明確な担当主体に結び付いていない。
- 一つのショットに、尺が処理できる以上のイベントを詰め込んでいる。
- カメラ演出が決定的なアクションを隠している。
- 編集で、単一のマスター動画と編集範囲が定義されていない。
- 延長で、実際に生成された境界ではなく、計画上の終点を引き継いでいる。
- 再試行で多くの変数を同時に変え、何が改善に効いたのか判断できない。

このリポジトリは、こうした繰り返し発生する制作上の問題を、一つの再利用可能な Agent Skill にまとめます。短いアイデアを形容詞の長い列に膨らませるのではありません。まず各素材が何を制御するかを決め、その後に見えるアクション、カメラ、照明、演技、音、連続性、最終状態を演出します。

その結果、生成、レビュー、修正、別の共同制作者への引き継ぎがしやすいプロンプトになります。

## この Skill でできること

`seedance-25` は、Agent が次の作業を行うための Skill です。

- ブリーフから新しい Seedance 2.5 プロンプトを作成する。
- 既存プロンプトを修正、圧縮、翻訳する。
- 文章を書く前に適切な生成経路を選ぶ。
- 画像、動画、音声リファレンスに明確な役割を割り当てる。
- 標準生成、段階生成、複数クリップによる長尺制作を計画する。
- 編集、延長、エンドポイント、絵コンテ、ブロックアウト、トランジション用プロンプトを書く。
- アイデンティティ、形状、プロップの所有、空間、カメラフェーズ、音声の連続性を守る。
- 失敗したテイクを診断し、採用、ポスト修正、部分編集、再抽選、書き直しから判断する。
- 再試行ごとに一つの変数だけを変更する。
- 生成前にプロンプト構造を検査する。

この Skill は、二種類の知識を意図的に分離しています。

1. **検証済みのプラットフォーム情報** — Dreamina Seedance 2.5 公式資料に記載された件数、尺、ロックされる設定、ワークフロー名。
2. **制作手法** — 再利用可能な演出、リファレンス契約、連続性、修正の方法。

この分離により、古い Seedance 2.0 の制限や未検証の第三者情報が、暗黙に「2.5 の仕様」として扱われることを防ぎます。

## Seedance 2.5 概要

以下の値は、[公式情報の境界](#公式情報の境界)に記載した Dreamina Seedance 2.5 公式ガイドに基づき、2026 年 8 月 3 日に検証したものです。対象は公式資料に記載された Dreamina の画面であり、すべての API や第三者サービスに自動的に適用されるものではありません。

| 機能 | Dreamina 2.5 公式ガイダンス |
|---|---|
| リファレンス素材の合計 | 最大 50 件 |
| 画像 | 最大 30 枚、各画像は 4K 以下 |
| 動画リファレンス | 最大 10 本、合計 30 秒以下 |
| 音声リファレンス | 最大 10 本、合計 30 秒以下 |
| 標準生成 | 4～30 秒 |
| 1 回の延長 | 4～30 秒 |
| ネストした延長 | 最終出力は最大 60 秒 |
| 記載されている出力解像度 | 480p、720p |

汎用または未確認の Seedance 2.5 接続先では、1 回の直接生成を 30 秒以内とします。それより長い作品は、独立して生成する複数クリップとして計画します。上限は目標値ではありません。この Skill は、何も制御しないリファレンスを除外し、現在のシーンに必要な素材だけを選択します。

現在の API フィールド、モデル ID、料金、クォータ、地域、アカウント、展開状況、各画面での提供状況は、固定された知識境界の対象外です。利用時に最新の公式資料を確認する必要があります。

## オペレーティングモデル

<p align="center">
  <img src="assets/skill-workflow.svg" alt="ブリーフ、モード選択、リファレンス契約、演出、コンパイル、Lint の六段階からなる Seedance 2.5 ワークフロー" width="100%">
</p>

すべての依頼は、同じ制御されたパイプラインを通ります。

1. **ブリーフ** — 目的、利用画面、尺、素材、必須条件、権利を確定する。
2. **モード選択** — 生成、編集、延長、エンドポイント、絵コンテ、ブロックアウト、トランジションのロジックを選ぶ。
3. **契約** — 各リファレンスの役割、権限、除外事項を定義する。
4. **演出** — 見えるイベント、カメラ、照明、演技、音、終点を定義する。
5. **コンパイル** — 正確なリファレンストークンを保った、コピー可能な自然言語プロンプトを作る。
6. **Lint** — 生成コストを使う前に構造リスクを検出する。

最後に、設定、リファレンス役割マップ、最終プロンプト、本当に重要なリスクまたは次の手順を、簡潔な制作契約として出力します。

## ここから始める

ブリーフに含まれる形容詞の数ではなく、制作目的に応じて経路を選びます。

| タスク | 使用する経路 | 最優先の保護 |
|---|---|---|
| 明確な単独ショット | 基本生成 | 一つの主要な可視イベントと一つの主要カメラ移動 |
| 画像、動画、音声リファレンス | マルチモーダル参照 | 素材ごとに一つの役割と明示的な除外事項 |
| 30 秒以内の複数イベント | 段階生成 | 各段階に一つの状態変化と一つの可視終点 |
| 30 秒を超える作品 | 複数クリップ制作 | 各クリップを 30 秒以内に分けて個別に生成する |
| 既存映像の変更 | 動画編集 | 単一マスター、単一編集範囲、保持リスト |
| 採用済み映像の続き | 前方または後方延長 | 観察した境界フレームを連続性の事実とする |
| 二つの終点 | 始点・終点フレーム生成 | 各終点を別々に定義し、連続アクションでつなぐ |
| 複数の順序付き状態 | 複数キーフレーム | 各アンカーの順序と到達状態を明示する |
| パネルグリッドやスケッチ | 絵コンテ参照 | 読み順、ショットの役割、線画の除外事項 |
| 3D グレーモデル | 粗い／精密なブロックアウト | 動きの骨格か完全形状かを分類する |
| 複数画像から素早く動画化 | One-Click Video | 素材順、動き量、編集リズム、パッケージ、音 |
| 二つのクリップを接続 | シームレストランジション | トリガー、被覆過程、到達状態、音声ブリッジ |
| 失敗または部分成功した出力 | 診断と再試行 | 先に判定し、その後一つの変数だけを変更する |

Skill は選択された経路に必要なリファレンス節だけを読みます。すべてのテンプレートを毎回読み込むことはありません。

## リファレンス素材は契約である

<p align="center">
  <img src="assets/reference-role-map.svg" alt="画像、動画、音声、ソース動画、キーフレーム素材を個別の出力要素へ結び付けるリファレンス役割マップ" width="100%">
</p>

各素材のリファレンス契約は、二つの問いに答えます。

1. この素材は何を制御してよいか。
2. この素材から何を転用してはいけないか。

例：

```text
@Image 1 defines Character A's facial features, hairstyle, and wardrobe.
Do not use its background, composition, pose, or lighting.

@Video 1 controls only Character A's motion path, timing, and camera rhythm.
Do not transfer the performer, wardrobe, room, logos, or source audio.

@Audio 1 controls only Character A's voice, delivery, and the quoted line.
Do not add background music.
```

妥協できない三つのルール：

- プラットフォームが挿入したリファレンストークンを正確に保持する。
- 各出力要素に対して一つの制御元を選ぶ。
- 何も制御しない素材をすべて削除する。

複数の画像が同一の被写体を示す場合、プロンプト内で明示し、出力数を固定します。複数ソースが競合する場合は、「すべてを混ぜる」と指示するのではなく、優先するソースを選択します。

## 演出型プロンプトの構造

最終プロンプトは次の順序でコンパイルします。

```text
Reference roles
→ Generation goal
→ Subject and primary event
→ Scene or stage progression
→ Camera
→ Light and visual treatment
→ Audio
→ Continuity and exclusions
```

この構造では、観察可能な選択を優先します。

- 「beautiful lighting」ではなく、「A hard window key from camera left cuts across the face」。
- 「dynamic camera」ではなく、「The dolly starts waist-high, tracks the runner from the left, then stops on the closed gate」。
- 「very emotional」ではなく、「Her gaze drops, jaw tightens, right hand releases the key, and breathing becomes shallow」。
- 「epic destruction」ではなく、「The glass fractures from the impact point, fragments catch the desk light, then settle on the floor」。

各アクションには、初期状態、トリガー、変化、結果、目に見える終点を持たせます。秒単位の指定は重要な受け渡し、登場、退場、トランジション、ビートに限定し、通常の物語は段階で整理します。

## 例：マルチモーダルシーン

### 制作ブリーフ

```text
Goal: a tense 12-second product reveal in a rain-darkened workshop.
References: one product image, one camera-motion clip, one ambience recording.
Must preserve: product geometry, engraved mark, and subject count.
Output: 16:9, 720p, 12 seconds.
```

### リファレンス役割マップ

```text
@Image 1 — product geometry, material, and engraved mark only;
             do not use its white background or studio reflections.
@Video 1 — camera path and acceleration only;
             do not transfer its room, performer, object, color grade, or audio.
@Audio 1 — rain ambience and distant metal resonance only;
             do not add speech or music.
```

### 最終プロンプト

```text
@Image 1 defines the exact geometry, dark brushed metal, and engraved mark of one product. Do not use its white background, studio composition, or reflections. @Video 1 controls only the camera path and acceleration; do not transfer its room, performer, object, color grade, or sound. @Audio 1 controls only rain ambience and distant metal resonance; do not add dialogue or music.

Generate a 12-second product reveal in a rain-darkened mechanical workshop. The frame begins close on a wet steel workbench with the product mostly hidden beneath a charcoal cloth. A gloved hand enters from frame right and pulls the cloth away in one continuous movement. Water beads remain on the product surface; the engraved mark becomes fully visible as the cloth clears it. End state: exactly one product stands unobstructed at the center of the bench, the hand has exited frame right, and the cloth rests at the far edge.

Camera: inherit only the path and acceleration from @Video 1, beginning at bench height, sliding left around the product, and settling in a centered three-quarter close-up. Light: a cold overhead work lamp creates a narrow rim on the wet metal while one warm furnace reflection moves across the side during the camera slide. Sound: preserve @Audio 1's rain and distant metal resonance, add one soft cloth drag and one restrained metal settle, with no speech and no music.

Maintain exactly one product, its geometry, engraved mark, material, bench position, and screen direction throughout. Do not add text, logos, extra hands, tools crossing the product, or additional products.
```

現在の画面に独立した設定項目がある場合、生成設定はプロンプトの外に置きます。

## モード別の保護規則

### 動画編集

編集プロンプトでは、次を宣言します。

- 一つのソース動画を唯一の編集マスターとする。
- 変更する一つのオブジェクト、領域、時間範囲、音声カテゴリを指定する。
- 必要に応じて、対象数と置換時の継承関係を指定する。
- 編集範囲外で変更してはいけないものを列挙する。

### 前方・後方延長

採用済み映像は元の計画より優先されます。プロンプトは観察した境界状態、つまり姿勢、視線、プロップの所有、空間、カメラ位置と移動フェーズ、継続中の被写体動作、音声フェーズから始めます。後方延長では、ソース開始後に現れる人物、プロップ、エフェクトが早く登場することも防ぎます。

### 始点・終点フレームとキーフレーム

各エンドポイントは個別に定義します。補助リファレンスはアイデンティティ、衣装、形状を制御できますが、エンドポイントの構図を上書きしてはいけません。複数キーフレームは順序付き状態を定義するもので、フレーム単位の再現ではありません。

### 絵コンテとブロックアウト

絵コンテはショット順と大まかな構図を制御し、線画スタイル、文字ラベル、仮キャラクターを除外します。粗いブロックアウトは時間・空間の骨格を制御し、精密なブロックアウトは完全形状を制御したうえで、素材、キャラクター、環境、スタイルを再レンダリングできます。

### シームレストランジション

トランジションには、物理的なトリガーまたは変形過程、ブリッジ中の連続動作、定義された到達構図、音声遷移が必要です。「シームレスにする」だけでは十分な演出指示になりません。

## 出力契約

通常の依頼では、Skill は次を返します。

1. **タスクモードと生成設定** — 尺、アスペクト比、解像度、ロック値、明示した前提。
2. **リファレンス役割マップ** — 各素材について使うもの、使わないもの。
3. **最終プロンプト** — 正確なリファレンストークンを保持した、直接コピーできるコードブロック。
4. **リスクまたは次の手順** — 成功に実質的な影響を与える一～三項目。

診断依頼では、次の形式を返します。

```text
Verdict → Evidence → One changed variable → Repaired prompt
```

主目的がすでに達成されている場合、ショット全体を再生成せず、採用、ポスト修正、単一レイヤーの編集を提案できます。

## プロンプトリンター

同梱リンターは決定的な構造チェックを行います。映像品質を予測したり、Seedance を呼び出したり、プラットフォームによるリファレンス結び付けを保証したりするものではありません。

プロンプトファイルを検査：

```bash
python3 seedance-25/scripts/lint_prompt.py prompt.txt --mode auto --duration 30
```

標準入力から草稿を渡す：

```bash
printf '%s\n' '@Video 1 is the source. Extend forward from the observed last frame...' \
  | python3 seedance-25/scripts/lint_prompt.py - --mode extend
```

機械可読の出力：

```bash
python3 seedance-25/scripts/lint_prompt.py prompt.txt --mode edit --json
```

明示的に指定できるモードは、`base`、`reference`、`long`、`edit`、`extend`、`first-last`、`keyframes`、`storyboard`、`blockout`、`transition` です。`auto` は最も可能性の高いモードを推定します。

リンターは、次のようなリスクを検査します。

- 予定する 1 回の直接生成が 30 秒を超えている。
- 無効、重複、空白、予定尺外の時間範囲。
- 複数のリファレンスに役割または除外事項がない。
- 編集に唯一のマスター、狭い範囲、保持リストがない。
- 延長に観察済み境界状態または連続性ロックがない。
- 始点・終点フレームの定義が不完全。
- キーフレームの順序がない。
- 絵コンテに読み順または線画除外がない。
- ブロックアウトの分類または継承規則がない。
- トランジションに二つのクリップ、トリガー、到達状態がない。
- 長いプロンプトに段階または目に見える終点がない。
- 一般的なスタイル強調語の過剰使用。
- 矛盾する音声指示。

エラーは非ゼロ終了コードを返します。警告と情報メモはレビュー用のシグナルです。

同梱セルフテストを実行：

```bash
python3 seedance-25/scripts/lint_prompt.py --self-test
```

## インストール

### 方法 A — Codex の個人 Skill

```bash
git clone git@github.com:sjinn-ai/seedance2.5-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R seedance2.5-skills/seedance-25 "${CODEX_HOME:-$HOME/.codex}/skills/seedance-25"
```

新しい Skill が自動検出されない場合は、インストール後にクライアントを再起動または更新してください。

### 方法 B — プロジェクトローカル Skill

Skill を使うプロジェクト内で実行：

```bash
mkdir -p .agents/skills
cp -R /path/to/seedance2.5-skills/seedance-25 .agents/skills/seedance-25
```

Agent クライアントが別の場所を要求する場合は、そのディレクトリを使用してください。実行時に必要な Skill は `seedance-25/` 内で完結しています。リポジトリ直下の `assets/` は README 専用です。

## Skill の使い方

名前で呼び出し、ブリーフと利用可能な素材情報を渡します。

```text
$seedance-25 Create a 30-second Seedance 2.5 prompt for a two-character chase.
Use @Image 1 for Character A's identity, @Image 2 for Character B's identity,
@Video 1 only for the motorcycle motion, and @Audio 1 for rain ambience.
Keep the red bag with Character A throughout. End on both characters under the station clock.
```

診断の例：

```text
$seedance-25 Diagnose this failed extension. The new segment duplicates the actor,
repeats the door opening, and reverses the camera direction. Return one changed
variable and a conservative repaired prompt.
```

Skill はユーザーが指定した言語で回答しますが、同梱される Skill の指示とリファレンス文書はすべて英語のままです。

## リポジトリ構成

```text
seedance2.5-skills/
├── README.md
├── README.zh-CN.md
├── README.ja.md
├── assets/
│   ├── reference-role-map.svg
│   ├── seedance-25-hero.png
│   └── skill-workflow.svg
└── seedance-25/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── capabilities-and-limits.md
    │   ├── quality-and-repair.md
    │   └── task-patterns.md
    └── scripts/
        └── lint_prompt.py
```

### Skill マップ

| ファイル | 役割 |
|---|---|
| `seedance-25/SKILL.md` | エントリーポイント、情報境界、モードルーター、演出ワークフロー、出力契約、安全性 |
| `capabilities-and-limits.md` | 検証済み Dreamina 2.5 値、タスク固有のロック設定、制限、事実表現ルール |
| `task-patterns.md` | 生成、リファレンス、長尺、編集、延長、エンドポイント、絵コンテ、ブロックアウト、トランジション、音声、演技、カメラのモード別パターン |
| `quality-and-repair.md` | テイク判定、一変数再試行、症状診断、連続性修正、テイクログ |
| `lint_prompt.py` | 英語・中国語プロンプトに対応する一般的な構造リスクのヒューリスティック検査 |
| `agents/openai.yaml` | Agent 向け表示名、説明、デフォルト呼び出しプロンプト |

## 検証

Codex の `skill-creator` パッケージがインストールされている場合、Skill 構造を検証できます。

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" seedance-25
```

リンターの回帰テスト：

```bash
python3 seedance-25/scripts/lint_prompt.py --self-test
```

このリポジトリは、ネットワーク接続なしで検証できるよう設計されています。ただし、API、料金、地域、クォータ、提供状況に関する時間依存の主張を行う前には、最新の公式資料をオンラインで確認する必要があります。

## 現在の状態と境界

| コンポーネント | 状態 | 境界 |
|---|---|---|
| コア Skill ワークフロー | 利用可能 | プロンプトと制作計画を生成する。動画生成サービスは呼び出さない |
| リファレンスライブラリ | 利用可能 | 下記の公式ガイドと制作手法に基づく |
| プロンプトリンター | 利用可能、ヒューリスティック | 構造リスクを検出する。美的品質やモデル準拠度は評価しない |
| README ビジュアル | 利用可能 | 説明用の図であり、Seedance の生成サンプルではない |
| API 統合 | 未収録 | 画面ごとの API は別途、最新情報の検証が必要 |

このリポジトリは Seedance 2.5 へのアクセスを主張せず、生成結果を保証せず、クライアントにアップロードされたメディアを権利証明として扱いません。実在人物の肖像や声、ブランド、音楽、保護されたキャラクターは、適切な許可を得て使用するか、独自の同等表現に置き換えてください。

## 公式情報の境界

このリポジトリの Seedance 2.5 機能情報は、次の資料に基づいています。

- [Dreamina Seedance 2.5 User Guide](https://bytedance.larkoffice.com/wiki/NjnWwvf4BiFYFLk2RzrcEgaunGf)
- [Dreamina Seedance 2.5 Prompt Guide](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)

2026 年 8 月 3 日、公式ページをユーザー提供のコピー済みテキストとブラウザで比較しました。目次と本文テキストは完全でした。埋め込み画像、完成動画、一部の視覚比較はコピーに含まれていないため、このリポジトリではそれらの例を視覚的に検証済みとは記述しません。

ワークフロー設計は、MIT ライセンスの [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) からも学んでいます。特に、モードルーティング、リファレンス契約、連続性の事実、一変数リテイク方式を参考にしました。Seedance 2.5 の機能と数値に関する主張には、上記の 2.5 公式資料のみを使用します。

## 設計基準

この Skill が作る強いプロンプトには、次の特性があります。

- **結び付いている** — 重要な素材、キャラクター、製品、プロップ、台詞に明確な担当がある。
- **観察できる** — アクション、感情、照明、音、終点を見たり聞いたりできる。
- **連続している** — アイデンティティ、形状、所有関係、空間、画面方向、カメラフェーズ、音声状態が一貫する。
- **範囲が限定されている** — 編集は一つのレイヤーを変更し、延長は一つの実際の境界を継承し、各段階は一つの主要状態変化を持つ。
- **レビューできる** — 何が成功し、何が失敗し、次にどの一変数を変更するか判断できる。
- **事実に忠実である** — プラットフォーム情報が、検証済みの公式根拠と現在の利用画面の範囲内に収まる。

原則はシンプルです。

> リファレンスが権限を定義し、演出が変化を定義し、採用済み映像が事実を定義する。

## クレジット

- 機能とワークフローの事実を提供する Dreamina Seedance 2.5 公式資料。
- このリポジトリの構成と制作思考に影響を与えた、高品質なオープンソース参照アーキテクチャ [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0)。
