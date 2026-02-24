# 4. Pythonインストール（uv使用）

## uvインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 仮想環境作成

```bash
uv venv
source .venv/bin/activate
```

## PyTorchテンプレ

```bash
uv pip install torch torchvision torchaudio
```

```python
import torch
print(torch.tensor([1,2,3]) * 2)
```
