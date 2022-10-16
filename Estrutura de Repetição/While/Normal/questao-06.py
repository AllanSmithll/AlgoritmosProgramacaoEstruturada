alt_chico = 1.50
alt_ze = 1.10
cresc_chico = 0.02
cresc_ze = 0.03
anos = 0

while alt_chico > alt_ze:
    anos = anos + 1
    alt_chico = alt_chico + cresc_chico
    alt_ze = alt_ze + cresc_ze 

print(f'Serão necessários {anos} anos para que Zé seja maior que Chico')