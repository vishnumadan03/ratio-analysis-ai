import matplotlib

matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as Patch
from io import BytesIO
import base64
from sklearn.linear_model import LinearRegression
import numpy as np


def generate_current_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=range(4, 58)
    )

    df.columns = df.columns.str.strip().str.replace("\n", "", regex=True)

    # Rename and clean columns
    if "Ratio" in df.columns:
        df.rename(columns={"Ratio": "Current Ratio"}, inplace=True)
    else:
        raise KeyError("'Ratio' column not found after cleaning.")
    # df.rename(columns={"Ratio":"Current Ratio"}, inplace=True)

    plt.figure(figsize=(3, 3))
    plt.pie(df["Current Ratio"], labels=df["Year"], autopct="%1.1f%%", startangle=90)
    plt.title("Current Ratio Distribution by Year")
    # Save to buffer
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_quick_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=12, nrows=3
    )

    plt.figure(figsize=(3, 3))
    plt.pie(
        df["Quick Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["green", "yellow", "blue"],
    )
    plt.title("Quick Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_proprietary_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=19, nrows=3
    )

    plt.figure(figsize=(4, 3))
    plt.pie(
        df["Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["purple", "red", "blue"],
    )
    plt.title("Proprietary Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_inventory_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=33, nrows=3
    )

    plt.figure(figsize=(5, 3))
    plt.pie(
        df["Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["green", "yellow", "red"],
    )
    plt.title("Inventory turnover Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_fixed_asset_turnover_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=40, nrows=3
    )

    plt.figure(figsize=(5, 3))
    plt.pie(
        df["Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["blue", "orange", "brown"],
    )
    plt.title("Fixed asset turnover Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_gross_profit_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=47, nrows=3
    )

    plt.figure(figsize=(4, 3))
    plt.pie(
        df["Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["yellow", "brown", "indigo"],
    )
    plt.title("Gross profit Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def generate_net_profit_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=54, nrows=3
    )

    if "Ratio" in df.columns:
        df.rename(columns={"Ratio": "Net Profit Ratio"}, inplace=True)
    else:
        raise KeyError("'Ratio' column not found after cleaning.")

    plt.figure(figsize=(3, 3))
    plt.pie(
        df["Net Profit Ratio"],
        labels=df["Year"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["green", "blue", "orange"],
    )
    plt.title("Net profit Ratio Distribution by Year")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def future_prediction_current_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=range(4, 58)
    )

    if "Ratio" in df.columns:
        df.rename(columns={"Ratio": "Current Ratio"}, inplace=True)
    else:
        raise KeyError("'Ratio' column not found after cleaning.")

    x = df[["Year"]]
    y = df["Current Ratio"]

    model = LinearRegression()
    model.fit(x, y)

    future_years = np.array([[2024], [2025], [2026], [2027], [2028]])

    future_years_df = pd.DataFrame(future_years, columns=["Year"])

    future_predictions = model.predict(future_years_df)

    plt.figure(figsize=(5, 4))
    # Plot actual data
    plt.scatter(df["Year"], df["Current Ratio"], color="blue", label="Actual Data")

    # Plot predicted data
    plt.plot(
        future_years.flatten(),
        future_predictions,
        color="red",
        linestyle="dashed",
        label="Predicted Data",
    )

    plt.xlabel("Year")
    plt.ylabel("Current Ratio")
    plt.title("Future Prediction of Current Ratio")
    plt.legend()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")


def future_prediction_net_profit_ratio():
    df = pd.read_excel(
        r"./data/project.xlsx", sheet_name="Sheet1", skiprows=54, nrows=3
    )

    if "Ratio" in df.columns:
        df.rename(columns={"Ratio": "Net Profit Ratio"}, inplace=True)
    else:
        raise KeyError("'Ratio' column not found after cleaning.")

    x = df[["Year"]]
    y = df["Net Profit Ratio"]

    model = LinearRegression()
    model.fit(x, y)

    future_years = np.array([[2024], [2025], [2026], [2027], [2028]])

    future_years_df = pd.DataFrame(future_years, columns=["Year"])
    future_predictions = model.predict(future_years_df)

    # Combine actual and predicted data
    years = list(df["Year"]) + list(future_years.flatten())
    ratios = list(df["Net Profit Ratio"]) + list(future_predictions)

    # Define bar colors (Blue for actual, Red for predicted)
    colors = ["blue"] * len(df["Year"]) + ["red"] * len(future_years)

    # Create the bar chart
    plt.figure(figsize=(5, 4))
    plt.bar(years, ratios, color=colors)

    bars = plt.bar(years, ratios, color=colors)
    # Add labels
    plt.xlabel("Year")
    plt.ylabel("Net Profit Ratio")
    plt.title("Future Prediction of Net Profit Ratio")

    plt.legend([bars[0], bars[-1]], ["Actual Data", "Predicted Data"])

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.read()).decode("utf-8")
