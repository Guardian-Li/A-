from tkinter import *
from tkinter import font
from stock import *

def show_res(buy_price, sell_price, commission,Text,stock_num):
    buy_price=float(buy_price)
    sell_price=float(sell_price)
    commission=float(commission)
    stock_num=int(stock_num)*100
    res = calculate(commission,stock_num,buy_price,sell_price)
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
    ft=font.Font(size=14)
    Text.tag_add('tag','end')
    Text.tag_config(
        'tag',
        font=ft
    )
    Text.delete('1.0','end')
    Text.insert('end',"差价:"+str(rmb((res["sell_price"]-res["buy_price"])*stock_num))+"\n",'tag')
    Text.insert('end',"总盈利:"+str(res["benefit"])+"\n",'tag')
    Text.insert('end',"印花税:"+str(res["stamp_num"])+"\n",'tag')
    Text.insert('end',"买入过户费:"+str(res["transfer_fee_buy"])+'\n','tag')
    Text.insert('end',"卖出过户费:"+str(res["transfer_fee_sell"])+'\n','tag')
    Text.insert('end',"总手续费:"+str(res["handling_fee"])+"\n",'tag')
    Text.insert('end',"\n")


if __name__ == '__main__':
    tk = Tk()
    tk.title("手续费快速计算器")
    label_commission=Label(tk,text="佣金‰")
    label_commission.pack()
    commission=StringVar(value="0.13")
    Entry_commission = Entry(textvariable=commission)
    Entry_commission.pack()
    label_buy_price=Label(tk,text="买入价格")
    label_buy_price.pack()
    Entry_buy_price=Entry(tk)
    Entry_buy_price.pack()
    label_sell_price = Label(tk, text="卖出价格")
    label_sell_price.pack()
    Entry_sell_price=Entry()
    Entry_sell_price.pack()
    labal_stock_num=Label(tk,text="购买数量（手）")
    labal_stock_num.pack()
    Entry_stock_num =  Entry(tk)
    Entry_stock_num.pack()
    Result_text=Text(tk)
    Result_text.pack()


    Button_cal = Button(tk,text="计算",command=lambda:show_res(commission=Entry_commission.get(),
                                                              buy_price=Entry_buy_price.get(),
                                                              sell_price=Entry_sell_price.get(),
                                                              Text=Result_text,
                                                             stock_num=Entry_stock_num.get()),width=40,height=15)
    Button_cal.pack()
    tk.mainloop()


