import pandas
import re
import sys
sys.path.append("..")

data = pandas.read_csv('train.csv', index_col='PassengerId')

def get_nubmer_of_pass():
    """
Какое количество мужчин и женщин ехало на параходе? 
Приведите два числа через пробел.
    """
    sex_counts = data['Sex'].value_counts()
    print('{} {}'.format(sex_counts['male'], sex_counts['female']))

def get_number_of_embarked():
    """
    Подсчитайте сколько пассажиров загрузилось на борт в различных портах? 
    Приведите три числа через пробел.
    """
    embarked_counts = data['Embarked'].value_counts()
    print('{} {} {}'.format(embarked_counts['S'], embarked_counts['C'], embarked_counts['Q']))

def get_number_of_drowned():
    """
    Посчитайте долю погибших на параходе (число и процент)?
    """
    drowned_counts = data['Survived'].value_counts()
    drowned_percent = 100.00 * drowned_counts[0] / drowned_counts.sum()
    print("{} {:0.2f}%".format(drowned_counts[0], drowned_percent))

def get_number_of_pass_by_classes():
    """
    Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    allclasses_counts = data['Pclass'].value_counts()
    first = 100.00 * allclasses_counts[1] / allclasses_counts.sum()
    second = 100.00 * allclasses_counts[2] / allclasses_counts.sum()
    third = 100.00 * allclasses_counts[3] / allclasses_counts.sum()
    print("{:0.2f} {:0.2f} {:0.2f}".format(first, second, third))

def get_correl():
    """
    Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    correl = data['SibSp'].corr(data['Parch'])
    print("{:0.2f}".format(correl))    

def get_more_corr():
    """
    Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    возрастом и параметром survival;
    полом человека и параметром survival;
    классом, в котором пассажир ехал, и параметром survival.
    """
    age_surv_correl = data['Age'].corr(data['Survived'])
    #sex_surv_fem_correl = data['Sex' == 'female'].corr(data['Survived'])
    #sex_surv_mal_correl = data['Sex' == 'male'].corr(data['Survived'])
    plclass_surv_correl = data['Pclass'].corr(data['Survived'])
    print("{:0.2f} {:0.2f}".format(age_surv_correl, plclass_surv_correl))

def get_ages():
    """
    Посчитайте средний возраст пассажиров и медиану
    """
    ages = data['Age'].dropna()
    print("{:0.2f} {:0.2f}".format(ages.mean(), ages.median()))

def get_fare():
    """
    Посчитайте среднюю цену за билет и медиану.
    """    
    fare = data['Fare'].dropna()
    print("{:0.2f} {:0.2f}".format(fare.mean(), fare.median()))

def only_name(name):
    # Первое слово до запятой - фамилия
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)
    # Если есть скобки - то имя пассажира в них
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)
    # Удаляем обращения
    name = re.sub('(Miss\. |Mrs\. |Mr\. |Master\. |Ms\. )', '', name)
    # Берем первое оставшееся слово и удаляем кавычки
    name = name.split(' ')[0].replace('"', '')

    return name

def get_male_name():
    """
    Какое самое популярное мужское имя на корабле?
    """
    male_names = data[data['Sex'] == 'male']['Name'].map(only_name)
    male_names_counts = male_names.value_counts()
    print(male_names_counts.head(1).index.values[0])

def get_popular_names():
    """
    Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    adult_male_names = data[data['Age'] > 15 ][data['Sex'] == 'male']['Name'].map(only_name)
    adult_male_names_counts = adult_male_names.value_counts()
    adult_female_names = data[data['Age'] > 15 ][data['Sex'] == 'female']['Name'].map(only_name)
    adult_female_names_counts = adult_female_names.value_counts()
    print(adult_male_names_counts.head(1).index.values[0],adult_female_names_counts.head(1).index.values[0])

if __name__ == "__main__":
    sys.stdout=open("answers.txt","w")
    get_nubmer_of_pass()
    get_number_of_embarked()
    get_number_of_drowned()
    get_number_of_pass_by_classes()
    get_correl()
    get_more_corr()
    get_ages()
    get_fare()
    get_male_name()
    get_popular_names()
    sys.stdout.close()
