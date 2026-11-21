from tkinter import *
import math

num1 = ''
num2 = ''
oper = ''
flag_oper = False
flag_equal = False
memory = 0
ans = 0
expression = ''


#----------------------------------------------------------------
def num_insert(numb):
    global num1, num2, flag_equal, expression

    if flag_equal and not flag_oper:
        num1 = ''
        num2 = ''
        expression = ''
        flag_equal = False

    if not flag_oper:
        if num1 == 'Err':
            num1 = ''

        num1 += numb
        expression += numb
        lcd['text'] = expression

    else:
        if num2 == 'Err':
            num2 = ''

        num2 += numb
        expression += numb
        lcd['text'] = expression
        
#----------------------------------------------------------------

def calculate():
    global num1, num2, oper

    if not num1 or not num2:
        return False

    try:
        n1 = float(num1)
        n2 = float(num2)

        if oper == '+':
            result = n1 + n2
        elif oper == '-':
            result = n1 - n2
        elif oper == '*':
            result = n1 * n2
        elif oper == '/':
            if n2 == 0:
                result = 'Err'
            else:
                result = n1 / n2
        else:
            return False

        if result == 'Err':
            num1 = 'Err'
            num2 = ''
            oper = ''
            return False

        num1 = str(result)
        num2 = ''
        oper = ''

        return True

    except:
        num1 = 'Err'
        num2 = ''
        oper = ''
        return False
    
#---------------------------------------------------------------    

def oper_insert(operator):
    global oper, flag_oper, flag_equal, expression, num2

    if num1 == 'Err':
        return

    if flag_oper and num2:
        calculate()

    elif flag_equal:
        flag_equal = False

    oper = operator
    flag_oper = True
    num2 = ''

    expression = num1 + ' ' + operator + ' '
    lcd['text'] = expression
#----------------------------------------------------------------
def clear():
    global num1, num2, oper, flag_oper, flag_equal, expression

    num1 = num2 = oper = ''
    expression = ''
    flag_oper = flag_equal = False

    lcd['text'] = '0'

#----------------------------------------------------------------
def rev_sig():
    global num1, num2
    if not flag_oper:
        if num1:
            num1 = str(float(num1) * -1)
            lcd['text'] = num1
    else:
        if num2:
            num2 = str(float(num2) * -1)
            lcd['text'] = num2

#----------------------------------------------------------------

def func_insert(func):
    global num1, num2, ans, flag_oper, flag_equal, expression
    
    if flag_oper and num2:
        if not calculate():
            return
        flag_oper = False

    if func == 'pi':
        result = math.pi

    elif func == 'e':
        result = math.e

    else:
        if not num1 or num1 == 'Err':
            return

        try:
            number = float(num1)

            if func == 'sqrt':
                result = math.sqrt(number) if number >= 0 else 'Err'

            elif func == 'sin':
                result = math.sin(math.radians(number))

            elif func == 'cos':
                result = math.cos(math.radians(number))

            elif func == 'tan':
                result = math.tan(math.radians(number)) if number % 180 != 90 else 'Err'

            elif func == 'cot':
                result = 1 / math.tan(math.radians(number)) if number % 180 != 0 else 'Err'

            elif func == 'asin':
                result = math.degrees(math.asin(number)) if -1 <= number <= 1 else 'Err'

            elif func == 'acos':
                result = math.degrees(math.acos(number)) if -1 <= number <= 1 else 'Err'

            elif func == 'atan':
                result = math.degrees(math.atan(number))

            elif func == 'ex':
                result = math.exp(number)

            else:
                return

        except:
            result = 'Err'

    num1 = str(result)
    num2 = ''
    flag_oper = False
    flag_equal = True

    expression = num1
    lcd['text'] = expression

    if result != 'Err':
        ans = result

#----------------------------------------------------------------

def total():
    global num1, num2, oper, flag_oper, flag_equal, ans
    if not num1 or not num2:
        return

    try:
        n1 = float(num1)
        n2 = float(num2)
        if oper == '+':
            total_number = n1 + n2
        elif oper == '-':
            total_number = n1 - n2
        elif oper == '*':
            total_number = n1 * n2
        elif oper == '/':
            total_number = n1 / n2 if n2 != 0 else 'Err'
        else:
            return

        lcd['text'] = str(total_number)
        num1 = str(total_number)
        num2 = ''
        oper = ''
        flag_oper = False
        flag_equal = True
        if total_number != 'Err':
            ans = total_number
    except:
        lcd['text'] = 'Err'

