from tkinter import *
from tkinter import messagebox as messagebox


class Calc(Frame):
        
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.result = "+"
        self.create()

    def create(self):
        self.formula = "0"
        self.label = Label(text = self.formula, font = (20), bg = "#FFFFFF",\
                           fg = "#333")
        self.label.place(x = 11, y = 50)

        btns = ["C", "<", "+", "3", "4", "-", "1", "2", ".", "0", "="]

        x = 10
        y = 140
        for b in btns:
            com = lambda x = b: self.logic(x)
            if b != "=":
                Button(text = b, bg = "#000080", activebackground = "#191970", font = (15), fg = "#FFFFFF",\
                       activeforeground = "#FFFFFF", command = com).place(x = x, y = y, width = 115, height = 79)
            else:
                Button(text = b, bg = "#000080", activebackground = "#191970", font = (15), fg = "#FFFFFF",\
                       activeforeground = "#FFFFFF", command = com).place(x = x, y = y, width = 232, height = 79)
            x += 117
            if x > 280:
                x = 10
                y += 81

        #Создание меню.        
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        submenu = Menu(menubar, tearoff=0)

        option_menu2 = Menu(submenu, tearoff=0)

        option_menu2.add_command(label = "Сложение (+)", command = lambda: self.logic("+"))
        option_menu2.add_command(label = "Вычитание (-)", command = lambda: self.logic("-"))
        option_menu2.add_command(label = "Результат (=)", command = lambda: self.logic("="))
        submenu.add_cascade(label = "Арифметика", menu=option_menu2)

        submenu.add_separator()
        submenu.add_command(label = "Выход", command = self.exit)
        menubar.add_cascade(label = "Команды", menu = submenu)
        
        menubar.add_command(label = "О программе", command = self.info)

    @staticmethod
    def translate_to(n):
        num = str(n)
        sign = 1
        res = 0
        if num[0] == "-":
            sign = -1
            num = num[1:]
        if num.count(".") == 1:
            res = 0
            p = len(num[0 : num.index(".")]) - 1
            for i in range(0, num.index(".")):
                res += eval(num[i]) * 5 ** p
                p -= 1
            p = -1
            for i in range(num.index(".") + 1, len(num)):
                res += eval(num[i]) * 5 ** p
                p -= 1
        if num.count(".") == 0:
            res = 0
            p = len(num) - 1
            for i in range(len(num)):
                res += eval(num[i]) * 5 ** p
                p -= 1
                
        #res = round(res, 6)
        return res * sign
    

    @staticmethod
    def calc_and_trans(expr):
        try:
            num = str(eval(expr))
        except:
            return
        sign = 1
        nums = num.split(".")
        if nums[0][0] == "-":
            sign = -1
            nums[0] = str(abs(int(nums[0])))
        int_part = int(nums[0])
        mods = []
        while int_part != 0:
            mods.append(str(int_part % 5))
            int_part //= 5
        mods.reverse()
        try:
            int_part = int("".join(mods))
        except ValueError:
            int_part = 0
        if len(nums) == 1:
            return str(sign * int_part)
        else:
            float_part = float("0." + nums[1])
            n = 0
            float_nums = []
            while float_part != 0.0 :
                float_part *= 5
                if float_part >= 1:
                    float_nums.append(str(int(float_part)))
                    float_part -= int(float_part)
                else:
                    float_nums.append("0")
                #print("n = ", n)
                n += 1
                if n == 8:
                    break
            float_part = "0." + "".join(float_nums)
            try:
                result = sign * (float(int_part) + float(float_part))
            except ValueError:
                try:
                    result = sign * (0.0 + float(float_part))
                except ValueError:
                    result = 0
                    
            return str(result)

    def logic(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "<":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            self.result += str(self.translate_to(self.formula))
            #print(self.result)
            self.formula = self.calc_and_trans(self.result)
            self.result = ""
        elif operation == "+":
            if self.formula == "0":
                pass
            else:
                self.result += str(self.translate_to(self.formula)) + " + "
                self.formula = "0"
        elif operation == "-" and self.formula != "0":
            self.result += str(self.translate_to(self.formula)) + " - "
            self.formula = "0"
        else:
            if self.formula == "0":
                self.formula = ""
            if operation != "." or self.formula.count(".") < 1:
                self.formula += operation
            if len(self.result) == 0:
                self.formula = ""
                self.result += "+"
                self.formula += operation
        self.update()

    def key(self, event):
        if event.char in ["0", "1", "2", "3", "4", "-", ".", "+", "="] or event.keysym == "BackSpace":
            if event.keysym == "BackSpace":
                event.char = "<"
            if event.char == "." and self.formula.count(".") < 1 or event.char != ".":
                self.logic(event.char)

    def update(self):
        if self.formula == "":
            self.formula = "0"
        if len(self.formula) < 24:
            self.label.configure(text=self.formula)

    @staticmethod
    def info():
        messagebox.showinfo(message = "Калькулятор вычитает и складывает в пятеричной системе счисления.")

    def exit(self):
        #self.quit()
        root.destroy()
        

if __name__ == "__main__":
    root = Tk()
    root["bg"] = "#FFFFFF"
    root.geometry("370x475+500+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Calc(root)
    app.pack()
    root.bind_all("<Key>", app.key)
    root.mainloop()

