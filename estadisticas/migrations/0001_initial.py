# Generated by Django 2.1.2 on 2019-02-05 15:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 379651))),
                ('hto', models.IntegerField()),
                ('hb', models.DecimalField(decimal_places=2, max_digits=5)),
                ('creatinina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('glucemia', models.IntegerField()),
                ('otro', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('peso', models.FloatField()),
                ('etnia', models.CharField(choices=[('HISP_LATINO', 'Hisp_Latino'), ('NEGRO', 'Negro'), ('ASIATICO', 'Asiatico'), ('OTRA', 'Otra')], default='HISP_LATINO', max_length=15)),
                ('dislipemia', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='No ', max_length=15)),
                ('tabaco', models.CharField(choices=[('SI', 'Si'), ('NO', 'No'), ('EX+1AÑO', 'Ex+1año'), ('EX-1AÑO', 'Ex-1año')], default='No ', max_length=15)),
                ('diabetes', models.CharField(choices=[('NO', 'No'), ('SI-DIETA', 'Si con dieta'), ('SI-MEDICACION', 'Si con medicacion'), ('SI-INSULINA', 'Si con insulina')], default='No ', max_length=15)),
                ('hipertension', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='No ', max_length=15)),
                ('antecedentes_heredo_familiares', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='No ', max_length=15)),
                ('ritmo', models.CharField(choices=[('RS', 'RS'), ('FA PAROX', 'FA parox'), ('FA CONT_PERSIS', 'FA cont/pers'), ('MCP', 'MCP'), ('OTRA', 'Otro')], default='RS', max_length=15)),
                ('hemostasia', models.CharField(choices=[('NO', 'No'), ('Si_Acenoc_Warf', 'Si_Acenoc_Warf'), ('Si_Heparina_Sodica', 'Si_Heparina_Sodica'), ('Si_Heparina_bajo_peso', 'Si_Heparina_bajo_peso'), ('Si_IIB/IIIA_Tirofiban', 'Si_IIB/IIIA_Tirofiban')], default='No ', max_length=25)),
                ('iam', models.CharField(choices=[('NO', 'No'), ('< 0,25', '< 0,25'), ('< 1', '< 1 Dia'), ('1..7 ', 'de 1 a 7 Dias'), ('8..21', 'de 8 a 21 Dias'), ('>22', 'Mas de 22 dias'), ('>90', 'Mas de 90 dias')], default='No ', max_length=25)),
                ('cirugia_cardiaca_previa', models.CharField(choices=[('NO', 'No'), ('CRM', 'Si CRM previo'), ('VALVULAR', 'Si valvular previo'), ('COMBINADO', 'Si combinado previo'), ('OTRA', 'Si Otra')], default='No ', max_length=25)),
                ('antecedentes_cerebro_vascular', models.CharField(choices=[('NO', 'No'), ('TIA', 'T.I.A.'), ('ACV', 'A.C.V.'), ('CAROTIDA > 50', 'Carotida > 50 %')], default='No ', max_length=25)),
                ('patologia_renal_previa', models.CharField(choices=[('NO', 'No  cc > 85 ml/min'), ('MODERADO', 'Si Moderada cc > 50 < 80 ml/min'), ('SEVERO', 'Si Severo < 50 ml/min'), ('DIALISIS', 'Si dialisis')], default='No ', max_length=35)),
                ('ultima_creatinina', models.CharField(max_length=10)),
                ('epoc', models.CharField(choices=[('NO', 'No'), ('LEVE', 'Leve'), ('MODERADO', 'Moderado'), ('SEVERO', 'Severo'), ('OTRA', 'Otra'), ('DESCONOCIDO', 'Desconocido')], default='No ', max_length=35)),
                ('vasculopatia_preiferica', models.CharField(choices=[('NO', 'No'), ('Clau. Itte', 'Clau. Itte'), ('Amputacion', 'Amputacion'), ('Bypass/ATP', 'Bypass/ATP'), ('Indice T/B <0.9 o equivalente', 'Indice T/B <0.9 o equivalente')], default='No ', max_length=35)),
                ('inmunocomprometido', models.BooleanField(choices=[('SI', 'SI'), ('NO', 'NO')], default='No ')),
                ('movilidad_reducida', models.BooleanField(choices=[('SI', 'SI'), ('NO', 'NO')], default='No ')),
                ('sintomas_ingreso', models.CharField(choices=[('ASINTOMATICO', 'Asintomatico'), ('Angor', 'Angor'), ('Disnea', 'Disnea'), ('Sincope', 'Sincope'), ('IC <2 sem', 'IC <2 sem'), ('Shock', 'Shock'), ('Fiebre', 'Fiebre'), ('OTRO', 'Otro')], default='OTRO', max_length=35)),
                ('clase_funcional', models.CharField(choices=[('o', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('1-2 a 3-4', '1-2 a 3-4')], default='o', max_length=35)),
                ('sintomas_cirugia', models.CharField(choices=[('ACE', 'ACE'), ('AI', 'AI'), ('Angina Equivalente', 'Angina Equivalente'), ('SCA-sin elevación ST', 'SCA-sin elevación ST'), ('SCA-con elevación ST', 'SCA-con elevación ST'), ('OTRO', 'Otro'), ('ASINTOMATICO', 'Asintomatico')], default='ASINTOMATICO', max_length=35)),
                ('Comentarios', models.CharField(default='Sin Comentarios', max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ayudantes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')], max_length=15)),
                ('altura', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cirugia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('fecha', models.DateTimeField()),
                ('prioridad', models.CharField(max_length=50)),
                ('incidencia', models.CharField(choices=[('Primer Cirugia', 'Primer Cirugia'), ('Reoperacion', 'Reoperacion'), ('2da Reoperacion', '2da Reoperacion'), ('3ra Reoperacion', '3ra Reoperacion'), ('4ta Reoperacion', '4ta Reoperacion')], default='Primera', max_length=35, verbose_name='Incidencia Cirugia')),
                ('tipo_cirugia', models.CharField(max_length=100)),
                ('peso_cirugia', models.CharField(choices=[('CRM', 'CRM'), ('1_NO_CRM', '1-No CRM'), ('2_CIRUGIA', '2-Cirugias'), ('OTRA MENOR', 'Otra Menor')], default='CRM', max_length=35)),
                ('abordaje', models.CharField(choices=[('Esternotomia mediana', 'Esternotomia mediana'), ('Mini Esternotomia Anterior', 'Mini Esternotomia Anterior'), ('Mini Toracotomia', 'Mini Toracotomia'), ('Subxifoideo', 'Subxifoideo')], max_length=35)),
                ('descripcion', models.CharField(max_length=150)),
                ('sts', models.FloatField(max_length=4)),
                ('euroII', models.FloatField(max_length=4)),
                ('syntax', models.FloatField(max_length=4)),
                ('endocarditis', models.IntegerField()),
                ('tiempo_cec', models.IntegerField(verbose_name='Tiempo CEC (min)')),
                ('tiempo_clampeo', models.IntegerField(verbose_name='Tiempo Clampeo (min)')),
                ('paro_circulatorio', models.IntegerField(verbose_name='Tiempo CEC (min)')),
                ('canula', models.CharField(choices=[('Sin CEC', 'Sin CEC'), ('Art AO/Ven Cava única(AD)', 'Art AO/Ven Cava única(AD)'), ('Art AO/Ven Cava única(FEM)', 'Art AO/Ven Cava única(FEM)'), ('Art AO/VenBiCava', 'Art AO/VenBiCava'), ('Art Axilar/ Ven Cava única(AD)', 'Art Axilar/ Ven Cava única(AD)'), ('Art Axilar/Ven Fem', 'Art Axilar/Ven Fem'), ('Art Fem/Ven Fem', 'Art Fem/Ven Fem'), ('OTRA', 'Otra')], max_length=35)),
                ('perfusion', models.CharField(choices=[('Sin CEC', 'Sin CEC'), ('Cardioplejia sanguínea (Buckberg)', 'Cardioplejia sanguínea (Buckberg)'), ('Hipotermia moderada', 'Hipotermia moderada'), ('Hipotermia profunda', 'Hipotermia profunda'), ('Hemofiltracion', 'Hemofiltracion'), ('Cell Saver', 'Cell Saver')], max_length=35)),
                ('aorta_calcificada', models.BooleanField(choices=[('SI', 'SI'), ('NO', 'NO')])),
                ('cardioplejia', models.CharField(choices=[('Rivero L51/52', 'Rivero L51/52'), ('Celsior', 'Celsior'), ('Rivero L62 Mini', 'Rivero L62 Mini'), ('Del Nido', 'Del Nido'), ('HTK', 'HTK'), ('Wisconsin', 'Wisconsin'), ('Anterograda', 'Anterograda'), ('Retrograda', 'Retrograda'), ('Ambas (Antero+Retrograda)', 'Ambas (Antero+Retrograda)'), ('Reperfusion', 'Reperfusion')], max_length=35)),
                ('presentacion', models.CharField(choices=[('N/A', 'No Corresponde'), ('Estenosis', 'Estenosis'), ('Insuficiencia', 'Insuficiencia'), ('Enfermedad (+Estenosis)', 'Enfermedad (+Estenosis)'), ('Enfermedad (+Insuficiencia)', 'Enfermedad (+Insuficiencia)'), ('OTRA', 'Otra')], max_length=35)),
                ('mecanismo', models.CharField(max_length=100)),
                ('vao_bicuspide', models.CharField(choices=[('NO', 'No'), ('Si tipo 0 (sin rafe)', 'Si tipo 0 (sin rafe)'), ('Si Tipo 1 (1Rafe, intercoronariano)', 'Si Tipo 1 (1Rafe, intercoronariano)'), ('Si tipo 1 (1rafe, CD/NC)', 'Si tipo 1 (1rafe, CD/NC)'), ('Si tipo 1 (1Rafe, CI/NC)', 'Si tipo 1 (1Rafe, CI/NC)'), (' Si Tipo 2 (2 Rafes)', 'Si Tipo 2 (2 Rafes)'), ('Si Otra', 'Si Otra')], max_length=35)),
                ('patologia_mitral', models.CharField(choices=[('N/A', 'No corresponde'), ('VALVA ANTERIOR', 'Valva anterior'), ('VALVA POSTERIOR', 'Valva posterior'), ('BIVALVAR', 'bivalvar')], max_length=35)),
                ('abordaje_mitral', models.CharField(choices=[('NO', 'no'), ('Auriculotomia izquierda', 'Auriculotomia izquierda'), ('transeptal (AD)', 'Transeptal (AD)'), ('transaortico', 'Transaortico'), ('OTRO', 'Otro')], max_length=35)),
                ('maze', models.CharField(choices=[('NO', 'No'), ('SI-MAZE IV(bilateral)', 'SI-MAZE IV(bilateral)'), ('SI-MAZE IV(izquierdo)', 'SI-MAZE IV(izquierdo)'), ('SI-Venas pulmonares', 'SI-Venas pulmonares'), ('Si-MAZE IV(c/Crio)', 'Si-MAZE IV(c/Crio)'), ('Si Otra', 'Si-Otra')], max_length=35)),
                ('tipo_valvula', models.CharField(choices=[('N/A', 'No Corresponde'), ('Biologica', 'Biologica'), ('Mecanica', 'Mecanica'), ('Plastica', 'Plastica'), ('Tumor', 'Tumor'), ('Bio/Plastica', 'Bio/Plastica'), ('Mec/Plastica', 'Mec/Plastica'), ('Bio/Bio', 'Bio/Bio'), ('Mec/Mec', 'Mec/Mec'), ('Otra (describir)', 'Otra (describir)')], max_length=35)),
                ('db_campo_60', models.CharField(choices=[('Plastica', 'Plastica'), ('Conversion', 'Conversion'), ('Reemplazo', 'Reemplazo'), ('Tumor', 'Tumor')], max_length=35)),
                ('numero_valvula', models.IntegerField()),
                ('marca_protesis', models.CharField(max_length=50)),
                ('modelo_protesis', models.CharField(max_length=50)),
                ('numero_puentes', models.CharField(choices=[('o', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('>5', '5 o mas')], max_length=5)),
                ('numero_vasos', models.CharField(choices=[('o', '0'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=5)),
                ('tronco_izquierda', models.CharField(max_length=50)),
                ('conductos', models.CharField(choices=[('N/A', 'No corresponde'), ('SITA(1mamaria +/- vena)', 'SITA(1mamaria +/- vena)'), ('BITA(2mamarias)', 'BITA(2mamarias)'), ('SVG(todo vena)', 'SVG(todo vena)'), ('BITA+SVG (2mam+vena)', 'BITA+SVG (2mam+vena)'), ('mamaria+radial', 'mamaria+radial'), ('mamaria+radial+vena', 'mamaria+radial+vena'), ('radial', 'radial')], max_length=5)),
                ('extubado_enquirofano', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=3)),
                ('hemoderivados_intra', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=3)),
                ('ayudante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estadisticas.Ayudantes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cirujanos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')], max_length=15)),
                ('altura', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Clinicas',
                'verbose_name': 'Clinica',
            },
        ),
        migrations.CreateModel(
            name='Complicaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('arritmia', models.CharField(choices=[('NO', 'No'), ('FA <48h ', 'FA <48h '), ('FA >48h ', 'FA >48h '), ('TV/FV ', 'TV/FV '), ('BAV <7dias ', 'BAV < 7dias '), ('MCP definitivo ', 'MCP definitivo '), ('Otra (describir)', 'Otra')], max_length=25)),
                ('sangrado_medico', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=5)),
                ('reop_internado', models.CharField(choices=[('NO', 'No'), ('Sangrado/Taponamiento', 'Sangrado/Taponamiento'), ('Isquemia/IAM', 'Isquemia/IAM'), ('Inestabilidad esternal', 'Inestabilidad esternal'), ('Mediastinitis', 'Mediastinitis'), ('Disfuncion protésica/hemolisis', 'Disfuncion protésica/hemolisis')], max_length=35)),
                ('renal', models.CharField(choices=[('NO', 'No'), ('IRA', 'IRA'), ('Dialisis', 'Dialisis')], max_length=35)),
                ('infectologicas', models.CharField(choices=[('No ', 'No '), ('Herida superficial ', 'Herida superficial '), ('mediastinitis ', 'mediastinitis '), ('Safenectomia ', 'Safenectomia '), ('Neumonia ', 'Neumonia '), ('Asociada a catéter ', 'Asociada a catéter '), ('ITU ', 'ITU ')], max_length=35)),
                ('neurologicas', models.CharField(choices=[('No ', 'No'), ('TIA', 'TIA'), ('ACV sin secuela', 'ACV sin secuela '), ('ACV con secuela', 'ACV con secuela '), ('convulsión', 'convulsión '), ('Sme. Confusional', 'Sme. Confusional ')], max_length=35)),
                ('isquemia_iam', models.CharField(choices=[('No ', 'No'), ('SI', 'Si'), ('Si ATC', 'Si ATC'), ('Si CRM', 'Si CRM')], max_length=35)),
                ('sme_bajo', models.CharField(choices=[('No ', 'No'), ('Si(inotrópicos) ', 'Si(inotrópicos) '), ('Si (IABP/BCIAO)', 'Si (IABP/BCIAO)'), ('Si(Asist.Ventricular) ', 'Si(Asist.Ventricular)')], max_length=35)),
                ('sme_vasoplejico', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=35)),
                ('inotropicos', models.CharField(choices=[('No ', 'No'), ('Dopamina', 'Dopamina'), ('Noradrenalina', 'Noradrenalina'), ('Fenilefrina', 'Fenilefrina'), ('Vasopresina', 'Vasopresina'), ('Adrenalina', 'Adrenalina'), ('Milrinona', 'Milrinona'), ('Levosimendan', 'Levosimendan'), ('Dobutamina', 'Dobutamina')], max_length=35)),
                ('respiratorias', models.CharField(choices=[('No ', 'No'), ('Si-Neumonia', 'Si-Neumonia'), ('Si-traqueostomia', 'Si-traqueostomia'), ('Si-TEP', 'Si-TEP'), ('SI-EPOC relacionadas', 'SI-EPOC relacionadas'), ('Si-ARM>48h', 'Si-ARM>48h')], max_length=35)),
                ('hiperglucemia', models.CharField(choices=[('No ', 'NO'), ('No (BIC)', 'No (BIC)'), ('Si (Correcciones)', 'Si (Correcciones)')], max_length=35)),
                ('plaquetopenia', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=35)),
                ('aco_alta', models.CharField(choices=[('Domicilio', 'Domicilio'), ('Tercer Nivel', 'Tercer Nivel'), ('Obito', 'Obito')], max_length=35)),
                ('obito_internacion', models.BooleanField(default=False)),
                ('otra', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ecodoppler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('diam_diastolico', models.IntegerField(verbose_name='Diametro Diast.')),
                ('diam_sistolico', models.IntegerField(verbose_name='Diametro Sisto,')),
                ('septum_iv', models.IntegerField(verbose_name='Septum IV')),
                ('pared_posterior', models.IntegerField(verbose_name='Pared Posterior')),
                ('auricula_izquierda_unidad', models.CharField(choices=[('MM', 'MM'), ('CM2', 'CM2'), ('ML/M2', 'ML/M2')], max_length=5)),
                ('auricula_izquierda_medida', models.IntegerField()),
                ('raiz_aortica', models.IntegerField(verbose_name='Raiz Aortica')),
                ('ao_tx_a', models.IntegerField(verbose_name='AoTx Diam. Anillo')),
                ('ao_tx_is', models.IntegerField(verbose_name='AoTx Diam. Interseno')),
                ('ao_tx_ust', models.IntegerField(verbose_name='AoTx Diam. Union sinu-tubular ')),
                ('ao_tx_t', models.IntegerField(verbose_name='AoTx Diam. Tubular ')),
                ('fey_vi', models.IntegerField(verbose_name='Fey VI')),
                ('fsvi', models.CharField(choices=[('Conservada', 'Conservada > 50 %'), ('Leve', 'Leve'), ('Moderada', 'Moderada 30-50 %'), ('Severa', 'Severa 21-30 %'), ('Muy Severo', 'Muy Severo <= 20 %')], max_length=25)),
                ('tapse', models.IntegerField(verbose_name='TAPSE (mm)')),
                ('fsvd', models.CharField(choices=[('Conservada', 'Conservada > 50 %'), ('Leve', 'Leve'), ('Moderada', 'Moderada 30-50 %'), ('Severa', 'Severa 21-30 %'), ('Muy Severo', 'Muy Severo <= 20 %')], max_length=25)),
                ('pato_val_aortica', models.CharField(choices=[('No ', 'No'), ('Estenosis Aortica', 'Si - Estenosis Aortica'), ('Trivial', 'Si - Insuficiencia Trivial'), ('Leve', 'Si - Insuficiencia Leve'), ('Moderada', 'Si - Insuficiencia Moderada'), ('Severa', 'Si - Insuficiencia Severa')], max_length=25)),
                ('val_aortica_area', models.FloatField(max_length=5)),
                ('val_aortica_grad_max', models.IntegerField()),
                ('val_aortica_grad_med', models.IntegerField()),
                ('val_aortica_vel', models.FloatField(max_length=5)),
                ('pato_val_mitral', models.CharField(choices=[('No ', 'No'), ('Estenosis Mitral', 'Si - Estenosis mitral'), ('Trivial', 'Si - Insuficiencia Trivial'), ('Leve', 'Si - Insuficiencia Leve'), ('Moderada', 'Si - Insuficiencia Moderada'), ('Severa', 'Si - Insuficiencia Severa')], max_length=25, verbose_name='Patologia Val. Tricuspide')),
                ('mecanismo_mitral', models.CharField(max_length=200, verbose_name='Mecanismo mitral')),
                ('pato_val_tricuspidea', models.CharField(choices=[('No ', 'No'), ('Leve', 'Leve'), ('Moderada', 'Moderada'), ('Severa', 'Severa')], max_length=25, verbose_name='Patologia Val. Tricuspide')),
                ('pulmonar', models.IntegerField(verbose_name='Pulmonar PAP')),
                ('hipertension', models.CharField(choices=[('No ', 'No'), ('Si_PAP_31-55_mmHg', 'Si (PAP 31-55 mmHg)'), ('Si_PAP_>_55_mmHg', 'Si (PAP > 55 mmHg)')], max_length=25)),
                ('comentario', models.CharField(max_length=100, verbose_name='Comentario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ECP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Estados Critico Preoperatorio',
                'verbose_name': 'Estado Critico Preoperatorio',
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Estudios',
                'verbose_name': 'Estudio',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 378925))),
                ('hto', models.IntegerField()),
                ('hb', models.DecimalField(decimal_places=2, max_digits=5)),
                ('leucocitos', models.IntegerField()),
                ('plaquetas', models.IntegerField()),
                ('urea', models.IntegerField()),
                ('hba1c', models.DecimalField(decimal_places=1, max_digits=4)),
                ('glucemia', models.IntegerField()),
                ('tp', models.IntegerField()),
                ('kptt', models.IntegerField()),
                ('rin', models.DecimalField(decimal_places=1, max_digits=4)),
                ('otro', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicacion_Habitual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Medicamentos Habituales',
                'verbose_name': 'Medicacion Habitual',
            },
        ),
        migrations.CreateModel(
            name='Opciones_metodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Metodos',
                'verbose_name': 'Metodo',
            },
        ),
        migrations.CreateModel(
            name='Opciones_viabilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Opciones de viabilidad',
                'verbose_name': 'Opcion_de viabilidad',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')], max_length=15)),
                ('altura', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Procedimientos',
                'verbose_name': 'Procedimiento',
            },
        ),
        migrations.CreateModel(
            name='Resultados_seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Resultados de Seguimientos',
                'verbose_name': 'Resultado de Seguimiento',
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 380154))),
                ('vivo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=3)),
                ('clase_funcional', models.CharField(choices=[('o', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('1-2 a 3-4', '1-2 a 3-4')], max_length=30)),
                ('reinternacion_cardiaca', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=3)),
                ('reinternacion_fecha', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 380239))),
                ('reinternacion_detalle', models.CharField(max_length=200)),
                ('reintervencion_cardiaca', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=3)),
                ('reintervencion_fecha', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 380302))),
                ('reintervencion_detalle', models.CharField(max_length=200)),
                ('anticoagulado', models.CharField(choices=[('No ', 'No'), ('Si-Acenocumarol (Sintrom)', 'Si-Acenocumarol (Sintrom)'), ('SI-Warfarina (Coumadin)', 'SI-Warfarina (Coumadin)')], max_length=3)),
                ('comentario', models.CharField(max_length=250)),
                ('estudios', models.ManyToManyField(to='estadisticas.Estudio')),
                ('resultados', models.ManyToManyField(to='estadisticas.Resultados_seguimiento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transfusiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Transfusiones',
                'verbose_name': 'Transfusion',
            },
        ),
        migrations.CreateModel(
            name='Viablilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367443))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 5, 12, 39, 42, 367475))),
                ('export_date', models.DateTimeField(blank=True, null=True)),
                ('isquemia', models.ManyToManyField(related_name='Isquemia', to='estadisticas.Opciones_viabilidad')),
                ('metodo_viabilidad', models.ManyToManyField(to='estadisticas.Opciones_metodo')),
                ('necrosis', models.ManyToManyField(related_name='Necrosis', to='estadisticas.Opciones_viabilidad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='complicaciones',
            name='transfusiones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estadisticas.Transfusiones'),
        ),
        migrations.AddField(
            model_name='cirugia',
            name='cirujano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estadisticas.Cirujanos'),
        ),
        migrations.AddField(
            model_name='cirugia',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estadisticas.Clinica'),
        ),
        migrations.AddField(
            model_name='cirugia',
            name='procedimientos',
            field=models.ManyToManyField(to='estadisticas.Procedimiento'),
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='estado_critico',
            field=models.ManyToManyField(to='estadisticas.ECP'),
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='medicacion_habitual',
            field=models.ManyToManyField(to='estadisticas.Medicacion_Habitual'),
        ),
    ]