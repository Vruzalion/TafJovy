import time
from tkinter import *
import os
from pathlib import Path
from tkinter import ttk
from tkinter.simpledialog import askstring
import shutil
from tkinter.messagebox import showinfo

tk = Tk()

tk.title('FILE MANAGER JOVY')
tk.geometry("1400x850")
a = StringVar()  # permet de modifier la barre d'acces ( definir le chemin du repertoire courant)
L = []  # permet de stocker les chemins des elements a copier
rep = []  # permet de stocker les differents repertoires a utilisers pour le boutton precedent
rep2 = []  # permet de stocker les differents repertoires a utilisers pour le boutton suivant

#  creation des panels
frame_1 = PanedWindow(tk, orient=HORIZONTAL)
frame_1.pack(expand=False, fill=BOTH, side=TOP)

frame_3 = PanedWindow(tk, orient=HORIZONTAL)
frame_3.pack(expand=False, fill=BOTH, side=TOP)

frame_2 = PanedWindow(tk, orient=HORIZONTAL)
frame_2.pack(expand=False, fill=BOTH, side=BOTTOM)

frame_4 = PanedWindow(tk, orient=VERTICAL)
frame_4.pack(expand=False, fill=BOTH, side=LEFT)

frame_5 = PanedWindow(tk, orient=VERTICAL)
frame_5.pack(expand=False, fill=BOTH, side=LEFT)

frame_6 = PanedWindow(tk, orient=VERTICAL)
frame_6.pack(expand=False, fill=BOTH, side=RIGHT)

frame_7 = PanedWindow(tk, orient=VERTICAL)
frame_7.pack(expand=True, fill=BOTH, side=RIGHT)

#       definition des images
copy = PhotoImage(file='images/copy_24px.png')
paste = PhotoImage(file='images/paste_24px.png')
deletee = PhotoImage(file='images/delete_24px.png')
new_folder = PhotoImage(file='images/new_folder_24px.png')
research = PhotoImage(file='images/search_24px.png')
renamee = PhotoImage(file='images/rename_24px.png')
disk = PhotoImage(file='images/disk_24px.png')
suiv = PhotoImage(file='images/next_16px.png')
prec = PhotoImage(file='images/previous_16px.png')
tree_folder = PhotoImage(file='images/folder_tree_16px.png')
couper = PhotoImage(file='images/coupon_16px.png')
# ajout des differents bouttons
boutton_new_folder = Button(frame_1, state='normal', text='Nouveau dossier', image=new_folder)
boutton_new_folder.grid(row=0, column=0)
boutton_copy = Button(frame_1, state='normal', text='copier', image=copy)
boutton_copy.grid(row=0, column=1)
boutton_paste = Button(frame_1, state='normal', text='coller', image=paste)
boutton_paste.grid(row=0, column=2)
boutton_delete = Button(frame_1, state='normal', text='supprimer', image=deletee)
boutton_delete.grid(row=0, column=3)
boutton_rename = Button(frame_1, state='normal', text='renommer', image=renamee)
boutton_rename.grid(row=0, column=4)
boutton_couper = Button(frame_1,state='normal', text='couper', image=couper)
boutton_couper.grid(row=0, column=5)
label = Label(frame_1)

boutton_prec = Button(frame_3, state='normal', image=prec)
boutton_prec.grid(row=0, column=0)
boutton_next = Button(frame_3, state='normal', image=suiv)
boutton_next.grid(row=0, column=1)
entree_1 = Entry(frame_3, textvariable=a, width=195)
entree_1.grid(row=0, column=2, columnspan=80, sticky=EW)
entree_2 = Entry(frame_3)
entree_2.grid(row=0, column=83, columnspan=20, sticky=EW)

#  declaration des arbres
tree = ttk.Treeview(frame_4)
tree.pack(expand=True, fill=BOTH)
tree.heading('#0',image= tree_folder, text='Arborescence')

colonne = ('Nom', 'Type', 'Taille', 'Mise a jour le',)

tree_2 = ttk.Treeview(frame_7, columns=colonne, show='headings')
tree_2.heading('Nom', text='Nom')
tree_2.heading('Mise a jour le', text='Mise a jour le')
tree_2.heading('Type', text='Type')
tree_2.heading('Taille', text='Taille')

