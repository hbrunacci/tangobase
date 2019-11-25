from django.db import models
from datetime import datetime,timezone
# Create your models here.

# Basicas
si = 'SI'
no = 'NO'
otra = 'OTRA'
otro = 'OTRO'
desconocido = 'DESCONOCIDO'
leve = 'LEVE'
moderado = 'MODERADO'
severo = 'SEVERO'
asintomatico = 'ASINTOMATICO'
no_corresponde = 'N/A'
cero = 'o'
uno = '1'
dos = '2'
tres = '3'
cuatro = '4'
cinco = '5'

mas_cinco = '>5'

mm = 'MM'
cm2 = 'CM2'
mlm2 = 'ML/M2'

ai_unidades = ((mm, 'MM'),
               (cm2, 'CM2'),
               (mlm2, 'ML/M2'),
               )

si_no = ((si,'Si'),
         (no,'No'),
         )

#Genero
masc = 'MASCULINO'
fem = 'FEMENINO'

masc_fem = ((masc,'Masculino'),
            (fem,'Femenino'),
            )


#etnia
hisp= 'HISP_LATINO'
neg = 'NEGRO'
asi = 'ASIATICO'

etnias = ((hisp,'Hisp_Latino'),
         (neg,'Negro'),
         (asi,'Asiatico'),
         (otra,'Otra')
         )

#Fumador
ex_mas_uno = 'EX+1AÑO'
ex_menos_uno = 'EX-1AÑO'

si_no_ex = ((si,'Si'),
           (no,'No'),
           (ex_mas_uno,'Ex+1año'),
           (ex_menos_uno, 'Ex-1año'),
           )

#Diabetes
dieta = 'SI-DIETA'
medicacion = 'SI-MEDICACION'
insulina = 'SI-INSULINA'

diab_si_no = ((no,'No'),
              (dieta,'Si con dieta'),
              (medicacion,'Si con medicacion'),
              (insulina,'Si con insulina')
              )
#Ritmo
rs = 'RS'
fap = 'FA PAROX'
fac = 'FA CONT_PERSIS'
mcp = 'MCP'

ritmo = ((rs,'RS'),
         (fap, 'FA parox'),
         (fac, 'FA cont/pers'),
         (mcp, 'MCP'),
         (otra, 'Otro')
         )

#Hemostasia
acenoc = 'Si_Acenoc_Warf'
hsodica ='Si_Heparina_Sodica'
hbpeso ='Si_Heparina_bajo_peso'
tirofiban = 'Si_IIB/IIIA_Tirofiban'

hemos = ((no,'No'),
              (acenoc, 'Si_Acenoc_Warf'),
              (hsodica,'Si_Heparina_Sodica'),
              (hbpeso,'Si_Heparina_bajo_peso'),
              (tirofiban,'Si_IIB/IIIA_Tirofiban')
              )


#iam_previo
menor_seis_horas = '< 0,25'
dias_menos_uno = '< 1'
dias_mas_uno = '1..7 '
dias_mas_ocho = '8..21'
dias_mas_veintiuno ='>22'
dias_mas_noventa= '>90'

iam_previo = ((no,'No'),
              (menor_seis_horas , '< 0,25'),
              (dias_menos_uno , '< 1 Dia'),
              (dias_mas_uno , 'de 1 a 7 Dias'),
              (dias_mas_ocho, 'de 8 a 21 Dias'),
              (dias_mas_veintiuno ,'Mas de 22 dias'),
              (dias_mas_noventa, 'Mas de 90 dias')
              )

#Cirugia Cardiaca Previa:
crm = 'CRM'
valvular = 'VALVULAR'
combinado= 'COMBINADO'

cirugia_card_previa = ((no,'No'),
                       (crm,'Si CRM previo'),
                       (valvular,'Si valvular previo'),
                       (combinado,'Si combinado previo'),
                       (otra,'Si Otra')
                       )


#Ant. Cerebro Vascular:
tia = 'TIA'
acv = 'ACV'
carotida_mas50 = 'CAROTIDA > 50'

ant_ceb_vascular = ((no,'No'),
                    (tia,'T.I.A.'),
                    (acv,'A.C.V.'),
                    (carotida_mas50,'Carotida > 50 %')
                    )


#Patologia Renal Previa:
dialisis = 'DIALISIS'


p_renal_previa = ((no,'No  cc > 85 ml/min'),
                  (moderado, 'Si Moderada cc > 50 < 80 ml/min'),
                  (severo, 'Si Severo < 50 ml/min'),
                  (dialisis, 'Si dialisis')
                  )

#EPOC:
# No, Leve, Moderado, Severo, Otra, Desconocido

epoc = ((no,'No'),
        (leve,'Leve'),
        (moderado,'Moderado'),
        (severo,'Severo'),
        (otra,'Otra'),
        (desconocido,'Desconocido'))

#Vasculopatia Periferica:

clau_itte = 'Clau. Itte'
amputacion ='Amputacion'
byoass  = 'Bypass/ATP'
tb_menos_09 = 'Indice T/B <0.9 o equivalente'

