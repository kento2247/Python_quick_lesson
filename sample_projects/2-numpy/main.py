import numpy as np


def main() -> None:
    x = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    y = np.array([10, 20, 30, 40, 50], dtype=np.float64)
    a = np.array([[1, 2], [3, 4]], dtype=np.float64)
    b = np.array([[5, 6], [7, 8]], dtype=np.float64)

    print("=== 1次元配列 ===")
    print("x:", x)
    print("y:", y)
    print("x + y:", x + y)
    print("xの平均:", x.mean())
    print("yの標準偏差:", y.std())

    print("\n=== 2次元配列 ===")
    print("A:")
    print(a)
    print("B:")
    print(b)
    print("A @ B:")
    print(a @ b)


if __name__ == "__main__":
    main()
