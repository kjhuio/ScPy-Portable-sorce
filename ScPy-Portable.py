import customtkinter as ctk
from tkinter import messagebox as msg
import scratchattach as scratch
#end import space

def buttonlogin():
    yn = msg.askyesno("警告","ログインしますか?")
    if yn:
        pass_word = Entry_password.get()
        user_name = Entry_username.get()
        try :
            scratch.login(user_name,pass_word)
        except :
            msg.showerror("エラー","ログインに失敗しました。",options="ユーザー名またはパスワードが間違っています。")
        else :
            msg.showinfo("成功!","ログインに成功しました。")
def varconnect() :
    cyn = msg.askyesno("警告","変数を変更しますか?")
    if cyn :
        if Entry_password.get() and Entry_username.get() and Entry_ProjectID.get() and Entry_varname.get() and Entry_var.get():
            pass_word = Entry_password.get()
            user_name = Entry_username.get()
            varname = Entry_varname.get()
            try :
                projectid_int = int(Entry_ProjectID.get())
                cloudvar_int = int(Entry_var.get())
            except :
                msg.showerror("エラー","プロジェクトIDまたは変数値が数字ではありません。")
            else :
                sessiond = scratch.login(user_name,pass_word)
                connection = sessiond.connect_cloud(project_id=projectid_int)
                try :
                    connection.set_var(varname,cloudvar_int)
                except :
                    msg.showerror("エラー","クラウド変数のセットに失敗しました。")
                else :
                    msg.showinfo("成功!","クラウド変数のセットに成功しました。")


root = ctk.CTk()

FONT_TYPE = "meiryo"
root.fonts = (FONT_TYPE,15)
root.fontssmall = (FONT_TYPE,10)
root.fontsbig = (FONT_TYPE,20)
root.iconbitmap("favicon.ico")
root.geometry("400x600")
root.title("ScPy-Portable")

copyrightLabel = ctk.CTkLabel(master=root,text="created by qwe0412 & kjhuio 2024",font=root.fontssmall)
copyrightLabel.place(x=120,y=580)
Entry_username = ctk.CTkEntry(master=root,placeholder_text="ここにユーザー名を入力",font=root.fonts,width=280)
Entry_username.place(x=100,y=100)
Entry_userLabel = ctk.CTkLabel(master=root,text="ユーザ名:",font=root.fonts)
Entry_userLabel.place(x=20,y=100)
Entry_password = ctk.CTkEntry(root,260,font=root.fonts,placeholder_text="ここにパスワードを入力",show="*")
Entry_password.place(x=120,y=140)
Entry_passLabel = ctk.CTkLabel(master=root,text="パスワード:",font=root.fonts)
Entry_passLabel.place(x=20,y=140)
LoginButton = ctk.CTkButton(master=root,text="Scratchにログイン",font=root.fonts,command=buttonlogin)
LoginButton.place(x=120,y=180)
Entry_ProjectID = ctk.CTkEntry(root,240,placeholder_text="ここにプロジェクトIDを入力",font=root.fonts)
Entry_ProjectID.place(x=140,y=220)
Project_Label = ctk.CTkLabel(master=root,text="プロジェクトID:",font=root.fonts)
Project_Label.place(x=20,y=220)
Entry_varname = ctk.CTkEntry(root,280,placeholder_text="ここに変数名を入力",font=root.fonts)
Entry_varname.place(x=100,y=260)
Entry_varLabl = ctk.CTkLabel(master=root,text="変数名:",font=root.fonts)
Entry_varLabl.place(x=20,y=260)
Entry_var = ctk.CTkEntry(root,280,placeholder_text="ここに変数値を入力",font=root.fonts)
Entry_var.place(x=100,y=300)
Entry_varLab2 = ctk.CTkLabel(master=root,text="変数値:",font=root.fonts)
Entry_varLab2.place(x=20,y=300)
connectButton = ctk.CTkButton(master=root,text="クラウド変数を変更",font=root.fonts,command=varconnect)
connectButton.place(x=120,y=360)

root.mainloop()