vascu_periferica = ((no,'No'),
                    (clau_itte,'Clau. Itte'),
                    (amputacion,'Amputacion'),
                    (byoass, 'Bypass/ATP'),
                    (tb_menos_09, 'Indice T/B <0.9 o equivalente')
                    )

#Sintomas Ingreso:
angor = 'Angor'
disnea = 'Disnea'
sincope = 'Sincope'
ic = 'IC <2 sem'
shock = 'Shock'
fiebre = 'Fiebre'
# Otro

sintomas_ingreso = (
    (asintomatico, 'Asintomatico'),
    (angor, 'Angor' ),
    (disnea, 'Disnea' ),
    (sincope, 'Sincope'),
    (ic,'IC <2 sem' ),
    (shock, 'Shock' ),
    (fiebre, 'Fiebre' ),
    (otro,'Otro'),
    )

#Clase Funcional:
#  0, I, II, III, IV, I/II a III/IV
media = '1-2 a 3-4'

clase_funcional = (
    (cero, '0'),
    (uno, '1'),
    (dos, '2'),
    (tres, '3'),
    (cuatro, '4'),
    (media, '1-2 a 3-4'),
)

#Sintomas Cirugia:
ace ='ACE'
ai = 'AI'
ae ='Angina Equivalente'
sca_sin_elevacion = 'SCA-sin elevación ST'
sca_con_elevacion = 'SCA-con elevación ST'
# otro =Otro,
# asintomatico.

sintomas_cirugia = ((ace, 'ACE'),
                    (ai, 'AI'),
                    (ae, 'Angina Equivalente'),
                    (sca_sin_elevacion, 'SCA-sin elevación ST'),
                    (sca_con_elevacion, 'SCA-con elevación ST'),
                    (otro,'Otro'),
                    (asintomatico, 'Asintomatico')
                   )

#Incidencia Cirugia:
Cirugia_1 = 'Primer Cirugia'
Cirugia_2 = 'Reoperacion'
Cirugia_3 = '2da Reoperacion'
Cirugia_4 = '3ra Reoperacion'
Cirugia_5 = '4ta Reoperacion'

incidencias = (
    (Cirugia_1, 'Primer Cirugia'),
    (Cirugia_2, 'Reoperacion'),
    (Cirugia_3,'2da Reoperacion'),
    (Cirugia_4, '3ra Reoperacion'),
    (Cirugia_5, '4ta Reoperacion'))

#Estado Critico Preoperatorio(Tiene que poder seleccionarse mas de una cosa):
#  No,
#  RCP<1h,
# RCP<24h,
# Shock cardiogenico (al momento de la cx),
# shock cardiogenico (ahora no, pero <24h),
# IABP (BCIAO) – Colocado PreOp, IABP (BCIAO) –
# Colocado IntraOp,
#  IABP (BCIAO) –
# Colocado PosOp,
# Inotropicos,
# ARM PreOp,
# Oligoanuria (<10ml/h)

#Peso_Cirugia
#CRM
#1 NO CRM
#2 Cirugias
#Otra menor

no_crm = '1_NO_CRM'
dos_cirugias = '2_CIRUGIA'
otra_menor= 'OTRA MENOR'


peso_cirugia = ((crm,'CRM'),
                (no_crm,'1-No CRM'),
                (dos_cirugias,'2-Cirugias'),
                (otra_menor,'Otra Menor'))

#
#Abordaje:

e_mediana = 'Esternotomia mediana'
e_mini_anterior = 'Mini Esternotomia Anterior'
taracotomia = 'Mini Toracotomia'
subxifoideo = 'Subxifoideo'

abordaje = ((e_mediana,'Esternotomia mediana'),
            (e_mini_anterior, 'Mini Esternotomia Anterior'),
            (taracotomia, 'Mini Toracotomia'),
            (subxifoideo, 'Subxifoideo'))

#
#
#endocarditis:
si_tratada = 'SI TRATADA SIN ATB'
si_activa = 'SI ACTIVA INTRA ATB'

endocarditis = ((no,'No'),
                (si_tratada,'Si tratada (ahora sin ATB)'),
                (si_activa,'SI activa (Intra ATB)'))
#
# Canulacion:

sin_cec = 'Sin CEC'
art_cava_ad = 'Art AO/Ven Cava única(AD)'
art_cava_fem = 'Art AO/Ven Cava única(FEM)'
art_bicava = 'Art AO/VenBiCava'
art_axilar_ad = 'Art Axilar/ Ven Cava única(AD)'
art_axilar_fem = 'Art Axilar/Ven Fem'
art_fem_ven = 'Art Fem/Ven Fem'

canulacion = ((sin_cec, 'Sin CEC'),
              (art_cava_ad, 'Art AO/Ven Cava única(AD)'),
              (art_cava_fem, 'Art AO/Ven Cava única(FEM)'),
              (art_bicava, 'Art AO/VenBiCava'),
              (art_axilar_ad, 'Art Axilar/ Ven Cava única(AD)'),
              (art_axilar_fem, 'Art Axilar/Ven Fem'),
              (art_fem_ven, 'Art Fem/Ven Fem'),
              (otra, 'Otra')
              )

