"""
CSVデータの整形処理を提供するモジュール
Author:
    Florian Seto
"""

import logging

import pandas as pd


logger = logging.getLogger(__name__)


def remove_columns(dataframe: pd.DataFrame, columns_to_remove: list[str]) -> pd.DataFrame:
    """
    指定された列をDataFrameから削除します。

    Args:
        dataframe: 整形対象のDataFrame。
        columns_to_remove: 削除対象の列名一覧。
    Returns:
        指定列を削除したDataFrame。
    """

    # 元データを変更しないようにコピーして処理する
    formatted_dataframe = dataframe.copy()

    # 指定された削除対象列が存在するか確認する
    missing_columns = [
        column
        for column in columns_to_remove
        if column not in formatted_dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"削除対象の列が存在しません: {missing_columns}")

    # 指定された不要列を削除する
    formatted_dataframe = formatted_dataframe.drop(columns=columns_to_remove)

    logger.info(f"不要列削除完了: removed_columns={columns_to_remove}, remaining_columns={len(formatted_dataframe.columns)}")

    return formatted_dataframe



def rename_columns(dataframe: pd.DataFrame, column_name_map: dict[str, str]) -> pd.DataFrame:
    """
    指定された列名を変更します。

    Args:
        dataframe: 整形対象のDataFrame。
        column_name_map: 変更前と変更後の列名。
    Returns:
        列名を変更したDataFrame。
    """

    # 元データを変更しないようにコピーする
    formatted_dataframe = dataframe.copy()

    # 変更対象の列が存在するか確認する
    missing_columns = [
        column_name
        for column_name in column_name_map
        if column_name not in formatted_dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"列名変更対象の列が存在しません: {missing_columns}")

    # 指定された列名を変更する
    formatted_dataframe = formatted_dataframe.rename(columns=column_name_map)

    logger.info(f"列名変更完了: renamed_columns={column_name_map}")

    return formatted_dataframe


def reorder_columns(dataframe: pd.DataFrame, column_order: list[str]) -> pd.DataFrame:
    """
    DataFrameの列を指定された順番に並べ替えます。

    Args:
        dataframe: 整形対象のDataFrame。
        column_order: 並べ替え後の列名一覧。
    Returns:
        列を指定順に並べ替えたDataFrame。
    """

    # 元データを変更しないようにコピーする
    formatted_dataframe = dataframe.copy()

    # 並べ替え対象の列が存在するか確認する
    missing_columns = [
        column
        for column in column_order
        if column not in formatted_dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"列順変更対象の列が存在しません: {missing_columns}")

    # 指定された順番に列を並べ替える
    formatted_dataframe = formatted_dataframe.loc[:, column_order]

    logger.info(f"列順変更完了: column_order={column_order}")

    return formatted_dataframe
