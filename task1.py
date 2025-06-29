import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Задание 1 (Вариант 2)

- Функция возвращающая DataFrame по указанному пути к датасету.
Причем загруженный DataFrame остается в памяти для последующей
обработки.
- Функция отображения гистограммы цены.
- Функция отображения гистограммы размера дома.
- Функция отображения точечной диаграммы зависимости цены и
размера дома.
- Функция отображения круговой диаграммы в процентах количества
домов в разных районах.
- Функция отображения гистограммы количества домов в зависимости
от года постройки.
- Функция отображения на одном рисунке диаграммы количества
спальных комнат в зависимости от района и диаграммы количества
ванных комнат в зависимости от района.
"""


def get_df_by_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def histogram(
    ax,
    df: pd.DataFrame,
    title: str,
    col: str,
    bins: int | None = None,
    alpha: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
):
    ax.hist(df[col], bins=bins, alpha=alpha)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def scatter(
    ax,
    df: pd.DataFrame,
    title: str,
    size_col: str,
    price_col: str,
    alpha: float | None = 0.75,
    dot_size: float | None = 10.0,
    xlabel: str | None = None,
    ylabel: str | None = None,
):
    ax.scatter(df[size_col], df[price_col], alpha=alpha, s=dot_size)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def pie(
    ax,
    df: pd.DataFrame,
    title: str,
    neighborhood_col: str,
    autopct: str | None = "%1.1f%%",
):
    print(df[neighborhood_col].value_counts())
    ax.pie(
        df[neighborhood_col].value_counts(),
        labels=df[neighborhood_col].unique(),
        autopct=autopct,
    )
    ax.set_title(title)


def main():
    plt.close("all")

    df = get_df_by_csv("dataset_house_price1.csv")
    fig, axs = plt.subplots(2, 3, figsize=(16, 9))
    # fig.delaxes(axs[1, 1])
    fig.subplots_adjust(wspace=0.3, hspace=0.5)

    show_price_histogram = lambda: histogram(
        ax=axs[0, 0],
        df=df,
        title="Distribution of house prices",
        col="Price",
        xlabel="Price",
        ylabel="Count",
    )
    show_house_size_histogram = lambda: histogram(
        ax=axs[0, 1],
        df=df,
        title="Distribution of house sizes",
        col="SquareFeet",
        bins=100,
        xlabel="Size",
        ylabel="Count",
    )
    show_relationship_between_house_price_and_size = lambda: scatter(
        ax=axs[0, 2],
        df=df,
        title="Relationship of house size and price",
        size_col="SquareFeet",
        price_col="Price",
        xlabel="Price",
        ylabel="Size",
    )
    show_count_of_houses_by_neighborhoods = lambda: pie(
        ax=axs[1, 0],
        df=df,
        title="Count of houses by neighborhood",
        neighborhood_col="Neighborhood",
    )
    show_count_of_houses_by_year = lambda: histogram(
        ax=axs[1, 1],
        df=df,
        title="Count of houses by year",
        col="YearBuilt",
        bins=25,
        xlabel="Year",
        ylabel="Count",
    )
    # TODO

    show_price_histogram()
    show_house_size_histogram()
    show_relationship_between_house_price_and_size()
    show_count_of_houses_by_neighborhoods()
    show_count_of_houses_by_year()

    plt.show()


if __name__ == "__main__":
    main()
