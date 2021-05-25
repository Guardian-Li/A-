from decimal import Decimal


def rmb(x):
    return float(Decimal(x).quantize(Decimal("0.00")))


def calculate(base_commission_percent=0.13, buy_stock_num=100, buy_price=1, sell_price=2):
    base_commission = 5
    base_commission_percent = base_commission_percent / 1000
    stamp_duty = 0.1 / 100
    # 印花税费
    transfer_fee_percent = 0.002 / 100
    # 过户费
    buy_stock_num = buy_stock_num
    buy_price = buy_price
    sell_price = sell_price
    buy_total_price = buy_stock_num * buy_price
    sell_total_price = sell_price * buy_stock_num
    buy_commission = 5 if rmb(buy_total_price * base_commission_percent) < 5 else rmb(
        buy_total_price * base_commission_percent)
    sell_commission = 5 if rmb(sell_total_price * base_commission_percent) < 5 else rmb(
        buy_total_price * base_commission_percent)
    stamp_num =rmb(sell_total_price * stamp_duty)  # 印花税 卖出收取
    transfer_fee_buy = rmb(buy_total_price * transfer_fee_percent)
    transfer_fee_sell = rmb(sell_total_price * transfer_fee_percent)
    transfer_fee = rmb(transfer_fee_buy + transfer_fee_sell)
    # 过户费
    total_commission = buy_commission + sell_commission
    handling_fee = rmb(stamp_num + transfer_fee + total_commission)
    # print("数量:",buy_stock_num)
    # print("买入价:",buy_price)
    # print("卖出价",sell_price)
    # print("差价:",sell_total_price-buy_total_price)
    # print("印花税:",stamp_num)
    # print("买入过户费:",transfer_fee_buy)
    # print("卖出过户费:",transfer_fee_sell)
    # print("过户费:",transfer_fee)
    # print("总手续费:",handling_fee)
    # print("盈利:",rmb((sell_price-buy_price)*buy_stock_num-handling_fee))
    res = {}
    res["buy_stock_num"]=buy_stock_num
    res["buy_price"]=buy_price
    res["sell_price"]=sell_price
    res["stamp_num"]=stamp_num
    res["transfer_fee_buy"]=transfer_fee_buy
    res["transfer_fee_sell"]=transfer_fee_sell
    res["transfer_fee"]=transfer_fee
    res["handling_fee"]=handling_fee
    res["benefit"]=rmb((sell_price-buy_price)*buy_stock_num-handling_fee)
    return res

if __name__ == '__main__':
    calculate()