"""2.uzdevums.<br>
Lietotājs ievada kvadrāta malas garumu centimetros (>5cm). <br>
Sastādīt programmas kodu, kas aprēķina, par cik procentiem mainīsies kvadrāta laukums, ja tā malas garums tiek mainīts par 5cm.<br> 
Atbildi izvadīt veselos procentos."""

x=float(input("Ievadi kvadrāta malu(>5cm): "))
y=x+5
s=x*2
s1=y*2
procenti=(s1-s)/s*100
print(procenti,"%")