import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    race_count = df['race'].value_counts()

    # Qual é a idade média dos homens?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # Qual é a porcentagem de pessoas que possuem diploma de Bacharelado?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Qual a porcentagem de pessoas com educação avançada (Bacharelado, Mestrado ou Doutorado) que ganham mais de 50K?
    higher_education = df.query("education == 'Bachelors' or education == 'Masters' or education == 'Doctorate'")

    # Qual a porcentagem de pessoas sem educação avançada que ganham mais de 50K?
    lower_education = df.query("education != 'Bachelors' and education != 'Masters' and education != 'Doctorate'")
    
    # Porcentagem de pessoas com salário >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').sum() * 100 / len(higher_education), 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() * 100 / len(lower_education), 1)

    # Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # Qual a porcentagem das pessoas que trabalham o número mínimo de horas por semana e possuem salário superior a 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() * 100 / len(num_min_workers), 1)

    # Qual país tem a maior porcentagem de pessoas que ganham mais de 50K?
    value_highest_earning_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = value_highest_earning_country.idxmax()
    highest_earning_country_percentage = round(value_highest_earning_country.max(), 1)

    # Qual é a ocupação mais comum entre aqueles que ganham mais de 50K na Índia?
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')] \
                        .groupby('occupation').size().idxmax()

    # NÃO MODIFIQUE ABAIXO DESTA LINHA
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