#----------------------------------------------------------------
def ans_insert():
    global num1, num2
    if not flag_oper:
        num1 = str(ans)
        lcd['text'] = num1
    else:
        num2 = str(ans)
        lcd['text'] = num2

#----------------------------------------------------------------
def memory_store():
    global memory
    if not flag_oper and num1:
        memory = float(num1)
    elif flag_oper and num2:
        memory = float(num2)

def memory_recall():
    global num1, num2
    if not flag_oper:
        num1 = str(memory)
        lcd['text'] = num1
    else:
        num2 = str(memory)
        lcd['text'] = num2

def memory_clear():
    global memory
    memory = 0

def memory_add():
    global memory
    if not flag_oper and num1:
        memory += float(num1)
    elif flag_oper and num2:
        memory += float(num2)

def memory_subtract():
    global memory
    if not flag_oper and num1:
        memory -= float(num1)
    elif flag_oper and num2:
        memory -= float(num2)

def change_mode():

    if frm1_right.winfo_ismapped():


        frm1_right.grid_remove()

        frm1.columnconfigure(0, weight=1)
        frm1.columnconfigure(1, weight=0)

        btn_mode['text'] = 'Scientific'

        win.geometry('500x600+150+150')

    else:


        frm1.columnconfigure(0, weight=2)
        frm1.columnconfigure(1, weight=1)

        frm1_right.grid()

        btn_mode['text'] = 'Standard'

        win.geometry('750x600+150+150')

#-------------------------------------------------------------------------


win = Tk()
win.geometry('500x600+150+150')
win.configure(bg='#3B3C36')
win.title('Calculator')
win.resizable(True, True)


# LCD
lcd = Label(win, height=3, text='0', fg='white',
            font=('Arial', 20, 'bold'), relief='sunken',
            bg='#3B3C36', anchor='e')

lcd.pack(side=TOP, fill=X, padx=5, pady=5)

btn_mode = Button(win,
                  text='Scientific',
                  font=('Arial', 12, 'bold'),
                  bg='#3B3C36',
                  fg='white',
                  command=change_mode)

btn_mode.pack(side=TOP, anchor='w', pady=3)

# فريم اصلي

frm1 = Frame(win, bg='#3B3C36')
frm1.pack(side=TOP, fill=BOTH, expand=True)

frm1.columnconfigure(0, weight=4)
frm1.columnconfigure(1, weight=2)
frm1.rowconfigure(0, weight=1)


frm1_left = Frame(frm1, bg='#3B3C36')
frm1_left.grid(row=0, column=0, sticky='nsew')


frm1_right = Frame(frm1, bg='#3B3C36')
frm1_right.grid(row=0, column=1, sticky='nsew')


frm1_right.grid_remove()

frm1.columnconfigure(0, weight=1)
frm1.columnconfigure(1, weight=0)


# تنظیم ستون ها و ردیف های ماشین حساب معمولی

for i in range(4):
    frm1_left.columnconfigure(i, weight=1)

for i in range(6):
    frm1_left.rowconfigure(i, weight=1)


# تنظیم ستون ها و ردیف های قسمت علمی

for i in range(2):
    frm1_right.columnconfigure(i, weight=1)

for i in range(6):
    frm1_right.rowconfigure(i, weight=1)


#نصب و فرانت

# بخش مهندسي 1

sqrt_img = PhotoImage(file='sqrt.png')
b_sqrt = Button(frm1_right,
                bg='#6d6e71',
                activebackground='#6d6e71',
                image=sqrt_img,
                command=lambda: func_insert('sqrt'))
b_sqrt.image = sqrt_img

sin_img = PhotoImage(file='sin.png')
b_sin = Button(frm1_right, bg='#56aeef', activebackground='#56aeef', image=sin_img, command=lambda: func_insert('sin'))
b_sin.image = sin_img