#
#
# Perfusion:
    # Sin CEC,

cardio_sanguinea = 'Cardioplejia sanguínea (Buckberg)'
hiportemia_mod = 'Hipotermia moderada'
hipotermia_pro = 'Hipotermia profunda'
hemofiltracion = 'Hemofiltracion'
cell_saver = 'Cell Saver'

perfusion_op = ((sin_cec, 'Sin CEC'),
             (cardio_sanguinea, 'Cardioplejia sanguínea (Buckberg)'),
             (hiportemia_mod, 'Hipotermia moderada'),
             (hipotermia_pro, 'Hipotermia profunda'),
             (hemofiltracion, 'Hemofiltracion'),
             (cell_saver, 'Cell Saver'),
             )

#
# Cardioplejia (Tipo y via de administración):
rivero_l51 = 'Rivero L51/52'
celsior = 'Celsior'
rivero = 'Rivero L62 Mini'
del_nido = 'Del Nido'
htk = 'HTK'
wisconsin = 'Wisconsin'
anterograda = 'Anterograda'
retrograda = 'Retrograda'
ambas = 'Ambas (Antero+Retrograda)'
reperfusion = 'Reperfusion'
#Otra,

cardioplejia = ((rivero_l51, 'Rivero L51/52'),
                (celsior, 'Celsior'),
                (rivero, 'Rivero L62 Mini'),
                (del_nido, 'Del Nido'),
                (htk, 'HTK'),
                (wisconsin, 'Wisconsin'),
                (anterograda, 'Anterograda'),
                (retrograda, 'Retrograda'),
                (ambas, 'Ambas (Antero+Retrograda)'),
                (reperfusion, 'Reperfusion')
                )


#
# Presentacion:
# 'No Corresponde,
estenosis = 'Estenosis'
insuficiencia ='Insuficiencia'
enferm_estenosis = 'Enfermedad (+Estenosis)'
enferm_insuficiencia = 'Enfermedad (+Insuficiencia)'
# 'Otra'

presentacion = ((no_corresponde, 'No Corresponde'),
                (estenosis, 'Estenosis'),
                (insuficiencia, 'Insuficiencia'),
                (enferm_estenosis, 'Enfermedad (+Estenosis)'),
                (enferm_insuficiencia, 'Enfermedad (+Insuficiencia)'),
                (otra, 'Otra'))

#
# VAO Bicuspide:
    # 'No',
si_sin_rafe = 'Si tipo 0 (sin rafe)'
si_intercoronario = 'Si Tipo 1 (1Rafe, intercoronariano)'
si_cd_nc = 'Si tipo 1 (1rafe, CD/NC)'
si_ci_nc = 'Si tipo 1 (1Rafe, CI/NC)'
si_dos_rafes =' Si Tipo 2 (2 Rafes)'
si_otra = 'Si Otra'

vao_bicuspide_op = ((no, 'No'),
                    (si_sin_rafe, 'Si tipo 0 (sin rafe)'),
                    (si_intercoronario, 'Si Tipo 1 (1Rafe, intercoronariano)'),
                    (si_cd_nc, 'Si tipo 1 (1rafe, CD/NC)'),
                    (si_ci_nc, 'Si tipo 1 (1Rafe, CI/NC)'),
                    (si_dos_rafes, 'Si Tipo 2 (2 Rafes)'),
                    (si_otra, 'Si Otra'))
#
# Patologia Mitral:
    # No corresponde,
    # Valva anterior,
    # valva posterior,
    # bivalvar
    #
valva_anterior = 'VALVA ANTERIOR'
valva_posterior = 'VALVA POSTERIOR'
bivalvar = 'BIVALVAR'

patologia_mitral = ((no_corresponde,'No corresponde'),
                    (valva_anterior,'Valva anterior'),
                    (valva_posterior,'Valva posterior'),
                    (bivalvar,'bivalvar')
                    )

# Abordaje mitral:
    # No,
    # Auriculotomia izquierda,
    # transeptal (AD),
    # transaortico,
    # otro.

auriculotomia_izq = 'Auriculotomia izquierda'
transeptal = 'transeptal (AD)'
transaortico = 'transaortico'

abordaje_mitral = ((no,'no'),
                   (auriculotomia_izq,'Auriculotomia izquierda'),
                   (transeptal,'Transeptal (AD)'),
                   (transaortico,'Transaortico'),
                   (otro,'Otro')
                   )

#

# Op.deMaze(FA):
    # No,
    # SI-MAZE IV(bilateral),
    # SI-MAZE IV(izquierdo),
    # SI-Venas pulmonares,
    # Si-MAZE IV(c/Crio),
    # SI-Otra.

si_maze_bi = 'SI-MAZE IV(bilateral)'
si_maze_izq =  'SI-MAZE IV(izquierdo)'
si_venas_pulmonare = 'SI-Venas pulmonares'
si_maze_vrio = 'Si-MAZE IV(c/Crio)'


