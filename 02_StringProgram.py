"""
names='AafjeAaidAalilyannaAaliyahAaminaAamiraAaralynAbabuoAbanaAbarneAbbathaAbbeyAbbieAbbyAbcdeAbedabunAbejeAbelinaAbenaAbeniAbequaAbercrombieAbetziAbeyAbeytuAbhaAbhilashaAbiaAbibaAbibolaAbigailAbihailAbileneAbishagAbitalAblaAbraAbriannaAbriellaAbrielleAbriendaAbrilAbrinaAbstinenceAcaciaAcadiaAcanthaAcasiaAccaliaAcelineAcelynnAcevedoAchaiaAchavaAchelleAchsaAcostaAcotasAcsahAdaAdabellaAdahAdairAdaletAdalia'
name1=[]
A=names.count('A')
a=names.count('a')
length=len(names)
print(length)

import string
name='siva'
c=0
strBuildfunction =dir(name)
for s in strBuildfunction:
    c+=1
print(c)
i=0
for m in dir(string):
    print(m)
    i+=1
print(i)

----------------------------
name='siva'
name1='balaji'
print(dir(name))
for n in dir(name):
    if not n.startswith('__'):
        print(n)
---------------------------------"""
names='AafjeAaidAalilyannaAaliyahAaminaAamiraAaralynAbabuoAbanaAbarneAbbathaAbbeyAbbieAbbyAbcdeAbedabunAbejeAbelinaAbenaAbeniAbequaAbercrombieAbetziAbeyAbeytuAbhaAbhilashaAbiaAbibaAbibolaAbigailAbihailAbileneAbishagAbitalAblaAbraAbriannaAbriellaAbrielleAbriendaAbrilAbrinaAbstinenceAcaciaAcadiaAcanthaAcasiaAccaliaAcelineAcelynnAcevedoAchaiaAchavaAchelleAchsaAcostaAcotasAcsahAdaAdabellaAdahAdairAdaletAdalia'

name1=names.split('A')
print(name1)
c=0
for n in name1:

    if not n.strip()=='':
        print('A'+n)
    c+=1
print(c)


