import numpy as np 
import pandas as pd



def pricesData(read_path):
    data = pd.read_csv(read_path, encoding='gb18030')
    #print(len(data))

    use_data = data[['日期','收盘价']]
    #print(use_data.head())
    #test_data = use_data[:3290]
    test_data = use_data[:75]
    #print(len(test_data))
    #print(test_data.tail())

    prices = np.array(test_data['收盘价']).tolist()[::-1]
    #print(prices[:5])

    return prices


def rules1(prices):
    # base rules: 每天定投100
    print("运行规则1...")
    cost_day = 100
    counts = 0

    last_day_price = prices[-1]
    print("最后一天收盘价： ", last_day_price)
    test_days = len(prices[:-1])
    print("测试投资天数： ", test_days)
    print("方案： 每天定投 ", cost_day)

    for i,price in enumerate(prices[:-1]):

        counts += cost_day/price

    print("------")
    cost_all = cost_day*test_days
    print("总投入： ", cost_all)
    sale_money = counts*last_day_price
    print("卖出价： ", sale_money)

    result_money = sale_money-cost_all
    print("收益金额： ", result_money)

    result_ratio = result_money/cost_all
    print("收益率： ", result_ratio)


def main():

    read_path = "data/000001.csv"

    # 1. prepare data
    prices = pricesData(read_path)


    # 2. 
    result1 = rules1(prices)
    print("rule 1 result: ", result1)


if __name__ == '__main__':
    main()