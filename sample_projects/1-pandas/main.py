import pandas as pd


def main():
    df = pd.read_csv("sample.csv")

    print("=== 元データ ===")
    print(df)

    # 列を追加
    df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 29, 39, 120], labels=["20s", "30s", "40+"])
    df["Salary_k"] = (df["Salary"] / 1000).round(1)

    # 都市ごとの集計
    summary = (
        df.groupby("City", as_index=False)
        .agg(
            people=("Name", "count"),
            avg_age=("Age", "mean"),
            avg_salary=("Salary", "mean"),
            max_salary=("Salary", "max"),
        )
        .sort_values("avg_salary", ascending=False)
    )
    summary["avg_age"] = summary["avg_age"].round(1)
    summary["avg_salary"] = summary["avg_salary"].round(0).astype(int)

    print("\n=== 都市ごと集計 ===")
    print(summary)

    # 給与トップ3
    top3 = df.sort_values("Salary", ascending=False).head(3)[["Name", "City", "Salary"]]
    print("\n=== 給与トップ3 ===")
    print(top3.to_string(index=False))


if __name__ == "__main__":
    main()