demaze = ((no,'No'),
          (si_maze_bi, 'SI-MAZE IV(bilateral)'),
          (si_maze_izq, 'SI-MAZE IV(izquierdo)'),
          (si_venas_pulmonare, 'SI-Venas pulmonares'),
          (si_maze_vrio, 'Si-MAZE IV(c/Crio)'),
          (si_otra, 'Si-Otra'))





#
# Valv.Biolog. o Mec:
# no corresponde ='No corresponde'
biologica ='Biologica'
mecanica ='Mecanica'
plastica ='Plastica'
tumor ='Tumor'
bio_plastica ='Bio/Plastica'
mec_plastica ='Mec/Plastica'
bio_bio ='Bio/Bio'
mec_mec ='Mec/Mec'
otra='Otra (describir)'

valv_biolog = ((no_corresponde,'No Corresponde'),
               (biologica ,'Biologica'),
               (mecanica ,'Mecanica'),
               (plastica ,'Plastica'),
               (tumor ,'Tumor'),
               (bio_plastica ,'Bio/Plastica'),
               (mec_plastica ,'Mec/Plastica'),
               (bio_bio ,'Bio/Bio'),
               (mec_mec ,'Mec/Mec'),
               (otra,'Otra (describir)'),
               )

# Plastica/reemplazo/conversión/tumor

conversion = 'Conversion'
reemplazo = 'Reemplazo'
tumor = 'Tumor'

campo_60 = ((plastica,'Plastica'),
            (conversion,'Conversion'),
            (reemplazo,'Reemplazo'),
            (tumor,'Tumor')
            )
#

# Nro de puentes:
    # 0,
    # 1,
    # 2,
    # 3,
    # 4,
    # >5

puentes = ((cero,'0'),
           (uno,'1'),
           (dos,'2'),
           (tres,'3'),
           (cuatro,'4'),
           (mas_cinco,'5 o mas'))

#
# Nro de vasos:
    # 0,
    # 1,
    # 2,
    # 3
    #
nro_vasos = ((cero, '0'),
           (uno, '1'),
           (dos, '2'),
           (tres, '3'))

# Conductos:
    # No corresponde,
sita_1_mas_menos_vena ='SITA(1mamaria +/- vena)'
bita_2_mamarias ='BITA(2mamarias)'
svg_todo_vena ='SVG(todo vena)'
bita_svg_2_mam_vena ='BITA+SVG (2mam+vena)'
mamaria_radial ='mamaria+radial'
mamaria_radial_vena ='mamaria+radial+vena'
radial ='radial'

conductos = ((no_corresponde, 'No corresponde'),
             (sita_1_mas_menos_vena, 'SITA(1mamaria +/- vena)'),
             (bita_2_mamarias, 'BITA(2mamarias)'),
             (svg_todo_vena, 'SVG(todo vena)'),
             (bita_svg_2_mam_vena, 'BITA+SVG (2mam+vena)'),
             (mamaria_radial, 'mamaria+radial' ),
             (mamaria_radial_vena, 'mamaria+radial+vena'),
             (radial, 'radial'),)


    #
#
# Hemoderivados IntraOp:
    # No,
rojos = 'Rojos'
plasma = 'Plasma'
crioprecipitados = 'Crioprecipitados'
plaquetas = 'Plaquetas'
sinteticos_fibrinogeno = 'Sinteticos-Fibrinogeno(Haemocompletan®)'
sinteticos_plasmaticos  = 'Sinteticos-Plasmaticos (Beriplex®)'
sinteticos_factorvii = 'Sinteticos-FactorVII(novoseven®)'


hemoderivados = ((no, 'No'),
                 (rojos, 'Rojos'),
                 (plasma, 'Plasma'),
                 (crioprecipitados , 'Crioprecipitados'),
                 (plaquetas, 'Plaquetas'),
                 (sinteticos_fibrinogeno, 'Sinteticos-Fibrinogeno(Haemocompletan®)'),
                 (sinteticos_plasmaticos, 'Sinteticos-Plasmaticos (Beriplex®)'),
                 (sinteticos_factorvii, 'Sinteticos-FactorVII(novoseven®)'),
                 )



# POSOP
#
# Arritmia:


fa_menos_48h = 'FA <48h '
fa_mas_48h = 'FA >48h '
tv_FV = 'TV/FV '
bav_menos_7dias = 'BAV <7dias '
mcp_definitivo = 'MCP definitivo '

arritmia = ((no,'No'),
            (fa_menos_48h, 'FA <48h '),
            (fa_mas_48h, 'FA >48h '),
            (tv_FV, 'TV/FV '),
            (bav_menos_7dias, 'BAV < 7dias '),
            (mcp_definitivo, 'MCP definitivo ' ),
            (otra,'Otra'))



# Reoperacion internado:
    # No,

sangrado = 'Sangrado/Taponamiento'
isquemia = 'Isquemia/IAM'
inestabi_esternal = 'Inestabilidad esternal'
mediastinitis = 'Mediastinitis'
disfuncion_protesica_hemolisis = 'Disfuncion protésica/hemolisis'

reoperacion_internado = ((no , 'No'),
                         (sangrado , 'Sangrado/Taponamiento'),
                         (isquemia , 'Isquemia/IAM'),
                         (inestabi_esternal , 'Inestabilidad esternal'),
                         (mediastinitis , 'Mediastinitis'),
                         (disfuncion_protesica_hemolisis , 'Disfuncion protésica/hemolisis'),)





