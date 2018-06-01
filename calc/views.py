from django.shortcuts import render

'''
def calc(request):
    if request.method == "POST":
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        d = a + b
        return render(request, 'calc/calc.html', {'c': 'your number is equal to ' + str(d)})
    else:
        return render(request, 'calc/calc.html', {})
'''

def calc(request):
    if request.method == "POST":
        if request.POST.get('form_type') == 'BB_form':
            sdano = float(request.POST.get('sdano'))
            ordered_m = float(request.POST.get('ordered_m'))
            g_price = float(request.POST.get('g_price'))
            min_m = float(request.POST.get('min_m'))
            radio = request.POST.get('BB')
            
            if sdano < 5:
                m = 0
            elif sdano >= 5 and sdano < 10:
                m = 1.5*sdano + 5
            elif sdano >= 10 and sdano <25:
                m = 0.3333*sdano + 16.6667
            else:
                m = sdano

            if m < 1.2*ordered_m:
                money = m*g_price
            elif m >= 1.2*ordered_m and m < 1.5*ordered_m:
                money = 1.2*ordered_m*g_price + (m - 1.2*ordered_m)*0.5*g_price
            elif m >= 1.5*ordered_m and m < 2*ordered_m:
                money = 1.2*ordered_m*g_price + 0.3*ordered_m*0.5*g_price + (m - 1.5*ordered_m)*0.25*g_price
            else:
                money = 1.2*ordered_m*g_price + 0.3*ordered_m*0.5*g_price + 0.5*ordered_m*0.25*g_price + (m - 2*ordered_m)*0.1*g_price

            if ordered_m < 10:
            	order = 1.5*ordered_m + 5
            elif ordered_m >= 10 and ordered_m < 25:
            	order = 0.3333*ordered_m + 16.6667
            else:
            	order = ordered_m

            ordered_money = order*g_price

            if radio == 'B1' and sdano >= min_m:
                money = money*1.25 + 25
                ordered_money = ordered_money*1.25 + 25
            elif radio == 'B2' and sdano >= min_m:
                money = money*1.5 + 50
                ordered_money = ordered_money*1.5 + 50
            elif radio == 'B3' and sdano >= min_m:
                money = money*1.5 + 75
                ordered_money = ordered_money*1.5 + 75
            elif radio == 'B4' and sdano >= min_m:
                money = money*2 + 100
                ordered_money = ordered_money*2 + 100
            elif radio == 'B5' and sdano >= min_m:
                money = money*2 + 150
                ordered_money = ordered_money*2 + 150
            elif radio == 'B6' and sdano >= min_m:
                money = money*2 + 200
                ordered_money = ordered_money*2 + 200
            elif radio == 'B7' and sdano >= min_m:
                money = money*2 + 250
                ordered_money = ordered_money*2 + 250
            elif radio == 'B8' and sdano >= min_m:
                money = money*2 + 300
                ordered_money = ordered_money*2 + 300

            money = round(money)
            ordered_money = round(ordered_money)

            
            return render(request, 'calc/calc.html', {'money': money, 'ordered_money': "Заказано " + str(round(ordered_m)) + " грамм за " + str(ordered_money) + " USD"})




        elif request.POST.get('form_type') == 'KD_form':
            sdano = float(request.POST.get('sdano'))
            ordered_m = float(request.POST.get('ordered_m'))
            g_price = float(request.POST.get('g_price'))
            radio = request.POST.get('KD')
            m = sdano

            if m < 1.2*ordered_m:
                money = m*g_price
            elif m >= 1.2*ordered_m and m < 1.5*ordered_m:
                money = 1.2*ordered_m*g_price + (m - 1.2*ordered_m)*0.5*g_price
            elif m >= 1.5*ordered_m and m < 2*ordered_m:
                money = 1.2*ordered_m*g_price + 0.3*ordered_m*0.5*g_price + (m - 1.5*ordered_m)*0.25*g_price
            else:
                money = 1.2*ordered_m*g_price + 0.3*ordered_m*0.5*g_price + 0.5*ordered_m*0.25*g_price + (m - 2*ordered_m)*0.1*g_price


            ordered_money = ordered_m*g_price

            if radio == 'KD1':
            	money = money
            	ordered_money = ordered_money
            elif radio == 'KD2':
            	money = money*1.2
            	ordered_money = ordered_money*1.2
            elif radio == 'KD3':
            	money = money*1.5
            	ordered_money = ordered_money*1.5
            elif radio == 'KD4':
            	money = money*2
            	ordered_money = ordered_money*2

            money = round(money)
            ordered_money = round(ordered_money)

            return render(request, 'calc/calc.html', {'money': money, 'ordered_money': "Заказано " + str(round(ordered_m)) + " грамм за " + str(ordered_money) + " USD"})

        elif request.POST.get('form_type') == 'N_form':
            sdano = float(request.POST.get('sdano'))
            ordered_m = float(request.POST.get('ordered_m'))
            N_price = float(request.POST.get('N_price'))

            if sdano <= ordered_m:
                money = sdano/ordered_m*N_price

            elif sdano > ordered_m and sdano < 1.5*ordered_m:
                money = N_price + (sdano - ordered_m)*0.5*N_price/ordered_m

            elif sdano >=1.5* ordered_m and sdano < 2*ordered_m:
                money = N_price + 0.25*N_price + (sdano - 1.5*ordered_m)*0.25*N_price/ordered_m
            else:
                money = N_price + 0.25*N_price + 0.125*N_price + (sdano - 2*ordered_m)*0.1*N_price/ordered_m
            money = round(money)

            return render(request, 'calc/calc.html', {'money': money, 'ordered_money': "Заказано " + str(round(ordered_m)) + " грамм за " + str(round(N_price)) + " USD"})
    else:
        return render(request, 'calc/calc.html', {})

        

