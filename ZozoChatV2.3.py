import tkinter as tk
import os


form=tk.Tk()
form.title('Zozamad Chat V2.3')
form.geometry('500x250')
form.resizable(False,False)

yazi=tk.Label(form,text='ZozoChatV2.3 IRC Chata Hoşgeldiniz.',font='serif 15')
yazi.pack()
# Bu Kisim Ise Verileri Printe Donusturuyor



def receive():
    entry2=ent1.get()
    entry=ent2.get()
    print(entry2,':',entry)

def cu():
    print('''H	Periyodik tablo	He
Li	Be		B	C	N	O	F	Ne
Na	Mg		Al	Si	P	S	Cl	Ar
K	Ca	Sc	Ti	V	Cr	Mn	Fe	Co	Ni	Cu	Zn	Ga	Ge	As	Se	Br	Kr
Rb	Sr	Y	Zr	Nb	Mo	Tc	Ru	Rh	Pd	Ag	Cd	In	Sn	Sb	Te	I	Xe
Cs	Ba	 	Hf	Ta	W	Re	Os	Ir	Pt	Au	Hg	Tl	Pb	Bi	Po	At	Rn
Fr	Ra	 	Rf	Db	Sg	Bh	Hs	Mt	Ds	Rg	Cn	Nh	Fl	Mc	Lv	Ts	Og	 
 	La	Ce	Pr	Nd	Pm	Sm	Eu	Gd	Tb	Dy	Ho	Er	Tm	Yb	Lu
 	Ac	Th	Pa	U	Np	Pu	Am	Cm	Bk	Cf	Es	Fm	Md	No	Lr	''')



def temizle():
    os.system('cls')

# Asagi Kisimda Veriler Verilip ent1 Adli Stringden Aliniyor

talimat1=tk.Label(form,text='Isim : ')
talimat1.pack()
ent1=tk.Entry(width=20,fg='red',bg='black',font='serif 15',)
ent1.pack()
talimat2=tk.Label(form,text='Mesaj : ')
talimat2.pack()
ent2=tk.Entry(width=30,fg='purple',bg='black',font='serif 15')
ent2.pack()


tus2=tk.Button(form,text='Element Say',bg='black',fg='green',font='serif 10', command=cu)
tus2.pack()

tus3=tk.Button(form,text='Chati Temizle',bg='black',fg='blue',command=temizle)
tus3.pack()

tus=tk.Button(form,text='Enter',bg='black',fg='yellow',font='serif 10', command=receive,width='20',heigh='2')
tus.pack()

telif=tk.Label(form,text='© Butun Telif Haklari Zozamad Group a Saklidir ©',font='serif 8')
telif.pack()
form.mainloop()
# Made By RootManX#7356