#
# Renales:
    #   No,
    #   IRA,
    #   Dialisis
#
ira = 'IRA'
dialisis = 'Dialisis'

renales = ((no,'No'),
           (ira,'IRA'),
           (dialisis,'Dialisis'))



# Infectologicas:

herida_superficial = 'Herida superficial '
mediastinitis = 'mediastinitis '
safenectomia = 'Safenectomia '
neumonia = 'Neumonia '
asociada_cateter = 'Asociada a catéter '
itu = 'ITU '

infectologia = ((no, 'No '),
                (herida_superficial, 'Herida superficial '),
                (mediastinitis, 'mediastinitis '),
                (safenectomia, 'Safenectomia '),
                (neumonia, 'Neumonia '),
                (asociada_cateter, 'Asociada a catéter '),
                (itu , 'ITU '),)



#
# Neurologicas:

#No = 'No'
tia = 'TIA'
acv_sin_secuela = 'ACV sin secuela'
acv_con_secuela = 'ACV con secuela'
convulsion = 'convulsión'
sme_confusional = 'Sme. Confusional'


neurologicas = ((no, 'No'),
                (tia, 'TIA'),
                (acv_sin_secuela, 'ACV sin secuela '),
                (acv_con_secuela, 'ACV con secuela '),
                (convulsion, 'convulsión '),
                (sme_confusional, 'Sme. Confusional '))

# Isquemia/IAM:
    # NO,
    # si,
    # si(ATC),
    # si(CRM).

si_atc = 'Si ATC'
si_crm = 'Si CRM'

isquemia = ((no, 'No'),
            (si, 'Si'),
            (si_atc, 'Si ATC'),
            (si_crm, 'Si CRM'))

# Sme.Bajo Gasto:
#no = 'No'
si_inotropicos = 'Si(inotrópicos) '
si_IABP  = 'Si (IABP/BCIAO)'
si_Ventricular = 'Si(Asist.Ventricular) '

sme_bajo_gasto = ((no,'No'),
                  (si_inotropicos , 'Si(inotrópicos) '),
                  (si_IABP  , 'Si (IABP/BCIAO)'),
                  (si_Ventricular , 'Si(Asist.Ventricular)'),
                  )

## Inotropicos:
#No,            ='No,          '
Dopamina      ='Dopamina'
Noradrenalina ='Noradrenalina'
Fenilefrina   ='Fenilefrina'
Vasopresina   ='Vasopresina'
Adrenalina    ='Adrenalina'
Milrinona     ='Milrinona'
Levosimendan  ='Levosimendan'
Dobutamina    ='Dobutamina'

inotropicos = ((no,'No'),
               (Dopamina     ,'Dopamina'),
               (Noradrenalina,'Noradrenalina'),
               (Fenilefrina  ,'Fenilefrina'),
               (Vasopresina  ,'Vasopresina'),
               (Adrenalina   ,'Adrenalina'),
               (Milrinona    ,'Milrinona'),
               (Levosimendan ,'Levosimendan'),
               (Dobutamina   ,'Dobutamina'))




# Respiratorias:
    # No,
si_neumonia = 'Si-Neumonia'
si_traqueostomia = 'Si-traqueostomia'
si_tep = 'Si-TEP'
si_epoc = 'SI-EPOC relacionadas'
si_arm = 'Si-ARM>48h'

respiratorias = ((no,'No'),
                 (si_neumonia, 'Si-Neumonia'),
                 (si_traqueostomia, 'Si-traqueostomia'),
                 (si_tep, 'Si-TEP'),
                 (si_epoc, 'SI-EPOC relacionadas'),
                 (si_arm, 'Si-ARM>48h'),)



# Hiperglucemia:
    # No,
    # Si(correcciones),
    # No(BIC)

si_correciones = 'Si (Correcciones)'
no_bic = 'No (BIC)'

hiperglucemia = ((no, 'No'),
                 (no_bic, 'No (BIC)'),
                 (si_correciones, 'Si (Correcciones)')
                 )

#
# Alta/Obito:
    # Domicilio,
    # Tercer Nivel,
    # Obito.

domicilio = 'Domicilio'
tercer_nivel= 'Tercer Nivel'
obito = 'Obito'

alta = ((domicilio,'Domicilio'),
        (tercer_nivel,'Tercer Nivel'),
        (obito,'Obito')
        )
#
## Estudios Complementarios PreOp
#
#  VI Diametros: 0/0
# 	Se pueden llamar “VI_D” y “VI_S” (numero de 3 digitos sin decimales)
#
# Septum IV/ Pared posterior: 0/0
# 	Se pueden llamar “Septum” y “PPost” (numero de 3 digitos sin decimales)


# Transfusiones(Tiene que poder seleccionarse mas de una cosa):
    # No,
    # Politransfusion,
    # Rojos,
    # Plasma,
    # Crioprecipitados,
    # Plaquetas,
    # Sinteticos-Fibrinogeno (Haemocompletan®),
    # Sinteticos-Plasmaticos(Beriplex®),
    # Sinteticos-FactorVII(Novoseven®).
    #

