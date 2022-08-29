import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cuentas.tsv", sep="\t")

df = df.groupby('Tipo')['Importe'].sum()

print(df)

incomes = pd.DataFrame(columns=['Tipo', 'Importe'])
bills = pd.DataFrame(columns=['Tipo', 'Importe'])

for ind in df.index:
    if df[ind] > 0:
        incomes = incomes.append({'Tipo':ind,'Importe':df[ind]},ignore_index=True)
    else:
        bills = bills.append({'Tipo':ind,'Importe':-df[ind]},ignore_index=True)

plt.pie(bills.Importe, labels=bills.Tipo)
plt.show() 

plt.pie(incomes.Importe, labels=incomes.Tipo)
plt.show() 
