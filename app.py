import streamlit as st
import pandas as pd
# import numpy as np
import joblib

model_pipeline = joblib.load('model.joblib')

def predict_dropout(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model_pipeline.predict(input_df)
    return prediction[0]

st.title("Prediksi Dropout Siswa")

marital_status = st.number_input('Status Marital', min_value=0, max_value=1, step=1)
st.write("0 = Wanita    1 = Pria")
application_mode = st.number_input('Mode Aplikasi', min_value=0, max_value=20, step=1)
st.write("1 - 1st phase - general contingent 2 - Ordinance No. 612/93 5 - 1st phase - special contingent (Azores Island) 7 - Holders of other higher courses 10 - Ordinance No. 854-B/99 15 - International student (bachelor) 16 - 1st phase - special contingent (Madeira Island) 17 - 2nd phase - general contingent 18 - 3rd phase - general contingent 26 - Ordinance No. 533-A/99, item b2) (Different Plan) 27 - Ordinance No. 533-A/99, item b3 (Other Institution) 39 - Over 23 years old 42 - Transfer 43 - Change of course 44 - Technological specialization diploma holders 51 - Change of institution/course 53 - Short cycle diploma holders 57 - Change of institution/course (International)")
application_order = st.number_input('Urutan Aplikasi', min_value=1, max_value=10, step=1)
st.write("The order in which the student applied. (Numerical) Application order (between 0 - first choice; and 9 last choice)")
course = st.number_input('Course', min_value=0, max_value=10000, step=1)
st.write("The course taken by the student. (Categorical) 33 - Biofuel Production Technologies 171 - Animation and Multimedia Design 8014 - Social Service (evening attendance) 9003 - Agronomy 9070 - Communication Design 9085 - Veterinary Nursing 9119 - Informatics Engineering 9130 - Equinculture 9147 - Management 9238 - Social Service 9254 - Tourism 9500 - Nursing 9556 - Oral Hygiene 9670 - Advertising and Marketing Management 9773 - Journalism and Communication 9853 - Basic Education 9991 - Management (evening attendance)")
daytime_evening_attendance = st.number_input('Kehadiran Siang/Malam', min_value=0, max_value=1, step=1)
st.write("Whether the student attends classes during the day or in the evening. (Categorical) 1 – daytime 0 - evening")
previous_qualification = st.number_input('Kualifikasi Sebelumnya', min_value=0, max_value=10, step=1)
st.write("The qualification obtained by the student before enrolling in higher education. (Categorical) 1 - Secondary education 2 - Higher education - bachelor's degree 3 - Higher education - degree 4 - Higher education - master's 5 - Higher education - doctorate 6 - Frequency of higher education 9 - 12th year of schooling - not completed 10 - 11th year of schooling - not completed 12 - Other - 11th year of schooling 14 - 10th year of schooling 15 - 10th year of schooling - not completed 19 - Basic education 3rd cycle (9th/10th/11th year) or equiv. 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 42 - Professional higher technical course 43 - Higher education - master (2nd cycle)")
previous_qualification_grade = st.number_input('Nilai Kualifikasi Sebelumnya', min_value=0.0, max_value=200.0, step=0.1)
st.write("Grade of previous qualification (between 0 and 200)")
nacionality = st.number_input('Kewarganegaraan', min_value=0, max_value=100, step=1)
st.write("The nationality of the student. (Categorical) 1 - Portuguese; 2 - German; 6 - Spanish; 11 - Italian; 13 - Dutch; 14 - English; 17 - Lithuanian; 21 - Angolan; 22 - Cape Verdean; 24 - Guinean; 25 - Mozambican; 26 - Santomean; 32 - Turkish; 41 - Brazilian; 62 - Romanian; 100 - Moldova (Republic of); 101 - Mexican; 103 - Ukrainian; 105 - Russian; 108 - Cuban; 109 - Colombian")
mothers_qualification = st.number_input('Kualifikasi Ibu', min_value=0, max_value=50, step=1)
st.write("The qualification of the student's mother. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 22 - Technical-professional course 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)")
fathers_qualification = st.number_input('Kualifikasi Ayah', min_value=0, max_value=50, step=1)
st.write("The qualification of the student's father. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 13 - 2nd year complementary high school course 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 20 - Complementary High School Course 22 - Technical-professional course 25 - Complementary High School Course - not concluded 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 31 - General Course of Administration and Commerce 33 - Supplementary Accounting and Administration 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)")
mothers_occupation = st.number_input('Pekerjaan Ibu', min_value=0, max_value=20, step=1)
st.write("The occupation of the student's mother. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants")
fathers_occupation = st.number_input('Pekerjaan Ayah', min_value=0, max_value=20, step=1)
st.write("The occupation of the student's father. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 101 - Armed Forces Officers 102 - Armed Forces Sergeants 103 - Other Armed Forces personnel 112 - Directors of administrative and commercial services 114 - Hotel, catering, trade and other services directors 121 - Specialists in the physical sciences, mathematics, engineering and related techniques 122 - Health professionals 123 - teachers 124 - Specialists in finance, accounting, administrative organization, public and commercial relations 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 135 - Information and communication technology technicians 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 154 - Protection and security services personnel 161 - Market-oriented farmers and skilled agricultural and animal production workers 163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence 171 - Skilled construction workers and the like, except electricians 172 - Skilled workers in metallurgy, metalworking and similar 174 - Skilled workers in electricity and electronics 175 - Workers in food processing, woodworking, clothing and other industries and crafts 181 - Fixed plant and machine operators 182 - assembly workers 183 - Vehicle drivers and mobile equipment operators 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants 195 - Street vendors (except food) and street service providers")
admission_grade = st.number_input('Nilai Masuk', min_value=0.0, max_value=20.0, step=0.1)
st.write("Admission grade (between 0 and 200)")
displaced = st.number_input('Displaced', min_value=0, max_value=1, step=1)
st.write("Whether the student is a displaced person. (Categorical) 1 – yes 0 – no")
educational_special_needs = st.number_input('Kebutuhan Khusus Pendidikan', min_value=0, max_value=1, step=1)
st.write("Whether the student has any special educational needs. (Categorical) 1 – yes 0 – no")
debtor = st.number_input('Debtor', min_value=0, max_value=1, step=1)
st.write("Whether the student is a debtor. (Categorical) 1 – yes 0 – no")
tuition_fees_up_to_date = st.number_input('Biaya Kuliah Tepat Waktu', min_value=0, max_value=1, step=1)
st.write("Whether the student's tuition fees are up to date. (Categorical) 1 – yes 0 – no")
gender = st.number_input('Jenis Kelamin', min_value=0, max_value=1, step=1)
st.write("The gender of the student. (Categorical) 1 – male 0 – female")
scholarship_holder = st.number_input('Pemegang Beasiswa', min_value=0, max_value=1, step=1)
st.write("Whether the student is a scholarship holder. (Categorical) 1 – yes 0 – no")
age_at_enrollment = st.number_input('Usia Saat Pendaftaran', min_value=0, max_value=100, step=1)
st.write("The age of the student at the time of enrollment. (Numerical)")
international = st.number_input('Internasional', min_value=0, max_value=1, step=1)
st.write("Whether the student is an international student. (Categorical) 1 – yes 0 – no")
curricular_units_1st_sem_credited = st.number_input('Unit Kurikulum 1st Sem Diakui', min_value=0, max_value=100, step=1)
curricular_units_1st_sem_enrolled = st.number_input('Unit Kurikulum 1st Sem Terdaftar', min_value=0, max_value=100, step=1)
curricular_units_1st_sem_evaluations = st.number_input('Evaluasi Unit Kurikulum 1st Sem', min_value=0, max_value=100, step=1)
curricular_units_1st_sem_approved = st.number_input('Unit Kurikulum 1st Sem Disetujui', min_value=0, max_value=100, step=1)
curricular_units_1st_sem_grade = st.number_input('Nilai Unit Kurikulum 1st Sem', min_value=0.0, max_value=20.0, step=0.1)
curricular_units_1st_sem_without_evaluations = st.number_input('Unit Kurikulum 1st Sem Tanpa Evaluasi', min_value=0, max_value=100, step=1)
curricular_units_2nd_sem_credited = st.number_input('Unit Kurikulum 2nd Sem Diakui', min_value=0, max_value=100, step=1)
curricular_units_2nd_sem_enrolled = st.number_input('Unit Kurikulum 2nd Sem Terdaftar', min_value=0, max_value=100, step=1)
curricular_units_2nd_sem_evaluations = st.number_input('Evaluasi Unit Kurikulum 2nd Sem', min_value=0, max_value=100, step=1)
curricular_units_2nd_sem_approved = st.number_input('Unit Kurikulum 2nd Sem Disetujui', min_value=0, max_value=100, step=1)
curricular_units_2nd_sem_grade = st.number_input('Nilai Unit Kurikulum 2nd Sem', min_value=0.0, max_value=20.0, step=0.1)
curricular_units_2nd_sem_without_evaluations = st.number_input('Unit Kurikulum 2nd Sem Tanpa Evaluasi', min_value=0, max_value=100, step=1)
unemployment_rate = st.number_input('Tingkat Pengangguran', min_value=0.0, max_value=100.0, step=0.1)
inflation_rate = st.number_input('Tingkat Inflasi', min_value=-10.0, max_value=10.0, step=0.1)
gdp = st.number_input('GDP', min_value=0.0, max_value=100.0, step=0.1)



input_data = {
    'Marital_status': marital_status,
    'Application_mode': application_mode,
    'Application_order': application_order,
    'Course': course,
    'Daytime_evening_attendance': daytime_evening_attendance,
    'Previous_qualification': previous_qualification,
    'Previous_qualification_grade': previous_qualification_grade,
    'Nacionality': nacionality,
    'Mothers_qualification': mothers_qualification,
    'Fathers_qualification': fathers_qualification,
    'Mothers_occupation': mothers_occupation,
    'Fathers_occupation': fathers_occupation,
    'Admission_grade': admission_grade,
    'Displaced': displaced,
    'Educational_special_needs': educational_special_needs,
    'Debtor': debtor,
    'Tuition_fees_up_to_date': tuition_fees_up_to_date,
    'Gender': gender,
    'Scholarship_holder': scholarship_holder,
    'Age_at_enrollment': age_at_enrollment,
    'International': international,
    'Curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
    'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
    'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
    'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
    'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
    'Curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations,
    'Curricular_units_2nd_sem_credited': curricular_units_2nd_sem_credited,
    'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
    'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
    'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
    'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
    'Curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations,
    'Unemployment_rate': unemployment_rate,
    'Inflation_rate': inflation_rate,
    'GDP': gdp
}

if st.button('Predict'):
    result = predict_dropout(input_data)
    st.write(f"Prediksi Status: {result}")