cos_img = PhotoImage(file='cos.png')
b_cos = Button(frm1_right, image=cos_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('cos'))
b_cos.image = cos_img

tan_img = PhotoImage(file='tan.png')
b_tan = Button(frm1_right, image=tan_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('tan'))
b_tan.image = tan_img


b_sqrt.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
b_sin.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
b_cos.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
b_tan.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)


#بخش مهندسي 2

cot_img = PhotoImage(file='cot.png')
b_cot = Button(frm1_right, image=cot_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('cot'))
b_cot.image = cot_img

asin_img = PhotoImage(file='asin.png')
b_asin = Button(frm1_right, image=asin_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('asin'))
b_asin.image = asin_img

acos_img = PhotoImage(file='acos.png')
b_acos = Button(frm1_right, image=acos_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('acos'))
b_acos.image = acos_img

atan_img = PhotoImage(file='atan.png')
b_atan = Button(frm1_right, image=atan_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('atan'))
b_atan.image = atan_img


b_cot.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
b_asin.grid(row=2, column=1, sticky='nsew', padx=2, pady=2)
b_acos.grid(row=3, column=0, sticky='nsew', padx=2, pady=2)
b_atan.grid(row=3, column=1, sticky='nsew', padx=2, pady=2)



# بخش مهندسي 3

ex_img = PhotoImage(file='ex.png')
b_ex = Button(frm1_right, image=ex_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('ex'))
b_ex.image = ex_img

e_img = PhotoImage(file='e.png')
b_e = Button(frm1_right, image=e_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('e'))
b_e.image = e_img

pi_img = PhotoImage(file='pi.png')
b_pi = Button(frm1_right, image=pi_img, bg='#56aeef', activebackground='#56aeef', command=lambda: func_insert('pi'))
b_pi.image = pi_img

ans_img = PhotoImage(file='ans.png')
b_ans = Button(frm1_right, image=ans_img, bg='#56aeef', activebackground='#56aeef', command=ans_insert)
b_ans.image = ans_img


b_ex.grid(row=4, column=0, sticky='nsew', padx=2, pady=2)
b_e.grid(row=4, column=1, sticky='nsew', padx=2, pady=2)
b_pi.grid(row=5, column=0, sticky='nsew', padx=2, pady=2)
b_ans.grid(row=5, column=1, sticky='nsew', padx=2, pady=2)




# ماشين حساب استاندارد

ms_img = PhotoImage(file='ms.png')
b_ms = Button(frm1_left, image=ms_img, bg='#6d6e71', activebackground='#6d6e71', command=memory_store)
b_ms.image = ms_img

mc_img = PhotoImage(file='mc.png')
b_mc = Button(frm1_left, image=mc_img, bg='#6d6e71', activebackground='#6d6e71', command=memory_clear)
b_mc.image = mc_img

mr_img = PhotoImage(file='mr.png')
b_mr = Button(frm1_left, image=mr_img, bg='#6d6e71', activebackground='#6d6e71', command=memory_recall)
b_mr.image = mr_img

c_img = PhotoImage(file='c.png')
b_c = Button(frm1_left, image=c_img, bg='#6d6e71', activebackground='#6d6e71', command=clear)
b_c.image = c_img


b_ms.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
b_mc.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
b_mr.grid(row=0, column=2, sticky='nsew', padx=2, pady=2)
b_c.grid(row=0, column=3, sticky='nsew', padx=2, pady=2)



mplus_img = PhotoImage(file='mplus.png')
b_mplus = Button(frm1_left, image=mplus_img, bg='#56aeef', activebackground='#56aeef',command=memory_add)
b_mplus.image = mplus_img

mminus_img = PhotoImage(file='mminus.png')
b_mminus = Button(frm1_left, image=mminus_img, bg='#56aeef', activebackground='#56aeef', command=memory_subtract)
b_mminus.image = mminus_img

mul_img = PhotoImage(file='mul.png')
b_mul = Button(frm1_left, image=mul_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: oper_insert('*'))
b_mul.image = mul_img

div_img = PhotoImage(file='div.png')
b_div = Button(frm1_left, image=div_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: oper_insert('/'))
b_div.image = div_img