conservada= 'Conservada'
leve = 'Leve'
moderada = 'Moderada'
severa = 'Severa'
muy_severo = 'Muy Severo'

fsv_op = ((conservada , 'Conservada > 50 %'),
           (leve , 'Leve'      ),
           (moderada , 'Moderada 30-50 %'  ),
           (severa , 'Severa 21-30 %'    ),
           (muy_severo , 'Muy Severo <= 20 %'),
           )

si_31_55 = 'Si_PAP_31-55_mmHg'
si_mas_55 = 'Si_PAP_>_55_mmHg'

htp = ((no,'No'),
       (si_31_55, 'Si (PAP 31-55 mmHg)'),
       (si_mas_55, 'Si (PAP > 55 mmHg)'),
       )

pat_tric_op = ((no,'No'),
               (leve, 'Leve'),
               (moderada, 'Moderada'),
               (severa, 'Severa'),
               )

si_estenosis_aor = 'Estenosis Aortica'
si_estenosis_mitral = 'Estenosis Mitral'
si_insuf_trivial = 'Trivial'
si_insuf_leve ='Leve'
si_insuf_moderada ='Moderada'
si_insuf_severa ='Severa'

pat_val_aortica = ((no, 'No'),
                   (si_estenosis_aor, 'Si - Estenosis Aortica'),
                   (si_insuf_trivial, 'Si - Insuficiencia Trivial'),
                   (si_insuf_leve, 'Si - Insuficiencia Leve'),
                   (si_insuf_moderada, 'Si - Insuficiencia Moderada'),
                   (si_insuf_severa, 'Si - Insuficiencia Severa'),
                   )

pat_mitral_op =  ((no, 'No'),
                  (si_estenosis_mitral, 'Si - Estenosis mitral'),
                  (si_insuf_trivial, 'Si - Insuficiencia Trivial'),
                  (si_insuf_leve, 'Si - Insuficiencia Leve'),
                  (si_insuf_moderada, 'Si - Insuficiencia Moderada'),
                  (si_insuf_severa, 'Si - Insuficiencia Severa'),
                  )


si_acenocumarol = 'Si-Acenocumarol (Sintrom)'
si_warfarina = 'SI-Warfarina (Coumadin)'

anticuagulado_op = ((no, 'No'),
                    (si_acenocumarol, 'Si-Acenocumarol (Sintrom)'),
                    (si_warfarina, 'SI-Warfarina (Coumadin)')
                    )