vide = Label(tree_2, text='Le dossier est vide', background='white')
frame_7.add(tree_2)

# ajout de les barres de defilement a la frame
scrollbar = Scrollbar(frame_5)
frame_5.add(scrollbar)
scrollbar_2 = Scrollbar(frame_6)
frame_6.add(scrollbar_2)

scrollbar.config(command=tree.yview)
scrollbar_2.config(command=tree_2.yview)

#    Insertion des repertoires

disques = [chr(x) + ':' for x in range(10, 90) if os.path.exists(chr(x) + ':')]
folders =  disques

#  actualisation automatique des disques
def autodesk():
    l = [chr(x) + ':' for x in range(10, 90) if os.path.exists(chr(x) + ':')]
    t =  l
    z = entree_1.get()

    for i in l:
        if i not in tree.get_children():
            tree.insert('', "end", i, text=i, image=disk)
        else:
            pass

    for i in tree.get_children():
        if i not in t:
            tree.delete(i)

            if z[:2] == i:
                a.set('')
                for ligne in tree_2.get_children():
                    tree_2.delete(ligne)
            else:
                pass

        else:
            pass

    tk.after(1, autodesk)

tk.after(1, autodesk)


# affiche les elements d'un repertoire dans l'arbre central
def peupler_arbre(j):
    liste = []

    try:
            for entry in os.listdir(j):
                try:
                    if os.path.isfile(os.path.join(j, entry)):
                        try:
                            chemin_sd_sf = os.path.join(j, entry)
                            date = time.ctime(os.path.getctime(chemin_sd_sf))
                            FN, FE = os.path.splitext(chemin_sd_sf)
                            q = len(FE)

                            if (FE[1:] != 'sys') and (FE[1:] != 'ini') and (entry[0] != '$'):
                                type_1 = 'Fichier ' + FE[1:]
                                taille = Path(chemin_sd_sf).stat().st_size
                                liste.append((entry[:-q], type_1, str(taille) + " octet(s)", date, chemin_sd_sf))

                        except OSError as e:
                            print(e)
                            tk.messagebox.showerror('ERREUR', message=str(e))

                    else:
                        try:
                            chemin_sd_sf = os.path.join(j, entry)
                            date = time.ctime(os.path.getctime(chemin_sd_sf))
                            type_1 = 'Dossier de Fichiers'
                            taille = Path(chemin_sd_sf).stat().st_size
                            if (entry != "System Volume Information") and (entry[0] != '$'):
                                liste.append((entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))
                        except OSError as e:
                            print(e)
                            tk.messagebox.showerror('ERREUR', message=str(e))
                except (OSError, TypeError, PermissionError):
                    pass
            for ligne in tree_2.get_children():
                tree_2.delete(ligne)
            for ligne in liste:
                tree_2.insert('', 'end', values=ligne)

    except (OSError, TypeError, PermissionError):
        pass


