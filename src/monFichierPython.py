def alcool (a):
    """Number ->Number"""
    #D:dict[Number:Number]
    D={0.5:2, 0.8:10, 1.5:32}
    #pre:Number
    pre=0
    #Min:Number
    Min=10000
    if a==0:
        return 1
    else:
        #k:Number
        for k in D:
           if  abs(a-k)<Min:
               Min=abs(a-k)	    
               pre=k
        return a*D[pre]/pre

 
def eveil(e):
    """int->int"""
    if e>=17 and e<21:
        return alcool(0.5)
    elif e>=21:
        return alcool(0.8)
    return 1

def moment(m):
    """Number->Number"""
    if (2<=m and m<=5) or (13<=m and m<=16): 
        return 5.6
    return 1

def Week_End(WE):
    """bool->Number"""
    if WE==True:
        return 2.7
    return 1
    
    
def jour(j):
    """str->int"""
    if j=='Lundi' or j=='lundi':
        return 1
    elif j=='Mardi' or j=='mardi':
        return 2
    elif j=='Mercredi' or j=='mercredi':
        return 3
    elif j=='Jeudi' or j=='jeudi':
        return 4
    elif j=='Vendredi' or j=='vendredi':
        return 5
    elif j=='Samedi' or j=='samedi':
        return 6
    elif j=="Dimanche" or j=="dimanche":
        return 7
        
        
#BROUILLON à àméliorer, diviser
def voie1(a,m,WE,sexe,j):                                            
    “””Number*int*bool*str*int->
    hyp: 0<m<=24, sexe=”femme” ou sexe=”homme”   “”””
    #coeff:Number
    coeff=1
    #coeffalcool:Number
    coeffalcool=1
    #h:Number
    h=m
    #h1:Number   
    h1=0
    #r:int
    r=1
    while 
        if tour>1:   #apres premiere h de conduite 
             if alcool(a)>=1 and sexe==”homme”:  #genre du conducteur
                   a=a - 0,125
             elif alcool(a)>= 1:
                   a= a - 0.0925  
             coeffalcool=alcool(a) 

            if jour(j)==5 and h==24:   #WE ou non
                   WE= True
            elif jour(j)==7 and h==24:
                   WE= False
            coeffWE=Week_End(WE)
            
            if (h-h1)%2==0:   #aire de repos obligatoire 20min
                   h=h+(⅓)
                   h1=(⅓)*r
                   r=r+1
      tour=tour+1
      coeff=coeff*Week_End(WE)*moment(h)     
      h=h+1
    return  tour  
      
      