class Transfusiones(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Transfusion'
        verbose_name_plural = 'Transfusiones'

class ECP(models.Model):
    descripcion = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Estado Critico Preoperatorio'
        verbose_name_plural = 'Estados Critico Preoperatorio'

#Medicacion habitual (Tiene que poder seleccionarse mas de una cosa):
# AAS,
# Clopidogrel (u otro),
# Estatinas,
# IECA(-pril),
# ARA (-artan),
# B-Bloqueantes (-lol),
# Antagonistas cálcicos (-pina),
# Otros hipolipimiantes,
# Metformina (u otro hipoglucemiante),
# Amiodarona/Ivabradina/Digoxina,
# Otro anti-arritmico, diuréticos,
# acenocumarol/warfarina,
# levotiroxina.


class Medicacion_Habitual(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Medicacion Habitual'
        verbose_name_plural = 'Medicamentos Habituales'


class Clinica(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Clinica'
        verbose_name_plural = 'Clinicas'


class Procedimiento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'


class Opciones_viabilidad(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Opcion_de viabilidad'
        verbose_name_plural = 'Opciones de viabilidad'


class Opciones_metodo(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Metodo'
        verbose_name_plural = 'Metodos'


class Resultados_seguimiento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Resultado de Seguimiento'
        verbose_name_plural = 'Resultados de Seguimientos'



class Estudio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'




class BaseTable(models.Model):

    id = models.AutoField(editable=False, primary_key=True)
    created_date = models.DateTimeField(editable=False,
        default=datetime.now())
    update_date = models.DateTimeField(editable=False,
        default=datetime.now())
    export_date = models.DateTimeField(editable=False,
        blank=True, null=True)

    class Meta:
        abstract = True

class Paciente(BaseTable):

    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(choices=masc_fem, max_length=15)
    altura = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

class Cirujanos(BaseTable):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Cirujano'
        verbose_name_plural = 'Cirujanos'


class Ayudantes(BaseTable):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Ayudante'
        verbose_name_plural = 'Ayudantes'


class Cirugia(BaseTable):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    prioridad = models.CharField(max_length=50)
    incidencia = models.CharField(max_length=35, verbose_name='Incidencia Cirugia', choices=incidencias,
                                  default='Primera')
    procedimientos = models.ManyToManyField(Procedimiento)
    tipo_cirugia = models.CharField(max_length=100)
    peso_cirugia = models.CharField(max_length=35, choices=peso_cirugia, default=crm)
    abordaje = models.CharField(max_length=35, choices=abordaje)
    descripcion = models.CharField(max_length=150)
    cirujano = models.OneToOneField(Cirujanos, on_delete=models.CASCADE)
    ayudante = models.OneToOneField(Ayudantes, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cirugia'
        verbose_name_plural = 'Cirugias'


class Antecedentes(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='antecedentes')
    peso = models.FloatField()
    etnia = models.CharField(max_length=15, choices=etnias, default=hisp)
    dislipemia = models.CharField(max_length=15, choices=si_no,default=no)
    tabaco = models.CharField(max_length=15, choices=si_no_ex,default=no)
    diabetes = models.CharField(max_length=15, choices=diab_si_no,default=no)
    hipertension = models.CharField(max_length=15, choices=si_no,default=no)
    antecedentes_heredo_familiares = models.CharField(max_length=15, choices=si_no,default=no)
    ritmo = models.CharField (max_length=15, choices=ritmo,default=rs)
    hemostasia = models.CharField(max_length=25, choices=hemos,default=no)
    iam = models.CharField(max_length=25, choices=iam_previo,default=no)
    cirugia_cardiaca_previa = models.CharField(max_length=25, choices=cirugia_card_previa,default=no)
    antecedentes_cerebro_vascular = models.CharField(max_length=25, choices=ant_ceb_vascular, default=no)
    patologia_renal_previa = models.CharField(max_length=35, choices=p_renal_previa,default=no)
    ultima_creatinina = models.CharField(max_length=10)
    epoc = models.CharField(max_length=35, choices=epoc,default=no)
    vasculopatia_preiferica = models.CharField(max_length=35, choices=vascu_periferica,default=no)
    inmunocomprometido = models.CharField(max_length=2, choices=si_no,default=no)
    movilidad_reducida = models.CharField(max_length=2, choices=si_no,default=no)
    sintomas_ingreso = models.CharField(max_length=35, choices=sintomas_ingreso, default=otro)
    clase_funcional = models.CharField(max_length=35, choices=clase_funcional,default=cero)
    sintomas_cirugia = models.CharField(max_length=35, choices=sintomas_cirugia,default=asintomatico)
    estado_critico = models.ManyToManyField(ECP)
    medicacion_habitual = models.ManyToManyField(Medicacion_Habitual)
    Comentarios = models.CharField(max_length=300,default='Sin Comentarios')

    class Meta:
        verbose_name = 'Antecedentes'
        verbose_name_plural = 'Antecedentes'


class Datos_En_Cirugia(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='datos_en_cirugia')
    sts = models.FloatField(max_length=4)
    euroII = models.FloatField(max_length=4)
    syntax = models.FloatField(max_length=4)
    endocarditis = models.IntegerField()
    tiempo_cec = models.IntegerField(verbose_name='Tiempo CEC (min)')
    tiempo_clampeo = models.IntegerField(verbose_name='Tiempo Clampeo (min)')
    paro_circulatorio = models.IntegerField(verbose_name='Tiempo CEC (min)')
    canula = models.CharField(max_length=35, choices=canulacion)
    perfusion = models.CharField(max_length=35, choices=perfusion_op)
    aorta_calcificada = models.CharField(max_length=2, choices=si_no)
    cardioplejia = models.CharField(max_length=35, choices=cardioplejia)
    presentacion = models.CharField(max_length=35, choices=presentacion)
    mecanismo = models.CharField(max_length=100)
    vao_bicuspide = models.CharField(max_length=35, choices=vao_bicuspide_op)
    patologia_mitral = models.CharField(max_length=35, choices=patologia_mitral)
    abordaje_mitral = models.CharField(max_length=35, choices=abordaje_mitral)
    maze = models.CharField(max_length=35, choices=demaze)
    tipo_valvula = models.CharField(max_length=35, choices=valv_biolog)
    db_campo_60 = models.CharField(max_length=35, choices=campo_60)
    numero_valvula = models.IntegerField()
    marca_protesis = models.CharField(max_length=50)
    modelo_protesis = models.CharField(max_length=50)
    numero_puentes = models.CharField(max_length=5, choices=puentes)
    numero_vasos = models.CharField(max_length=5, choices=nro_vasos)
    tronco_izquierda = models.CharField(max_length=50)
    conductos = models.CharField(max_length=50, choices=conductos)
    extubado_enquirofano = models.CharField(choices=si_no, max_length=3)
    hemoderivados_intra = models.CharField(choices=si_no, max_length=3)


class Complicaciones(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE, related_name='complicaciones')
    arritmia = models.CharField(max_length=25, choices=arritmia, default=no)
    sangrado_medico = models.CharField(max_length=3, choices=si_no, default=no)
    transfusiones = models.ForeignKey(Transfusiones, on_delete=models.CASCADE)
    reop_internado = models.CharField(max_length=35, choices=reoperacion_internado, default=no)
    renal = models.CharField(max_length=35, choices=renales, default=no)
    infectologicas = models.CharField(max_length=35, choices=infectologia, default=no)
    neurologicas = models.CharField(max_length=35, choices=neurologicas, default=no)
    isquemia_iam = models.CharField(max_length=35, choices=isquemia, default=no)
    sme_bajo = models.CharField(max_length=35, choices=sme_bajo_gasto, default=no)
    sme_vasoplejico = models.CharField(max_length=35, choices=si_no, default=no)
    inotropicos = models.CharField(max_length=35, choices=inotropicos, default=no)
    respiratorias = models.CharField(max_length=35, choices=respiratorias, default=no)
    hiperglucemia = models.CharField(max_length=35, choices=hiperglucemia, default=no)
    plaquetopenia = models.CharField(max_length=35, choices=si_no, default=no)
    aco_alta = models.CharField(max_length=35, choices=alta, default=no)
    obito_internacion = models.CharField(max_length=3, choices=si_no, default=no)
    otra = models.CharField(max_length=150, default='')


class Ecodoppler(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='ecodoppler')
    diam_diastolico = models.IntegerField(verbose_name='Diametro Diast.')
    diam_sistolico = models.IntegerField(verbose_name='Diametro Sisto,')
    septum_iv = models.IntegerField(verbose_name='Septum IV')
    pared_posterior = models.IntegerField(verbose_name='Pared Posterior')
    auricula_izquierda_unidad = models.CharField(max_length=5, choices=ai_unidades)
    auricula_izquierda_medida = models.IntegerField()
    raiz_aortica = models.IntegerField(verbose_name='Raiz Aortica')
    ao_tx_a = models.IntegerField(verbose_name='AoTx Diam. Anillo')
    ao_tx_is = models.IntegerField(verbose_name='AoTx Diam. Interseno')
    ao_tx_ust = models.IntegerField(verbose_name='AoTx Diam. Union sinu-tubular ')
    ao_tx_t = models.IntegerField(verbose_name='AoTx Diam. Tubular ')
    fey_vi = models.IntegerField(verbose_name='Fey VI')
    fsvi = models.CharField(max_length=25, choices=fsv_op)
    tapse = models.IntegerField(verbose_name='TAPSE (mm)')
    fsvd = models.CharField(max_length=25, choices=fsv_op)
    pato_val_aortica = models.CharField(max_length=25, choices=pat_val_aortica)
    val_aortica_area = models.FloatField(max_length=5)
    val_aortica_grad_max = models.IntegerField()
    val_aortica_grad_med = models.IntegerField()
    val_aortica_vel = models.FloatField(max_length=5)
    pato_val_mitral = models.CharField(max_length=25, verbose_name='Patologia Val. Tricuspide', choices=pat_mitral_op)
    mecanismo_mitral = models.CharField(verbose_name='Mecanismo mitral', max_length=200)
    pato_val_tricuspidea = models.CharField(max_length=25,verbose_name='Patologia Val. Tricuspide', choices=pat_tric_op)
    pulmonar = models.IntegerField(verbose_name='Pulmonar PAP')
    hipertension = models.CharField(choices=htp, max_length=25)
    comentario = models.CharField(verbose_name='Comentario', max_length=100)


class Viablilidad(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='viabilidad')
    isquemia = models.ManyToManyField(Opciones_viabilidad, related_name='Isquemia')
    necrosis = models.ManyToManyField(Opciones_viabilidad, related_name='Necrosis')
    metodo_viabilidad = models.ManyToManyField(Opciones_metodo)


class Laboratorio(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='laboratorio')
    fecha = models.DateTimeField(default=datetime.now())
    hto = models.IntegerField()
    hb = models.DecimalField(max_digits=5, decimal_places=2)
    leucocitos = models.IntegerField()
    plaquetas = models.IntegerField()
    urea = models.IntegerField()
    hba1c = models.DecimalField(max_digits=4, decimal_places=1)
    glucemia = models.IntegerField()
    tp = models.IntegerField()
    kptt = models.IntegerField()
    rin = models.DecimalField(max_digits=4, decimal_places=1)
    otro = models.CharField(max_length=100)


class Alta(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='alta')
    fecha = models.DateTimeField(default=datetime.now())
    hto = models.IntegerField()
    hb = models.DecimalField(max_digits=5, decimal_places=2)
    creatinina = models.DecimalField(max_digits=4, decimal_places=1)
    glucemia = models.IntegerField()
    otro = models.CharField(max_length=100)



class Seguimiento(BaseTable):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE,related_name='seguimiento')
    fecha = models.DateTimeField(default=datetime.now())
    vivo = models.CharField(choices=si_no, max_length=3)
    clase_funcional = models.CharField(choices=clase_funcional, max_length=30)
    reinternacion_cardiaca = models.CharField(choices=si_no, max_length=3)
    reinternacion_fecha = models.DateTimeField(default=datetime.now())
    reinternacion_detalle = models.CharField(max_length=200)
    reintervencion_cardiaca = models.CharField(choices=si_no, max_length=3)
    reintervencion_fecha = models.DateTimeField(default=datetime.now())
    reintervencion_detalle = models.CharField(max_length=200)
    anticoagulado = models.CharField(choices=anticuagulado_op, max_length=3)
    estudios = models.ManyToManyField(Estudio)
    resultados = models.ManyToManyField(Resultados_seguimiento)
    comentario = models.CharField(max_length=250)


