import pandas
import streamlit as st

def make_dataframe(csv):
    df = pandas.read_csv(csv, encoding='shift-jis')
    buy_l = []
    payout_l = []
    for i, j in zip(df['購入'], df[df.columns[7]]):
        i = i.replace("￥", "")
        i = int(i.replace(",", ""))
        j = j.replace("￥", "")
        j = j.replace("---", "0")
        j = int(j.replace(",", ""))
        buy_l.append(i)
        payout_l.append(j)
    df['購入'] = buy_l
    df[df.columns[7]] = payout_l
    # net_income = df['購入'].sum() - df['ペイアウト '].sum()
    return df

def get_total_income(df):
    return df['ペイアウト '].sum() - df['購入'].sum()

def main():
  st.title("Binary Option")
  st.header("11/01 ~ 11/14 の収益分析")
  df = make_dataframe("history.csv")
  total_income = get_total_income(df)

  st.text("合計収益(円)")
  st.text(total_income)

  st.text("データフレーム出力")
  st.dataframe(df)
  # st.table(df)




if __name__ == "__main__":
  main()