import pandas as pd

# a
def func_a(df):
    output = pd.DataFrame()
    output["days"] = sorted(df["days"].unique())
    output["mean_values"] = df.groupby("days").mean().values
    output["median_values"] = df.groupby("days").median().values
    output["max_values"] = df.groupby("days").max().values
    output["min_values"] = df.groupby("days").min().values
    return output

# b
def func_b(df):
    output = pd.DataFrame()
    output[["employee", "pos"]] = df[["employee", "pos"]].drop_duplicates(subset=["employee"]).sort_values(by="employee")
    output["amount_diff"] = (df.groupby("employee")["amount"].max() - df.groupby("employee")["amount"].min()).values
    return output.sort_values(by="amount_diff", ascending=False).iloc[:2].reset_index(drop=True)

# Test Sample
if __name__ == "__main__":

    # a
    df = pd.DataFrame({'days': [1, 1, 2, 2, 1, 3, 4],
                'values': [10, 10, 5, 3, -2, 4, 20]})
    print("\na:")
    print("input:\n", df)
    print("output:\n", func_a(df))

    # b
    df = pd.DataFrame({'employee': [1001, 1002, 1004, 1001, 1001, 1002, 1004, 1005, 1005],
                       'pos': [2, 2, 2, 2, 2, 2, 2, 2, 2],
                       'amount': [125, 542, 2345, 892, 100, 1234, 657, 34, 35]})
    print("\nb:")
    print("input:\n", df)
    print("output:\n", func_b(df))