# affiche les sous-dossiers d'un dossier et liste ses elements dans l'arbre de droite
def treeDossiers(r):
    click = tree.focus()
    click_info = tree.item(click)['text']
    noeud = tree.parent(click)
    liste = []

    if noeud != '':
        i = tree.item(noeud)['text']
        j = os.path.join(i, click_info)
        noeud = tree.parent(noeud)
        while noeud != '':
            i = tree.item(noeud)['text']
            j = os.path.join(i, j)
            noeud = tree.parent(noeud)
    else:
        j = Path(click_info + '//')

    a.set(j)
    if j not in rep:
        rep.append(j)
    else:
        pass

    try:
        for i in tree.get_children(click_info):
            tree.delete(i)
        for ligne in tree_2.get_children():
            tree_2.delete(ligne)
        for entry in os.listdir(j):
            try:
                if os.path.isfile(os.path.join(j, entry)):
                    try:
                        chemin_sd_sf = os.path.join(j, entry)
                        date = time.ctime(os.path.getctime(chemin_sd_sf))
                        FN, FE = os.path.splitext(chemin_sd_sf)
                        q = len(FE)

                        if (FE[1:] != 'sys'):
                            type_1 = 'Fichier ' + FE[1:]
                            taille = Path(chemin_sd_sf).stat().st_size
                            liste.append((entry[:-q], type_1, str(taille) + " octet(s)", date, chemin_sd_sf))
                            tree_2.insert('', 'end',
                                          values=(entry[:-q], type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                    except OSError as e:
                        print(e)
                        tk.messagebox.showerror('ERREUR', message=str(e))

                else:
                    try:
                        chemin_sd_sf = os.path.join(j, entry)
                        date = time.ctime(os.path.getctime(chemin_sd_sf))
                        type_1 = 'Dossier de Fichiers'
                        taille = Path(chemin_sd_sf).stat().st_size
                        if (entry != "System Volume Information") and (entry[0] != '$'):
                            liste.append((entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                            tree.insert(click_info, 'end', entry, text=entry, image=new_folder)
                            tree_2.insert('', 'end',
                                          values=(entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))
                    except OSError as e:
                        print(e)
                        tk.messagebox.showerror('ERREUR', message=str(e))
            except (OSError, TypeError, PermissionError):
                pass

    except (OSError, TypeError, PermissionError):
        pass


# liste les elements d'un repertoire selectionne dans l'arbre de gauche sans afficher ses sous-dossiers
def listage(r):
    click = tree.focus()
    click_info = tree.item(click)['text']
    noeud = tree.parent(click)
    liste = []

    if noeud != '':
        i = tree.item(noeud)['text']
        j = os.path.join(i, click_info)
        noeud = tree.parent(noeud)
        while noeud != '':
            i = tree.item(noeud)['text']
            j = os.path.join(i, j)
            noeud = tree.parent(noeud)
    else:
        j = Path(click_info + '//')

    a.set(j)
    if j not in rep:
        rep.append(j)
    else:
        pass

    try:
        for ligne in tree_2.get_children():
            tree_2.delete(ligne)
        for entry in os.listdir(j):
            try:
                if os.path.isfile(os.path.join(j, entry)):
                    try:
                        chemin_sd_sf = os.path.join(j, entry)
                        date = time.ctime(os.path.getctime(chemin_sd_sf))
                        FN, FE = os.path.splitext(chemin_sd_sf)
                        q = len(FE)

                        if (FE[1:] != 'sys'):
                            type_1 = 'Fichier ' + FE[1:]
                            taille = Path(chemin_sd_sf).stat().st_size
                            liste.append((entry[:-q], type_1, str(taille) + " octet(s)", date, chemin_sd_sf))
                            tree_2.insert('', 'end',
                                          values=(entry[:-q], type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                    except OSError as e:
                        print(e)
                        tk.messagebox.showerror('ERREUR', message=str(e))

                else:
                    try:
                        chemin_sd_sf = os.path.join(j, entry)
                        date = time.ctime(os.path.getctime(chemin_sd_sf))
                        type_1 = 'Dossier de Fichiers'
                        taille = Path(chemin_sd_sf).stat().st_size
                        if (entry != "System Volume Information") and (entry[0] != '$'):
                            liste.append((entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                            tree_2.insert('', 'end',
                                          values=(entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))
                    except OSError as e:
                        print(e)
                        tk.messagebox.showerror('ERREUR', message=str(e))
            except (OSError, TypeError, PermissionError):
                pass
    except (OSError, TypeError, PermissionError):
        pass


#  permet de naviguer dans l'arbre central
def deroulement(r):
    click = tree_2.focus()
    che = (tree_2.item(click)['values'])[4]

    if os.path.isfile(che):
        os.startfile(che)
    else:
        try:
            peupler_arbre(che)
            a.set(che)
            rep.append(che)
        except OSError as e:
            print(e)
            tk.messagebox.showerror('erreur', message=str(e))


tree.bind("<Double-1>", treeDossiers)
tree.bind('<<TreeviewSelect>>', listage)
tree_2.bind('<Double-1>', deroulement)


# renommer un element
def rename(r):
    click = tree_2.focus()
    g = entree_1.get()
    che = (tree_2.item(click)['values'])[4]
    new_name = askstring("Renommer", "NOUVEAU NOM ?")

    if os.path.isdir(che):
        new_che = Path(os.path.join(g, new_name))
        os.rename(che, new_che)
    else:
        new_che = Path(os.path.join(g, new_name) + os.path.splitext(che)[1])
        os.rename(che, new_che)

    for i in tree_2.get_children():
        tree_2.delete(i)
    peupler_arbre(g)

boutton_rename.bind('<Button-1>', rename)


# creer un nouveau dossier
def create_folder(event):
    liste=[]
    k = 1
    i = entree_1.get()
    nom = "Nouveau dossier "
    j = os.path.join(i, nom)
    if not os.path.exists(j):
        os.mkdir(j)
    else:
        nom = "Nouveau dossier " + str(k)
        j = os.path.join(i, nom)
        while os.path.exists(j):
            k += 1
            nom = "Nouveau dossier " + str(k)
            j = os.path.join(i, nom)
        os.mkdir(j)

    for entry in os.listdir(i):
        try:
            if os.path.isfile(os.path.join(i, entry)):
                try:
                    chemin_sd_sf = os.path.join(i, entry)
                    date = time.ctime(os.path.getctime(chemin_sd_sf))
                    FN, FE = os.path.splitext(chemin_sd_sf)
                    q = len(FE)

                    if (FE[1:] != 'sys') & (FE[1:] != 'ini'):
                        type_1 = 'Fichier ' + FE[1:]
                        taille = Path(chemin_sd_sf).stat().st_size

                        liste.append((entry[:-q], type_1, str(taille) + " octet(s)", date, chemin_sd_sf))

                except OSError as e:
                    print(e)
                    tk.messagebox.showerror('ERREUR', message=str(e))

            elif (os.path.isdir(os.path.join(i, entry))):
                try:
                    chemin_sd_sf = os.path.join(i, entry)
                    date = time.ctime(os.path.getctime(chemin_sd_sf))
                    type_1 = 'Dossier de Fichiers'
                    taille = Path(chemin_sd_sf).stat().st_size
                    if (entry != "$RECYCLE.BIN") and (entry != "System Volume Information"):
                        liste.append((entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                except OSError as e:
                    print(e)
                    tk.messagebox.showerror('ERREUR', message=str(e))
        except (OSError, TypeError, PermissionError):
            pass
    for ligne in tree_2.get_children():
        tree_2.delete(ligne)
    for ligne in liste:
        tree_2.insert('', 'end', values=ligne)


boutton_new_folder.bind('<Button-1>', create_folder)


#       Supprimer un element
def delete(event):
    B = tree_2.selection()

    for click in B:
        che = (tree_2.item(click)['values'])[4]

        try:
            if os.path.isfile(che):
                os.remove(che)
                tree_2.delete(click)
            else:
                if len(os.listdir(che)) == 0:
                    os.rmdir(che)
                    tree_2.delete(click)
                else:
                    shutil.rmtree(che)
                    tree_2.delete(click)
        except OSError as e:
            showinfo('ERREUR', message=str(e))


tk.bind('<Delete>', delete)
boutton_delete.bind('<Button-1>', delete)


# copie des elements
def copie(event):
    L.clear()
    for click in tree_2.selection():
        L.append((tree_2.item(click)['values'])[4])
    L.append("0")


boutton_copy.bind('<Button-1>', copie)


# la taille reelle des dossiers
def real_size(folder_path):
    total_size = Path(folder_path).stat().st_size

    for item in os.listdir(folder_path):
        itempath = os.path.join(folder_path, item)

        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)

        elif os.path.isdir(itempath):
            total_size += real_size(itempath)

    return total_size


#fonction coller
def coller(event):
    d = entree_1.get()
    for s in L[:-1]:
        if s not in [os.path.join(d, j) for j in os.listdir(d)]:
            if os.path.isfile(s):
                shutil.copy(s, d)
                date = time.ctime(os.path.getctime(s))
                fn, fe = os.path.splitext(s)
                if (fe[1:] != 'sys') and (fe[1:] != 'ini'):
                    type_1 = 'Fichier ' + fe[1:]
                    taille = Path(s).stat().st_size
                    tree_2.insert('', 'end', values=(Path(s).stem, type_1, str(taille) + " octet(s)", date, s))

            elif os.path.isdir(s):
                j = os.path.join(d, os.path.basename(s))
                total, used, free = shutil.disk_usage(j[:2])
                if j not in [os.path.join(d, i) for i in os.listdir(d)]:
                    if len(os.listdir(s)) == 0:
                        taille = Path(s).stat().st_size
                    else:
                        taille = real_size(s)

                    if free > taille:
                        #os.mkdir(j)
                        shutil.copytree(s,j)
                        date = time.ctime(os.path.getctime(j))
                        type_1 = 'Dossier de Fichiers'
                        taille = Path(j).stat().st_size

                        tree_2.insert('', 'end',
                                  values=(os.path.basename(j), type_1, str(taille) + "    octet(s)", date, j))
                    else:
                        showinfo('ALERT', message="Espace insuffisant !!")
                else:
                    showinfo('ALERT', message="Cet element existe deja.")
                    pass

        else:
            showinfo('ALERT', message="Element existant.")
            pass
        if L[-1]=="0":
            pass
        else:
             try:
                if os.path.isfile(s):
                    os.remove(s)
                else:
                    if len(os.listdir(s)) == 0:
                        os.rmdir(s)
                    else:
                        shutil.rmtree(s)
             except OSError as e:
                showinfo('ERREUR', message=str(e))



boutton_paste.bind('<Button-1>', coller)


#  rechercher
def rechercher(event):
    a = entree_2.get()
    liste = []
    j = entree_1.get()

    for ligne in tree_2.get_children():
        tree_2.delete(ligne)

    for entry in os.listdir(j):
        try:
            if (os.path.isfile(os.path.join(j, entry))) & (a in entry):
                try:
                    chemin_sd_sf = os.path.join(j, entry)
                    date = time.ctime(os.path.getctime(chemin_sd_sf))
                    FN, FE = os.path.splitext(chemin_sd_sf)
                    q = len(FE)

                    if (FE[1:] != 'sys') & (FE[1:] != 'ini'):
                        type_1 = 'Fichier ' + FE[1:]
                        taille = Path(chemin_sd_sf).stat().st_size

                        liste.append((entry[:-q], type_1, str(taille) + " octet(s)", date, chemin_sd_sf))

                except OSError as e:
                    print(e)
                    tk.messagebox.showerror('ERREUR', message=str(e))

            elif (os.path.isdir(os.path.join(j, entry))) & (a in entry):
                try:
                    chemin_sd_sf = os.path.join(j, entry)
                    date = time.ctime(os.path.getctime(chemin_sd_sf))
                    type_1 = 'Dossier de Fichiers'
                    taille = Path(chemin_sd_sf).stat().st_size
                    if (entry != "$RECYCLE.BIN") and (entry != "System Volume Information"):
                        liste.append((entry, type_1, str(taille) + "    octet(s)", date, chemin_sd_sf))

                except OSError as e:
                    print(e)
                    tk.messagebox.showerror('ERREUR', message=str(e))
        except (OSError, TypeError, PermissionError):
            pass
    for ligne in tree_2.get_children():
        tree_2.delete(ligne)
    for ligne in liste:
        tree_2.insert('', 'end', values=ligne)

entree_2.bind('<KeyRelease-Return>', rechercher)

#fonction couper
def couper_element():
    L.clear()
    for click in tree_2.selection():
        L.append((tree_2.item(click)['values'])[4])
    L.append("1")

boutton_couper.config(command=couper_element)

#fonction precedent
def previous(r):
    n = len(rep)
    l = entree_1.get()
    m = rep.index(l) - 1

    if (n == 0) or (m == 0):
        pass
    else:
        j = rep[m]
        a.set(j)
        peupler_arbre(j)

boutton_prec.bind('<Button-1>', previous)

# fonction suivant
def next(r):
    n = len(rep)
    l = entree_1.get()
    m = rep.index(l) + 1
    if (n == 0) or (m > n):
        pass

    else:
        j = rep[m]
        a.set(j)
        peupler_arbre(j)

boutton_next.bind('<Button-1>', next)


tk.mainloop()