b_mplus.grid(row=1, column=0,  sticky='nsew', padx=2, pady=2)
b_mminus.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)
b_mul.grid(row=1, column=2, sticky='nsew', padx=2, pady=2)
b_div.grid(row=1, column=3, sticky='nsew', padx=2, pady=2)




# نصب و دکمه هاي اعداد و ساير دکمه هاي ماشين حساب معمولي


seven_img = PhotoImage(file='seven.png')
b7 = Button(frm1_left, image=seven_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('7'))
b7.image = seven_img

eight_img = PhotoImage(file='eight.png')
b8 = Button(frm1_left, image=eight_img, bg='#6d6e71', activebackground='#6d6e71',command=lambda: num_insert('8'))
b8.image = eight_img

nine_img = PhotoImage(file='nine.png')
b9 = Button(frm1_left, image=nine_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('9'))
b9.image = nine_img

minus_img = PhotoImage(file='minus.png')
b_minus = Button(frm1_left, image=minus_img, bg='#c42337', activebackground='#c42337', command=lambda: oper_insert('-'))
b_minus.image = minus_img


b7.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
b8.grid(row=2, column=1, sticky='nsew', padx=2, pady=2)
b9.grid(row=2, column=2, sticky='nsew', padx=2, pady=2)
b_minus.grid(row=2, column=3, sticky='nsew', padx=2, pady=2)




four_img = PhotoImage(file='four.png')
b4 = Button(frm1_left, image=four_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('4'))
b4.image = four_img

five_img = PhotoImage(file='five.png')
b5 = Button(frm1_left, image=five_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('5'))
b5.image = five_img

six_img = PhotoImage(file='six.png')
b6 = Button(frm1_left, image=six_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('6'))
b6.image = six_img

plus_img = PhotoImage(file='plus.png')
b_plus = Button(frm1_left, image=plus_img, bg='#6d6e71',
                activebackground='#6d6e71', command=lambda: oper_insert('+'))
b_plus.image = plus_img


b4.grid(row=3, column=0, sticky='nsew', padx=2, pady=2)
b5.grid(row=3, column=1, sticky='nsew', padx=2, pady=2)
b6.grid(row=3, column=2, sticky='nsew', padx=2, pady=2)
b_plus.grid(row=3, column=3, sticky='nsew', padx=2, pady=2)



one_img = PhotoImage(file='one.png')
b1 = Button(frm1_left, image=one_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('1'))
b1.image = one_img

two_img = PhotoImage(file='two.png')
b2 = Button(frm1_left, image=two_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('2'))
b2.image = two_img

three_img = PhotoImage(file='three.png')
b3 = Button(frm1_left, image=three_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('3'))
b3.image = three_img


b1.grid(row=4, column=0, sticky='nsew', padx=2, pady=2)
b2.grid(row=4, column=1, sticky='nsew', padx=2, pady=2)
b3.grid(row=4, column=2, sticky='nsew', padx=2, pady=2)




eq_img = PhotoImage(file='equalsign.png')
b_eq = Button(frm1_left, image=eq_img, bg='#6d6e71', activebackground='#6d6e71', command=total)
b_eq.image = eq_img

b_eq.grid(row=4, column=3, rowspan=2, sticky='nsew', padx=2, pady=2)



zero_img = PhotoImage(file='zero.png')
b0 = Button(frm1_left, image=zero_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('0'))
b0.image = zero_img


dot_img = PhotoImage(file='dot.png')
b_dot = Button(frm1_left,image=dot_img, bg='#6d6e71', activebackground='#6d6e71', command=lambda: num_insert('.'))
b_dot.image = dot_img


plusminus_img = PhotoImage(file='plusminus.png')
b_sign = Button(frm1_left, image=plusminus_img, bg='#6d6e71', activebackground='#6d6e71', command=rev_sig)
b_sign.image = plusminus_img


b_sign.grid(row=5, column=0, sticky='nsew', padx=2, pady=2)
b0.grid(row=5, column=1, sticky='nsew', padx=2, pady=2)
b_dot.grid(row=5, column=2, sticky='nsew', padx=2, pady=2)


win.mainloop()

